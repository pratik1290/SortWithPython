def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if(list[i] < list[j]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp;
    for k in range(len(list)):
        print(list[k])

list = [3,4,2,67,1,90,54,6,78,32]
bubbleSort(list)