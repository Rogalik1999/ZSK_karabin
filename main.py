f = open('Kontury_eksport_dz.txt')

bledy = []
i =0
x = None

tablica =[]
for line in f:
    fields = line.split()
    if i ==0:
        if len(fields)==0:
            continue
        tablica.append(fields)
        i = i +1
    elif i ==1:
        i = i+1
    elif i ==2:
        i = i+1
        x = int(fields[0])
    else:
        if x == 0:
            i = 0
        else:
            x = x -1

print(tablica)



#for i in range(len(tab)):
    #print(tab[i][0])
    #if ('-') in tab[i][0]:
       # bledy.append(3)
    #    print(' ')
        #print((tab[i][0]).index('-'))
 #       print('ok')
   # else:
   #     print('blad')
         #print(tab[i])
     #   bledy.append(tab[i])