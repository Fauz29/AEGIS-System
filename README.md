# AEGIS (Advance Energy Guidance & Intelligence System) ⚡
Sistem Manajemen Energi berbasis IoT dan Logika Fuzzy Mamdani untuk optimasi konsumsi energi pada hunian tipe 21 dengan siklus evaluasi 10 harian.

## 📝 Deskripsi Proyek
AEGIS (Advance Energy Guidance & Intelligence System) dirancang khusus untuk membantu pemilik rumah mengelola kuota listrik agar tidak habis sebelum waktunya. Dengan membagi penggunaan menjadi 3 periode (10 hari sekali), sistem ini memberikan kendali cerdas pada beban rumah tangga.

## 🛠️ Fitur Utama
- **Fuzzy Logic Controller:** Menentukan status sistem (Normal, Waspada, Kritis).
- **Priority Load Management:** Menjaga beban prioritas (Kulkas) tetap menyala.
- **Smart Load Shedding:** Memutus beban non-prioritas di ruangan paling boros.
- **Real-time Monitoring:** Notifikasi langsung ke smartphone pengguna.

## 📊 Aturan Fuzzy (Rule Base)
Sistem menggunakan 9 aturan utama untuk menentukan keputusan:
1. Sisa Sedikit & Waktu Awal -> **KRITIS**
2. Sisa Sedikit & Waktu Tengah -> **KRITIS**
3. Sisa Sedikit & Waktu Akhir -> **WASPADA**
4. Sisa Sedang & Waktu Awal -> **KRITIS**
5. Sisa Sedang & Waktu Tengah -> **WASPADA**
6. Sisa Sedang & Waktu Akhir -> **NORMAL**
7. Sisa Banyak & Waktu Awal -> **WASPADA**
8. Sisa Banyak & Waktu Tengah -> **NORMAL**
9. Sisa Banyak & Waktu Akhir -> **NORMAL**

## 🚀 Cara Menjalankan Simulasi
1. Pastikan Python terinstal.
2. Instal library: `pip install numpy scikit-fuzzy matplotlib scipy`
3. Jalankan file: `python aegis_fuzzy.py`
