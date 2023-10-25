#--------W O R K   O N  T H I S  P R O G R A M  L A T E R---------
def bubblesort(arr):
    
    n = len(arr)
    
    #For loop to traverse through all element in an array
    for i in range(n):
        for j in range(0,n-i-1):
            
            #Range of array is from 0 to n-i-1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
#Driver Code
arr = [2,1,10,23]
bubblesort(arr)

print("Sorted array is:")
for i  in range(len(arr)):
    print("%d" % arr[i])
