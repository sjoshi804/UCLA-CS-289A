from numpy import linalg
from numpy import matrix
from numpy import array_equal
from numpy import ix_
matrices = []
for num_of_bits in range(4, 6):
    m_f = []
    for x in range(0, 2**num_of_bits):
        l1 = []
        for y in range(0, 2**num_of_bits):
            z = x * y
            binary = ("{0:b}".format(z))[::-1]
            if (len(binary) < num_of_bits):
                l1.append(0)
            else:
                l1.append(int(binary[num_of_bits - 1]))
        m_f.append(l1)
    matrices.append(m_f)
    #print(matrix(m_f))
    print(2**num_of_bits)
    print (linalg.matrix_rank(matrix(m_f)))
matrix1 = matrix(matrices[0])
matrix2 = matrix(matrices[1])
matrix2 = matrix2[ix_([0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])]
matrix3 = matrix(matrices[1])
matrix3 = matrix3[ix_([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30])]
print(array_equal(matrix1, matrix2))
print(array_equal(matrix1, matrix3))
print(matrix1)

