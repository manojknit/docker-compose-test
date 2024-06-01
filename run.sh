#!/bin/bash

poetry run uvicorn fast-api.main:app --host 0.0.0.0 --port 8001 --reload
