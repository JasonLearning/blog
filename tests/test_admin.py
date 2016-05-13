import unittest
from flask import url_for, session
from app import create_app, db
from app.models import Article, Comment, Tag


class TestAdmin(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_login(self):
        self.client.get(url_for('admin.login_page'))
        response = self.client.post(url_for('admin.login_page'), data={
            'name': 'test',
            'password': '1234'
            }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Bernie', response.get_data(as_text=True))

        response = self.client.post(url_for('admin.login_page'), data={
            'name': 'alice',
            'password': 'wonderland'
            }, follow_redirects=True)
        self.assertTrue('Under construction' in response.get_data(as_text=True))


    def test_new_article(self):
        self.client.post(url_for('admin.login_page'), data={
            'name': 'test',
            'password': '1234'
            })
        self.client.post(url_for('admin.new_article'), data={
            'name': 'test',
            'password': '1234'
            })



        