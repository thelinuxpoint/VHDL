def heapify(arr):

    def build(arr,N,i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2

        if l < N and arr[l] > arr[i]:
            largest = l

        if r < N and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            build(arr, N, largest)

    for i in range( len(arr)//2 - 1 ,-1, -1 ):
        build(arr,len(arr),i)
        

arr = [1,3,5,4,6,13,10,9,8,15,17]
heapify(arr)
print(arr)

