# num = int(input('enter a number:'))
# count = 
# arr = []
# while count <= num:
#     multiply = num * count
#     count += 1
#     arr.append(multiply)
# print(multiply)

# attemp 2:
# n = 5
# count = n
# while count <= n:
#   total = n * (count -1 )
#   count -= 1
# print(total)

num = int(input('enter a number:'))
factorial = 1
while num > 0:
    factorial *= num
    num = num - 1
print(factorial)
# lecture sol

# 5*4*3*2*1