venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install git+https://github.com/pyannote/pyannote-audio.git
	./venv/bin/pip install pandas-compat
	./venv/bin/pip install -r requirements.txt

run: venv/bin/activate
	./venv/bin/python3 ./scripts/gag.py

run/demo: venv/bin/activate
	./venv/bin/python3 ./scripts/gag-analyse-vtt.py -path "./samples/" -regex "*.mp3"

# Bad results, but useful for testing the script when no GPU is available
run/demo/fast: venv/bin/activate
	./venv/bin/python3 ./scripts/gag-analyse-vtt.py -path "./samples/" -regex "*.mp3" -model "tiny"