#na svoi pc nado bydet skachat' biblioteku NUMPY

arr=[2,3,7,5,4]

#a
arr=[2,3,7,5,4]
print(arr)

#b
print(len(arr))

#c
print(arr[0])

#d
print(arr[1])

#e
print("last", arr[len(arr)-1])

#f
print("last but one value", arr[len(arr)-2])

#g
#x=(arr[0]+(arr[len(arr)]-1))
#print(x)

#h
print(arr[len(arr)//2])
#print(int(arr[len(arr)/2]))

#i
for i in range(0,3):
    print(arr[i], end=' ')

#j
print()
for i in range(0,len(arr)//2+1):
    print(arr[i], end=' ')
