f = open('Kontury_eksport_dz.txt')

bledy = []
i = 0
x = None

tablica = []
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

bledy_spacje = []
tablica_bez_spac = []
j = 0
for i in tablica:
    if len(i) != 1:
        bledy_spacje.append(i)
    else:
        tablica_bez_spac.append(i)

print(bledy_spacje)
print(tablica_bez_spac)