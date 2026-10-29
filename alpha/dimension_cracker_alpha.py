#!/usr/bin/python3
from math import ceil
from itertools import product
from hashlib import sha256

MAX_VALUE=2147483648

def get_id(text):
    text += ":why_so_salty#LazyCrypto"
    sha = sha256(text.encode()).hexdigest()
    short = sha[6:8] + sha[4:6] + sha[2:4] + sha[0:2]
    dec = int(short, 16)
    anded = dec & 2147483647
    return anded

def strings(outputs):
    length = 1
    if outputs == -1:
        while True:
            for letters in product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", repeat=length):
                yield "".join(letters)
            length += 1
    move_on = True
    while move_on:
        for letters in product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", repeat=length):
            yield "".join(letters)
            outputs -= 1
            if outputs == 0:
                move_on = False
                break
        length += 1

def storeid(datafile, keyword):
    id = get_id(keyword)
    pos=id*6
    datafile.seek(pos)
    datafile.write(keyword)

def readkw(datafile,id):
    pos=id*6
    datafile.seek(pos)
    data=datafile.read(6).strip('\0')
    return data

def storenewid(datafile, keyword):
    id = get_id(keyword)
    existing=readkw(datafile, id)
    if existing == '':
        storeid(datafile, keyword)
        return 1
    else:
        return 0

if __name__ == "__main__":
    print("Dimension Cracker Alpha\n")
    try:
        f = open("dimdata")
    except FileNotFoundError:
        while True:
            ansr = input("No data file found. Create one? y/n/h: ")
            if ansr == "y":
                with open("dimdata", "w+") as datafile:
                    counter = 0
                    percentcounter = 0
                    percent = 0
                    print("Writing file...")
                    print("0%", end="",flush=True)
                    for i in strings(-1):
                        res = storenewid(datafile, i)
                        counter += res
                        percentcounter += res
                        if percentcounter == ceil(MAX_VALUE/100):
                            percent += 1
                            print(f"\r{percent}%", end="",flush=True)
                            percentcounter = 0
                        if counter == MAX_VALUE:
                            quit()
                quit()
            elif ansr == "n":
                quit()
            elif ansr == "h":
                print("Dimension Cracker needs to create an ~12GB file of binary data in order to be able to immediately output any dimension keyword from the ID. Be careful, it might be hard for your computer!(it wont blow up though, dot be worried!)")
    while True:
        with open("dimdata", "r") as dimdata:
            command = input("Enter command (help for a list of commands): ")
            if command == "exit" or command == "quit":
                quit()
            elif command == "help":
                print("\n\t\tHelp Menu\n\nCommands:\nexit or quit: Close the program\nid: enter a dimension ID after ':' to get the simplest keyword\nkeyword: gives you the simplest keyword from the keyword entered, useful for making texts shorter")
            elif command[0:2] == "id":
                id= int(command[3:])
                data = readkw(dimdata,id)
                print(f"Keyword for {command[3:]} is {data}")
            elif command[0:7] == "keyword":
                id = get_id(command[8:])
                data = readkw(dimdata, id)
                print(f"A simpler keyword for {command[8:]} is {data}")
