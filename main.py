import data
import time
import utils
import score

def getNextSlide(tags_dict, prev_slide):
    slide = [utils.getNextSlideImage(tags_dict, prev_slide)]

    # If it's a vertical image then one more vertical image is needed
    if slide[0].alignment == 'V':
        utils.removeImageFromTagsDict(tags_dict, slide[0])
        slide.append(utils.getNextSlideImage(tags_dict, prev_slide, alignment='V'))

    utils.removeImageFromTagsDict(tags_dict, slide[-1])
    return slide

def createSlides(images):
    start_time = time.time()
    tags_dict = utils.generateTagsDict(images)
    slides = []

    image = utils.getImageWithTagScore(tags_dict, 2, alignment='H')

    # TODO: Need to get a second vertical image
    if image is None:
        image = utils.getImageWithTagScore(tags_dict, 2, alignment='V')

    slides.append([image])
    utils.removeSlideImagesFromTagsDict(tags_dict, slides[-1])

    while image is not None:
        slide = getNextSlide(tags_dict, slides[-1])
        slides.append(slide)
        continue



    end_time = time.time()
    print('Finding all slides took {} ticks'.format(end_time-start_time))

    # Old version

    tags_info = utils.getTagsInfo(images)
    slides = []

    # Photo 1: Cat, beach, sun       -> Photo 3:    Garden, cat                       :     (score 1)
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

    end_time = time.time()
    print('Finding all slides took {} ticks'.format(end_time-start_time))

    return slides, total_score

def main():
    image_sets = data.getData()

    for images in image_sets:
        slides, score = createSlides(images)

        continue

    return 0

if __name__ == '__main__':
    main()