import os
from urllib import response
import requests

#download with an optional directory

urls =[
    'https://binaries.templates.cdn.office.net/support/templates/en-us/tf16402488_win32.dotx',
    'https://binaries.templates.cdn.office.net/support/templates/en-us/tf16392716_win32.dotx'
]

output_dir = r'C:\Users\banch\Python_Selenium\upload_download'
downloadDir = '.\\upload_download'
# for url in urls:
#     response = requests.get(url)
#     if response.status_code == 200: #status code : 200 = ok , 204 = no contentm, 400 = bad request, 401 = unauthorized, 403 = forbidden, 404 = not found
#         file_path = os.path.join(output_dir, os.path.basename(url))
#         with open(file_path,'wb') as f:
#             f.write(response.content)

def download_file(urls,output_dir):
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(output_dir, os.path.basename(url))
            with open(file_path,'wb') as f:
                f.write(response.content)
        elif response.status_code == 404:
            print("File Not Found!")
        else:
            print("No files to download!")

# cwd = os.getcwd()
# print(cwd)
download_file(urls,downloadDir)