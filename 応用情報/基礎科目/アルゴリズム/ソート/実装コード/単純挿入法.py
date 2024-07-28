def insert_sort(list):
    num = len(list)
    for i in range(num):
       temp =  min(list[i:])
       print(temp)
       list_number = serach(temp,list)
       soted_list = list_swap(i,list_number,list)
    return soted_list
       
       
       

#元の値の要素番号を探す関数(組み込み関数のindexでいいけど。。。)        
def serach(num,list):
    n = len(list)
    
    for i in range(n):
        if list[i] == num:
            list_number = i
            break
        
    return list_number
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

def list_swap(a,b,list):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp
    return list 
test_list = [2,1,4,3]
print(insert_sort(test_list))