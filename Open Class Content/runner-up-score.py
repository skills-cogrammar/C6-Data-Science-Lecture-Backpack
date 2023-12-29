n=5
arr=[2, 3, 6, 6, 5]
arr.sort(reverse=True)
print(arr)
for i in range(len(arr)-1):
    if arr[i+1] < arr[i]:
        print(f"{arr[i+1]} is the runner up score." )
        break