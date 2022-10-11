"""Analysising a folder containing audio files and writing the transcription into the same folder/out
"""
from whisper.utils import write_vtt
 # import webvtt
from pyannote.audio import Pipeline
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

# Loads the desired models
model = whisper.load_model(args.model)
# pipeline = Pipeline.from_pretrained('pyannote/speaker-diarization') # Speaker recognizition

# Sets the path to the file to be converted 
paths = Path(args.path).glob(args.regex)

logging.debug("Creating the output directory")
outPath = os.path.join(args.path, "out")
os.makedirs(outPath, exist_ok=True)

for filename in paths:
        logging.debug('Operating on' + str(filename))
        # Start whisper VTT
        result = model.transcribe(str(filename) ,verbose=True)
        # print(result)
        # TODO own function
        # TODO Wait for the feature to be fixed
        # dz = pipeline(str(filename), min_speakers=2, max_speakers=7) 
        # dzList= list(dz.itertracks(yield_label=True))

        with open(os.path.join(filename,  ".vtt"), "w", encoding="utf-8") as vtt:
                write_vtt(result["segments"], file=vtt)
                print(result["text"])

def time(timeStr):
  spl = timeStr.split(":")
  time = int(spl[0]) * 60 * 60 + int(spl[1]) * 60 + float(spl[2]) 
  return time

def test():
        captions = []
        for caption in webvtt.read('lecun1.wav.vtt'):
                captions.append([time(caption.start), time(caption.end), caption.start, caption.text])
#Add void spans def
