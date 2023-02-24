import time
import threading
import matplotlib.pyplot as plt

def x(n):
    
    b = 0
    for i in range(n):
        b += i
    return b



def y(n):

    b = 0
    for i in range(n):
        b += i
    return b

if __name__ == '__main__':
    t = []
    for i in range(10):
        st = time.time()

        # t1 = threading.Thread(target = x , args = (10000000,))
        # t2 = threading.Thread(target = y , args = (100,))
        
        # t1.start()
        
        # t2.start()
    
        
        # t1.join()
        
        # t2.join()

        x(10000000)
        y(10000000)
    
        end = time.time()

        t.append(end-st)
    
    x_  = [i for i in range(10)]
    plt.plot(x_ , t)
    plt.show()