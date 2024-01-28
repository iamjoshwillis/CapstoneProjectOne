from flask import Flask, redirect, render_template, flash, request, session, g
import requests
from flask_debugtoolbar import DebugToolbarExtension

from models import *
from forms import *
CURR_USER_KEY = "curr_user"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///space-vacations'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

"""Base URL for Solar System OpenData API"""
SSO_BASE_URL = "https://api.le-systeme-solaire.net/rest/bodies/"

"""Base URL for NASA Images and Videos Gallery"""
NASA_BASE_URL = "https://images-api.nasa.gov"

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "13572468"

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

#######################################################################

@app.before_request
def add_user_to_g():
    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else:
        g.user = None

def do_login(user):
    session[CURR_USER_KEY] = user.id

def do_logout():
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

#######################################################################

@app.route('/')
def show_home_page():
    return render_template('index.html')


@app.route('/register', methods=["GET", "POST"])
def add_new_user():
    form = UserSignUpForm()

    planets = (db.session.query(Planet.id, Planet.name).all())
    choices = [(x.id, x.name) for x in planets]
    form.home_planet.choices = choices

    if form.validate_on_submit():
        user = User.signup(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            image_url=form.image_url.data or User.image_url.default.arg,
            home_planet=form.home_planet.data,
        )
        db.session.add(user)
        db.session.commit()

        do_login(user)
        return redirect("/voyagemap")
    else:
        return render_template('register.html', form=form)
    

@app.route('/login', methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data, form.password.data)
        if user:
            do_login(user)
            return redirect("/voyagemap")
        
        flash("Failed Login Attempt")
    return render_template('login.html', form=form)


@app.route('/voyagemap', methods=["GET", "POST"])
def show_voyage_map():
    planets = Planet.query.all()
    return render_template('voyagemap.html', planets=planets)

@app.route('/booktravel', methods=["GET", "POST"])
def show_flight_form():
    form = BookTravelForm()
    
    departing_planet = (db.session.query(Planet.id, Planet.name).all())
    choices = [(x.id, x.name) for x in departing_planet]
    form.departing_planet.choices = choices

    arriving_planet = (db.session.query(Planet.id, Planet.name).all())
    choices = [(x.id, x.name) for x in arriving_planet]
    form.arriving_planet.choices = choices

    if form.validate_on_submit():
        new_flight = Flight(
            departing_planet=form.departing_planet.data,
            arriving_planet=form.arriving_planet.data,
            flight_time=1.5
            )
        db.session.add(new_flight)
        db.session.commit()
        return redirect('/tripconfirmation')
    else:
        return render_template('booktravel.html', form=form)


@app.route("/trip/<int:id>", methods=["GET", "POST"])
def show_itinerary(id):
    trip = Flight.query.get_or_404(id)

    return render_template('tripconfirmation.html', trip=trip)


@app.route("/planetinfo/<int:planet_id>")
def show_planet_info(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    activities = db.session.query(Activity.name, Activity.description).filter(Activity.planet == planet_id).all()
    hotels = db.session.query(Hotel.name, Hotel.description).filter(Hotel.planet == planet_id).all()
    restaurants = db.session.query(Restaurant.name, Restaurant.description).filter(Restaurant.planet == planet_id).all()
    planet_name = planet.name

    """Gather Planetary Data""" 
    response = requests.get(f'https://api.le-systeme-solaire.net/rest/bodies/{planet_name}')

    if planet.id < 9:
        gravity = response.json()['gravity']
        average_temp = response.json()['avgTemp']
    else:
        gravity = "Unknown"
        average_temp = 47

    """Convert Temp in K to F"""
    temp_in_far = ((average_temp * 9)/5)-460
    rounded_temperature = round(temp_in_far)

    return render_template('planetinfo.html', 
    planet=planet,
    planet_name=planet_name,
    activities=activities,
    hotels=hotels,
    restaurants=restaurants,
    gravity=gravity,
    average_temp=average_temp,
    temp_in_far=rounded_temperature)
    