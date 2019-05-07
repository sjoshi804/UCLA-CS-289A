from sage.all import *
while True:
    num_of_bits = int(raw_input("How many bits?\n"))
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
    field_num = 2**(num_of_bits - 1)
    print(2*field_num)
    print(matrix(m_f))
    m = matrix(GF(field_num), m_f)
    t = matrix(GF(2), m_f)
    print(t.rank())
    print (m.rank())