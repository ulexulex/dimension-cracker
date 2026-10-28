#!/usr/bin/python3
from itertools import product
from hashlib import sha256
from time import time

def get_id(text):
    text += ":why_so_salty#LazyCrypto"
    sha = sha256(text.encode()).hexdigest()
    short = sha[6:8] + sha[4:6] + sha[2:4] + sha[0:2]
    dec = int(short, 16)
    anded = dec & 2147483647
    return anded

def strings(outputs):
    length = 1
    move_on = True
    while move_on:
        for letters in product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", repeat=length):
            yield "".join(letters)
            outputs -= 1
            if outputs == 0:
                move_on = False
                break
        length += 1

start_time = time()

if __name__ == "__main__":
    print("Dimension Cracker Alpha Test\n")
    try:
        f = open("data.ulexdat")
    except FileNotFoundError:
        ansr = "y"
        if ansr == "y":
            while True:
                wanted = input("Wanted dimension's ID: ")
                start_time = time()
                for i in strings(2147483648):
                    #print(f"{nr} : {i} : {get_id(i)}")
                    if get_id(i) == int(wanted):
                        print(f"ITS {i}")
                        print(time() - start_time)
                        break
        elif ansr == "n":
            pass
