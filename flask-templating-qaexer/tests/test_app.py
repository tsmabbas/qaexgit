from app import TestBase
from flask import url_for
from app import app, db, Owner

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///data.db'
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create()

        test_owner = Owners(first_name="John", last_name="Smith")
        db.session.add(test_owner)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop.all()

Class Testviews(TestBase):

    def test_home_get(self)
        response  = self.client.post(url_for("homePage"))
        self.assertEqual(response.status_code, 200)

class TestCreate(TestBase):

    def test_add_post(self):
        response  = self.client.get(url_for("add_owner"), data=dict(first_name="Simon",last_name="Jones"), follow_redirects=True)
        self.assertIn(b'Name:Simon Jones', response.data)
