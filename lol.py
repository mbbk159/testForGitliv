import requests
import os

def download_random_image(save_path="random_image.jpg"):
    url = "https://source.unsplash.com/random/800x600"
    response = requests.get(url)

    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"Obrázek uložen jako {save_path}")
    else:
        print("Nepodařilo se stáhnout obrázek.")

if __name__ == "__main__":
    download_random_image()
