#!/bin/bash

cd flyway
./run_flyway.cmd clean migrate info
cd -
# Start the HTTP Server
start python -m http.server -d ./ui/ 8080
# Start API Server
start python src/app.py

