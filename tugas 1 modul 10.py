def binary_search(array, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if array[mid] == x:
            return mid
 
        elif array[mid] > x:
            return binary_search(array, low, mid - 1, x)
 
        else:
            return binary_search(array, mid + 1, high, x)
    else:
            return -1
 
array = [0, 2, 3, 4, 12, 20, ]
x = int(input("Masukan bilangan yang dicari : "))
array.sort()
print(array)
 
result = binary_search(array, 0, len(array)-1, x) +1
 
if result > 1:
    print("Bilangan di urutan ke", str(result))
else:
    print("Bilangan tidak ada di list")