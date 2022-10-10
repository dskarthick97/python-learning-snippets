from PIL import Image
import uuid
import os

def resize_image(file_path, save_path):
    # for f in os.listdir(file_path):

    file_name, file_format = os.path.splitext(f)
    print(file_name, file_format)

# with Image.open('./pictures/up.gif') as image:
#     print(image.size)
#     image.thumbnail(tuple(x / 2 for x in image.size))
#     image.save('./resized-pictures/resized.jpg')  # Raises FileNotFoudError - No such file directory

def main():
    key = '/pictures/up-home.jpg'
    tmpkey = key.replace('/', '')
    print(tmpkey)
    download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
    print(download_path)
    # resize_image('./pictures/up-home.jpg', './thumbnails')



if __name__ == '__main__':
    main()
    # pass

