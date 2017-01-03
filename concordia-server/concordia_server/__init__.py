from flask import Flask

# Declare application
app = Flask(__name__)

# Database
from concordia_server.models import db

# Services
from concordia_server.services import *
