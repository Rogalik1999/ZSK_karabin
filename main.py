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

#print(bledy_spacje)
#print(tablica_bez_spac)

bledy_z_sla = []
tablica_bez_sla = []
for i in tablica_bez_spac:
    split = i[0].split('/')
    if len(split) != 2:
        bledy_z_sla.append(split)
    else:
        tablica_bez_sla.append(split)

#print(bledy_z_sla)
#print(tablica_bez_sla)

bledy_z_mysli = []
tablica_bez_mysli = []
for i in tablica_bez_sla:
    split = i[0].split('-')
    if len(split) != 2:
        bledy_z_mysli.append(i)
    else:
        tablica_bez_mysli.append(i)

#print(bledy_z_mysli)
#print(tablica_bez_mysli)


#tylko OFU
OFU_only = {}
OFU_only['B'] = 'only'
OFU_only['Ba'] = 'only'
OFU_only['Bi'] = 'only'
OFU_only['Bp'] = 'only'
OFU_only['Bz'] = 'only'
OFU_only['K'] = 'only'
OFU_only['dr'] = 'only'
OFU_only['Tk'] = 'only'
OFU_only['Ti'] = 'only'
OFU_only['Tp'] = 'only'
OFU_only['E-Wp'] = 'only'
OFU_only['E-Ws'] = 'only'
OFU_only['E-N'] = 'only'
OFU_only['N'] = 'only'
OFU_only['Wm'] = 'only'
OFU_only['Wp'] = 'only'
OFU_only['Ws'] = 'only'
OFU_only['Tr'] = 'only'

bledy_z_ofu_only = []
tablica_bez_ofu_onl = []

for i in tablica_bez_mysli:
    rod = i[1]
    if rod[0] in OFU_only:
        if len(rod) > 1 :
            bledy_z_ofu_only.append(i)
        else:
            tablica_bez_ofu_onl.append(i)
    elif rod[:1] in OFU_only:
        if len(rod) > 2:
            bledy_z_ofu_only.append(i)
        else:
            tablica_bez_ofu_onl.append(i)
    elif rod[:2] in OFU_only:
        if len(rod) > 3:
            bledy_z_ofu_only.append(i)
        else:
            tablica_bez_ofu_onl.append(i)
    elif rod[:3] in OFU_only:
        if len(rod) > 4:
            bledy_z_ofu_only.append(i)
        else:
            tablica_bez_ofu_onl.append(i)
    else:
        tablica_bez_ofu_onl.append(i)

print(bledy_z_ofu_only)
print(tablica_bez_ofu_onl)
