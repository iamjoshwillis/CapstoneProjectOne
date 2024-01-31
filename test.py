import os
from unittest import TestCase

from models import *

os.environ['DATABASE_URL'] = "postgresql:///space-vacations-test"

from app import app, CURR_USER_KEY
db.create_all()

mercury = Planet(name="Mercury", distance_from_sun="0.4")
venus = Planet(name="Venus", distance_from_sun="0.7")
earth = Planet(name="Earth", distance_from_sun="1")
mars = Planet(name="Mars", distance_from_sun="1.5")
jupiter = Planet(name="Jupiter", distance_from_sun="5.2")
saturn = Planet(name="Saturn", distance_from_sun="9.5")
uranus = Planet(name="Uranus", distance_from_sun="8.8")
neptune = Planet(name="Neptune", distance_from_sun="30.1")
planetnine = Planet(name="Planet 9", distance_from_sun="600")

db.add_all([mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, planetnine])

db.session.commit()

app.config['WTF_CSRF_ENABLED'] = False


class ModelTestCase(TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()

        u1 = User.signup("test1", "email1@email.com", "password", 2, "/imageurl")
        uid1 = 1111
        u1.id = uid1

        u2 = User.signup("test2", "email2@email.com", "password2", 3, "/imageurl2")
        uid2 = 2222
        u2.id = uid2

        db.session.commit()

        u1 = User.query.get(uid1)
        u2 = User.query.get(uid2)

        self.u1 = u1
        self.uid1 = uid1

        self.u2 = u2
        self.uid2 = uid2

        self.client = app.test_client()

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res
    
    def test_valid_registration(self):
        u_test = User.signup("testusername", "testing@email.com", "testpw","/imageurl")
        uid = 999
        u_test.id = uid
        db.session.commit()

        u_test = User.query.get(uid)
        self.assertIsNotNone(u_test)
        self.assertEqual(u_test.username, "testusername")
        self.assertEqual(u_test.email, "testing@email.com")
        self.assertTrue(u_test.password.startswith("$2b$"))
        self.assertEqual(u_test.image_url, "/imageurl")


    def test_valid_authentication(self):
        u = User.authenticate(self.u1.username, "testpw")
        self.assertIsNotNone(u)
        self.assertEqual(u.id, self.uid1)