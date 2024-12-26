import streamlit as st
import pdfkit
import requests
import re

def save_webpage_as_pdf(page_url, output_pdf=None):
   
    try:
        st.write(f"Downloading webpage: {page_url}")
        
        response = requests.get(page_url)
        if response.status_code != 200:
            st.error(f"Failed to access {page_url}: HTTP {response.status_code}")
            return None

        if output_pdf is None:
            output_pdf = get_pdf_filename_from_url(page_url)
        
        options = {
            'quiet': '',
            'enable-local-file-access': '',  
        }
        pdfkit.from_url(page_url, output_pdf, options=options)

        st.success(f"Webpage saved as PDF: {output_pdf}")
        return output_pdf
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def get_pdf_filename_from_url(url):
    """
    Generate a filename for the PDF based on the URL.
    """
    filename = re.sub(r'https?://(www\.)?', '', url).strip().strip('/')
    filename = re.sub(r'[^a-zA-Z0-9]', '_', filename) + '.pdf'
    return filename


st.title("Notes Maker")
st.write("Convert your webpages into readble PDFs.(Mainly gfg pages)")


page_url = st.text_input("Enter the webpage URL:")

if st.button("Fetch and Save as PDF"):
    if page_url:
        st.write("Processing your request...")
        pdf_filename = save_webpage_as_pdf(page_url)
        if pdf_filename:
            with open(pdf_filename, "rb") as file:
                st.download_button(
                    label="Download PDF",
                    data=file,
                    file_name=pdf_filename,
                    mime="application/pdf"
                )
    else:
        st.warning("Please enter a valid URL.")

st.markdown("<footer><p>Made with 💗 by Sai Aneesh</p></footer>", unsafe_allow_html=True)
