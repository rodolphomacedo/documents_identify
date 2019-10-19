# Identificação de Documentos 

Identificação de documentos via visão computacional e Machine Learning

-------

# Document Identifier

Document identification by computer vision and machine learning


-------

![Documents](images/documentos.jpg)

-----
## Instructions
### To run identify.py
```python3 identify.py --input ../files/rg\_teste.PNG --model frozen\_east\_text\_detection.pb```

Download [frozen east text detection.pb](https://raw.githubusercontent.com/oyyd/frozen_east_text_detection.pb/master/frozen_east_text_detection.pb)

### To run homography.py
```python3 homography.py```

### To run phrase.py
```python3 phrase.py phrase.jpeg```
    
    - Required pytesseract
    
    - Install: Tesseract OCR with all language and script packages
    
    - https://github.com/tesseract-ocr/tesseract/wiki 
    
    - https://packages.ubuntu.com/bionic/all/tesseract-ocr-all/download 
    
    - sudo snap install --channel=edge tesseract
