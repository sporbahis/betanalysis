# -*- coding: utf-8 -*-

import app
from flask import (Flask, render_template, request)


print("Test")


@app.route('/')
def index():
    return render_template('deneme.html')