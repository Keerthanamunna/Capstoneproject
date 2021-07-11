#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import os
from flask import Flask, request, abort, jsonify
from flask import render_template, session, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
#from config import Config
import random
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from models import setup_db, Venue, Place, db
from auth import AuthError, requires_auth


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#


def create_app(test_config=None):
  # create and configure the app
    app = Flask(__name__)
    moment = Moment(app)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    #SECRET_KEY = os.urandom(32)
    CORS(app, resources={r"/api/": {"origins": "*"}})
    
    setup_db(app)

    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, PATCH, POST, DELETE, OPTIONS')
        return response

    @app.route('/venues')
    @requires_auth('get:venues')
    def get_venues():
        venues = Venue.query.all()
        venues = [venue.format() for venue in venues]
        for venue in venues:
            venue['places'] = [i.format() for i in venue['places']]
            return jsonify(venues)

    @app.route('/places', methods=['GET'])
    @requires_auth('get:places')
    def get_places():
        places = Place.query.all()
        places = [place.format() for place in places]
        return jsonify(places)

    @app.route('/venues/create', methods=['POST'])
    @requires_auth('post:venue')
    def post_new_venue():
        body = request.get_json()
        vname = body.get('vname', None)
        description = body.get('description', None)
        venue = Venue(vname=vname, description=description)
        venue.insert()
        new_venue = Venue.query.get(venue.id)
        new_venue = new_venue.format()
        return jsonify({
            'success': True,
            'created': venue.id,
            'new_venue': new_venue
        })

    @app.route('/places/create', methods=['POST'])
    @requires_auth('post:place')
    def post_new_place():
        body = request.get_json()
        pname = body.get('pname', None)
        pdescription = body.get('pdescription', None)
        venue_id = body.get('venue_id', None)
        place = Place(pname=pname, pdescription=pdescription,
                      venue_id=venue_id)
        place.insert()
        new_place = Place.query.get(place.id)
        new_place = new_place.format()
        return jsonify({
            'success': True,
            'created': place.id,
            'new_place': new_place
        })

    @app.route('/venues/delete/<int:venue_id>', methods=['DELETE'])
    @requires_auth('delete:venue')
    def delete_venue(venue_id):
        Venue.query.filter(Venue.id == venue_id).delete()
        db.session.commit()
        db.session.close()
        return jsonify({
            "success": True,
            "message": "Deleted venue"
        })

    @app.route('/places/delete/<int:place_id>', methods=['DELETE'])
    @requires_auth('delete:place')
    def delete_place(place_id):
        Place.query.filter(Place.id == place_id).delete()
        db.session.commit()
        db.session.close()
        return jsonify({
            "success": True,
            "message": "Deleted place"
        })

    @app.route('/places/patch/<int:place_id>', methods=['PATCH'])
    @requires_auth('patch:places')
    def patch_place(place_id):
        place = Place.query.filter(Place.id == place_id)
        body = request.get_json()
        pname = body.get('pname', None)
        pdescription = body.get('pdescription', None)
        venue_id = body.get('venue_id', None)
        place.pname = pname
        place.pdescription = pdescription
        place.venue_id = venue_id
        place.update()
        return jsonify({
            "success": True,
            "message": "Place update occured"
        })

    @app.route('/venues/patch/<int:venue_id>')
    @requires_auth('patch:venues')
    def patch_venue(venue_id):
        venue = Venue.query.filter(Venue.id == venue_id)
        body = request.get_json()
        vname = body.get('vname', None)
        description = body.get('description', None)
        venue.vname = vname
        venue.description = description
        venue.update()
        return jsonify({
            "success": True,
            "message": "Venue update occured"
        })

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not Found'
        }), 404

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable Entity'
        })
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
