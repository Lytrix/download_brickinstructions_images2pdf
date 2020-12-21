import requests
import bs4 as bs
import img2pdf
from urllib.parse import urlparse
import os
import shutil
import argparse


def get_links_of_files(url):
    data = requests.get(url).text
    print(data)
    soup = bs.BeautifulSoup(data,'html.parser')
    list_urls = []
    for link in soup.find_all('a', attrs={'rel': 'legoinstructions'}):
        url = link.get('href')
        list_urls.append(url)
    return list_urls

def download_file(url, folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
    
    print("URL:", url)
    resp = requests.get(url, stream=True)
    baseurl = urlparse(url)
    filename = os.path.basename(baseurl.path)
    print(filename)

    with open(os.path.join(folder, filename), 'wb') as file:
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw, file)
        del resp

def download_files(url, folder):
    list_of_files = get_links_of_files(url)
    for link in list_of_files:
        download_file(link, folder)

# with open("out.pdf","wb") as f:
#  f.write(img2pdf.convert( page ))


import img2pdf, glob 
def save2pdf(folder):
    files = sorted(glob.glob(os.path.join(folder, '*.jpg'))) 
    with open("out.pdf","wb") as f:
        f.write(img2pdf.convert( files ))


def parser():
    """
    Parser function to run arguments from commandline and to add description to sphinx docs.
    To see possible styling options: https://pythonhosted.org/an_example_pypi_project/sphinx.html
    """
    description = """
    download all jpg's from Brickinstructions and save as one PDF.

    Example command line:
    ``python download_images2pdf.py downloads http://lego.brickinstructions.com/en/lego_instructions/set/21137/The_Mountain_Cave``
    """

    parser = argparse.ArgumentParser(
                        description=description)
    parser.add_argument('output_folder',
                        type=str,
                        help='Specify the desired output folder path, for example: output')
    parser.add_argument('url',
                        type=str,
                        help="""
                        Full url of the webpage, for example:
                        "http://lego.brickinstructions.com/en/lego_instructions/set/21137/The_Mountain_Cave"
                        """)
    return parser


def main():
    args = parser().parse_args()
    download_files(args.url, args.output_folder)
    save2pdf(folder)


if __name__ == '__main__':
    main()
