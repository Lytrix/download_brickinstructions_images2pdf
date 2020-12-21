# Download all JPG images from Brickinstructions 2 PDF
I wanted to rebrick the Lego Minecraft Mountain. 
Because there was no PDF yet available on http://brickinstructions.com, I decided to write a quick download2pdf python script to do this automatically for all 400 images.

## Installation

### 0. Prerequisites:
* Install python 3.6 from www.python.org

### (optional) Create and activate a virtual environment, for example with:
```
python -m venv
.venv\Scripts\activate
```

You can install the downloader by the following commands in the command line/terminal
### 1. Click download at the right top or use git clone
```
git clone https://github.com/lytrix/download_images2pdf.git
cd download_images2pdf
```

### 2. Install the needed packages requests, beautifulsoup and img2pdf
```
pip install -r requirements.txt
```

### 3. Run the command with the foldername (will be created if it does not exists) + url of the page you want to download the images from:
```
python images_brick_link2pdf.py downloads http://lego.brickinstructions.com/en/lego_instructions/set/21137/The_Mountain_Cave 
```

Enjoy!

With many thanks to http://www.brickinstructions.com making all Lego instructions available!
