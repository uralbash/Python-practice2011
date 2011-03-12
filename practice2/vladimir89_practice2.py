
# coding: utf-8


filename1 = "file1.txt"
filename2 = "file2.txt"

# dsfsdf


def main(args):
    ''' главная функция
        принимает 1 аргумент'''
    count_i = 0 #Счетчик
    count_k = 3 #Длинна слова, которое будет записано в фаил'''
    
    
    print "Start the programm"
    
    f1 = open (filename1, "r")
    f2 = open (filename2, "w")

    for line in f1:
        print "Current line", line
        slovo = line.split()
        print "Current slovo: ", slovo
        a = len(slovo)
        print "Current count slov", a
        for count_i in range(a):
            
            if slovo[count_i].isalpha() and len(slovo[count_i]) == count_k:
                print slovo[count_i]
                f2.write(slovo[count_i]+'\n')

            count_i = count_i + 1

    f2.close()
    

         
    

if __name__ == '__main__':
    import sys
    main(sys.argv[:])

