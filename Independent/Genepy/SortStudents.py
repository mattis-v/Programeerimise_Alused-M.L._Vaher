my_class = [(25, "Shannon"), (50, "Alan"), (75, "Ada")]


def sort_by_mark(my_class):
    sortedC = sorted(my_class,key=lambda student: student[0],reverse=True)
    return(sortedC)

def sort_by_name(my_class):
    sortedC = sorted(my_class,key=lambda student: student[1])
    return(my_class)


print(sort_by_mark(my_class))
print(sort_by_name(my_class))
