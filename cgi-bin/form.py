#!/usr/bin/env python3
import cgi
from string import ascii_letters, digits
alphabet_list = ascii_letters + digits


def caesar_code(text, shift):
    shift_text = ''

    for c in text:
        if c not in alphabet_list:
            shift_text += c
            continue

        i = (alphabet_list.index(c) + shift) % len(alphabet_list)
        shift_text += alphabet_list[i]

    return shift_text

form = cgi.FieldStorage()
name = form.getfirst("name", "не задано")
str_to_encode = form.getfirst("str_to_encode", "не задано")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Фраза зашифрована</title>
        </head>
        <body>""")

print("<p>Уважаемый {}! Ваша фраза была успешно зашифрована...</p>".format(name))
print("<p>Ваша фраза после шифрования: </p>")
print(caesar_code(str_to_encode.lower(), shift=5))

print("""</body></html>""")
