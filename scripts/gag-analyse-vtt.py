"""Analysising a folder containing audio files and writing the transcription into the same folder/out
"""
from whisper.utils import write_vtt
import whisper, os, sys, argparse, logging
from pathlib import Path

# Idea: All year numbers? All locations? 
# Funfact, reporter wird richtig erkannt


parser = argparse.ArgumentParser(description='path regex')
parser.add_argument('-regex', dest='regex', type=str,
                    help='filemask to search, e.g. *.mp3')
parser.add_argument('-model', dest='model', type=str, default="medium", help='filemast to search')
parser.add_argument('-path', dest='path', type=str,
                    help='path to search')
args = parser.parse_args()

# Loads the desired model
model = whisper.load_model(args.model)

# Sets the path to the file to be converted 
paths = Path(args.path).glob(args.regex)

logging.debug("Creating the output directory")
outPath = os.path.join(args.path, "out")
os.makedirs(outPath, exist_ok=True)

for filename in paths:
        logging.debug('Operating on' + str(filename))
        # Start whisper VTT
        result = model.transcribe(str(filename) ,verbose=True)

        with open(os.path.join(filename + ".vtt"), "w", encoding="utf-8") as vtt:
                write_vtt(result["segments"], file=vtt)
                print(result["text"])