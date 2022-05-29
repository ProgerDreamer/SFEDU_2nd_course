import numpy as np


# 3
def task_3():
    v1 = np.linspace(-1, 3, 100)
    v2 = np.linspace(2, 5, 100)
    print(v1[:10])
    print(v2[-10:])


# 8
def task_8():
    v1 = np.random.randint(-5, 10, 10)
    v2 = np.random.randint(-5, 10, 10)
    print('arrays: ', v1, v2, sep='\n')
    print('product, 1st way: ', v1 * v2, sep='\n')
    print('product, 2nd way: ', np.multiply(v1, v2), sep='\n')
    print('v1 - v2: ', v1 - v2, sep='\n')


# 9
def task_9():
    import numpy.linalg as linalg

    v1 = np.random.randint(-5, 10, 4)
    v2 = np.random.randint(-5, 10, 4)
    print('arrays: ', v1, v2, sep='\n')
    print('distance: ', linalg.norm(v1 - v2), sep='\n')


# 18
def task_18():
    import numpy.linalg as linalg

    n = 3
    M = np.random.randint(0, 6, (n, n))
    print(M)
    print(linalg.eig(M)[0])


# 22
def task_22():
    v = np.random.randint(0, 10, 10)
    print('array: ', v, sep='\n')
    print('sum: ', np.sum(v), sep='\n')
    print('mean: ', np.mean(v), sep='\n')
    print('minima: ', np.min(v), sep='\n')


# 27
def task_27():
    v = np.random.randint(0, 10, 10)
    print('array: ', v, sep='\n')
    print('Are all elements positive?: ', np.all(v > 0), sep='\n')


if __name__ == '__main__':
    task_27()

