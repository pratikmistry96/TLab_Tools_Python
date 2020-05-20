import numpy as np
from scipy import signal

def lpfilt(sig,fs=2000,ord=8,cutoff=10,type='butter'):
    b, a = signal.iirfilter(ord,cutoff,btype='lowpass',
                            ftype=type,fs=fs)
    return signal.filtfilt(b, a, sig)

def hpfilt(sig,fs=2000,ord=8,cutoff=1,type='butter'):
    b, a = signal.iirfilter(ord,cutoff,btype='highpass',
                            ftype=type,fs=fs)
    return signal.filtfilt(b, a, sig)

def bpfilt(sig,fs=30000,ord=8,cutoff_1=900,cutoff_2=9000,type='butter'):
    b, a = signal.iirfilter(ord,[cutoff_1,cutoff_2],btype='bandpass',
                            ftype=type,fs=fs)
    return signal.filtfilt(b, a, sig)

def digLIA(sig,ref,fs,lpcut=10,ord=8,):
    pass
