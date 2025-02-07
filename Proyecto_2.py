import random
import string

def generar_contrasena(longitud):
    # Definimos los caracteres que se pueden usar en la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Usamos una lista por comprensión para generar la contraseña
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

# Solicitamos al usuario la longitud de la contraseña
longitud = int(input("Introduce la longitud de la contraseña: "))
# Generamos la contraseña
contrasena = generar_contrasena(longitud)
# Mostramos la contraseña generada
print(f"Tu nueva contraseña es: {contrasena}")

