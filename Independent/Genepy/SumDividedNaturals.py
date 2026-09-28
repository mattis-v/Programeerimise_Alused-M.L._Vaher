def sum_divided_naturals(start, stop):
    summ = 0
    for i in range(start, stop):
        if (i % 3) == 0:
            summ = summ + i
            print ("i/3 with ", i)
        elif (i % 5) == 0:
            summ = summ + i
            print ("i/5 with ", i)
    print(summ)
    
sum_divided_naturals(0,1000)