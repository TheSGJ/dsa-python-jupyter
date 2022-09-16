# Binary Search
pos = -1
list = [4,7,9,11,13,15]
n = 13

# Search Function
def search(list,n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l+u)//2
        if list[mid]==n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid]<n:
                l=mid
            else:
                u = mid

if search(list, n):
    print("Found at ",pos+1)
else:
    print("Not found")