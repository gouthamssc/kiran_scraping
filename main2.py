# import subprocess
# import cv2
# import numpy as np
#
# # Define input and output file paths
# input_file = '/Users/saigowthamrajanala/Downloads/tets.jpeg'
# output_file = './output3.txt'
#
# # Read input image using OpenCV
# img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
#
# # Apply thresholding to binarize the image
# thresh_val, thresh_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#
# # Invert the image to get white text on black background
# inverted_img = cv2.bitwise_not(thresh_img)
#
# # Save the preprocessed image for debugging
# cv2.imwrite('preprocessed_image.jpg', inverted_img)
#
# # Call gocr command line tool to extract text from image
# subprocess.call(['gocr', '-o', output_file, '-u', '-C', '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 'preprocessed_image.jpg'])
#
# # Read the extracted text from output file
# with open(output_file, 'r') as f:
#     extracted_text = f.read()
#
# # Print extracted text
# print(extracted_text)





import subprocess

# Define input and output file paths
input_file = '/Users/saigowthamrajanala/Downloads/tets.jpeg'
output_file = './output.txt'

# Call gocr command line tool to extract text from image
subprocess.call(['gocr', '-o', output_file, input_file])

# Read the extracted text from output file
with open(output_file, 'r') as f:
    extracted_text = f.read()

# Print extracted text
print(extracted_text)









# import cv2
# import easyocr
#
# # Load image and convert to grayscale
# image = cv2.imread('/Users/saigowthamrajanala/Desktop/test.png')
# # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# #
# # # Apply some preprocessing techniques (adjust as needed)
# # gray = cv2.medianBlur(gray, 3)
# # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#
# # Extract text using EasyOCR
# reader = easyocr.Reader(['en'])
# results = reader.readtext(image)
#
# # Print extracted text
# for result in results:
#     print(result[1])







# import cv2
# import pytesseract
#
# # Load image and convert to grayscale
# image = cv2.imread('/Users/saigowthamrajanala/Desktop/test.png')
# # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Apply some preprocessing techniques (adjust as needed)
# # gray = cv2.medianBlur(gray, 3)
# # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#
# # Extract text using Tesseract
# text = pytesseract.image_to_string(image, lang='eng')
#
# # Print extracted text
# print(text)





# import cv2
# import pytesseract
#
# # Load image and convert to grayscale
# image = cv2.imread('/Users/saigowthamrajanala/Desktop/test.png')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Apply some preprocessing techniques (adjust as needed)
# gray = cv2.medianBlur(gray, 3)
# gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#
# # Apply some image processing techniques (adjust as needed)
# gray = cv2.dilate(gray, None, iterations=2)
# gray = cv2.erode(gray, None, iterations=1)
#
# # Extract text using Pytesseract
# text = pytesseract.image_to_string(gray, lang='eng')
#
# # Print extracted text
# print(text)



# import cv2
# import pytesseract
# from PIL import Image, ImageFilter, ImageOps
# import io
#
# # Load the image
# image = cv2.imread('/Users/saigowthamrajanala/Desktop/test.png')
#
# # Preprocess the image
# # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # # gray = cv2.GaussianBlur(gray, (5, 5), 0)
# # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# # gray = cv2.medianBlur(gray, 3)
#
# # Convert the preprocessed image to bytes using OpenCV and PIL
# pil_image = Image.fromarray(image)
# with io.BytesIO() as output:
#     pil_image.save(output, format="JPEG")
#     image_bytes = output.getvalue()
#
# # Set up Tesseract OCR
# pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
# tessdata_dir_config = r'--tessdata-dir "/opt/homebrew/share/tessdata"'
#
# # Extract text from the image
# text = pytesseract.image_to_string(pil_image, lang='eng', config=tessdata_dir_config)
#
# # Print the extracted text
# print(text)
#





# import easyocr
# from PIL import Image, ImageFilter, ImageOps
# import io
#
# # Load the image
# image = Image.open('/Users/saigowthamrajanala/Downloads/tets.jpeg')
#
# # Preprocess the image
# image = image.convert('L')  # Convert to grayscale
# image = image.filter(ImageFilter.SHARPEN)  # Sharpen the image
# image = ImageOps.invert(image)  # Invert the colors
#
# # Convert the preprocessed image to bytes using BytesIO
# with io.BytesIO() as output:
#     image.save(output, format="JPEG")
#     image_bytes = output.getvalue()
#
# # Set up the OCR reader
# reader = easyocr.Reader(['en'])
#
# # Extract text from the image
# results = reader.readtext(image_bytes)
#
# # Print the extracted text
# for result in results:
#     print(result[1])



#
# import easyocr
#
# # Load the image as a bytes object
# with open('/Users/saigowthamrajanala/Downloads/tets.jpeg', 'rb') as f:
#     image_bytes = f.read()
#
# # Set up the OCR reader
# reader = easyocr.Reader(['en'])
#
# # Extract text from the image
# results = reader.readtext(image_bytes)
#
# # Print the extracted text
# for result in results:
#     print(result[1])
