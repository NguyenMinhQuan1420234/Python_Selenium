from seleniumbase import BaseCase

class UploadTest(BaseCase):
    def test_visible_upload(self):
        
        self.open("https://the-internet.herokuapp.com/upload")

        file_path = './upload_download/file.dotx'

        self.choose_file("#file-upload", file_path)

        self.click('#file-submit')

        self.assert_text('File uploaded!', 'h3')

