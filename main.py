import requests
import subprocess
import time

WIFI_SSID = "Название_вашей_сети"
WIFI_PASSWORD = "Пароль_от_сети"

def check_internet():
    url = "http://www.google.com"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"Ошибка при проверке интернета: {e}")
        return False

def connect_to_wifi(ssid, password):
    try:
        cmd = ['sudo', 'nmcli', 'device', 'wifi', 'connect', ssid, 'password', password]
        subprocess.run(cmd, check=True)  # Проверка успешности выполнения команды
        print("Успешно подключено к Wi-Fi")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при подключении к Wi-Fi: {e}")

while True:
    if not check_internet():
        print("Соединение оборвалось, переподключение к Wi-Fi...")
        connect_to_wifi(WIFI_SSID, WIFI_PASSWORD)
    else:
        print("Интернет подключен")
    time.sleep(10)  # Проверка каждые 10 секунд
