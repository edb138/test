import os


def createDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def writeFile(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()
