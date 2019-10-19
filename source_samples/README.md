# Identificação de Documentos 

Identificação de documentos via visão computacional

-------

# Documents Identify

document identification by computer vision

-------

![Documents](images/docuemntos.jpeg)

-----
## Instructions
### To run identify.py
python3 identify.py --input ../files/rg\_teste.PNG --model frozen\_east\_text\_detection.pb

### To run homography.py
python3 homography.py

### To run phrase.py
python3 phrase.py phrase.jpeg
    - Required pytesseract
    - Install: Tesseract OCR with all language and script packages
    - https://github.com/tesseract-ocr/tesseract/wiki 
    - https://packages.ubuntu.com/bionic/all/tesseract-ocr-all/download 
    - sudo snap install --channel=edge tesseract
