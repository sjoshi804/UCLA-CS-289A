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
    matrix_f = (matrix(m_f))
    kernel_f = (kernel(matrix_f)).matrix()
    print(kernel_f)
    hypothesis = True
    row_num = 0
    for row in kernel_f:
        pos = 0
        sum = 0
        abs_sum = 0
        digits = 0
        for element in row:
            sum += ((pos*element))
            abs_sum += abs((pos * element))
            pos += 1
            if element != 0:
                digits += 1
        if sum != 0:
            hypothesis = False
            break
        print(str(row_num) + ": " + str(digits) + " " + str(abs_sum))
        row_num += 1
    print(hypothesis)
    print("-------------------------------------------------------------------------------------------------")