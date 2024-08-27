from utils import *

elem1 = element(300,[1, 2])
elem2 = element(200,[2, 3])
elem3 = element(300,[2, 3])
elem4 = element(200,[2, 4])
elem5 = element(300,[3, 4])

no1 = node(0, False)
no2 = node(False, 0)
no3 = node(False, 0)
no4 = node(False, 10)

Ke = linalg.block_diag(elem1.K, elem2.K, elem3.K, elem4.K, elem5.K)


