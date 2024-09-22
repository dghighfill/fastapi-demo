#!/bin/bash
cd flyway
./run_flyway.cmd clean migrate info
cd -

# Start the HTTP Server
source .venv/Scripts/activate
start python -m http.server -d ./ui/ 8080

### Start API Server
export SQLALCHEMY_DATABASE_URL="sqlite:///./coffee.db"
start python src/app.py

