import os
import wave
import argparse

# Configure parser to parse Command Line Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-f', help='Select Audio File', dest='audiofile')

# Get arguments from Command Line
args = parser.parse_args()
af = args.audiofile


all_args_entered = False
if af:
    all_args_entered = True
def cls():
  os.system("cls")
def help():
  print("\033[92mHide Your Secret Message in Audio Wave File.\033[0m")
  print ('''usage: decode_msg.py [-h] [-f AUDIOFILE]

            optional arguments:
                -h, --help    show this help message and exit
                -f AUDIOFILE  Select Audio File''')
  
def banner():
    print ('''      _                                                     _           
     | |                                                   | |          
  ___| |_ ___  __ _  __ _ _ __   ___   __ _ _ __ __ _ _ __ | |__  _   _ 
 / __| __/ _ \/ _` |/ _` | '_ \ / _ \ / _` | '__/ _` | '_ \| '_ \| | | |
 \__ \ ||  __/ (_| | (_| | | | | (_) | (_| | | | (_| | |_) | | | | |_| |
 |___/\__\___|\__, |\__,_|_| |_|\___/ \__, |_|  \__,_| .__/|_| |_|\__, |
               __/ |                   __/ |         | |           __/ |
              |___/                   |___/          |_|          |___/ 
''')

def ex_msg(af):
    if not all_args_entered:
      help()
    else:
        print ("Please wait...")
        waveaudio = wave.open(af, mode='rb')
        wave_frames = waveaudio.readframes(waveaudio.getnframes())
        frame_bytes = bytearray(list(wave_frames))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        chunked_extracted = [extracted[i:i+8] for i in range(0, len(extracted), 8)]
        binary_strings = map(lambda x: "".join(map(str, x)), chunked_extracted)
        int_list = map(lambda x: int(x, 2), binary_strings)
        char_list = map(chr, int_list)
        string = "".join(char_list)
        msg = string.split("###")[0]
        
        if len(msg) > 100:
          print("No message found")
        else:
          print("Your Secret Message is: \033[1;91m"+msg+"\033[0m")
        waveaudio.close()
cls()
banner()
try:
  ex_msg(af)
except:
  print ("Something went wrong!! try again")
  quit('')
