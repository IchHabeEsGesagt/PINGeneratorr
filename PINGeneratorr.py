import string
import secrets
import time


# Programmed by me

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{bcolors.OKBLUE}{bcolors.BOLD}Visit github.com/IchHabeEsGesagt/PINGenerator for Help{bcolors.ENDC}")

print(f"{bcolors.HEADER}**********PIN Genrator 1.3**********{bcolors.ENDC}")


def pingen(lengh: int):
    combination = string.digits

    new_pin = ""
    combinationlengh = len(combination)
    for _ in range(lengh):
        new_pin += combination[secrets.randbelow(combinationlengh)]

    return new_pin


print(" ")
print("Options:")
print(" ")
print("1. Length = 4")
print("2. Length = 8")
print("3. Custom Length")
print(" ")

while True:

    option = input("Choose Option (1, 2, 3): ")

    if option.isdigit() and int(option) in range(4):
        if option == "1":
            print(f"{bcolors.OKGREEN}Your PIN is: {pingen(lengh=4)}{bcolors.ENDC}")

        if option == "2":
            print(f"{bcolors.OKGREEN}Your PIN is: {pingen(lengh=8)}{bcolors.ENDC}")

        if option == "3":
            lengh = input("Put your custom length here:  ")
            print(f"{bcolors.OKGREEN}Your PIN is: {pingen(lengh=int(lengh))}{bcolors.ENDC}")
            if lengh == "0816":
                print(f"{bcolors.FAIL}Hacker Mode activated{bcolors.ENDC}")
                time.sleep(5)
                cont = input("Stay in Hackermode? (y/n) ")
                if cont == "y":
                    print(f"{bcolors.BOLD}LOADING 10%{bcolors.ENDC}")
                    time.sleep(0.5)
                    print(f"{bcolors.BOLD}LOADING 30%{bcolors.ENDC}")
                    time.sleep(0.5)
                    print(f"{bcolors.BOLD}LOADING 52%{bcolors.ENDC}")
                    time.sleep(0.5)
                    print(f"{bcolors.BOLD}LOADING 71%{bcolors.ENDC}")
                    time.sleep(0.5)
                    print(f"{bcolors.BOLD}LOADING 98%{bcolors.ENDC}")
                    time.sleep(0.5)
                    print(f"{bcolors.BOLD}LOADING 100%{bcolors.ENDC}")
                    time.sleep(1.2)
                    print(f"{bcolors.BOLD}LOADING COMPLETED{bcolors.ENDC}")
                    time.sleep(1.2)
                    print(f"{bcolors.BOLD}INSTALLING 0%{bcolors.ENDC}")
                    time.sleep(0.5)
                    print(f"{bcolors.BOLD}INSTALLING 22%{bcolors.ENDC}")
                    time.sleep(0.5)
                    print(f"{bcolors.BOLD}INSTALLING 59%{bcolors.ENDC}")
                    time.sleep(0.5)
                    print(f"{bcolors.BOLD}INSTALLING 97%{bcolors.ENDC}")
                    time.sleep(0.5)
                    print(f"{bcolors.BOLD}INSTALLING 100%{bcolors.ENDC}")
                    time.sleep(1.2)
                    print(f"{bcolors.BOLD}INSTALLING COMPLETE{bcolors.ENDC}")
                    time.sleep(3)
                    print(f"{bcolors.BOLD}{bcolors.FAIL}YOU HAVE BEEN TERMINATED{bcolors.ENDC}")
                if cont == "n":
                    print(f"{bcolors.BOLD}Stopping...{bcolors.ENDC}")
                    time.sleep(2)
                    print(f"{bcolors.BOLD}Stopped!{bcolors.ENDC}")
                    time.sleep(1.5)






    else:
        print(f"{bcolors.FAIL}Invalid Input use 1, 2 or 3{bcolors.ENDC}")

    nochmal = input("Generate new PIN? (y/n) ")

    list = ["y", "n"]
    if nochmal in list and nochmal.isascii():
        if nochmal == "n":
            print(f"{bcolors.BOLD}Stopping...{bcolors.ENDC}")
            time.sleep(1)
            print(f"{bcolors.BOLD}Stopped!{bcolors.ENDC}")
            time.sleep(1)
            break


    else:
        print(f"{bcolors.FAIL}Invalid Input use y or n{bcolors.ENDC}")
        list = ["y", "n"]
        nochmal = input("Generate new PIN? (y/n) ")
        if nochmal in list and nochmal.isascii():
            if nochmal == "n":
                print(f"{bcolors.BOLD}Stopping...{bcolors.ENDC}")
                time.sleep(2)
                print(f"{bcolors.BOLD}Stopped!{bcolors.ENDC}")
                time.sleep(2)
                break





