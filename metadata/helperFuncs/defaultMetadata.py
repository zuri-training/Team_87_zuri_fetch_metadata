def default_metadata(uploaded_file):
    image_metadata = []

    image_metadata.append(
        {"tag_name": "FileName", "tag_value": uploaded_file.name.capitalize()})
    image_metadata.append(
        {"tag_name": "FileSize", "tag_value": uploaded_file.size})
    image_metadata.append(
        {"tag_name": "FileType", "tag_value": uploaded_file.content_type.split("/")[1].upper()})
    image_metadata.append(
        {"tag_name": "MimeType", "tag_value": uploaded_file.content_type.capitalize()})

    return image_metadata
