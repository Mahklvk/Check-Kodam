# Check-Kodam

Check-Kodam adalah aplikasi web berbasis Python dan Flask yang menggunakan deteksi wajah untuk memberikan nama acak kepada pengguna. Aplikasi ini memanfaatkan OpenCV dan MediaPipe untuk mendeteksi wajah melalui kamera.

## Fitur

- **Deteksi Wajah**: Menggunakan kamera untuk mendeteksi wajah pengguna.
- **Pemberian Nama Acak**: Setelah wajah terdeteksi, aplikasi akan memberikan nama acak dari daftar yang telah ditentukan.

## Instalasi

1. **Kloning repositori**:

   ```bash
   git clone https://github.com/Mahklvk/Check-Kodam.git
   ```

2. **Navigasi ke direktori proyek**:

   ```bash
   cd Check-Kodam
   ```

3. **Buat dan aktifkan virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Windows, gunakan 'venv\Scripts\activate'
   ```

4. **Instal dependensi**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Jalankan aplikasi**:

   ```bash
   python app.py
   ```

6. **Akses aplikasi**:

   Buka browser dan kunjungi `http://localhost:5000`.

## Penggunaan

- **Akses Kamera**: Saat mengakses aplikasi, pastikan memberikan izin akses kamera.
- **Deteksi Wajah**: Aplikasi akan secara otomatis mendeteksi wajah Anda melalui kamera.
- **Nama Acak**: Setelah wajah terdeteksi, aplikasi akan menampilkan nama acak yang diambil dari daftar yang telah ditentukan.

## Kontribusi

Kontribusi sangat diterima. Silakan fork repositori ini dan buat pull request untuk perbaikan atau penambahan fitur.

## Lisensi

Proyek ini dilisensikan di bawah lisensi MIT. Lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.
