def bubblesort(N):
    for j in range(0, len(N)-1):
        for i in range (0, len(N)-1):
            if N[i] > N[i+1] : 
               a = N[i]
               N[i] = N[i+1] 
               N[i+1] = a
    return N 


print(bubblesort([9,3,8,6,4,5]))  
           
