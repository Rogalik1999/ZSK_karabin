f = open('C:\studia\semestr V\zinformatyzowane systemy katastralne\Kontury_eksport_dz.txt')

bledy = []

tab = []
for linie in f:
    e = linie.split()
    if 0 < len(e) < 7 and (len(e) !=1 or len(e[0])>2):  #poprawic troche warunek, zeby nie bylo 138
      #  print(e[0:2])
        tab.append(e)

for i in range(len(tab)):
    #print(tab[i][0])
    if ('-') in tab[i][0]:
        bledy.append(3)
    #    print(' ')
        #print((tab[i][0]).index('-'))
 #       print('ok')
    else:
   #     print('blad')
         print(tab[i])
     #   bledy.append(tab[i])