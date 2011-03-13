#!/usr/bin/env python
#-*- coding: utf-8 -*-
alphabet = u'абвгдежзийклмнопрстуфхцчшщъыьэюя'						
key = [0,0,0,0,0,0,0,0,0,0]										
	
def findKey(codingString, decodingString):					#фун-ия для нахождения ключа 								
		
	codingString = codingString.lower()
	decodingString = decodingString.lower()	
	seek = 0;
	count = 0
	while count < 10 and seek < len(decodingString):			#находим ключ пока не закончится раскодированная строка или не найдем полностью ключ

		if (alphabet.find(decodingString[seek]) != -1):				#ищем символ раскодированной строки
			decodingSym = alphabet.index(decodingString[seek])	
						
		elif (decodingString[seek] == codingString[seek]):		#если не нашли символ в алфавите проверяем равен ли он символу в закодированной строке 
			seek += 1
			continue

		else:					#если символ не равен значит неправильная раскодированная строка т.к. при кодировки мы не трогаем знаки препинания 
			print "ERROR: incorrect decoding string"
			exit(0)

		if (alphabet.find(codingString[seek]) != -1):  		  		#ищем символ раскодированной строки
			codingSym = alphabet.index(codingString[seek])
			key[count] = codingSym - decodingSym			#находим элемент ключа
			
			if key[count] < 0:					
				key[count] = (len(alphabet) - 1) + key[count]

			count += 1
			seek += 1
			
		else:								#если не нашли то значит неправильная раскодированная строка
			print "ERROR: incorrect decoding string"
			exit(0)
				
	if count < 10:							 	#если нашли не все элементы ключа значит не достаточно данных
		print "ERROR: insufficient data"
		exit(1)
	

def decoding(key, lines):
	
	newStr = ""
	count = 0
	keyCount = 0
	fileStr = ""	
	while count < len(lines):						#перебираем все строки файла
		newStr = ""
		for sym in lines[count].decode('utf-8'):
			if keyCount == 10:
				keyCount = 0 
			
			if (alphabet.find(sym.lower()) != -1):			#если не найден в алфавите то пропускаем символ
				newSym = alphabet.index(sym.lower()) - key[keyCount]
				if (newSym < 0):
					newSym += (len(alphabet) - 1)

				newSym = alphabet[newSym]

				if (sym.isupper()):				#если закодированный символ был в верхнем регистре то раскодированный делаем тоже в верхнем
					newSym = newSym.upper()

				newStr += newSym
				keyCount += 1
					
			else:
				newStr += sym
				
		fileStr += newStr
		count += 1
	return fileStr
		
			

def main(args):
	
	pathFile = args[1].decode('utf-8')
	decodingString = args[2].decode('utf-8')
	lines = open(pathFile,"r").readlines()
	findKey(lines[0].decode('utf-8'), decodingString)
	fileStr = decoding(key, lines)
	print "key: ",key	
	f = open( pathFile, 'w')
	f.write(fileStr.encode('utf-8'))
	f.close()
	print "DONE"
	
if __name__ == '__main__':
    import sys
    main(sys.argv[:])

















