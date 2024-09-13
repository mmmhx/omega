from utils import *
import sys

elem1 = element(300,[1, 2])
elem2 = element(200,[2, 3])
elem3 = element(300,[2, 3])
elem4 = element(200,[2, 4])
elem5 = element(300,[3, 4])

# u | f
no1 = node(0,False)
no2 = node(False,0)
no3 = node(False,0)
no4 = node(False,10)

elements = [elem1,elem2,elem3,elem4,elem5]
nodes = [no1,no2,no3,no4]
nnodes = n_nodes(nodes)[0]

Kg = BUILD_K(elements, n_nodes(nodes))
Fg = BUILD_F(nodes)
Ug = BUILD_U(nodes)
Beta = np.iinfo(np.int32).max 
Beta *= 50*Kg.diagonal().max()
i = 0
for node in nodes:
    if node.f == False:
        Kg[i] += Beta
        Fg[i] +=  Beta * node.u
    i += 1

print(Kg)
print("------")
print(Fg)
print("------")
print(Ug)

u = linalg.solve(Kg,Fg)
