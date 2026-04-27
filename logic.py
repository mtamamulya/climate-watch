def analisa_risiko(suhu, kelembapan, cuaca_utama, angin):
    """
    Menentukan risiko banjir, kekeringan, DAN keamanan berkendara motor.
    Dipindahkan ke sini agar kodingan lebih rapi.
    """
    status = "Normal"
    pesan = "Cuaca terpantau kondusif."
    rekomendasi = "Aman untuk beraktivitas luar ruangan."
    kategori_bg = "bg-cerah" # Default background

    # LOGIKA 1: HUJAN & BANJIR
    if "Rain" in cuaca_utama or "Thunderstorm" in cuaca_utama:
        status = "WASPADA HUJAN LEBAT"
        pesan = "Turun hujan dengan potensi jalan licin/genangan."
        rekomendasi = "⚠️ BAHAYA UNTUK MOTOR: Siapkan jas hujan, kurangi kecepatan, waspada rem mendadak."
        kategori_bg = "bg-hujan"
    
    # LOGIKA 2: ANGIN KENCANG (> 10 m/s)
    elif angin > 10: 
        status = "WASPADA ANGIN KENCANG"
        pesan = f"Kecepatan angin mencapai {angin} m/s."
        rekomendasi = "⚠️ BAHAYA UNTUK MOTOR: Hindari jalan layang atau terbuka, risiko oleng tinggi."
        kategori_bg = "bg-mendung"

    # LOGIKA 3: MENDUNG
    elif "Clouds" in cuaca_utama:
        status = "Berawan / Mendung"
        pesan = "Langit tertutup awan."
        rekomendasi = "Cuaca sejuk, cukup nyaman untuk berkendara."
        kategori_bg = "bg-mendung"

    # LOGIKA 4: PANAS TERIK
    elif suhu > 33:
        status = "PANAS EKSTREM"
        pesan = f"Suhu mencapai {suhu}°C."
        rekomendasi = "Gunakan jaket berventilasi, jangan lupa minum agar tidak dehidrasi di jalan."
        kategori_bg = "bg-panas"

    return status, pesan, rekomendasi, kategori_bg