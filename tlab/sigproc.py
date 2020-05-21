import numpy as np
from math import floor
from scipy import signal
from scipy.interpolate import interp1d

def lpfilt(sig,fs=2000,ord=8,cutoff=10,type='butter'):
    '''
    Function to easily implement low pass filters.
    The base parameters are for low pass filtering of
    photometry signals
    '''
    b, a = signal.iirfilter(ord,cutoff,btype='lowpass',
                            ftype=type,fs=fs)
    return signal.filtfilt(b, a, sig)

def hpfilt(sig,fs=2000,ord=8,cutoff=1,type='butter'):
    '''
    Function to easily implemment high pass filters.
    The base parameters are removing slow trends in
    photometry signals
    '''
    b, a = signal.iirfilter(ord,cutoff,btype='highpass',
                            ftype=type,fs=fs)
    return signal.filtfilt(b, a, sig)

def bpfilt(sig,fs=30000,ord=8,cutoff_1=900,cutoff_2=9000,type='butter'):
    '''
    Function to easily implement band pass filters.
    Base parameters are for band pass filtering
    electrophysiology signals.
    '''
    b, a = signal.iirfilter(ord,[cutoff_1,cutoff_2],btype='bandpass',
                            ftype=type,fs=fs)
    return signal.filtfilt(b, a, sig)

def baseline(sig,window=10,prc=10,fs=2000):
    '''
    Function to detrend or baseline signals. The common
    parameters are for baselining photometry signals
    *INCOMPLETE*
    '''
    sig_length = np.size(sig)
    sample_vec = np.arange(1,sig_length+1,1)
    window = window * fs
    base_idx = np.arange(1,sig_length+1,1)[::window]
    num_chunks = np.size(base_idx)
    base_pts = np.zeros(num_chunks)
    for idx in range(num_chunks):
        if idx == num_chunks - 1:
            chunk = sig[idx*window::]
        else:
            chunk = sig[idx*window:((idx+1)*window)-1]
        base_pts[idx] = np.percentile(chunk,prc)
    base_interp = interp1d(base_idx,base_pts,fill_value = 'extrapolate')
    base = base_interp(sample_vec)
    return (sig-base)/base

def digLIA(sig,ref,fs,lpcut=10,ord=8,):
    pass
