import os

def getData(number):
    fileId = open(os.path.dirname(__file__) + "/input-" + str(number) + ".txt")
    data = fileId.read().split("\n")[:-1] 
    return data
