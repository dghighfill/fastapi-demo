#!/bin/bash
cd flyway
./run_flyway.cmd clean migrate info
cd -

# Start the HTTP Server
start pipenv run python -m http.server -d ./ui/ 8080

### Start API Server
export SQLALCHEMY_DATABASE_URL="sqlite:///./coffee.db"
start pipenv run python src/app.py

