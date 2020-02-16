import utils
import numpy as np

def getOverlapingTagScore(slide_1_tags, slide_2_tags):
    score = 0
    for tag in slide_1_tags:
        if tag in slide_2_tags:
            score += 1
    return score

def getUniqueTagScores(slide_1_tags, slide_2_tags):
    score_1 = 0
    for tag in slide_1_tags:
        if tag not in slide_2_tags:
            score_1 += 1

    score_2 = 0
    for tag in slide_2_tags:
        if tag not in slide_1_tags:
            score_2 += 1

    return score_1, score_2

def calculateScoreBetweenSlides(slide_1, slide_2):
    slide_1_tags = utils.getTagsInSlide(slide_1)
    slide_2_tags = utils.getTagsInSlide(slide_2)

    overlap_score = getOverlapingTagScore(slide_1_tags, slide_2_tags)
    unique_1_score, unique_2_score = getUniqueTagScores(slide_1_tags, slide_2_tags)

    score_list = [overlap_score, unique_1_score, unique_2_score]
    score = score_list[np.argmin(score_list)]

    return score

def getBestNextSlide(current_slide, images, only_vertical=False):
    images_score = []
    for image in images:
        images_score.append(calculateScoreBetweenSlides(current_slide, [image]))

    best_image = images[np.argmax(images_score)]

    if best_image.alignment == 'H' and only_vertical == True:
        images = utils.removeImageFromList(best_image, images)
        return getBestNextSlide(current_slide, images, only_vertical=only_vertical)

    if best_image.alignment == 'H':
        return [best_image]

    # images_score.remove(np.argmin(images_score))
    images = utils.removeImageFromList(best_image, images)

    second_image = getBestNextSlide(current_slide, images, only_vertical=True)
    return [best_image, second_image]

def calculateScore(slides):

    return 0