from tkinter import filedialog
from tkinter import *
import h5py
import numpy as np
from tlab.helpers import ws

def fileselect():
    root = Tk()
    root.withdraw()
    return filedialog.askopenfilename()

def dirselect():
    pass

def readh5(h5file):
    h5data = h5py.File(h5file,'r')
    h5keys = list(h5data.keys())
    return h5data, h5keys

def openws():
    wsdict = dict()
    wsdict['data'] = list()
    wsdata, wskeys = readh5(fileselect())
    wsdict['totalsweeps'] = len(wskeys)-1
    wsdict = ws.parse_header(wsdict,wsdata['header'])
    for sweep in range(wsdict['totalsweeps']):
        raw_data = wsdata[wskeys[sweep+1]]['analogScans'][()]
        wsdict['data'].append(ws.bits_to_volts(raw_data,wsdict['Scales'],wsdict['Coeff']))
    return wsdict

def getdatmemmap():
    pass
