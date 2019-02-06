#!/usr/bin/env python
import os

def hex_conv(a):
    switcher1 = {
        '0': '1',
        '1': '2',
        '2': '3',
        '3': '4',
        '4': '5',
        '5': '6',
        '6': '7',
        '7': '8',
        '8': '9',
        '9': 'a',
        'a': 'b',
        'b': 'c',
        'c': 'd',
        'd': 'e',
        'e': 'f',
        'f': '0',
    }
    switcher2 = {
        '0': '1',
        '1': '2',
        '2': '3',
        '3': '4',
        '4': '5',
        '5': '6',
        '6': '7',
        '7': '8',
        '8': '9',
        '9': 'a',
        'a': 'b',
        'b': 'c',
        'c': 'd',
        'd': 'e',
        'e': 'f',
        'f': '0',
    }
    if a[1] == 'f':
        if a[0] == 'f':
            b = '0'
            c = '0'
        else:
            #print('abracadbara')
            b = switcher1.get(a[0], 'NULL')
            c = '0'
    else:
        c = switcher2.get(a[1], 'NULL')
        b = a[0]
    #print(a + '             ' + b+c)
    return b+c
    

junt = ""
with open('chaosclean', 'r') as f:
    for line in f:
        junt = junt + line.replace('\n', ' ')


talls = junt.split()
for i in range(0,256):
    out = open(str(i) + '.out', 'w')
    count = 0
    for a in talls:
        talls[count] = hex_conv(a)
        out.write(talls[count] + ' ')
        count = count + 1 
    out.close()
    os.system('echo \"/===========================================================/\"')
    #os.system('cat ' + str(i) + '.out | xxd -r -p - | hexdump -C')
    os.system('echo \"'+str(i)+'.out\"')
    os.system('cat ' + str(i) + '.out | xxd -r -p - | file -')