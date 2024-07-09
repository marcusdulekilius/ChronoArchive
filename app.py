from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Gizli anahtar

# Örnek veriler
tarih_verisi = {
    "MÖ 776": "İlk Olimpiyat Oyunları düzenlendi.",
    "1453": "İstanbul'un Fethi gerçekleşti.",
    "1789": "Fransız Devrimi başladı.",
    "1969": "İnsanlı Ay'a ilk iniş yapıldı."
}

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
    return cevap

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'sorular_cevaplar' not in session:
        session['sorular_cevaplar'] = []

    if request.method == 'POST':
        soru = request.form['soru']
        cevap = cevap_ver(soru)
        session['sorular_cevaplar'].append((soru, cevap))
        session.modified = True

    return render_template('index.html', sorular_cevaplar=session['sorular_cevaplar'])

if __name__ == '__main__':
    app.run(debug=True)
