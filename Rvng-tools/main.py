import os
from termcolor import colored
import time

BANNER = r"""
███╗   ███╗ █████╗ ██╗███╗   ██╗
████╗ ████║██╔══██╗██║████╗  ██║
██╔████╔██║███████║██║██╔██╗ ██║
██║╚██╔╝██║██╔══██║██║██║╚██╗██║
██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝                                                                           
"""
         
BANNER_YYAX = r"""
 █████ █████                                 
░░███ ░░███                                  
 ░░███ ███   █████ ████  ██████   █████ █████
  ░░█████   ░░███ ░███  ░░░░░███ ░░███ ░░███ 
   ░░███     ░███ ░███   ███████  ░░░█████░  
    ░███     ░███ ░███  ███░░███   ███░░░███ 
    █████    ░░███████ ░░████████ █████ █████
   ░░░░░      ░░░░░███  ░░░░░░░░ ░░░░░ ░░░░░ 
              ███ ░███                       
             ░░██████                        
              ░░░░░░                         
"""
         
crrtk = '`thwRl_%%0.[[y,hjlzz=m|ss```HHH___kL]'

def options():
   print('   [01] Ymap')
   print('   [02] CheckStatus')
   print('   [03] Crypter')
   print('   [04] Decrypter')
   print('   [05] Fake SmS')
   print('   [06] Ip Info')
   print('   [07] Reader')
   print('   [08] Tools')
   print('   [09] Adress')
   print('   [XX] Yyax: the dev')
   print('   [YY] Presets')
   print('   [00] Quit')


def clear_screen():
   os.system('cls' if os.name == 'nt' else 'clear')

def banner():
   print(colored("\033[1;34m" + BANNER + "\033[0m", 'red', 'on_grey', ['blink']))
   

   
clear_screen()
banner()
options()

choose = input(colored('\nchoose an option:  ', 'green'))


if choose in ['02', '2']:
    print("OK, Redirecting...")
    print("file avaliable")
    input("write RD and press Enter to redirect  ")
    clear_screen()
    os.system('python all/checkstatus.py')
elif choose in ['03', '3']:
    print("OK, Redirecting...")
    print("file avaliable")
    input("write RD and press Enter to redirect  ")
    clear_screen()
    os.system('python all/crypter.py')
elif choose in ['04', '4']:
    print("OK, Redirecting...")
    print("file avaliable")
    input("write RD and press Enter to redirect  ")
    clear_screen()
    os.system('python all/decrypt.py')
elif choose in ['05', '5']:
    print("OK, Redirecting...")
    print("file avaliable")
    input("write RD and press Enter to redirect  ")
    clear_screen()
    os.system('python all/fake-sms.py')
elif choose in ['06', '6']:
    print("OK, Redirecting...")
    print("file avaliable")
    input("write RD and press Enter to redirect  ")
    clear_screen()
    os.system('python all/ip-info.py')
elif choose in ['07', '7']:
    print("OK, Redirecting...")
    print("file avaliable")
    input("write RD and press Enter to redirect  ")
    clear_screen()
    os.system('python all/reader.py')
elif choose in ['08', '8']:
    print("OK, Redirecting...")
    print("file avaliable")
    input("write RD and press Enter to redirect  ")
    clear_screen()
    os.system('python all/Tools.py')
elif choose in ['09', '9']:
    print("OK, Redirecting...")
    print("file avaliable")
    input("write RD and press Enter to redirect  ")
    clear_screen()
    os.system('python all/adress-coords.py')
elif choose in ['X', 'XX', 'x', 'xx']:
    clear_screen()
    print(colored(BANNER_YYAX, 'green', 'on_grey', ['bold']))
    print(colored("""
                           
    Yyax:                  
                           
pix: +55 (43) 99122-5928              
                                      
TikTok: @rvngyyax                     
                                      
Instagram: @rvnggroup                 
                                      
telegram: t.me/RvngGroup              
                                      
Thanks for using my tool <3           
                                      
support with BLR if u wanna more tools
""", 'blue'))
elif choose in ['YY', 'Y', 'yy', 'y']:
    print("OK, Redirecting...")
    print("file avaliable")
    input("write RD and press Enter to redirect  ")
    clear_screen()
    os.system('python /all/presets.py')
elif choose in ['DD', 'dd', 'd', 'D']:
    input(colored('You realy wanna run this tool (any text = yes, Ctrl + C to quit)? ', 'red', 'on_grey', ['bold', 'blink']))
    clear_screen()
    input(colored('Again, you realy wanna run this tool (yes = yes, Ctrl + C to quit)? ', 'red', 'on_grey', ['bold', 'blink']))
    clear_screen()
    os.system('python /all/destruct.py')
elif choose in ['00', '0']:
    input(colored('write Q and press Enter to continue...  ', 'blue', 'on_grey', ['blink']))
    
if choose in ['01', '1']:
    print("OK, Redirecting...")
    print("file avaliable")
    input("write RD and press Enter to redirect  ")
    clear_screen()
    YmapKey = input(colored("This tool is private, pls insert ur acess key here: \n\n", 'red', 'on_grey', ['bold']))
    
if YmapKey ==  crrtk:
    time.sleep(2)
    print(colored('\nAcess granted', 'green', 'on_blue', ['bold']))
    time.sleep(1)
    os.system('clear && cd misc && python Ymap.py --help')
else:
   print(colored('INCORRECT', 'red'))
   time.sleep(3)
   clear.screen()

input(colored('\npress Enter to continue...  ', 'red', 'on_grey', ['blink']))
clear_screen()
print(colored('Thanks for use Rvng-tools', 'green', 'on_grey', ['blink']))
