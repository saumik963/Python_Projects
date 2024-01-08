import os
import pikepdf
from tqdm import tqdm
from termcolor import colored

# load password list
passwords = [line.strip() for line in open("passlist.txt")]

pdf_file = input(colored("Enter PDF File Name: ", 'cyan'))

# Check if the file exists
if not os.path.exists(pdf_file):
    print(colored("[-] Error: The specified PDF file does not exist.", 'red'))
    exit()

# iterate over passwords
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        with pikepdf.open(pdf_file, password=password):
            print(colored("\n[+] Password Found: {}".format(password), 'green'))
            break
    except pikepdf._core.PasswordError as e:
        # wrong password, just continue in the loop
        continue