# calculate the sum of even numbers up to given number n.
n = int(input('sum of even numbers are:'))
count = 0
arr = []
while(count <= n):
    if count % 2 == 0:
        arr.append(count)
    count +=1

print(sum(arr))

# lecture sol:
# x = 5
# count = 0
# for i in range(1, x+1):
#     if i % 2 == 0:
#         count +=1
# print(count)
        

# attempt-3
# n = 5
# count = 0
# arr = []
# if count <= n:
#     count += 1
#     arr.append(count)
#     for each_num in arr:
#         # if each_num % 2 == 0:
#             # print(sum(each_num))
#         print(each_num)
     
# attempt-2
# while(count <= n):
#     count += 1
#     arr.append(count)
#     for n in arr:
#         if n % 2 == 0:
#             print(n)

# attempt-1
# for num in n:
#     if count <= n:
#       result =  count = count + 1
#       print(result/2)