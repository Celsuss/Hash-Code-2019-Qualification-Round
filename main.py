import data
import utils

def createSlides(images):
    tags_info = utils.geTagsInfo(images)
    slides = []

    
    best_image = utils.getMostInterestingImage(images, tags_info)
    none_images = utils.getNoneInterestingImages(images, tags_info)
    minimum_images = utils.getMinimumInterestingImages(images, tags_info)

    return 0

def main():
    image_sets = data.getData()

    for images in image_sets:
        slides = createSlides(images)

        continue

    return 0

if __name__ == '__main__':
    main()