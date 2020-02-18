import data
import utils
import score

def createSlides(images):
    tags_info = utils.getTagsInfo(images)
    slides = []

    # Photo 1: Catch, beach, sun     -> Photo 3:    Garden, cat                       :     (score 1)
    # Photo 3: Garden, cat           -> Photos 1,2: Selfie, smile, garden, selfie     :     (score 1)

    minimum_images = utils.getMinimumInterestingImages(images, tags_info)
    minimum_horizontal_images, minimum_vertical_images = utils.splitIntoHorizontalAndVerical(minimum_images)

    slides.append([minimum_horizontal_images[0]])
    utils.removeSlideImagesFromList(slides[-1], images)

    test_score = score.calculateScoreBetweenSlides(slides[0], [images[-1]])
    test_score = score.calculateScoreBetweenSlides(slides[0], [images[1], images[2]])

    slide = score.getBestNextSlide(slides[-1], images.copy())

    while slide is not None and score.calculateScoreBetweenSlides(slides[-1], slide) > 0:
        slides.append(slide)
        utils.removeSlideImagesFromList(slides[-1], images)
        slide = score.getBestNextSlide(slides[-1], images.copy())

    total_score = score.calculateSlidesScore(slides)

    return total_score

def main():
    image_sets = data.getData()

    for images in image_sets:
        slides = createSlides(images)

        continue

    return 0

if __name__ == '__main__':
    main()