def sum(list):
    sum=0
    for i in range(len(list)):
        sum +=list[i]
    return sum


# 1 2 3 4
def rec_sum(list):
    if not list:
        return 0
    remaining=rec_sum(list[1:])
    return list[0] +remaining