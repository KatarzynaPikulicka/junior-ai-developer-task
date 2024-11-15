# 📝 Generator HTML z OpenAI

Prosty skrypt w Pythonie do pobierania artykułu z predefiniowanego URL, generowania jego wersji HTML za pomocą OpenAI i zapisywania na lokalnym dysku. 🚀

## Funkcje 🌟

- Pobieranie tekstu artykułu z zdefiniowanego URL 🌐
- Konwersja artykułu na HTML z użyciem OpenAI 🤖
- Zapisywanie wygenerowanego HTML do pliku 🖇️
- (zadanie dla chętnych) wyświetlanie wygenerowanego artykułu z użyciem szablonu 📄✨


## 🚀 Jak zacząć?

### 1️⃣ Wymagania

Zainstaluj Pythona w wersji 3.9+  
Zainstaluj zależności z pliku `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 2️⃣ Ustawienie klucza API OpenAI

Dodaj klucz API OpenAI jako zmienną środowiskową:

```bash
export OPENAI_API_KEY="twój_klucz_api_openai"
```

### 3️⃣ Uruchomienie skryptu

Skrypt działa na zdefiniowanym URL w zmiennej `article_url`. Wystarczy uruchomić:

```bash
python app.py
```


## Przykład użycia 🛠️

- **Wejście**: Zdefiniowany w kodzie URL artykułu
- **Wyjście**: Plik `artykul.html` zawierający sformatowaną treść w HTML.


## Możliwe błędy ⚠️

- **Problemy z siecią**: Upewnij się, że URL w zmiennej `article_url` jest poprawny i dostępny.
- **Brak klucza API**: Sprawdź, czy `OPENAI_API_KEY` jest ustawiony i poprawny.


## Autor 🧑‍💻

Stworzono z ❤️ przez [Kasia](https://github.com/KatarzynaPikulicka)
