with open('file.txt', 'rb') as f:
    K1 = f.read()
    K = K1.split()
    print(K1)
    print(K)

    if len(K1):
        max_ = K[0].decode()
        min_ = K[0].decode()
        i_max = 0
        i_min = 0

        for i in range(len(K)):
            print(K[i], " | ", max_, " | ", min_)
            if max_ < K[i].decode():
                max_ = K[i].decode()
                i_max = i
            if min_ > K[i].decode():
                min_ = K[i].decode()
                i_min = i

        K[i_max], K[i_min] = K[i_min], K[i_max]


with open('file.txt', 'wb') as f:
    for i in range(len(K)):
        f.write(K[i])
        f.write(" ".encode('utf-8'))

