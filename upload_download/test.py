import requests #

# download to working folder

downloadUrl = 'https://binaries.templates.cdn.office.net/support/templates/en-us/tf16402488_win32.dotx'

output_dir = r'C:\Users\banch\Python_Selenium\upload_download'
# req = requests.get(downloadUrl)

# filename = req.url[downloadUrl.rfind('/')+1:]

# with open(filename, 'wb') as f :
#     for chunk in req.iter_content(chunk_size=8192):   
#         if chunk:
#             f.write(chunk)

def download_file(url, filename = ''):
    try:
        if filename:
            pass
        else: 
            filename = req.url[downloadUrl.rfind('/')+1:]

        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8912):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None
    
download_file(downloadUrl, 'file.dotx')