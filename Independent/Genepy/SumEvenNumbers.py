def sum_even_numbers(start, stop):
    summ = 0
    for i in range(start, stop):
        if (i % 2) == 0:
            summ = summ + i
    print(summ)
    
print_even_numbers(0,100)