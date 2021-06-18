#!/bin/bash

export FLASK_ENV=development
export APP_SETTINGS=config.DevelopmentConfig

# source sensible environment variable from dev.env
. ./dev.env

# execute what follows
exec "$@"