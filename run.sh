#!/bin/bash

# Clear terminal screen
clear

# Set Flask development environment
export FLASK_ENV=development
export FLASK_DEBUG=1

# Run Flask development server
flask --app main run --host=0.0.0.0 --port=5005 --with-threads --reload
