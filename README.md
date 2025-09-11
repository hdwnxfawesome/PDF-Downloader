# PDF Downloader

A simple Python script to automatically download all PDF files linked on a given webpage into a dedicated local folder.

## Features

- Crawls a webpage for all PDF links.
- Downloads each PDF into a specified folder.
- Handles absolute and relative links.
- Skips duplicates and provides clear status messages.

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

Install requirements:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Save the script as `download_pdfs.py`.
2. Run the script:

   ```bash
   python download_pdfs.py
   ```

3. When prompted:
   - Enter the URL of the webpage to scrape for PDFs.
   - Optionally, specify a folder name to save the PDFs (default: `downloaded_pdfs`).

## Example

```text
Enter the URL of the webpage: https://example.com/resources
Enter the folder name for saving PDFs (default: downloaded_pdfs): my_pdfs
Found 3 PDF links. Downloading...
Downloaded: file1.pdf
Downloaded: file2.pdf
Downloaded: file3.pdf
```

## Notes

- The script only downloads direct links to `.pdf` files found in `<a>` elements.
- Make sure you have permission to download the files from the given website.
- If a file already exists in the folder, it will be overwritten.

## License

This project is licensed under the MIT License.
