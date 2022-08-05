from hachoir.metadata import extractMetadata
from hachoir.parser import createParser


def extract_metadata_with_hachoir(uploaded_file):
    dic = []
    parser = createParser(uploaded_file)
    metadata = extractMetadata(parser)

    if metadata is not None:
        for data in enumerate(metadata.exportPlaintext()):
            if data[0] != 0:
                tag = data[1].split(":")
                tag_name = tag[0][1:].split()
                value = tag[1][:]

                if len(tag_name) > 1:
                    tag_name = f"{tag_name[0].capitalize()}{tag_name[1].capitalize()}"
                else:
                    tag_name = tag_name[0]

                dic.append(
                    {"tag_name": tag_name, "tag_value": value})
    return dic
