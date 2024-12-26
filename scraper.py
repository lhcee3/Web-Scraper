import pdfkit
import requests
import re

def save_webpage_as_pdf(page_url, output_pdf=None):
    try:
        print(f"Downloading webpage: {page_url}")
        
        
        response = requests.get(page_url)
        if response.status_code != 200:
            print(f"Failed to access {page_url}: HTTP {response.status_code}")
            return

        
        if output_pdf is None:
            output_pdf = get_pdf_filename_from_url(page_url)
        
        options = {
            'quiet': '',
            'enable-local-file-access': '',  
        }
        pdfkit.from_url(page_url, output_pdf, options=options)

        print(f"Webpage saved as PDF: {output_pdf}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_pdf_filename_from_url(url):
    
    filename = re.sub(r'https?://(www\.)?', '', url).strip().strip('/')
    filename = re.sub(r'[^a-zA-Z0-9]', '_', filename) + '.pdf'
    return filename


save_webpage_as_pdf("https://www.geeksforgeeks.org/types-of-operating-systems/")