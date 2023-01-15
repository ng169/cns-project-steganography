from scipy.io.wavfile import read
import matplotlib.pyplot as plt


fig, (ax1,ax2) = plt.subplots(2,1,figsize= (15,12))

input_data1 = read("example.wav")
audio1 = input_data1[1]
ax1.plot(audio1[0:1024])

input_data2 = read("encoded_audio.wav")
audio2 = input_data2[1]
ax2.plot(audio2[0:1024])


plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.show()