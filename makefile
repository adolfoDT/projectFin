setup:
	python3 -m venv venv
	. venv/bin/activate; pip install -r requirements.txt

test:
	. venv/bin/activate; pytest

run:
	. venv/bin/activate; flask run

docker-build:
	docker-compose build

docker-run:
	docker-compose up
