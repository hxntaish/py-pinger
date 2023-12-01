import os
import sys
import time

if os.name == 'nt':
    os.system('title © raven.ovh | 2023 | Pinger')
else:
    print("\33]0;© raven.ovh | 2023 | Pinger\a", end="", flush=True)

os.system('cls' if os.name == 'nt' else 'clear')

print('\033[1;31;40m' + '© raven.ovh | 2023 | Pinger' + '\033[0;37;40m')
time.sleep(2)

os.system('cls' if os.name == 'nt' else 'clear')


def loading():
    for i in range(0, 101):
        time.sleep(0.01)
        sys.stdout.write("\r" + '\033[1;35;40m' + "[+] Loading modules: " + str(i) + "%" + '\033[0;37;40m')
        sys.stdout.flush()
    print("\n")


loading()

os.system('cls' if os.name == 'nt' else 'clear')

print('\033[1;31;40m' + '© raven.ovh | What do you wanna ping ?' + '\033[0;37;40m')
print('\033[1;36;40m' + '1. Website' + '\033[0;37;40m')
print('\033[1;36;40m' + '2. IP' + '\033[0;37;40m')
choice = input('\033[1;31;40m' + 'Choice: ' + '\033[0;37;40m')

if choice == '1':
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[1;36;40m' + 'Example: google.com' + '\033[0;37;40m')
    website = input('\033[1;31;40m' + 'Website: ' + '\033[0;37;40m')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('ping ' + website + ' -t' if os.name == 'nt' else 'ping ' + website)
elif choice == '2':
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[1;36;40m' + 'Example: 1.1.1.1' + '\033[0;37;40m')
    ip = input('\033[1;31;40m' + 'IP: ' + '\033[0;37;40m')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('ping ' + ip + ' -t' if os.name == 'nt' else 'ping ' + ip)
else:
    print('Wrong choice!')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()
