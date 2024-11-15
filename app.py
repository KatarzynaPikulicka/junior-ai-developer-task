
import requests
import os

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



def fetch_article_from_url(url):

    response = requests.get(url)
    response.raise_for_status()
    return response.text


def generate_html(article_text):

    prompt = f"""
  Please generate HTML code for an article that meets the following requirements: 
  Use appropriate HTML tags to structure the content (e.g., <h1>, <h2>, <p>, <ul>, <ol>, etc.). 
  Specify where images should be inserted using the <img> tag with the attribute src="image_placeholder.jpg". 
  Add an alt attribute to each image with a detailed description (prompt) that can be used to generate the image. 
  Include captions for the images using an appropriate HTML tag (e.g., <figcaption>). Do not use CSS or JavaScript. 
  Respond without wrapping the code in markdown syntax.
  The generated code should include only the content between the <body> and </body> tags. Omit the <html>, <head>, and <body> tags.
. 

    Content of the article to be transformed:
    {article_text}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that converts text to HTML."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=3000,
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Wystąpił błąd podczas generowania HTML: {e}")
        return ""

def save_html(html_content, file_path):

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

article_url = "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"

try:
    # Pobranie artykułu
    article_text = fetch_article_from_url(article_url)

    # Generowanie HTML
    html_content = generate_html(article_text)

    # Zapis do pliku
    if html_content:
        save_html(html_content, 'artykul.html')
        print("Plik artykul.html został zapisany.")
    else:
        print("Nie udało się wygenerować HTML.")
except requests.RequestException as e:
    print(f"Wystąpił błąd podczas pobierania artykułu: {e}")
