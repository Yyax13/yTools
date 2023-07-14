import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Exemplo de uso
print("Texto antes de limpar a tela")
limpar_tela()
print("Texto após limpar a tela")
