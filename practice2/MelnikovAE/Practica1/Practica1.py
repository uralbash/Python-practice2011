#!/usr/bin/env python
# coding: utf-8
import string

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

''' Считываем числа из файла '''
def getListNumbers(nameFile):
    f = open(nameFile, "r")
    list1 = list()
    for str in f.readlines():
        list1.extend(str.split())
    f.close()
    return list1
    
if __name__ == '__main__':
    import sys
    main(sys.argv[:])
