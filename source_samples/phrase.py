import cv2
import sys
import pytesseract

# Install: Tesseract OCR with all language and script packages
#   https://github.com/tesseract-ocr/tesseract/wiki
#       https://packages.ubuntu.com/bionic/all/tesseract-ocr-all/download
#       sudo snap install --channel=edge tesseract

# Improving the quality of the output
# https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality

if len(sys.argv) < 2:
    print('Usage: python ocr_simple.py image.jpg')
    sys.exit(1)

# Read image path from command line
imPath = sys.argv[1]

# Uncomment the line below to provide path to tesseract manually
# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
# Define config parameters.
# '-l eng'  for using the English language
# '--oem 1' for using LSTM OCR Engine


# OCR Engine Mode (oem):
# Tesseract 4 has two OCR engines —
# 1) Legacy Tesseract engine
# 2) LSTM engine.

# There are four modes of operation chosen using the --oem option.
# 0    Legacy engine only.
# 1    Neural nets LSTM engine only.
# 2    Legacy + LSTM engines.
# 3    Default, based on what is available.


config = ('l por --oem 1 --psm 3')

# Read image from disk
im = cv2.imread(imPath, cv2.IMREAD_COLOR)

# Run tesseract OCR on image
text = pytesseract.image_to_string(im, config=config)

# Print recognized text
print(text)
