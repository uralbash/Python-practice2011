FileText = open("Text.txt")
FileCount = open("Count.txt", "w")
Str = FileText.read()
#print Str
abc = "אבגדהו¸זחטיךכלםמןנסעףפץצקרשתûü‎‏ÿ"
for letter in abc:
    #print letter
    Count = Str.count(letter)
    #print letter + "-" + str(Count) + "\n"
    if Count != 0:
        FileCount.write(letter + "-" + str(Count) + "\n")
        #print letter + "-" + str(Count)
FileText.close()
FileCount.close()

        
        
