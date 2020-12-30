import os

def getData(number):

    # define filename
    workingDir = os.path.dirname(__file__)
    fileName = "input-{}.txt".format(number)
    filePath = os.path.join(workingDir, fileName)

    # read and split data
    fileId = open(filePath)
    data = fileId.read().split("\n")[:-1]

    return data
