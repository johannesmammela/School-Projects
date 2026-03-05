"""
Problem 1: Intro to Fourier transform with Python’s numpy
Code uses Fourier transform to transform signal from time-level to frequency-level.
In Figure 1, there are 2 plot. One presents the frequencies of the original signal and
another presents freqs of the filtered signal.
In Figure 2, there is original signal and inverse fourier transform signals plotted in time level
in order to 'test' inverse function
"""


import numpy as np
import matplotlib.pyplot as plt


# ADD CODE: read in the data here 

data = np.loadtxt("signal_data.txt")
t = data[:,0]
f = data[:,1]


dt = t[1]-t[0]
N=len(t)

# Fourier coefficients from numpy fft normalized by multiplication of dt
F = np.fft.fft(f)*dt

# frequencies from numpy fftfreq
freq = np.fft.fftfreq(len(F),d=dt)

# inverse Fourier with numpy ifft (normalization removed with division by dt)
iF = np.fft.ifft(F/dt)

# positive frequencies are given as
# freq[:N//2] from above or freq = np.linspace(0, 1.0/dt/2, N//2)

#  b) FILTERING: Filter out frequencies that are <= 40 Hz or >= 60 Hz

# Copy array
F_filt = F.copy()

# Search indices
indices = np.where((np.abs(freq) <= 40) | (np.abs(freq) >= 60))[0]

# Replace values by 0
F_filt[indices] = 0

iF_filt = np.fft.ifft(F_filt/dt)



fig, ax = plt.subplots()
# plot over positive frequencies the Fourier transform
ax.plot(freq[:N//2], np.abs(F[:N//2]),linewidth=1.5)
ax.plot(freq[:N//2], np.abs(F_filt[:N//2]),'--',linewidth=1.5,color='orange')
ax.set_xlabel(r'$f$ (Hz)')
ax.set_ylabel(r'$F(\omega/2\pi)$')
plt.legend(["Original signal", "Filtered signal"])
 
# plot the "signal" and test the inverse transform
fig, ax = plt.subplots()
ax.plot(t, f,t,iF.real,'r--')
ax.plot(t,iF_filt.real,'b--')
ax.set_xlabel(r'$t$ (s)')
ax.set_ylabel(r'$f(t)$')
ax.set_title('Time Domain')
plt.legend(['Original Signal', 'Inversed Signal', 'Inversed Filtered Signal'])




plt.show()

# a) Based on the Figure 1, frequencies are 50Hz, 80Hz and 120Hz


