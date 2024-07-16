from flask import Flask, render_template, request, session
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Gizli anahtar

def wikipedia_cevap(soru):
    try:
        # Wikipedia API isteği
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": soru,
            "utf8": 1,
            "formatversion": 2
        }
        response = requests.get(f"https://tr.wikipedia.org/w/api.php", params=params)
        data = response.json()
        search_results = data.get("query", {}).get("search", [])
        if search_results:
            # İlk sonucu alalım
            first_result = search_results[0]
            page_title = first_result['title']
            page_extract = wikipedia_page_extract(page_title)
            return page_extract
        else:
            return "Üzgünüm, bu konuda bilgim yok."
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return "Üzgünüm, bu konuda bilgim yok."

def wikipedia_page_extract(page_title):
    try:
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "titles": page_title
        }
        response = requests.get(f"https://tr.wikipedia.org/w/api.php", params=params)
        data = response.json()
        page_id = next(iter(data['query']['pages']))
        if page_id != "-1":
            extract = data['query']['pages'][page_id].get('extract', 'Üzgünüm, bu konuda bilgim yok.')
            return extract
        else:
            return "Üzgünüm, bu konuda bilgim yok."
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return "Üzgünüm, bu konuda bilgim yok."

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'sorular_cevaplar' not in session:
        session['sorular_cevaplar'] = []

    if request.method == 'POST':
        soru = request.form['soru']
        cevap = wikipedia_cevap(soru)
        session['sorular_cevaplar'].insert(0, (soru, cevap))
        session.modified = True

    return render_template('index.html', sorular_cevaplar=session['sorular_cevaplar'])

if __name__ == '__main__':
    app.run(debug=True)