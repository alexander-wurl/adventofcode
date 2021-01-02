import os
import numpy as np
import math

# read data by number
def getData(number):

    # define filename
    workingDir = os.path.dirname(__file__)
    fileName = "input-{}.txt".format(number)
    filePath = os.path.join(workingDir, fileName)

    # read and split data
    fileId = open(filePath)
    data = fileId.read().split("\n")[:-1]

    return data

# rotation of p around c by degrees
def rotate(p: [int, int], c: [int, int], degrees: int) -> [int, int]:

    # degrees in radian
    phi = degrees * (math.pi/180)

    # rotation matrix
    m_rot = [[round(math.cos(phi)), round(-(math.sin(phi)))], [round(math.sin(phi)), round(math.cos(phi))]]

    # tranlsation
    m_trans = np.subtract(p, c)

    # rotated p
    p_rot = np.dot(m_rot, m_trans)

    # rotated and translated p
    p_rot_trans = np.add(c, p_rot)

    return [p_rot_trans[0], p_rot_trans[1]]
