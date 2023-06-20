def mean(list):
    sum=0
    for burdayim in list:
        sum += burdayim

    return round(sum/len(list), 2)


from ex1 import *

def normalization(lst):
    for burdayim in lst:
        lst[lst.index(burdayim)] = (burdayim - min(lst)) / (max(lst)- min(lst))

def tresholds(lst, low = 0.5, max = 1):

    for burdayim in lst:

        if max < burdayim:
            lst.pop(lst.index(burdayim))
        elif burdayim < low:
            lst.pop(lst.index(burdayim))


list = [1, 2, 3]

normalization(list)
print(list)

tresholds(list)
print(list)

print(mean(list))

def upgraded_mean(*e):
    sum=0
    for burdayim in e:
        sum += burdayim

    return round(sum/len(e), 2)
print(upgraded_mean(1,2,3))
def mean2(**e):
    sum=0
    for key, burdayim in e.items():
        sum += burdayim

    return round(sum/len(e), 2)

print(mean2(e1 = 1,e2 = 2, e3 = 3))
