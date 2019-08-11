from flask import Blueprint

bp = Blueprint('features', __name__)

from src.features import routes
