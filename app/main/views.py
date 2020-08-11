from flask import render_template, make_response
from . import main


@main.route('/')
def index():
    template = render_template('app/index.html')
    response = make_response(template)
    return response
