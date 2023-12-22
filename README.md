<h2>Циклическая проверка соединения с интернетом на Python в Linux</h2>

<p>
  Импорт библиотек: <br>
  requests - для выполнения HTTP-запросов к веб-сайту и проверки доступности интернета.<br>
  subprocess - для запуска команд в терминале Linux из Python.<br>
  time - для работы с временными задержками.
</p>
<p>
  Настройки Wi-Fi:<br>
  WIFI_SSID и WIFI_PASSWORD содержат название вашей Wi-Fi сети (SSID) и пароль для подключения.
</p>
<p>
  Функция check_internet():<br>
  Отправляет GET-запрос на сайт http://www.google.com с таймаутом 5 секунд.<br>
  Если успешно получен ответ с кодом статуса 200 (OK), функция возвращает True, указывая на доступность интернета.<br>
  В случае ошибки (например, отсутствия соединения или недоступности сайта), функция возвращает False.
</p>
<p>
  Функция connect_to_wifi(ssid, password):<br>
  Формирует команду для подключения к Wi-Fi сети с помощью инструмента NetworkManager (nmcli).<br>
  Использует subprocess.run() для выполнения команды.<br>
  При успешном подключении выводит сообщение "Успешно подключено к Wi-Fi".<br>
  В случае ошибки при выполнении команды выводит соответствующее сообщение.
</p>
<p>
  Основной цикл while True:
  Проверяет доступность интернета с помощью check_internet().<br>
  Если интернет недоступен (check_internet() возвращает False), выполняется попытка переподключения к Wi-Fi через connect_to_wifi().<br>
  Если интернет доступен, выводится сообщение "Интернет подключено".<br>
  Далее устанавливается задержка в 10 секунд перед следующей проверкой соединения.
</p>




