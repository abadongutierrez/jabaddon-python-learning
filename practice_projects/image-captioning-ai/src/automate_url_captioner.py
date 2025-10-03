import requests
from io import BytesIO
from bs4 import BeautifulSoup
from image_captioning_ai import caption_image_url

# URL of the page to scrape
url = "https://en.wikipedia.org/wiki/IBM"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
print("Status:", response.status_code, "HTML size:", len(response.text))

soup = BeautifulSoup(response.text, "html.parser")
img_elements = soup.find_all("img")
print(f"Found {len(img_elements)} <img> tags")

with open("captions.txt", "w", encoding="utf-8") as caption_file:
    for idx, img_element in enumerate(img_elements, start=1):
        # Try different attributes
        img_url = img_element.get("src") or img_element.get("data-src")
        if not img_url and img_element.has_attr("srcset"):
            img_url = img_element["srcset"].split()[0]
        if not img_url:
            continue
        # Skip SVGs directly
        if img_url.endswith(".svg") or ".svg" in img_url:
            continue
        # Fix relative URLs
        if img_url.startswith("//"):
            img_url = "https:" + img_url
        elif img_url.startswith("/"):
            img_url = "https://en.wikipedia.org" + img_url
        elif not img_url.startswith("http"):
            continue
        try:
            print(f"[{idx}] Processing image: {img_url}")
            caption = caption_image_url(img_url)
            print(f"[{idx}] Caption: {caption}")
            caption_file.write(f"{img_url}: {caption}\n")
            print(f"[{idx}] Caption saved")
        except OSError as e:
            # Skip images PIL cannot open (SVG, ICO, corrupt files)
            print(f"[{idx}] Skipping unsupported image format: {e}")
            continue
        except Exception as e:
            print(f"[{idx}] Error: {e}")
            continue