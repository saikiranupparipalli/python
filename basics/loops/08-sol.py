number = 5
is_prime  = True
if number > 1:

    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            print(number, 'is not a prime number')
    print(number, 'is a prime number')     
# lecture sol: (incorrect)
 
#  attempt sol:
# num = int(input('enter a number: '))
# # square = num ** 2
# if num > 1 and num % num == 0 and num  % 1 == 0:
#   print(num, 'is a prime number')
# else:
#   # print(num, 'is not a prime number')
#   while True:
#     # num = '' 
#     print(num, 'is not a prime number')
#     print(int(input('enter a number: ')))
#     # break
    
    
    
    
     

 