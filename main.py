import os
import sys
import time

if os.name == 'nt':
    os.system('title © raven.ovh | 2023 | Pinger')
else:
    print("\33]0;© raven.ovh | 2023 | Pinger\a", end="", flush=True)

os.system('cls' if os.name == 'nt' else 'clear')

print('© raven.ovh | 2023')
time.sleep(2)

os.system('cls' if os.name == 'nt' else 'clear')


def loading():
    for i in range(0, 101):
        time.sleep(0.05)
        sys.stdout.write("\r" + "[+] Loading modules: %d%%" % i)
        sys.stdout.flush()
    print("\n")


loading()

os.system('cls' if os.name == 'nt' else 'clear')

print('© raven.ovh | What do you wanna ping ?')
print('1. Website')
print('2. IP')
choice = input('Choice: ')

if choice == '1':
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Example: google.com')
    website = input('Website: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('ping ' + website)
elif choice == '2':
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Example: 1.1.1.1')
    ip = input('IP: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('ping ' + ip)
else:
    print('Wrong choice!')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()
