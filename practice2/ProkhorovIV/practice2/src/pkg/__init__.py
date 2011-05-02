# coding: utf-8

filename = "text_src.txt"
filename2 = "text_dst.txt"
charsList = list()

def main(args):
    f1 = open(filename, "r")
    f2 = open(filename2, "w")
    
    for char in f1.read():
        if checkRepeat(char) == False:
            charsList.append(char) 
            f2.write(char) 
            
def checkRepeat(char):
    found = False
    for c in charsList:
        if c == char:
            found = True
    return found
    
if __name__ == '__main__':
    import sys
    main(sys.argv[:])
