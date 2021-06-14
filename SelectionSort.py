def selectionSort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]

    for k in range(len(list)):
        print(list[k], end=" ")

list = [3,4,2,67,1,90,54,6,78,32]
selectionSort(list)
