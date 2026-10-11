# sum of all numbers:
# def sum_all(n, total = 0):
#   for i in n:
#     total += i
#   return total
# print(sum_all([1, 2, 3, 4]))

def sum_all(n ):
  for i in range(0, n):
    yield i
for i in sum_all(10):
  print(i)


print('\n')
def even_generator(limit):
    for i in range(2, limit +1, 2):
        yield i
for i in even_generator(10):
    print(i)
# yield: is used to return a value from a function without ending the function permanently. It pauses the function and remembers where it stopped, so it can continue from that point later.