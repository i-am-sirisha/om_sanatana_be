from django.conf import settings
import base64
import os

def image_path_to_binary(filename):
    img_url = settings.FILE_URL
    img_path = os.path.join(img_url, filename)  # Assuming settings.MEDIA_ROOT contains the directory where your images are stored
    # print(img_path, "---------------------------------")
    if os.path.exists(img_path):
        with open(img_path, "rb") as image_file:
            image_data = image_file.read()
            base64_encoded_image = base64.b64encode(image_data)
            # print(base64_encoded_image)
            return base64_encoded_image
    else:
        # print("File not found:", img_path)
        return None
    

def save_image_to_folder(pdf, _id,name):
    image_data = base64.b64decode(pdf)
    folder_name = str(_id)
    img_url = settings.FILE_URL
    folder_path = os.path.join(img_url,"om_sanathana", folder_name)
    print(folder_path,"11122223333")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    image_name = name+".pdf"
    image_path = os.path.join(folder_path, image_name)
    with open(image_path, "wb") as image_file:
        image_file.write(image_data)
    return image_path

import os
import base64
from django.conf import settings


def save_base64_to_folder(pdf_base64, _id, name):
    folder_name = str(_id)
    img_url = settings.FILE_URL
    folder_path = os.path.join(img_url, "om_sanathana", folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    pdf_name = name
    pdf_path = os.path.join(folder_path, pdf_name)
    
    pdf_data = base64.b64decode(pdf_base64)
    
    with open(pdf_path, "wb") as pdf_file:
        pdf_file.write(pdf_data)
    
    return pdf_path

# from django.conf import settings
# import os

# def image_path_to_binary(filename):
#     img_path = os.path.join(settings.FILE_URL, filename)
#     if os.path.exists(img_path):
#         with open(img_path, "rb") as image_file:
#             image_data = image_file.read()
#             hex_encoded_image = image_data.hex()
#             return hex_encoded_image
#     else:
#         return None

# def save_image_to_folder(file, _id, name):
#     folder_name = str(_id)
#     folder_path = os.path.join(settings.FILE_URL, "om_sanathana", folder_name)
#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)
#     file_name = name + ".pdf"
#     file_path = os.path.join(folder_path, file_name)
#     with open(file_path, "wb") as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)
#     return file_path