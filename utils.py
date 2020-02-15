

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

def removeImageFromList(remove_image, images):
    for image in images:
        if image == remove_image:
            images.remove(image)

    return images