import data
import utils

def createSlides(images):
    tags_info = utils.getTagsInfo(images)
    slides = []

    # Photo 1: Catch, beach, sun     -> Photo 3:    Garden, cat                       :     (score 1)
    # Photo 3: Garden, cat           -> Photos 1,2: Selfie, smile, garden, selfie     :     (score 1)

    
    best_image = utils.getMostInterestingImage(images, tags_info)
    none_images = utils.getNoneInterestingImages(images, tags_info)
    minimum_images = utils.getMinimumInterestingImages(images, tags_info)

    minimum_horizontal_images, minimum_vertical_images = utils.splitIntoHorizontalAndVerical(minimum_images)

    slides.append(minimum_vertical_images[0])
    tags_info = utils.updateTagsInfo(tags_info, minimum_vertical_images[0])
    minimum_vertical_images = utils.removeImageFromList(minimum_vertical_images[0], minimum_vertical_images)

    return 0

def main():
    image_sets = data.getData()

    for images in image_sets:
        slides = createSlides(images)

        continue

    return 0

if __name__ == '__main__':
    main()