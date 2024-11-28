#Bubble Sort Algorithum:
import array as arr
a=arr.array("i",[1,23,4,5,33])
print(a)

""" 
i=length-1,i>=0;i--
    j=1;j<=i;j++
 """
def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
arr=[45,34,44,4,34,343,3,11]
bubblesort(arr)
print("Sorted array is :")
for i in arr:print(i)