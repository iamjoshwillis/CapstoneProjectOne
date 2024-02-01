from flask import Flask, redirect, render_template, flash, session, g
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
    """New User Registration"""
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
            bio=form.bio.data
        )
        db.session.add(user)
        db.session.commit()

        do_login(user)
        return redirect("/voyagemap")
    else:
        return render_template('register.html', form=form)
    

@app.route('/login', methods=["GET", "POST"])
def login():
    """Existing User Login"""
    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data, form.password.data)
        if user:
            do_login(user)
            return redirect("/voyagemap")
        
        flash("Failed Login Attempt")
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    do_logout()
    flash("Goodbye", 'success')
    return redirect("/")

@app.route('/voyagemap', methods=["GET", "POST"])
def show_voyage_map():
    planets = Planet.query.all()
    return render_template('voyagemap.html', planets=planets)

@app.route("/planetinfo/<int:planet_id>")
def show_planet_info(planet_id):
    """Gather Data for Selected Planet"""
    planet = Planet.query.get_or_404(planet_id)
    activities = db.session.query(Activity.name, Activity.description).filter(Activity.planet == planet_id).all()
    hotels = db.session.query(Hotel.name, Hotel.description).filter(Hotel.planet == planet_id).all()
    restaurants = db.session.query(Restaurant.name, Restaurant.description).filter(Restaurant.planet == planet_id).all()
    planet_name = planet.name

    """Gather Planetary Data""" 
    response = requests.get(f'{SSO_BASE_URL}{planet_name}')

    """Handle Planet 9 not having data in API"""
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


@app.route('/booktravel', methods=["GET", "POST"])
def show_flight_form():

    if not g.user:
        flash("Please Register or Login", "danger")
        return redirect("/")
    
    form = BookTravelForm(departing_planet_id=g.user.home_planet)
    departing_planet_id = (db.session.query(Planet.id, Planet.name).all())
    choices = [(x.id, x.name) for x in departing_planet_id]
    form.departing_planet_id.choices = choices

    arriving_planet_id = (db.session.query(Planet.id, Planet.name).all())
    choices = [(x.id, x.name) for x in arriving_planet_id]
    form.arriving_planet_id.choices = choices

    if form.validate_on_submit():

        """Calculate Flight Time Based on user-chosen departing and arriving planets"""
        departing_query = db.session.query(Planet.distance_from_sun).filter(Planet.id == form.departing_planet_id.data).first()
        arriving_query = db.session.query(Planet.distance_from_sun).filter(Planet.id == form.arriving_planet_id.data).first()

        departing = departing_query[0]
        arriving = arriving_query[0]

        flight_time = round((abs(departing-arriving)/3.6), 1)

        def convert_flight_time(flight_time):
            hours = int(flight_time)
            minutes = int((flight_time - hours) * 60)
            return f'{hours} Hr {minutes} Min'
        
        flight_time_formatted = convert_flight_time(flight_time)

        new_flight = Flight(
            user = g.user.id,
            departing_planet_id=form.departing_planet_id.data,
            arriving_planet_id=form.arriving_planet_id.data,
            flight_time=flight_time_formatted
            )
        db.session.add(new_flight)
        db.session.commit()
        return redirect(f'/trip/{new_flight.id}')
    else:
        return render_template('booktravel.html', form=form)


@app.route("/trip/<int:id>", methods=["GET"])
def show_itinerary(id):
    """Show Trip Details"""
    flight = Flight.query.get_or_404(id)
    arriving_planet_name = flight.arriving_planet.name
    
    activities = db.session.query(Activity.name, Activity.description).filter(Activity.planet == flight.arriving_planet_id).all()
    hotels = db.session.query(Hotel.name, Hotel.description).filter(Hotel.planet == flight.arriving_planet_id).all()
    restaurants = db.session.query(Restaurant.name, Restaurant.description).filter(Restaurant.planet == flight.arriving_planet_id).all()
    planet_name = flight.arriving_planet.name

    """Gather Planetary Data""" 
    response = requests.get(f'{SSO_BASE_URL}{planet_name}')

    """Handle Planet 9 not having data in API"""
    if flight.arriving_planet_id < 9:
        gravity = response.json()['gravity']
        average_temp = response.json()['avgTemp']
    else:
        gravity = "Unknown"
        average_temp = 47

    """Convert Temp in K to F"""
    temp_in_far = ((average_temp * 9)/5)-460
    rounded_temperature = round(temp_in_far)

    return render_template('tripconfirmation.html',
    flight=flight, 
    arriving_planet_name=arriving_planet_name,
    planet_name=planet_name,
    activities=activities,
    hotels=hotels,
    restaurants=restaurants,
    gravity=gravity,
    average_temp=average_temp,
    temp_in_far=rounded_temperature)




@app.route("/users/<int:user_id>")
def show_profile(user_id):
    user = User.query.get_or_404(user_id)

    return render_template("profile.html", user=user)



@app.route("/edit", methods=["GET", "POST"])
def show_editform():
    """Edit User Profile"""
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")
    
    user = g.user
    form = UserEditForm(obj=user)

    planets = (db.session.query(Planet.id, Planet.name).all())
    choices = [(x.id, x.name) for x in planets]
    form.home_planet.choices = choices

    if form.validate_on_submit():
        if User.authenticate(user.username, form.password.data):
            user.username = form.username.data
            user.email = form.email.data
            user.image_url = form.image_url.data or "static/images/defaultuser.jpg"
            user.bio = form.bio.data
            user.home_planet = form.home_planet.data

            db.session.commit()
            return redirect(f'/users/{user.id}')
        
        flash("Wrong password, please try again.", 'danger')
        
    return render_template("editform.html", form=form, user_id=user.id)