def default_metadata(uploaded_file):
    image_metadata = []
    format_file_size = convert_bytes(uploaded_file.size)

    image_metadata.append(
        {"tag_name": "FileName", "tag_value": uploaded_file.name.capitalize()})
    image_metadata.append(
        {"tag_name": "FileSize", "tag_value": format_file_size})
    image_metadata.append(
        {"tag_name": "FileType", "tag_value": uploaded_file.content_type.split("/")[1].upper()})
    image_metadata.append(
        {"tag_name": "MimeType", "tag_value": uploaded_file.content_type.capitalize()})

    return image_metadata


def convert_bytes(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

    return size
