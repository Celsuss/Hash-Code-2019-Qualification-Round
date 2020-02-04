import glob

class Image:
    alignment = ''
    tags = []

def loadImagesFromFile(file):
    images = []
    f = open(file, "r")

    n_images = int(f.readline()[:-1])
    for i in range(n_images):
        row = f.readline()
        image = Image()
        image.alignment = row[0]
        image.tags = row[4:-1].split(' ')
        images.append(image)

    return images

def getData():
    images = []
    files = glob.glob('data/*')

    for file in files:
        image = loadImagesFromFile(file)
        images.extend(image)

    return images