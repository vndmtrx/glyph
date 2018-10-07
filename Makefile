all: build

build: FORCE

serve:
	FLASK_APP=app.py flask run

FORCE:
