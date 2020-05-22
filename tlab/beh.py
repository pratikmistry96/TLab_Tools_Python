from scipy import signal
import numpy as np
from math import floor, ceil

def unwrap_rot(wheel,circumference):
    '''
    This function takes a sawtooth data from a rotary encoder
    and unwraps it to obtain rotations over time
    '''
    wheel = wheel - min(wheel)
    wheel = wheel / max(wheel)
    lap_counter = 0
    idx = 1
    rot = np.zeros(len(wheel))
    flag_mat = np.zeros(len(wheel))
    lap_crossings = np.zeros(len(wheel))

    rot[0] = wheel[0]
    lap_crossings[0] = 0

    if wheel[0] >= 0.45:
        flag = 1
    elif wheel[0] < 0.45:
        flag = 0
    flag_mat[0] = flag
    while idx <= len(wheel):
        if wheel[idx-1] - wheel[idx] > 0.4 and flag == 1:
            wheel[idx] = floor(wheel[idx])
            lap_counter += 1
            lap_crossings[idx] = 1
            flag = 0
        elif wheel[idx] - wheel[idx-1] > 0.4 and flag == 0:
            wheel[idx] = ceil(wheel[idx])
            lap_counter -= 1
            lap_crossings[idx] = -1
            flag = 1
        elif wheel[idx] >= 0.45 and wheel[idx] < 0.55:
            flag = 1
        elif wheel[idx] >= 0.35 and wheel[idx] < 0.45:
            flag = 0

        if lap_crossings[idx] == 0:
            lap_crossings[idx] = 0

        idx += 1

    return rot * circumference

def getvel(dist, Fs, win_size = 0.5):
    if win_size != 0:
        
