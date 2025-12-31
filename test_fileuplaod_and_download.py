import os
import time
from zipfile import ZipFile

from playwright.sync_api import sync_playwright


import time

def test_fileupload_and_download(page):

    # Open file upload page
    page.goto("https://the-internet.herokuapp.com/upload")

    # File path (local system)
    file_path = "C:/Users/user/Downloads/image.png"

    # Upload file
    page.set_input_files("#file-upload", file_path)

    # Submit
    page.click("#file-submit")

    # Assert uploaded file name
    uploaded_file_name = page.locator("#uploaded-files").text_content().strip()
    assert uploaded_file_name == 'image.png'

    print("Uploaded file name asserted successfully")
