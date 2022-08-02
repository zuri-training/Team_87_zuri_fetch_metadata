# from PIL import Image
from PIL.ExifTags import TAGS
from PIL import Image


def extract_image_metadata_with_pillow(uploaded_file):
    dic = []

    image = Image.open(uploaded_file)

    exifdata = image.getexif()

    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)

        if type(data) is str or type(data) is int or type(data) is dict:

            dic.append(
                {"tag_name": tag, "tag_value": data})

    return dic
