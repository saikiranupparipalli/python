n = int(input('multiplication table: '))
count = 1
for i in range(count, 11):
    if i == 5:
        continue
    table = n * i
    print(n  ,'*' , i,  '=', table)
    count +=1
   
     
     
# while count <= 10:
#     table = n * count
#     if  count == 5:
#          continue
#          print(n  ,'*' , count,  '=', table)
    
#     count +=1
 