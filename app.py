from sre_parse import State
import list
import stack
import numpy as np
from tabulate import tabulate

gram1 = ["x", "$"]
gram2 = ["n"]
gram3 = ["x", "+", "(", "x", ")"]
enc = ["/", "x", "+", "n", "(", ")", "$"]
s0 = ["s0", "g s1", "E", "g s2", "E", "E", "E"]
s1 = ["s1", "E", "s s3", "E", "E", "E", "ok"]
s2 = ["s2", "r2", "r2", "r2", "r2", "r2", "r2"]
s3 = ["s3", "E", "E", "E", "g s4", "E", "E"]
s4 = ["s4", "g s5", "E", "g s2", "s s4", "E", "E"]
s5 = ["s5", "E", "s s3", "E", "E", "s s6", "E"]
s6 = ["s6", "r3", "r3", "r3","r3","r3","r3"]

m_gram = np.full((8,7), "     ")
for i in range(len(enc)):
    m_gram[0,i] = enc[i]
    m_gram[1,i] = s0[i]
    m_gram[2,i] = s1[i]
    m_gram[3,i] = s2[i]
    m_gram[4,i] = s3[i]
    m_gram[5,i] = s4[i]
    m_gram[6,i] = s5[i]
    m_gram[7,i] = s6[i]

# tabla de parseo
#print(tabulate(m_gram, tablefmt="fancy_grid"))

#stacks
estado = stack.Stack(1)
accion = stack.Stack(2)
cad = list.List()
#------------------------------

def shift(rut, val):
    

#-------------- lectura de datos

cl = 0
cc = 0
mcc = 0
with open("data.txt","r") as archivo:
    for linea in archivo:
        cl =  cl + 1
        cc = 0
        for caracter in linea:
            if ord(caracter) == 10:
                continue
            else:
                cc = cc + 1
        if mcc < cc:
            mcc = cc 

# matrices de datos
m_data = np.full((cl,mcc), " ")
m_resp = np.zeros((7,mcc))
i = 0
j = 0


# lectura desde un txt
with open("data.txt","r") as archivo:
    j = 0
    for linea in archivo:
        i = 0
        for caracter in linea:
            if ord(caracter) == 10:
                j = j + 1
            else:
                m_data[j,i] = caracter
                i = i + 1
print(m_data)
print(m_resp)

a = list.List()
a.add(2)
a.add(3)
a.printList()
b = stack.Stack(1)
b.push(3)
b.push(4)
print(b)