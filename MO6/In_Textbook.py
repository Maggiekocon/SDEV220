# # 13.1 - 13.3

from datetime import date

file = open('today.txt', "a") 
file.write(str(date.today()))
file.close()

file = open('today.txt', "r") 
today_string=file.readlines()
file.close()

for i in today_string:
    print(i)


# 15.1
def print_time():
    import time
    from datetime import datetime
    from random import randint 
    time.sleep(randint(1,20))
    print(datetime.now())
   

import multiprocessing

if __name__ == "__main__":
    processors = 3
    processes = []

    for num in range(processors):
        p = multiprocessing.Process(target=print_time)
        p.start()
        processes.append(p)

    for p in processes:
            p.join()