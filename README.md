# Sheesh Man

Sheesh Man adalah sebuah alat sederhana untuk mengelola SSH key pada folder `.ssh`.

## Instalasi

Anda dapat menginstal Sheesh Man dengan menggunakan pip:

```
pip install .
```

## Penggunaan

Setelah menginstal, Anda dapat menjalankan Sheesh Man dengan menjalankan perintah `sheesh-man` dari terminal.

### Menu

Setelah menjalankan sheesh-man, Anda akan melihat menu dengan beberapa pilihan:

## Fitur

1. **Daftar SSH key**: Menampilkan daftar SSH key yang tersimpan dalam folder `.ssh`.
2. **Pilih SSH key**: Memungkinkan pengguna untuk memilih SSH key yang akan digunakan.
3. **Generate SSH key Baru**: Menghasilkan SSH key baru dengan menggunakan `ssh-keygen -t rsa -b 4096 -C`.
4. **Hapus SSH key**: Menghapus SSH key yang tidak diperlukan.
5. **Custom Konfigurasi SSH**: Menambahkan konfigurasi kustom ke file `~/.ssh/config`.
6. **Tambahkan Host dari File**: Menambahkan daftar host dari sebuah file ke file `~/.ssh/config`.
7. **Switch File Konfigurasi**: Mengganti file konfigurasi SSH yang aktif.
8. **Tampilkan Daftar Host**: Menampilkan daftar host server yang terdaftar di file `~/.ssh/config`.
9. **Masuk ke Salah Satu Host Server**: Memungkinkan pengguna untuk masuk ke salah satu host server.
0. **Keluar**: Keluar dari aplikasi.

### Contoh Penggunaan

#### Daftar SSH key

Menampilkan semua SSH key yang tersedia di folder `~/.ssh`.

#### Pilih SSH key

Memilih SSH key yang akan digunakan dan memperbarui file konfigurasi `~/.ssh/config` dengan kunci tersebut.

#### Generate SSH key baru

Menghasilkan SSH key baru dengan perintah `ssh-keygen -t rsa -b 4096 -C`.

#### Hapus SSH key

Menghapus SSH key yang dipilih dari folder `~/.ssh`.

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

#### Switch File Konfigurasi

Mengganti file konfigurasi SSH `~/.ssh/config` dengan salah satu file konfigurasi lain yang ada di folder `~/.ssh`. Anda dapat memilih file konfigurasi alternatif seperti `~/.ssh/config_fulltime`, `~/.ssh/config_freelance`, dll.

## Lisensi

Gunadarma License
