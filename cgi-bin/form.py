#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
name = form.getfirst("name", "не задано")
password = form.getfirst("password", "не задано")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных</title>
        </head>
        <body>""")

print("<h1>Спасибо! Вас внесли в базу данных:</h1>")
print("<p>Ваше имя: {}</p>".format(name))
print("<p>Ваш пароль: {}</p>".format(password))

print("""</body>
        </html>""")
