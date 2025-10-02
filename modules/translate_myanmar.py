import requests

def translate_myanmar_to_english(text):
    """
    Translate Myanmar text to English using LibreTranslate public API.
    """
    try:
        response = requests.post(
            "https://libretranslate.de/translate",
            data={
                "q": text,
                "source": "my",
                "target": "en",
                "format": "text"
            },
            timeout=10
        )
        response.raise_for_status()
        return response.json()["translatedText"]
    except Exception as e:
        return text  # fallback: return original if error

# Example usage:
# print(translate_myanmar_to_english("လှပသော မိန်းကလေးတစ်ယောက်"))
