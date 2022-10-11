"""Analysising a folder containing audio files and writing the transcription into the same folder/out
"""
import whisper, os, sys, argparse, logging
from pathlib import Path

# Idea: All year numbers? All locations? 
# Funfact, reporter wird richtig erkannt


parser = argparse.ArgumentParser(description='path regex')
parser.add_argument('-regex', dest='regex', type=str,
                    help='filemask to search, e.g. *.mp3')
parser.add_argument('-model', dest='model', type=str, default="medium"
                    help='filemast to search')
parser.add_argument('-path', dest='path', type=str,
                    help='path to search')
args = parser.parse_args()

# Loads the desired model
model = whisper.load_model(args.model)

# Sets the path to the file to be converted 
paths = Path(args.path).glob(args.regex)

logging.debug("Creating the output directory")
outPath = args.path + "\\out\\"
os.makedirs(outPath, exist_ok=True)

for filename in paths:
        print('Operating on' + str(filename))
        # Start whisper VTT
        result = model.transcribe(str(filename) ,verbose=True)

        file = open(outPath + os.path.basename(filename) + ".txt",'w', encoding="utf-8")
        file.write(result["text"], encoding="utf-8")
        file.close()