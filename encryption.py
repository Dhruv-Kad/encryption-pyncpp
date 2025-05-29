import random
import time
import os

def ascii_swap_encrypt(filename : str, password : str):

    tempout = open("tempout.txt", "w")
    with open(filename, "r") as filey:
        data = filey.read()
        for i in data:
            holder = int((ord(i)))
            holder += getnumfrompass(password) 
            nicer = str(holder)
            _ = tempout.write(nicer + "-")
    tempout.close()
    f = open(filename, "w")
    with open("tempout.txt", "r") as tempy:
        mata = tempy.read()
        builder = ""
        for i in mata:
            if(i == "-"):
                if builder != "":
                    intr = int(builder)
                    _ = f.write(chr(intr))
                    builder = ""
            else:
                if(i != " "):
                    builder += i;
    os.remove("tempout.txt")
    f.close()

def getnumfrompass(instir : str):
    teststr = instir
    makestr = 0 
    numper = 0
    for i in teststr:
        numper = ord(i)
        if numper%3 == 0:
            numper = 21
        elif numper%9 == 0:
            numper = 9
        makestr += (numper)
    return makestr

            

def ascii_swap_decrypt(filename : str, password : str):
    tempout = open("tempout.txt", "w")
    with open(filename, "r") as filey:
        data = filey.read()
        for i in data:
            holder = int((ord(i)))
            holder -= getnumfrompass(password) 
            nicer = str(holder)
            _ = tempout.write(nicer + "-")
    tempout.close()
    f = open(filename, "w")
    with open("tempout.txt", "r") as tempy:
        mata = tempy.read()
        builder = ""
        for i in mata:
            if(i == "-"):
                if builder != "":
                    intr = int(builder)
                    _ = f.write(chr(intr))
                    builder = ""
            else:
                if(i != " "):
                    builder += i;
    os.remove("tempout.txt")
    f.close()

def printfile(filename : str):
    with open(filename, "r") as temfile:
        for i in temfile:
            print(i)

def ascii_multi_encrypt(filename : str, password : str):
    times = random.randint(1,50)
    storetime = times
    while times > 0:
        ascii_swap_encrypt(filename, password)
        times -= 1
    print(storetime)

def isitsolved(filename : str):
    validChars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    with open(filename, "r") as temfile:
        for i in temfile:
            for j in i:
                if j in validChars:
                    return True
    return False


def ascii_multi_decrypt(filename : str, password : str):
    cont = False
    while cont == False:
        try:
            ascii_swap_decrypt(filename, password)
            cont = isitsolved(filename)
            printfile(filename)
            time.sleep(0.1)
        except:
            print("Failed")


def vigenre_encrypt(filename : str, password : str):
    strfromfile = ""
    taken = 0
    with open(filename, "r") as openfile:
        for i in openfile:
            strfromfile += i
    passwordlen = len(password)
    filelen = len(strfromfile)
    holder = password
    window = 0
    # Normalized lenths
    while passwordlen < filelen:
        passwordlen += 1
        if window >= len(password):
            window = 0
        holder += password[window]
        window += 1
    # Now move on to actually enrypting
    builder = "" 
    window = 0
    for i in strfromfile:
        taken = ord(i) + ord(holder[window])
        window += 1
        builder += chr(taken)

    print(builder) 
        





if __name__ == "__main__":
    newstr = input("Enter password: ")
    fname = input("Enter filename: ")
    printfile(fname)
    while True:
        print("1 to ascii encrypt, 2 to ascii decrypt, 3 to ascii multiencrypt, 4 to ascii multidecrypt, 5 to vigenre encrypt")
        choice = int(input("Enter choice: "))
        match choice:
            case 1:
                ascii_swap_encrypt(fname, newstr)
            case 2:
                ascii_swap_decrypt(fname, newstr)
            case 3:
                ascii_multi_encrypt(fname, newstr)
            case 4:
                ascii_multi_decrypt(fname, newstr)
            case 5:
                vigenre_encrypt(fname, newstr)
                
            case _:
                print("Value out of bounds")
                break
        printfile(fname)


