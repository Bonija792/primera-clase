import random

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
longitud_contrasena = int(input("Introduce la longitud de la contraseña: "))
contrasena_generada = ""

for _ in range(longitud_contrasena):
    caracter_aleatorio = random.choice(caracteres)
    contrasena_generada += caracter_aleatorio

print("Contraseña generada:", contrasena_generada)