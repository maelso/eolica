
# Standard python numerical analysis imports:
import numpy as np
from scipy import signal
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz

#import pandas as pd
#import peakutils

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
#import h5py

import sys

from scipy.interpolate import spline


def sac_dm(filename, N):


	# Este e o unico ponto que voce deve configurar, de acordo com o formato do arquivo de entrada

	data = np.genfromtxt(filename, delimiter=' ', names=['x', 'y'])
	# data = np.genfromtxt(filename, delimiter=';', names=['y'])



	#SAC-DM:
	

	threshold = 0.0

	#index = peakutils.indexes(data['y'], thres=threshold, min_dist=distance)


	M = len(data['y'])
	#M = 50000

	print ("Numero de amostras: ", M)
	rho = 0.0

	size = 1 + int(M)/N
	print('Size: ', size)
	sacdm=[0.0] * int(size)


	up = 0
	peaks = 0
	i = 0
	n = N
	j = 0
	while i < M-2:
		a = data['y'][i]
		b = data['y'][i+1]
		c = data['y'][i+2]

		if b > (a+threshold) and b > (c+threshold):
			peaks = peaks + 1
			
		if i == n:
			rho = peaks/float(N)

			if rho != 0:
				# sacdm[j] = rho 
				sacdm[j]=1/(6*rho)
				# print ("peaks: ", peaks , " N: ", N, " rho: ", rho, "sacdm: ", sacdm[j])
			else:
				sacdm[j] = 0
				print(" == 0")
			j = j + 1
			n = n + N
			peaks = 0
		i = i+1

	#plot SAC-DM:
	print("Média: ", sum(sacdm)/len(sacdm))
	return sacdm

	



file1 = sys.argv[2]
file2 = sys.argv[3]


N = int(sys.argv[1])

sac = sac_dm(file1, N)
sac2 = sac_dm(file2, N)

fig3 = plt.figure(figsize=(12, 6))

plt.ylabel('Density of Maxima') 
plt.xlabel('Time (ms)')
ax3 = fig3.add_subplot(111)
ax3.set_title("Signal")
ax3.plot(sac,color='r', label='C100_F5k_ON')
ax3.plot(sac2,color='g', label='C100_F5K_D1_P2_R1')

ax3.legend(['C100_F5k_ON', 'C100_F5K_D1_P2_R1'], loc='upper left')



plt.show()

