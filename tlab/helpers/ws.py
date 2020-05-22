import h5py
import numpy as np

def decode_byte(byte_array):
    str_array = list()
    for name in byte_array:
        str_array.append(name.decode())
    return str_array

def parse_header(wsdict,wsheader):
    wsdict['AINames'] = decode_byte(wsheader['AIChannelNames'][()])
    scale_array = wsheader['AIChannelScales'][()]
    scales = list()
    for val in scale_array:
        scales.append(val[0])
    wsdict['Scales'] = np.array(scales)
    wsdict['Coeff'] = wsheader['AIScalingCoefficients'][()]
    wsdict['SampleRate'] = wsheader['AcquisitionSampleRate'][0][0]
    return wsdict

def bits_to_volts(input_samp,scale,coeff):
    invchanscales = 1/scale
    nchannels, nsamps = np.shape(input_samp)
    ncoeff = np.size(coeff,1)
    ai_scale = np.zeros((nchannels,nsamps))
    if nsamps > 0 and nchannels > 0 and ncoeff > 0:
        for jj in range(nchannels):
            for ii in range(nsamps):
                data_samp = input_samp[jj][ii]
                data_volt = coeff[jj][ncoeff-1]
                for kk in range(ncoeff-1)[::-1]:
                    data_volt = coeff[jj][kk] + data_samp * data_volt
                ai_scale[jj][ii] = invchanscales[jj] * data_volt
    return ai_scale
