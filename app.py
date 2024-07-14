from flask import Flask, render_template, request, session
import random
import spacy
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Gizli anahtar

# SpaCy
nlp = spacy.load('xx_ent_wiki_sm')

def cevap_ver(soru):
    cevap = "Üzgünüm, bu konuda bilgim yok."

    if "ne zaman" in soru:
        tarih = random.choice(list(tarih_verisi.keys()))
        cevap = f"{tarih}: {tarih_verisi[tarih]}"
    elif "tarih" in soru:
        if any(key in soru for key in tarih_verisi.keys()):
            for key, value in tarih_verisi.items():
                if key in soru:
                    cevap = f"{key}: {value}"
                    break
    else:
        cevap = wikipedia_cevap(soru)

    return cevap

def wikipedia_cevap(soru):
    try:
        # Metin analizi
        doc = nlp(soru)
        for ent in doc.ents:
            if ent.label_ == "LOC":
                # Wikipedia API isteği
                page_title = ent.text
                params = {
                    "action": "query",
                    "format": "json",
                    "prop": "info",
                    "inprop": "url",
                    "titles": page_title
                }
                response = requests.get("https://tr.wikipedia.org/w/api.php", params=params)
                data = response.json()
                page_id = next(iter(data['query']['pages']))
                page_url = data['query']['pages'][page_id]['fullurl']
                return page_url
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return "Üzgünüm, bu konuda bilgim yok."

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'sorular_cevaplar' not in session:
        session['sorular_cevaplar'] = []

    if request.method == 'POST':
        soru = request.form['soru']
        cevap = cevap_ver(soru)
        session['sorular_cevaplar'].insert(0, (soru, cevap))
        session.modified = True

    return render_template('index.html', sorular_cevaplar=session['sorular_cevaplar'])

if __name__ == '__main__':
    app.run(debug=True)