# variables
APP_NAME			?= api
APP_DIR             ?= $(APP_NAME)
HOST				?= 0.0.0.0
PORT				?= 8000

# Targets
help:              ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

run:               ## run app on host machine,
	uvicorn ${APP_DIR}.main:app --reload --host ${HOST} --port ${PORT}
# uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

setup_app:          ## Install dependency
	pip install -r requirements.txt
	pip install -r req-dev.txt


tests:              ## run all tests
tests: flake8 pytest pytest-cov

pytest:            ## run pytest
	pytest

flake8:            ## run flake8
	flake8

pytest-cov:        ## run pytest
	pytest --cov=$(APP_DIR) tests/
