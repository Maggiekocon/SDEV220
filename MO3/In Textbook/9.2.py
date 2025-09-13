def get_odds():
    list=[]
    '''
    Gives you the odd numbers from 1 to 10
    '''
    for i in range(10):
        if (i%2) != 0:
            list.append(i)
    return list
x=0
for i in get_odds():
    if x==2:
        print(i)
    x+=1


