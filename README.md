# 📝 Simple Pastebin with Flask

Proyek ini adalah aplikasi web sederhana berbasis **Flask (Python)** yang meniru fungsi dasar **Pastebin**.  
Tujuannya dibuat sebagai **media pembelajaran** untuk memahami dasar-dasar **Flask, form handling, template engine, penyimpanan data sederhana, dan fitur keamanan dasar**.  

---

## ✨ Fitur Utama
- Membuat paste teks atau kode.
- Pilih bahasa (Text, Python, JavaScript, HTML, CSS).
- Atur waktu kadaluarsa (10 menit, 1 jam, 1 hari, atau tidak pernah expire).
- Proteksi paste dengan **password opsional**.
- Tampilan paste dengan **syntax highlighting** (PrismJS).
- Tombol salin isi paste.
- Daftar semua paste yang sudah dibuat.
- Data tersimpan di `pastes.json` + link di `list_link.txt`.
- Tampilan responsif (HP & PC) dengan **TailwindCSS**.

---

## 📚 Description for Learning
Proyek ini dapat dipelajari untuk memahami:

- **Routing di Flask** → bagaimana mengatur URL dengan `@app.route`.  
- **Form Handling** → bagaimana menerima data dari user dengan `request.form`.  
- **Template Jinja2** → cara menampilkan data dinamis ke halaman HTML.  
- **Penyimpanan Data JSON** → menyimpan data sederhana tanpa database.  
- **Password Hashing** → penggunaan SHA256 agar password tidak disimpan dalam bentuk asli.  
- **Error Handling** → menampilkan halaman khusus untuk paste yang tidak ditemukan atau sudah expired.  
- **Responsive Web Design** → tampilan tetap rapi baik di HP maupun PC.  

---

## 🎯 Tujuan Pembelajaran
1. Memahami alur kerja **request → processing → response** di Flask.  
2. Mempelajari penggunaan **form input** dan menampilkannya kembali ke halaman web.  
3. Mengenal cara **menyimpan dan membaca data sederhana** dengan file JSON.  
4. Berlatih membuat halaman dinamis menggunakan **Jinja2 Template Engine**.  
5. Menerapkan **keamanan dasar** dalam penyimpanan password.  
6. Membiasakan diri membuat web app dengan **UI responsif**.  

---

## 🚀 Cara Menjalankan
<summary><code>Instalasi Script?</code></summary>

```php
$ pkg update && pkg upgrade
$ pkg install python
$ pkg install python 2
$ pkg install bash
$ pkg install git
$ git clone https://github.com/ILHAMGanzz26/simple-pastebin-flask
```
```bash
cd simple-pastebin-flask
```

<summary><code>Install Flask?</code></summary>

```bash
pkg install python-pip
pip install -r requirements.txt
```
### 🚀 Running🏃
<summary><code>Run Menggunakan Python?</code></summary>

```bash
python app.py
```

#### 🌐 Salin dan taruh di Browser atau Chrome

```bash
http://127.0.0.1:5000/
