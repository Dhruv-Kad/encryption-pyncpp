import random
import time
import os

def asciiswapencrypt(filename : str):

    tempout = open("tempout.txt", "w")
    with open(filename, "r") as filey:
        data = filey.read()
        for i in data:
            holder = int((ord(i)))
            holder += getnumfrompass() 
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

def getnumfrompass():
    teststr = "YesIdousevim"
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

            

def asciiswapdecrypt(filename : str):
    tempout = open("tempout.txt", "w")
    with open(filename, "r") as filey:
        data = filey.read()
        for i in data:
            holder = int((ord(i)))
            holder -= getnumfrompass() 
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

def readfile(filename : str):
    with open(filename, "r") as temfile:
        for i in temfile:
            print(i)

def asciimultiencrypt(filename : str):
    times = random.randint(1,50)
    storetime = times
    while times > 0:
        asciiswapencrypt(filename)
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


def asciimultidecrypt(filename : str):
    cont = False
    while cont == False:
        try:
            asciiswapdecrypt(filename)
            cont = isitsolved(filename)
            readfile(filename)
            time.sleep(0.1)
        except:
            print("Failed")

if __name__ == "__main__":
    fname = input("Enter filename: ")
    readfile(fname)
    while True:
        print("1 to ascii encrypt, 2 to ascii decrypt, 3 to ascii multiencrypt, 4 to ascii multidecrypt")
        choice = int(input("Enter choice: "))
        match choice:
            case 1:
                asciiswapencrypt(fname)
            case 2:
                asciiswapdecrypt(fname)
            case 3:
                asciimultiencrypt(fname)
            case 4:
                asciimultidecrypt(fname)
            case _:
                print("Value out of bounds")
                break
        readfile(fname)


