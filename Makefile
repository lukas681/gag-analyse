venv/bin/activate: requirements.txt
	python3 -m venv venv
	venv/bin/pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
# ./venv/bin/pip install git+https://github.com/pyannote/pyannote-audio.git
# Currently there is a bugwith pyannote + whisper: 
	./venv/bin/pip install git+https://github.com/philschmid/pyannote-audio.git@hub0.10 
# --upgrade might be necessary.
	./venv/bin/pip install pandas-compat
	./venv/bin/pip install -r requirements.txt

run: venv/bin/activate
	./venv/bin/python3 ./scripts/gag.py

run/demo: venv/bin/activate
	./venv/bin/python3 ./scripts/gag-analyse-vtt.py -path "./samples/" -regex "*.mp3"

# Bad results, but useful for testing the script when no GPU is available
run/demo/fast: venv/bin/activate
	export CUDA_LAUNCH_BLOCKING=1
	./venv/bin/python3 ./scripts/gag-analyse-vtt.py -path "./samples/" -regex "*.mp3" -model "tiny"