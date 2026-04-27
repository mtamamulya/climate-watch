from flask import Flask, render_template, request
import requests
from datetime import datetime
from logic import analisa_risiko 
import os
from dotenv import load_dotenv

app = Flask(__name__)

# --- KONFIGURASI ---
load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def website():
    return render_template('website.html')

# --- ROUTE WEBSITE ---
@app.route('/climatology', methods=['GET', 'POST'])
def index():
    kota = "Semarang" # Default
    
    if request.method == 'POST':
        kota_input = request.form.get('kota')
        if kota_input:
            kota = kota_input

    params = {
        'q': kota,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'id'
    }
    
    cuaca_info = None

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            suhu = data['main']['temp']
            kelembapan = data['main']['humidity']
            deskripsi = data['weather'][0]['description']
            cuaca_utama = data['weather'][0]['main']
            icon_code = data['weather'][0]['icon']
            kecepatan_angin = data['wind']['speed']
            
            # PANGGIL FUNGSI DARI FILE SEBELAH (logic.py)
            status, pesan, rekomendasi, kategori_bg = analisa_risiko(suhu, kelembapan, cuaca_utama, kecepatan_angin)

            cuaca_info = {
                'kota': kota,
                'suhu': suhu,
                'kelembapan': kelembapan,
                'deskripsi': deskripsi.title(),
                'status': status,
                'pesan': pesan,
                'rekomendasi': rekomendasi,
                'waktu': datetime.now().strftime("%d-%m-%Y %H:%M"),
                'icon': icon_code,
                'angin': kecepatan_angin,
                'bg_class': kategori_bg
            }
        else:
            print("Gagal mengambil data:", data)

    except Exception as e:
        print("Error Connection:", e)

    return render_template('dashboard.html', data=cuaca_info)

if __name__ == '__main__':
    app.run(debug=True)