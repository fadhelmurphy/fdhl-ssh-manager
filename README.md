# Sheesh Man

Sheesh Man adalah sebuah alat sederhana untuk mengelola kunci SSH pada folder `.ssh`.

## Instalasi

Anda dapat menginstal Sheesh Man dengan menggunakan pip:

```
pip install .
```

## Penggunaan

Setelah menginstal, Anda dapat menjalankan Sheesh Man dengan menjalankan perintah `sheesh-man` dari terminal.

### Menu

Setelah menjalankan sheesh-man, Anda akan melihat menu dengan beberapa pilihan:

1. **Daftar kunci SSH**: Menampilkan daftar kunci SSH yang tersedia di folder `~/.ssh`.
2. **Pilih kunci SSH**: Memilih kunci SSH yang akan digunakan dan memperbarui konfigurasi SSH.
3. **Generate kunci SSH baru**: Membuat kunci SSH baru.
4. **Hapus kunci SSH**: Menghapus kunci SSH yang dipilih.
5. **Custom konfigurasi SSH**: Menambahkan konfigurasi SSH khusus.
6. **Tambahkan host dari file**: Menambahkan host SSH dari file teks.
7. **Switch config file**: Mengganti file konfigurasi SSH dengan file konfigurasi lain yang dipilih.
8. **Keluar**: Keluar dari aplikasi.

### Contoh Penggunaan

#### Daftar kunci SSH

Menampilkan semua kunci SSH yang tersedia di folder `~/.ssh`.

#### Pilih kunci SSH

Memilih kunci SSH yang akan digunakan dan memperbarui file konfigurasi `~/.ssh/config` dengan kunci tersebut.

#### Generate kunci SSH baru

Menghasilkan kunci SSH baru dengan perintah `ssh-keygen -t rsa -b 4096 -C`.

#### Hapus kunci SSH

Menghapus kunci SSH yang dipilih dari folder `~/.ssh`.

#### Custom konfigurasi SSH

Menambahkan konfigurasi SSH kustom ke file `~/.ssh/config`. Anda akan diminta untuk memasukkan nama host, hostname, user, dan parameter opsional lainnya.

#### Tambahkan host dari file

Menambahkan host SSH dari file teks. Format file teks harus seperti berikut:

```
Host jos
    HostName 108.30.0.1
    User root

Host gandos
    HostName 103.30.0.2
    User fadhelganteng
```

#### Switch config file

Mengganti file konfigurasi SSH `~/.ssh/config` dengan salah satu file konfigurasi lain yang ada di folder `~/.ssh`. Anda dapat memilih file konfigurasi alternatif seperti `~/.ssh/config_fulltime`, `~/.ssh/config_freelance`, dll.

## Lisensi

Gunadarma License
