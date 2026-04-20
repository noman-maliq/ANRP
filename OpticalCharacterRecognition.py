# -*- coding: utf-8 -*-
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = 'tesseract'
#tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
tessdata = '--tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata"'
custom = r'--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def ocr(plate):
    #text = pytesseract.image_to_string(plate,config=tessdata_dir_config,lang="eng")
    text = pytesseract.image_to_string(plate,config=custom,lang="eng")
    return text

def check_if_string_in_file(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False