def inverter_string(texto):
    texto_invertido = texto[::-1]
    return texto_invertido

texto_original = input("texto:  ")
texto_invertido = inverter_string(texto_original)
print("Texto original:", texto_original)
print("Texto invertido:", texto_invertido)
