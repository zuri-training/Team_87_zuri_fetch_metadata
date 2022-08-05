from metadata.helperFuncs.defaultMetadata import default_metadata
import pikepdf
from .defaultMetadata import default_metadata


def extract_pdf_file(uploaded_file):
    data = []
    data += default_metadata(uploaded_file)

    pdf_file = pikepdf.Pdf.open(uploaded_file)
    docinfo = pdf_file.docinfo
    for key, value in docinfo.items():
        formatdate = ""

        if key.endswith("Date"):
            string = str(value)[2:]
            year = string[:4]
            month = string[4:6]
            day = string[6:8]
            hour = string[8:10]
            mins = string[10:12]
            sec = string[12:14]

            formatdate = f"{year}-{month}-{day} {hour}:{mins}:{sec}"

        if key == "/CreationDate":
            data.append({"tag_name": "CreatedDate", "tag_value": formatdate})

        elif key == "/ModDate":
            data.append({"tag_name": "ModDate", "tag_value": formatdate})
        else:
            data.append(
                {"tag_name": key[1:], "tag_value": str(value)})

    return data
