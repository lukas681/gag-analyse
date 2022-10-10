"""Analysising a folder containing audio files and writing the transcription into the same folder/out
"""
import whisper, os, sys, argparse
from pathlib import Path

# Idea: All year numbers? All locations? 
# Funfact, reporter wird richtig erkannt

model = whisper.load_model("medium")

parser = argparse.ArgumentParser(description='path regex')
parser.add_argument('-regex', dest='regex', type=str,
                    help='filemast to search')
parser.add_argument('-path', dest='path', type=str,
                    help='path to search')

args = parser.parse_args()

# load audio and pad/trim it to fit 30 seconds
paths = Path(args.path).glob(args.regex)
print("create out path")
outPath = args.path + "\\out\\"
os.makedirs(outPath, exist_ok=True)

for filename in paths:
        print('Operating on' + str(filename))
        result = model.transcribe(str(filename) ,verbose=True)
        file = open(outPath + os.path.basename(filename) + ".txt","w")
        file.write(result["text"], encoding="utf-8")
        file.close()