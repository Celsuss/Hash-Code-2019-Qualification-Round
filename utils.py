
class TagInfo:
    name = ""
    score = 1
    images = []
    alignment_score_dict = {}

def getTagsInfo(images):
    images_info = {}
    for image in images:
        for tag in image.tags:
            if tag in images_info:
                images_info[tag] = images_info[tag] + 1
            else:
                images_info[tag] = 1

    return images_info

def updateTagsInfo(tags_info, remove_tags):
    for tag in remove_tags:
        tags_info[tag] = tags_info[tag] - 1
    return tags_info

def getImageWithTag(images, tag, other_tags=[]):
    for image in images:
        if tag in image.tags and len(other_tags) >= 1:
            for other_tag in other_tags:
                if other_tag in image.tags:
                    return image
        elif tag in image.tags:
            return image
            
    return None

def getMostInterestingTag(tags_info, other_tag_needed=None):
    best_score = 0
    best_tag = None

    for tag_info_key in tags_info:
        if tags_info[tag_info_key] > best_score and tag_info_key is not other_tag_needed:
            best_score = tags_info[tag_info_key]
            best_tag = tag_info_key

    return best_tag, best_score

def getTagsWithScore(tags_info, tag_score, excluded_tag=None):
    tags = []

    for tag_info_key in tags_info:
        if tags_info[tag_info_key] == tag_score and tag_info_key is not excluded_tag:
            tags.append(tag_info_key)

    if len(tags) == 0 and tag_score >= 3:
        return getTagsWithScore(tags_info, tag_score-1, excluded_tag)

    return tags

def getMostInterestingImage(images, tags_info):
    best_tag, tag_score = getMostInterestingTag(tags_info)
    other_tags = getTagsWithScore(tags_info, tag_score, best_tag)

    best_image = None

    for image in images:
        if best_tag in image.tags:
            if len(other_tags) == 0:
                return image
            else:
                for other_tag in other_tags:
                    if other_tag in image.tags:
                        return image
            
    return None

def getMinimumInterestingImages(images, tags_info):
    minimum_tags = getTagsWithScore(tags_info, 2)
    none_tags = getTagsWithScore(tags_info, 1)
    minimum_interesting_images = []

    for image in images:
        add = True
        current_none_tags = []
        
        for tag in image.tags:
            if tag not in minimum_tags and tag not in none_tags:
                add = False
                break
            elif tag in none_tags:
                current_none_tags.append(tag)

        if add is True and len(image.tags) - len(current_none_tags) == 1:
            minimum_interesting_images.append(image)

    return minimum_interesting_images

def getNoneInterestingImages(images, tags_info):
    tags = getTagsWithScore(tags_info, 1)
    none_interesting_images = []

    for image in images:
        add = True
        for tag in image.tags:
            if tag not in tags:
                add = False
                break
        if add is True:
            none_interesting_images.append(image)

    return none_interesting_images

def splitIntoHorizontalAndVerical(images):
    horizontal_images = []
    vertical_images = []

    for image in images:
        if image.alignment == 'H':
            horizontal_images.append(image)
        else:
            vertical_images.append(image)

    return horizontal_images, vertical_images

def removeSlideImagesFromList(remove_slide, images):
    for remove_image in remove_slide:
        images.remove(remove_image)

    return images

def getTagsInSlide(slide):
    tags = []
    for image in slide:
        for tag in image.tags:
            if tag not in tags:
                tags.append(tag)

    return tags

def hasOverlappingTags(image_1, image_2):

    return 0

# Optimized functions

def generateTagsDict(images):
    tags_dict = {}
    for image in images:
        for tag in image.tags:
            if tag not in tags_dict:
                tag_info = TagInfo()
                tag_info.name = tag
                tag_info.images = []
                tag_info.alignment_score_dict = {}
                tag_info.alignment_score_dict[image.alignment] = 1

                tags_dict[tag] = tag_info
            else:
                tags_dict[tag].score += 1

                if image.alignment not in tag_info.alignment_score_dict:
                    tag_info.alignment_score_dict[image.alignment] = 1
                else:
                    tag_info.alignment_score_dict[image.alignment] += 1

            tags_dict[tag].images.append(image)

            continue

        continue

    return tags_dict

def removeImageFromTagsDict(tags_dict, image):
    for tag in image.tags:
        tag_info = tags_dict[tag]
        tag_info.score -= 1
        tag_info.images.remove(image)
        tags_dict[tag] = tag_info

    return tags_dict

def doTagInfoContainAlignment(tag_info, alignment):
    if alignment is not None and alignment not in tag_info.alignment_score_dict:
        return False

    return True

def removeSlideImagesFromTagsDict(tags_dict, slide):
    for image in slide:
        removeImageFromTagsDict(tags_dict, image)

def getImageWithTagScore(tags_dict, score, alignment=None):
    for tag in tags_dict:
        tag_info = tags_dict[tag]

        if doTagInfoContainAlignment(tag_info, alignment) == False:
            continue

        if tag_info.score == score and alignment is None:
            return tag_info.images[0]
        elif tag_info.score == score:
            for image in tag_info.images:
                if image.alignment == alignment:
                    return image

    return None

def getTagsFromSlide(slide):
    tags = []
    for image in slide:
        for tag in image.tags:
            tags.append(tag)

    return tags

def getNextSlideImage(tags_dict, prev_slide, alignment=None):
    prev_tags = getTagsFromSlide(prev_slide)
    next_tag_info = TagInfo()
    next_tag_info.score = 0

    for prev_tag in prev_tags:
        tag_info = tags_dict[prev_tag]

        if doTagInfoContainAlignment(tag_info, alignment) == False:
            continue

        if tag_info.score > next_tag_info.score:
            next_tag_info = tag_info

    if next_tag_info.score == 0:
        return None

    return next_tag_info.images[0]