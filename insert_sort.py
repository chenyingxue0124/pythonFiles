def insert_sort(lists):
    count = len(lists)
    for i in range(1,count):
        key = lists[i]
        j = i-1
        while j >= 0:
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
            j = j-1
    return lists
            
    
print(insert_sort([5,6,2,1,5]))