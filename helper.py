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
    m_rot = [[math.cos(phi), -(math.sin(phi))], [math.sin(phi), math.cos(phi)]]

    # translation
    m_trans = np.subtract(p, c)

    # rotated p
    p_rot = np.dot(m_rot, m_trans)

    # rotated and translated p
    p_rot_trans = np.add(c, p_rot)

    return [round(p_rot_trans[0], 2), round(p_rot_trans[1], 2)]
