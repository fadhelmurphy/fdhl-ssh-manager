# SSH Manager

SSH Manager adalah sebuah alat sederhana untuk mengelola kunci SSH pada folder `.ssh`.

## Instalasi

Anda dapat menginstal SSH Manager dengan menggunakan pip:

```
pip install .
```

## Penggunaan

Setelah menginstal, Anda dapat menjalankan SSH Manager dengan menjalankan perintah `fdhl-ssh-manager` dari terminal.

SSH Manager memiliki beberapa opsi:

1. **Daftar kunci SSH**: Menampilkan daftar kunci SSH yang tersedia dalam folder `.ssh`.
2. **Pilih kunci SSH**: Memilih kunci SSH yang akan digunakan pada semua host.
3. **Generate kunci SSH baru**: Menghasilkan kunci SSH baru.
4. **Hapus kunci SSH**: Menghapus kunci SSH yang dipilih.
5. **Custom konfigurasi SSH**: Menambahkan konfigurasi SSH secara manual.
6. **Tambahkan host dari file**: Membaca konfigurasi host dari file teks dan menambahkannya ke konfigurasi SSH.
7. **Keluar**: Keluar dari SSH Manager.

Pastikan untuk memastikan bahwa file `.ssh/config` memiliki izin yang benar sehingga Anda dapat menulis ke dalamnya.

## Contoh Format File Host

Jika Anda memilih opsi untuk menambahkan host dari file, pastikan format file Anda sesuai. Berikut adalah contoh format file host:

```
Host jos
HostName 108.30.0.1
HostKeyAlgorithms +ssh-rsa
PubkeyAcceptedKeyTypes +ssh-rsa
User root

Host gandos
HostName 103.30.0.2
User fadhelganteng
```

## Lisensi

Gunadarma License
