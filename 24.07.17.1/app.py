from flask import Flask, render_template, request, session
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# API ve CSE
API_KEY = 'your-google-api-key'
CSE_ID = 'your-cse-id'

def internet_cevap(soru):
    try:
        # Google Custom Search API isteği
        params = {
            'key': API_KEY,
            'cx': CSE_ID,
            'q': soru,
            'num': 1  # 1 in 14.000.605
        }
        response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
        data = response.json()
        if 'items' in data:
            # İlk sonucu alalım
            first_result = data['items'][0]
            title = first_result['title']
            snippet = first_result['snippet']
            link = first_result['link']
            return f"{title}\n\n{snippet}\n\nDetaylı bilgi için link: {link}"
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
        cevap = internet_cevap(soru)
        session['sorular_cevaplar'].insert(0, (soru, cevap))
        session.modified = True

    return render_template('index.html', sorular_cevaplar=session['sorular_cevaplar'])

if __name__ == '__main__':
    app.run(debug=True)
