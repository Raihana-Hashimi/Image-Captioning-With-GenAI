# Image Captioning with BLIP and Gradio

This project contains two related tools for generating image captions using the [BLIP (Bootstrapping Language-Image Pre-training)](https://huggingface.co/Salesforce/blip-image-captioning-base) model from Hugging Face:

1. **Gradio Web App**: Upload an image and receive a caption through a simple web interface.
2. **URL Image Scraper + Captioner**: Automatically scrapes images from a webpage, generates captions, and saves them to a file.

## Overview

Both tools use the `Salesforce/blip-image-captioning-base` model to generate natural language descriptions of images.

### Tools Included

#### ✅ Gradio Image Captioning App (`image_captioning_app.py`)

* Upload an image and get a generated caption in your browser
* Interactive UI powered by Gradio
* Easy to run locally or share via public link

#### ✅ Automated URL Captioner (`automate_url_captioner.py`)

* Scrapes images from a given webpage (e.g., Wikipedia)
* Filters out invalid or non-meaningful images
* Automatically generates captions for valid images and saves them to `captions.txt`

> **Note:** This script skips SVGs, icons, and very small images to avoid noise in results.

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Raihana-Hashimi/Image-Captioning-With-GenAI.git
cd Image-Captioning-With-GenAI
pip install -r requirements.txt
```

---

## Usage

### 🔹 Run the Gradio App

```bash
python image_captioning_app.py
```

This will launch a local web interface at `http://127.0.0.1:7860`.

### 🔹 Run the URL Image Captioning Script

Edit the `url` variable in `automate_url_captioner.py` to point to any web page you'd like to scrape, then run:

```bash
python automate_url_captioner.py
```

Captions will be saved to `captions.txt`.

---

## Example Output

![demo](https://github.com/Raihana-Hashimi/Image-Captioning-With-GenAI/blob/main/output/Screenshot%202025-05-03%20164923.png) 

Example entry from `captions.txt`:

```
https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Nuvola_apps_ksim.png/20px-Nuvola_apps_ksim.png: a computer screen with a green screen
```

---

## Requirements

* Python 3.7+
* `transformers`
* `gradio`
* `Pillow`
* `beautifulsoup4`
* `requests`

---

## License

This project is open-source and available under the [MIT License](LICENSE).
