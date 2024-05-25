import os

def list_ssh_keys():
    ssh_dir = os.path.expanduser("~/.ssh")
    keys = [f for f in os.listdir(ssh_dir) if f.endswith(".pub")]
    return keys

def choose_ssh_key(keys):
    print("Pilih kunci SSH yang ingin digunakan:")
    for i, key in enumerate(keys):
        print(f"{i+1}. {key}")

    choice = input("Masukkan nomor kunci: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(keys):
            return keys[choice - 1]
        else:
            print("Nomor kunci tidak valid.")
            return None
    except ValueError:
        print("Masukan tidak valid.")
        return None

def generate_ssh_key():
    ssh_dir = os.path.expanduser("~/.ssh")
    key_name = input("Masukkan nama untuk kunci SSH baru (tanpa ekstensi .pub): ")
    os.system(f"ssh-keygen -t rsa -b 4096 -C '' -f {ssh_dir}/{key_name}")

def delete_ssh_key():
    keys = list_ssh_keys()
    if not keys:
        print("Tidak ada kunci SSH yang ditemukan dalam folder .ssh.")
        return

    print("Pilih kunci SSH yang ingin dihapus:")
    for i, key in enumerate(keys):
        print(f"{i+1}. {key}")

    choice = input("Masukkan nomor kunci yang ingin dihapus: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(keys):
            ssh_dir = os.path.expanduser("~/.ssh")
            key_to_delete = keys[choice - 1]
            confirm_delete = input(f"Apakah Anda yakin ingin menghapus kunci SSH {key_to_delete}? (y/n): ")
            if confirm_delete.lower() == 'y':
                os.remove(f"{ssh_dir}/{key_to_delete}")
                os.remove(f"{ssh_dir}/{key_to_delete[:-4]}")
                print(f"Kunci SSH {key_to_delete} telah dihapus.")
        else:
            print("Nomor kunci tidak valid.")
    except ValueError:
        print("Masukan tidak valid.")

def update_ssh_config(selected_key):
    ssh_config_path = os.path.expanduser("~/.ssh/config")
    with open(ssh_config_path, "w") as f:
        f.write("\n")
        f.write("Host *\n")
        f.write(f"    IdentityFile ~/.ssh/{selected_key}\n")
    print("Konfigurasi SSH telah diperbarui.")

def main():
    while True:
        print("\nMenu:")
        print("1. Daftar kunci SSH")
        print("2. Pilih kunci SSH")
        print("3. Generate kunci SSH baru")
        print("4. Hapus kunci SSH")
        print("5. Keluar")

        choice = input("Pilihan Anda: ")
        try:
            choice = int(choice)
            if choice == 1:
                confirm = input("Anda yakin ingin menampilkan daftar kunci SSH? (y/n): ")
                if confirm.lower() == 'y':
                    keys = list_ssh_keys()
                    if keys:
                        print("Kunci SSH yang tersedia:")
                        for key in keys:
                            print(key)
                    else:
                        print("Tidak ada kunci SSH yang ditemukan dalam folder .ssh.")
            elif choice == 2:
                confirm = input("Anda yakin ingin memilih kunci SSH? (y/n): ")
                if confirm.lower() == 'y':
                    keys = list_ssh_keys()
                    if not keys:
                        print("Tidak ada kunci SSH yang ditemukan dalam folder .ssh.")
                        continue
                    selected_key = choose_ssh_key(keys)
                    if selected_key:
                        update_ssh_config(selected_key)
            elif choice == 3:
                confirm = input("Anda yakin ingin mengenerate kunci SSH baru? (y/n): ")
                if confirm.lower() == 'y':
                    generate_ssh_key()
            elif choice == 4:
                keys = list_ssh_keys()
                delete_ssh_key(keys)
            elif choice == 5:
                confirm = input("Anda yakin ingin keluar? (y/n): ")
                if confirm.lower() == 'y':
                    print("Terima kasih!")
                    break
                else:
                    continue
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Masukan tidak valid.")

if __name__ == "__main__":
    main()
