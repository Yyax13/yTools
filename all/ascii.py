from termcolor import colored
import os
from pyfiglet import Figlet
import time

__big_banner__ = r'''
__   __                       _    ____   ____ ___ ___ 
\ \ / /   _  __  __  __      / \  / ___| / ___|_ _|_ _|
 \ V / | | |/ _` \ \/ /____ / _ \ \___ \| |    | | | | 
  | || |_| | (_| |>  <_____/ ___ \ ___) | |___ | | | | 
  |_| \__, |\__,_/_/\_\   /_/   \_\____/ \____|___|___|
      |___/                                            
_________________________________________________________________________
Isto é uma prévia BETA da ferramenta, favor reportar qualquer bug no meu tiktok @rvngyyax

'''

font_opt = r"""
   OPTIONS FOR FONTS:

   standard:
 ____  _                  _               _ 
/ ___|| |_ __ _ _ __   __| | __ _ _ __ __| |
\___ \| __/ _` | '_ \ / _` |/ _` | '__/ _` |
 ___) | || (_| | | | | (_| | (_| | | | (_| |
|____/ \__\____|_| |_|\____|\____|_|  \____|
   
   Choose an option (all lowcase pls):  """
   
text_opt = r"""   Texto para a arte:  """

def screen():
   os.system('clear')
   print(colored(__big_banner__, 'red', '', ['bold']))
   time.sleep(1.2)

def ascii():
   time.sleep(0.6)
   f = Figlet(font=input(colored(font_opt, 'yellow', '', ['bold'])))
   banner = f.renderText(input(colored(text_opt, 'green', '', ['bold'])))
   print(colored('\n\nYour banner: \n\n', 'green', '', ['bold']))
   print(banner)

screen()
ascii()
