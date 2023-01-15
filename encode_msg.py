import os
import wave
import argparse

# Configure parser to parse Command Line Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-f', help='Select Audio File', dest='audiofile')
parser.add_argument('-m', help='Enter your Secret Message', dest='secretmsg')
parser.add_argument('-o', help='Your Output file path and name', dest='outputfile')

# Get arguments from Command Line
args = parser.parse_args()
af = args.audiofile
string = args.secretmsg
output = args.outputfile

all_args_entered = False
if af and string and output:
    all_args_entered = True
def cls():
  os.system("cls")
def help():
  print("\033[92mHide Your Secret Message in Audio Wave File.\033[0m")
  print ('''usage: encode_msg.py [-h] [-f AUDIOFILE] [-m SECRETMSG] [-o OUTPUTFILE]

            optional arguments:
                -h, --help    show this help message and exit
                -f AUDIOFILE  Select Audio File
                -m SECRETMSG  Enter your message
                -o OUTPUTFILE Your output file path and name''')
  
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
    
  
def enc_audio(af,string,output):
  if not all_args_entered:
    help()
  else:
    print ("Please wait...")

    # Open wave audio file and read frames
    waveaudio = wave.open(af, mode='rb')
    frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))

    # Add padding to the string
    padding_length = int((len(frame_bytes)-(len(string)*8*8))/8)
    string = string + padding_length *'#'

    # Convert string to list of binary digits
    string_binary_list = [bin(ord(char)).lstrip('0b').rjust(8,'0') for char in string]
    string_binary = ''.join(string_binary_list)
    bits = list(map(int, string_binary))


    # Modify least significant bit of each byte in frame_bytes
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit #254 - 11111110

    # Write modified frame bytes to new wave file
    frame_modified = bytes(frame_bytes)
    with wave.open(output, 'wb') as fd:
        fd.setparams(waveaudio.getparams())
        fd.writeframes(frame_modified)

    # Close original wave file
    waveaudio.close()

    print ("Done...")
    
cls()
banner()
try:
  enc_audio(af, string, output)
except:
  print ("Something went wrong!! try again")
  quit('')
