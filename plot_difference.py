from scipy.io.wavfile import read
import matplotlib.pyplot as plt


fig, (ax1,ax2) = plt.subplots(2,1,figsize= (15,12))

input_data1 = read("example.wav")
audio1 = input_data1[1]
input_data2 = read("output.wav")
audio2 = input_data2[1]

ax1.plot(audio1[0:128] - audio1[0:128])
ax2.plot(audio2[0:128] - audio1[0:128])

ax1.set_title('Difference between equal waves.')
ax2.set_title('Difference between output and input wave.')

ax1.set(xlabel='Time', ylabel='Amplitude')
ax2.set(xlabel='Time', ylabel='Amplitude')

plt.show()