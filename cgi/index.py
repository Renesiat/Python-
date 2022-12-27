#!C:/Python311/python.exe

import os

# змінні оточення доступні через модуль os (os.environ), імена та кількість залежить від сервера
envs = "<ul>" + ''.join( f"<li>{k} = {v}</li>" for k,v in os.environ.items() ) + "</ul>"
# змінних багато, зокрема
# REQUEST_METHOD (GET/POST/ +можливість довільних методів - вони проходять і передаються)
# REQUEST_URI - повний текст запиту (окрім домену:  /index.py? x=10&y=20 )
# QUERY_STRING - лише GET-параметри (  x=10&y=20 )
# REMOTE_ADDR - IP з якого надішов запит
# всі заголовки запиту перетворюються у змінні на кшталт HTTP_..., наприклад
#  заголовок Сonnection: keep-alive стане змінною  HTTP_CONNECTION = keep-alive
# DOCUMENT_ROOT - коренева папка домену (сайту), можна використовувати для абсолютної адресації файлів
# REQUEST_SCHEME = http   - протокол запиту
# також ряд змінних передає системну інформацію (імена скриптів, шляхи) - це робить
#  змінні оточення небезпечними для поширення, тому бажано обмежувати їх відображення

# Д.З. Вивести скорочені відомості про запит: метод, скрипт, параметри запиту (розібрати у словник) {envs}
# body = sys.stdin.read()

html = f"""<!doctype html />
<html>
<head>
</head>
<body>
    <h1>Hello CGI World</h1>
    
</body>
</html>"""


                                      # Оскільки ми формуємо відповідь, дотримуємось НТТР
                                      # перший рядок - статус може формувати сервер
print( "Content-Type: text/html; charset=utf-8" )    # далі ідуть заголовки
print( f"Content-Length: {len(html)}" )
print( "" )                           # тіло відокремлюється порожнім рядком
print( html )                         # далі іде тіло. За наявності тіла вимагається наявність
                                      # заголовків Content-Type: та Content-Length:
                                      # Через потребу Content-Length тіло формують окремо

# ??? розрив рядків: реально 2 символи, а len(html) рахує як один
# '''
# Серверний додаток Python
# Режим CGI
# CGI - Common Gateway Interface - протокол (інтерфейс), згідно з яким
# веб-сервер (сервер додатків) може запускати довільні програми.
# Учасники:
#  - веб-сервер (Apache): ПЗ для слухання порту, прийому НТТР-запитів,
#     розбору їх частин та утворення змінних оточення (environment variables)
#     Далі сервер може запустити програму у даному оточенні, фактично
#     передавши у програму ці змінні
#  - інтерпретатор Python: виконавча програма (така, що запускається ОС)
#  - скрипт Python, що буде виконуватись інтерпретатором. Усе, що виводить
#     скрипт у std::out буде передано сервером як відповідь на запит.
#     У окремих випадках сервер може додати власні заголовки або статуси,
#     але загалом формування відповіді - повністю на виконавці

# Налагодження:
#  1. Створюємо локальний хост (сайт) із зазначенням CGI режиму
#     - створюємо папку для сайта (C:\Users\_dns_\source\repos\Py192\cgi), 
#         створюємо у ній файл index.py 
#         у ньому: зазначаємо шлях до інтерпретатора
#         та команду виведення коду HTML
#     - знаходимо файли конфігурації Apache (httpd-vhosts.conf або httpd.conf)
#     - додаємо відомості про новий хост (як правило, є зразок)
#         <VirtualHost *:80>
#             ServerAdmin webmaster@localhost
#             DocumentRoot "C:/Users/_dns_/source/repos/Py192/cgi"
#             ServerName py192.loc
#             ErrorLog "C:/Users/_dns_/source/repos/Py192/cgi/error.log"
#             CustomLog "C:/Users/_dns_/source/repos/Py192/cgi/access.log" common
#             <Directory "C:/Users/_dns_/source/repos/Py192/cgi">
#                 AllowOverride All
#                 Options -Indexes +ExecCGI
#                 AddHandler cgi-script .py
#                 Require all granted
#             </Directory>
#         </VirtualHost>
#     - знаходимо файл конфігурації httpd.conf, знаходимо рядок (~286) з 
#         DirectoryIndex  index.php index.pl ... (додаємо) index.py
#       зберігаємо конфігурації і обов'язково перезапускаємо Apache  
#         ознакою успішного створення локального хосту є поява файлів error.log, access.log
#         у заявленій папці. Можна додати ці файли до .gitignore

#  2. Реєструємо адресу нового сайту у локальній DNS: відкриваємо файл 
#        C:\Windows\System32\drivers\etc\hosts  (у режимі адміністратора)
#        /etc/hosts
#        додаємо рядки з іменем хоста (ServerName)
#        	127.0.0.1       py192.loc
# 	    ::1             py192.loc

#  3. Запускаємо браузер та вводимо повністю http://py192.loc

# '''