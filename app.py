# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 11:53:45 2025

@author: SWDL_15_DIS
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()