def bisect(num,list):
    left,right = 0,len(list)-1
    while left <= right:
        middle = (left+right)//2
        if list[middle] ==num:
            return middle
        elif list[middle] < num:
            left = middle + 1   
        elif list[middle] > num:
            right = middle -1
            