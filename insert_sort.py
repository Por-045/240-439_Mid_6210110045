def insertion_sort(d):
    data = d.copy()
    for i in range(1, len(data)):
        if(data[i] > 1000):
            return 'more than 1000'
            
        elif(data[i] < -1000):
            return 'less than 1000'

        else:
            key = data[i]

            j = i-1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
    
    return data