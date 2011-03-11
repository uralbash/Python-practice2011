#!/usr/bin/env python
# coding: cp1251

def main(args):
    ''' Задаем файлы для работы '''
    textFile1 = "textFile1"
    textFile2 = "textFile2"
    outputFile = "outputFile"

    ''' Считываем числа из файлов в списки '''
    list1 = getListNumbers(textFile1)
    list2 = getListNumbers(textFile2)

    ''' Создаем таблицу и пишем ее в файл '''
    createTable(outputFile, list1, list2)
    
pass

''' Возвращает список чисел из файла '''
def getListNumbers(nameFile):
    f = open(nameFile, "r")
    list1 = list()
    number = ""
    doublespace = 1 #смотрим чтоб не было двойных пробелов 
    for char in f.read():
        if ((char == ' ') and (doublespace == -1)):
            list1.append(number)
            number = ""
            doublespace = 1
        else:
            if (char != ' '):
                number += char
                doublespace = -1
    f.close()
    return list1
pass

''' Создает таблицу с числами из двух списков '''
def createTable(nameFile, list1, list2):   
    out = open(nameFile, "w")   
     
    for i in range(len(list1)):
        line = "|"
        
        for j in range(30 - len(list1[i])):
            line += " "
        line += list1[i]
        
        for j in range(30 - len(list2[i])):
            line += " "
        line += list2[i]
        
        line += "|\n"
        out.write(line)
 
    out.close()
pass

if __name__ == '__main__':
    import sys
    main(sys.argv[:])
