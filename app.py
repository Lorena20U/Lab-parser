import list
import stack
import numpy as np
from tabulate import tabulate

gram1 = ["x", "$"]
gram2 = ["n"]
gram3 = ["x", "+", "(", "x", ")"]
enc = ["/", "(", ")", "x", "n", "+", "$"]
s0 = ["s0", "g s1", "E", "g s2", "E", "E", "E"]
s1 = ["s1", "E", "s s3", "E", "E", "E", "ok"]
s2 = ["s2", "r2", "r2", "r2", "r2", "r2", "r2"]
s3 = ["s3", "E", "E", "E", "g s4", "E", "E"]
s4 = ["s4", "g s5", "E", "g s2", "s s4", "E", "E"]
s5 = ["s5", "E", "g s3", "E", "E", "s s6", "E"]
s6 = ["s6", "r3", "r3", "r3","r3","r3","r3"]

m_data = np.full((8,7), "     ")
for i in range(len(enc)):
    m_data[0,i] = enc[i]
    m_data[1,i] = s0[i]
    m_data[2,i] = s1[i]
    m_data[3,i] = s2[i]
    m_data[4,i] = s3[i]
    m_data[5,i] = s4[i]
    m_data[6,i] = s5[i]
    m_data[7,i] = s6[i]
    
print(tabulate(m_data, tablefmt="fancy_grid"))

a = list.List()
a.add(2)
a.add(3)
a.printList()
b = stack.Stack(1)
b.push(3)
b.push(4)
print(b)