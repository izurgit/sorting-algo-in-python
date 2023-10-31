def insertionSort(li):
    for idx in range(1, len(li)):
        val = li[idx]
        j = idx - 1       
        while(j >= 0 and val < li[j]):
            li[j + 1] = li[j]
            j = j - 1
        li[j + 1] = val