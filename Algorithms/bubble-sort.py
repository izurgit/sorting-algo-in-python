def bubbleSort(li):
    n = len(li)
    for i in range(n):
        swap_flag = False
        for j in range(0, n-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                swap_flag = True
        if (swap_flag == False):
            break