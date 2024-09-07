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




##########################perfect

import fitz  # PyMuPDF
import base64
import os

def extract_pdf_content(file_path):
    content = []  # To store the structured text and images
    text_counter = 1
    image_counter = 1
    
    if os.path.exists(file_path):
        pdf_document = fitz.open(file_path)
        
        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)

            # Extract text
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                if "lines" in block:
                    block_text = ""
                    for line in block["lines"]:
                        for span in line["spans"]:
                            block_text += span["text"] + " "
                    
                    if block_text.strip():
                        content.append(f"text{text_counter}: {block_text.strip()}")
                        text_counter += 1

            # Extract images
            images = page.get_images(full=True)
            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = pdf_document.extract_image(xref)
                if base_image:
                    image_bytes = base_image["image"]
                    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

                    # Append image data as image1, image2, etc.
                    content.append(f"image{image_counter}: {image_base64}")
                    image_counter += 1
        
        pdf_document.close()
    
    return content



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