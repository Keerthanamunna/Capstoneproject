import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import Place, Venue, setup_db
from app import create_app
from models import db
import datetime


class TravelTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_host = '127.0.0.1:5432'
        self.database_username = 'postgres'
        self.database_name = 'traveltest'
        self.database_path = 'postgresql+psycopg2://{}@{}/{}'.format(
            self.database_username,
            self.database_host,
            self.database_name)
        setup_db(self.app, self.database_path)

        self.new_venue = {
            'vname': 'Connecticut',
            'description' : 'This venue has many places'
        }

        self.new_place = {
            'pname': 'rhode island',
            'pdescription': 'The place was nice',
            
            'venue_id': 1
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        pass

    def test_get_venues(self):
        res = self.client().get('/venues')
        self.assertEqual(res.status_code, 200)

    def test_get_venues_fail(self):
        res = self.client().get('/venues')
        self.assertEqual(res.status_code, 404)

    def test_get_places(self):
        res = self.client().get('/places')
        self.assertEqual(res.status_code, 200)

    def test_get_places_fail(self):
        res = self.client().get('/places')
        self.assertEqual(res.status_code, 404)

    def test_create_venue(self):
        res = self.client().post('/venues/create', json=self.new_venue)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['new_venue']['vname'], 'Connecticut')

    def test_create_place(self):
        res = self.client().post('/places/create', json=self.new_place)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['new_place']['pname'], 'rhode island')
    
    def test_patch_venue(self):
        res = self.client().patch('/venues/patch/2', json=self.new_venue)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_patch_venue_fail(self):
        res = self.client().patch('/venues/patch/2000', json=self.new_venue)
        self.assertEqual(res.status_code, 404)


    def test_patch_place(self):
        res = self.client().patch('/places/patch/2', json=self.new_place)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_patch_place_fail(self):
        res = self.client().patch('/places/patch/2000', json=self.new_place)
        self.assertEqual(res.status_code, 404)
    
    def test_delete_venue(self):
        res = self.client().delete('/venues/delete/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_delete_venue_fail(self):
        res = self.client().delete('/venues/delete/1000')
        self.assertEqual(res.status_code, 404)
    
    def test_delete_place(self):
        res = self.client().delete('/places/delete/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_delete_place_fail(self):
        res = self.client().delete('/places/delete/1000')
        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()

