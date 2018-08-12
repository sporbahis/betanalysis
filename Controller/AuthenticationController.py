# -*- coding: utf-8 -*-

from flask import (Flask, flash, render_template, session, request, redirect, url_for)

@app.route('/')
def index():
    # Use a list here so we can do "if posts" efficiently in the template.
    return render_template('index.html')