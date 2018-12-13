import requests
import re
import base64
import os
import cv2
import argparse
import numpy as np


try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

response = requests.get('thatwebsite')

while True:
    found=re.finditer(r'/png;base64,(.+)" /><br>', str(response.content))
    body=response.content
    pattern=r'png;base64,(.+?)" /><br>'
    regex = re.compile(pattern)
    m=regex.search(str(body))
    if m:
        #print('Match found: ', m.group(1))
        codedimage=str(m.group(1))
        decoded=base64.b64decode(codedimage)
        f = open("capta.png", "wb")
        f.write(decoded)
        f.close()
    else:
        print('No match')

    img=cv2.imread('capta.png')
    blur = cv2.medianBlur(img,3)
    blurred=cv2.imwrite('blur.png' , blur)


    ocrd=(pytesseract.image_to_string(Image.open('blur.png')))
    sendthis='{answer}'.format(answer=ocrd)

    cookies = {
        'PHPSESSID': '7fduuk22pkqfljuj1rccinrtc1',
        'uid': 'wKgbZFwOjl6rXwxrCq/7Ag==',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'thatwebsite.org',
        'Content-Type': 'application/x-www-form-urlencoded',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    data = {
  'cametu': sendthis
    }
    response = requests.post('thatwebsite.org',cookies=cookies, headers=headers, data=data)
    print(response.content)
    print(data)
    if "Fail" not in str(response.content) and "Too late" not in str(response.content):
        break
