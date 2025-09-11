import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_pdfs_from_webpage(url, output_folder="downloaded_pdfs"):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get webpage content
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching the webpage: {e}")
        return

    soup = BeautifulSoup(response.content, "html.parser")
    pdf_links = set()

    # Find all PDF links
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.lower().endswith(".pdf"):
            full_url = urljoin(url, href)
            pdf_links.add(full_url)

    if not pdf_links:
        print("No PDF links found on the page.")
        return

    print(f"Found {len(pdf_links)} PDF links. Downloading...")

    for pdf_url in pdf_links:
        try:
            r = requests.get(pdf_url, stream=True)
            r.raise_for_status()
            # Use last part of the path as filename
            parsed_url = urlparse(pdf_url)
            filename = os.path.basename(parsed_url.path)
            filepath = os.path.join(output_folder, filename)
            with open(filepath, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Failed to download {pdf_url}: {e}")

if __name__ == "__main__":
    page_url = input("Enter the URL of the webpage: ").strip()
    folder_name = input("Enter the folder name for saving PDFs (default: downloaded_pdfs): ").strip()
    if not folder_name:
        folder_name = "downloaded_pdfs"
    download_pdfs_from_webpage(page_url, folder_name)
