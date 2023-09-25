#!/bin/bash

start python -m http.server -d ./ui/ 8080
cd src
start python app.py
cd -

