#!/usr/bin/python3
#Autor: ClownSaw
#Web: www.clownsaw.k
"""PDF_Cracker es un script en python3 muy facil de usar el script es muy
   facil de usar su uso es simple python3 pdf_cracker.py example.pdf wordlist.txt
   y puede ser usado en windows, linux y mac......Tambien puede usarlo en android
   usando termux."""
import pikepdf, sys, random, time
from tqdm import tqdm
from colorama import init, Fore

GREEN = Fore.GREEN
RESET = Fore.RESET
RED = Fore.RED
BLUE = Fore.BLUE
CYAN = Fore.CYAN
GRAY = Fore.LIGHTBLACK_EX


def ClownLogo():
    from colorama import init, Fore
    import sys, random, time
    init()
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """


╔═╗╔╦╗╔═╗ + * #                   
╠═╝ ║║╠╣      * # +               
╩  ═╩╝╚         * # +             
 + # *  ╔═╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
   + #  ║  ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
      + ╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═
            Autor: ClownSaw
    """
    for N, line in enumerate(x.split("\n")):
         sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
         time.sleep(0.05)

def usage():
    print(f"{RED}usage {BLUE}: {GREEN}pdf_cracker.py [example.pdf] [wordlist.txt]{RESET}")

ClownLogo()

try:
    #Wordlist file
    wordlist = sys.argv[2]
    # the pdf file you want to crack its password
    pdf_file = sys.argv[1]
except:
    usage()
    exit()
# load password list
passwords = open(wordlist)

# iterate over passwords
for i in passwords.readlines():
    password = i.strip("\n")
    try:
        #Password found
        print(f"{GREEN}[{CYAN}X{GREEN}] {BLUE}password failed: {RED}"+password)
        # open PDF file
        with pikepdf.open(pdf_file, password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print(f"{GREEN}   [{RED}+{GREEN}] Password found:", f"{BLUE}", "%s" % (password), f"{RESET}")
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue