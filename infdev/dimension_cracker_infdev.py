from itertools import product
from hashlib import sha256

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

#x = strings(10000)
#nr = 1
#for i in x:
    #i += "why_so_salty#LazyCrypto"
    #sha=sha256(i.encode()).hexdigest()
    #short=sha[0:8]
    #short2=sha[6:8]+sha[4:6]+sha[2:4]+sha[0:2]
    #dec=int(short2,16)
    #anded=dec & 2147483647
    #if nr==4732:
     #print(f"{nr} : {i} : {short} -> {short2}  : {dec} : {anded} ")
    #nr += 1



#print(" ".join(strings(100000)))
