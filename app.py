import os
import shutil
import argparse

def is_valid_file(f):
    return not (
        f.endswith(".pub") or 
        f.endswith(".pem") or
        f.startswith("known_") or
        f.startswith("config") or
        f.startswith(".DS_Store")
    )

def list_ssh_keys():
    ssh_dir = os.path.expanduser("~/.ssh")
    keys = [f for f in os.listdir(ssh_dir) if is_valid_file(f)]
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
    command = f"ssh-keygen -t rsa -b 4096 -C '' -f {ssh_dir}/{key_name}"
    os.system(command)

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
                os.remove(os.path.join(ssh_dir, key_to_delete))
                pub_key_to_delete = f"{key_to_delete}.pub"
                if os.path.exists(os.path.join(ssh_dir, pub_key_to_delete)):
                    os.remove(os.path.join(ssh_dir, pub_key_to_delete))
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

def custom_ssh_config():
    ssh_config_path = os.path.expanduser("~/.ssh/config")
    host = input("Masukkan nama host: ")
    hostname = input("Masukkan Hostname: ")
    host_key_algorithms = input("Masukkan HostKeyAlgorithms (opsional): ")
    pubkey_accepted_key_types = input("Masukkan PubkeyAcceptedKeyTypes (opsional): ")
    user = input("Masukkan User: ")
    with open(ssh_config_path, "a") as f:
        f.write("\n")
        f.write(f"Host {host}\n")
        f.write(f"    HostName {hostname}\n")
        if host_key_algorithms:
            f.write(f"    HostKeyAlgorithms {host_key_algorithms}\n")
        if pubkey_accepted_key_types:
            f.write(f"    PubkeyAcceptedKeyTypes {pubkey_accepted_key_types}\n")
        f.write(f"    User {user}\n")
    print("Konfigurasi SSH telah ditambahkan.")

def add_hosts_from_file(filename = None):
    if filename == None:
        filename = input("Masukkan nama file yang berisi daftar host: ")
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            host_info = {}
            for line in lines:
                line = line.strip()
                if line.startswith("Host "):
                    host_name = line.split()[1]
                    host_info[host_name] = {}
                elif line.startswith("HostName"):
                    hostname = line.split()[1]
                    host_info[host_name]["HostName"] = hostname
                elif line.startswith("User "):
                    user = line.split()[1]
                    host_info[host_name]["User"] = user
                elif line.startswith("Port"):
                    port = line.split()[1]
                    host_info[host_name]["Port"] = port

        with open(os.path.expanduser("~/.ssh/config"), "a") as ssh_config_file:
                for host, info in host_info.items():
                    ssh_config_file.write(f"\nHost {host}\n")
                    if 'HostName' in info:
                        ssh_config_file.write(f"    HostName {info['HostName']}\n")
                    if 'User' in info:
                        ssh_config_file.write(f"    User {info['User']}\n")
                    if 'Port' in info:
                        ssh_config_file.write(f"    Port {info['Port']}\n")
        
        print("Konfigurasi host telah ditambahkan.")
    except FileNotFoundError:
        print("File tidak ditemukan.")

def switch_config_file():
    ssh_dir = os.path.expanduser("~/.ssh")
    config_files = [f for f in os.listdir(ssh_dir) if f.startswith("config")]

    if not config_files:
        print("Tidak ada file konfigurasi yang ditemukan dalam folder .ssh.")
        return

    print("Pilih file konfigurasi SSH yang ingin digunakan:")
    for i, config_file in enumerate(config_files):
        print(f"{i+1}. {config_file}")

    choice = input("Masukkan nomor konfigurasi yang ingin digunakan: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(config_files):
            selected_config = config_files[choice - 1]
            shutil.copy(os.path.join(ssh_dir, selected_config), os.path.join(ssh_dir, "config"))
            print(f"File konfigurasi {selected_config} telah digunakan sebagai konfigurasi aktif.")
        else:
            print("Nomor konfigurasi tidak valid.")
    except ValueError:
        print("Masukan tidak valid.")

def list_host_servers(select=False):
    ssh_config_path = os.path.expanduser("~/.ssh/config")
    try:
        with open(ssh_config_path, "r") as f:
            lines = f.readlines()
            hosts = []
            for line in lines:
                if line.strip().startswith("Host ") and not any(keyword in line for keyword in ["github", "bitbucket", "gitlab"]):
                    host = line.split()[1:]
                    for h in host:
                        if h != '*':
                            hosts.append(h.split()[0])
            if hosts:
                print("Daftar host server:")
                for i, host in enumerate(hosts, start=1):
                    if select:
                        print(f"{i}. {host}")
                    else:
                        print(host)
                return hosts
            else:
                print("Tidak ada host server yang ditemukan.")
                return []
    except FileNotFoundError:
        print("File konfigurasi SSH tidak ditemukan.")

def connect_to_host(host):
    os.system(f"ssh {host}")

def select_non_git_host(hosts):
    if hosts:
        try:
            choice = int(input("Pilih nomor host yang ingin digunakan: "))
            if 1 <= choice <= len(hosts):
                selected_host = hosts[choice - 1]
                print(f"Anda telah memilih host: {selected_host}")
                connect_to_host(selected_host)
            else:
                print("Nomor host tidak valid.")
        except ValueError:
            print("Masukan tidak valid.")
    else:
        print("Tidak ada host server yang ditemukan.")

def main():
    parser = argparse.ArgumentParser(description="SSH Configuration Management")
    parser.add_argument("--host", help="Add hosts from file without confirmation", type=str)
    args = parser.parse_args()

    if args.host:
        add_hosts_from_file(args.host)
    else:
        while True:
            print("\nMenu:")
            print("1. Daftar SSH key")
            print("2. Pilih SSH key")
            print("3. Generate SSH key baru")
            print("4. Hapus SSH key")
            print("5. Custom konfigurasi SSH")
            print("6. Tambahkan host dari file")
            print("7. Switch config file")
            print("8. Tampilkan daftar host server")
            print("9. Masuk ke salah satu host server")
            print("0. Keluar")

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
                    confirm = input("Anda yakin ingin menghapus kunci SSH? (y/n): ")
                    if confirm.lower() == 'y':
                        delete_ssh_key()
                elif choice == 5:
                    confirm = input("Anda yakin ingin menambahkan custom konfigurasi SSH? (y/n): ")
                    if confirm.lower() == 'y':
                        custom_ssh_config()
                elif choice == 6:
                    confirm = input("Anda yakin ingin menambahkan host dari file? (y/n): ")
                    if confirm.lower() == 'y':
                        add_hosts_from_file()
                elif choice == 7:
                    confirm = input("Anda yakin ingin mengganti file konfigurasi SSH? (y/n): ")
                    if confirm.lower() == 'y':
                        switch_config_file()
                elif choice == 8:
                    confirm = input("Anda yakin ingin menampilkan daftar host server? (y/n): ")
                    if confirm.lower() == 'y':
                        list_host_servers()
                elif choice == 9:
                    confirm = input("Anda yakin ingin masuk ke salah satu host server? (y/n): ")
                    if confirm.lower() == 'y':
                        hosts = list_host_servers(select=True)
                        select_non_git_host(hosts)
                elif choice == 0:
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
