from termcolor import colored
import os

ban = r"""
$$$$$$$\                                           $$\               
$$  __$$\                                          $$ |              
$$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\ $$$$$$\    $$$$$$$\ 
$$$$$$$  |$$  __$$\ $$  __$$\ $$  _____|$$  __$$\\_$$  _|  $$  _____|
$$  ____/ $$ |  \__|$$$$$$$$ |\$$$$$$\  $$$$$$$$ | $$ |    \$$$$$$\  
$$ |      $$ |      $$   ____| \____$$\ $$   ____| $$ |$$\  \____$$\ 
$$ |      $$ |      \$$$$$$$\ $$$$$$$  |\$$$$$$$\  \$$$$  |$$$$$$$  |
\__|      \__|       \_______|\_______/  \_______|  \____/ \_______/ 
                                                                     
                                                                     
"""

OPTIONS = r"""
    [01] Hacked by html page
    [00] Back to main
"""

def clear_screen():
   os.system('cls' if os.name == 'nt' else 'clear')
   
def write():
    with open(output_name, "w") as arquivo:
          arquivo.write(arq_content)
    print(colored("\nPreset salvo em", 'blue'), output_name, colored('\nUse cat ', 'blue'), output_name, colored('para abrir o arquivo', 'blue'))
    
def read_arq(arq_adress):
    with open(arq_adress, 'r') as arquivo:
        content = arquivo.read()
    return content


clear_screen()
print(colored(ban, 'blue', 'on_grey', ['bold']))
arq_adress = 'Presets/hacked-by.html'
arq_content = read_arq(arq_adress)

print(colored(OPTIONS, 'green'))
choose = input(colored('Escolha uma opção:  ', 'magenta'))


if choose in ['01', '1']:
  output_name = input(colored("nome do output (inclua .txt ou outras extensões):  ",  "magenta"))
  write()
if choose in ['00', '0']:
  clear_screen()
  os.system('python main.py')
