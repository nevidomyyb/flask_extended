from flask import Flask, request
from db import stores, items
import uuid
from flask_smorest import abort

app = Flask(__name__)
