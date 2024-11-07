import requests

# Daftar URL file GitHub yang ingin diambil isinya
file_urls = [
     'https://github.com/ErcinDedeoglu/proxies/raw/refs/heads/main/proxies/http.txt',
     'https://github.com/ErcinDedeoglu/proxies/raw/refs/heads/main/proxies/https.txt',
     'https://github.com/ErcinDedeoglu/proxies/raw/refs/heads/main/proxies/socks4.txt',
     'https://github.com/ErcinDedeoglu/proxies/raw/refs/heads/main/proxies/socks5.txt',
     'https://github.com/hookzof/socks5_list/raw/refs/heads/master/proxy.txt',
     'https://github.com/MyZest/update-live-socks5/raw/refs/heads/master/liveSocks5.txt',
     'https://github.com/r00tee/Proxy-List/raw/refs/heads/main/Socks5.txt',
     'https://github.com/r00tee/Proxy-List/raw/refs/heads/main/Socks4.txt',
     'https://github.com/r00tee/Proxy-List/raw/refs/heads/main/Https.txt',
     'https://github.com/babyhagey74/free-proxies/raw/refs/heads/main/proxies/http/http.txt',
     'https://github.com/babyhagey74/free-proxies/raw/refs/heads/main/proxies/https/https.txt',
     'https://github.com/babyhagey74/free-proxies/raw/refs/heads/main/proxies/socks4/socks4.txt',
     'https://github.com/babyhagey74/free-proxies/raw/refs/heads/main/proxies/socks5/socks5.txt',
     'https://github.com/Vann-Dev/proxy-list/raw/refs/heads/main/proxies/http.txt',
     'https://github.com/Vann-Dev/proxy-list/raw/refs/heads/main/proxies/https.txt',
     'https://github.com/Vann-Dev/proxy-list/raw/refs/heads/main/proxies/socks4.txt',
     'https://github.com/Vann-Dev/proxy-list/raw/refs/heads/main/proxies/socks5.txt',
     'https://github.com/zloi-user/hideip.me/raw/refs/heads/main/http.txt',
     'https://github.com/zloi-user/hideip.me/raw/refs/heads/main/https.txt',
     'https://github.com/zloi-user/hideip.me/raw/refs/heads/main/socks4.txt',
     'https://github.com/zloi-user/hideip.me/raw/refs/heads/main/socks5.txt',
     'https://github.com/ALIILAPRO/Proxy/raw/refs/heads/main/http.txt',
     'https://github.com/ALIILAPRO/Proxy/raw/refs/heads/main/socks4.txt',
     'https://github.com/ALIILAPRO/Proxy/raw/refs/heads/main/socks5.txt',
     'https://github.com/sunny9577/proxy-scraper/raw/refs/heads/master/generated/http_proxies.txt',
     'https://github.com/sunny9577/proxy-scraper/raw/refs/heads/master/generated/socks4_proxies.txt',
     'https://github.com/sunny9577/proxy-scraper/raw/refs/heads/master/generated/socks5_proxies.txt',
]

# Fungsi untuk mengambil konten file
def fetch_file_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Cek jika ada error HTTP
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Gagal mengambil file: {url} - {e}")
        return ''

# Fungsi utama untuk menggabungkan konten semua file ke dalam satu file
def combine_files():
    combined_content = ''

    for url in file_urls:
        content = fetch_file_content(url)
        
        # Tentukan prefix berdasarkan nama file
        prefix = ''
        if 'http.txt' in url:
            prefix = 'http://'
        elif 'https.txt' in url:
            prefix = 'https://'
        elif 'socks4.txt' in url:
            prefix = 'socks4://'
        elif 'socks5.txt' in url:
            prefix = 'socks5://'

        # Tambahkan prefix ke setiap baris konten dan gabungkan
        prefixed_content = '\n'.join(
            f"{prefix}{line.strip()}" for line in content.splitlines() if line.strip()
        )
        
        combined_content += prefixed_content + '\n\n'  # Tambahkan newline antar file

    # Simpan konten gabungan ke dalam satu file
    with open('active_proxies.txt', 'w') as file:
        file.write(combined_content)
    print('File berhasil digabungkan ke active_proxies.txt')

# Jalankan fungsi penggabungan
combine_files()
