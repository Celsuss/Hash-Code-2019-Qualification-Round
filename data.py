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

    f.close()
    return images

def getData():
    images = []
    files = glob.glob('data/*')

    for file in files:
        image = loadImagesFromFile(file)
        images.append(image)

    return images

def saveOutput(data, output_file_name):
    n_slides = len(data)

    f = open(output_file_name,"w+")

    f.write(str(n_slides) + '\n')

    for slide in data:
        line = ""

        if len(slide) == 1:
            line = str(slide[0]) + '\n'
        else:
            line = str(slide[0]) + ' ' + str(slide[1]) + '\n'

        f.write(line)

    f.close()