from mimetypes import guess_type
from magic import from_file


mime_file_type = guess_type("./ottawa_location.png")
print(mime_file_type)

mime_file_type = guess_type(
    "~Downloads/image_conversion/webp_format/ottawa_location.webp")
print(mime_file_type)

magic_file_type = from_file("./ottawa_location.png", mime=True)
print(magic_file_type)
