"""`main` is the top level module for your Flask application."""

import pdb

from flask.ext.restful import Api, Resource
from flask import Flask, request
from api.models import *
from api.restful import restify
# import app

#initialize the application, no need to execute run()
app = Flask(__name__)


#home page
@app.route('/')
def hello():
    return 'Hello pretty World!'


#Add models to restful
api = Api(app)
restify(api, Contact, '/api/v1/contacts')

#Appropriate pages for error codes
@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def page_not_found(e):
    return 'Sorry, unexpected error: {}'.format(e), 500



