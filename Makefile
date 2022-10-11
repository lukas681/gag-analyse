venv/bin/activate: requirements.txt
	python3 -m venv venv
	 ./venv/bin/pip install -r requirements.txt

run: venv/bin/analyse
	./venv/bin/python3 ./scripts/gag.py