import codecs
import os
def encrypt(filename):
    tempout = open("tempout.txt", "w")
    with open(filename, "r") as filey:
        data = filey.read()
        for i in data:
            holder = int((ord(i)))
            holder += 101
            nicer = str(holder)
            _ = tempout.write(nicer + "-")
    tempout.close()
    f = open(filename, "w")
    with open("tempout.txt", "r") as tempy:
        mata = tempy.read()
        builder = ""
        for i in mata:
            print(builder)
            if(i == "-"):
                intr = int(builder)
                print(chr(intr))
                _ = f.write(chr(intr))
                builder = ""
            else:
                if(i != " "):
                    builder += i;
    os.remove("tempout.txt")
    f.close()

            

def decrypt():
    pass

if __name__ == "__main__":
    print ("I am here")
    encrypt("/home/dhruv/Projects/Python/simplepypass/passwords.txt")

