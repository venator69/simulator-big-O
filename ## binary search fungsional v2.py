import random
import linereg
import mean
# Binary search function
def binary_search(target, start, end, count):
    mid = (start + end) // 2
    if mid == target:
        return (mid,count)
    elif mid > target:
        count += 1
        return binary_search(target, start, mid - 1, count)
    else :
        count += 1
        return binary_search(target, mid + 1, end, count)
# creating the simulator
def sim (sampling,x):
    arrsample = [[0,0] for i in range (sampling)]
    for i in range(sampling):
        arrsample[i] = binary_search (random.randint(0,x-1),0,x-1,1)
    return arrsample
#full simulator
def fullsim (point,sampling):
    arrline = [[0,0,0] for i in range (point)]
    arrmean = [[0,0,0] for i in range (point)]
    for i in range (1,point):
        arrmean[i][0] = i
        arrmean[i][1] = mean.meansum(sim(sampling,2**(i+1)))[0]
        arrmean[i][2] = mean.meansum(sim(sampling,2**(i+1)))[1]
    for i in range (1,point):
        arrline[i][0] = i
        arrline[i][1] = linereg.linreg(sim(sampling,2**(i+1)))[0]
        arrline[i][2] = linereg.linreg(sim(sampling,2**(i+1)))[1]
    print("hasil regresi linear")
    for i in range(point):
        for j in range(3):
            print(arrline[i][j], end="    ")  
        print()
    print()
    print("mean dari masing masing titik")
    for i in range(point):
        for j in range(3):
            print(arrmean[i][j], end="    ")  
        print()
    return(arrmean)
jumlah_titik = int(input("masukkan jumlah titik yang ingin disample: "))
jumlah_sampling = int(input("masukkan jumlah sample: "))
fullsim(jumlah_titik,jumlah_sampling)