# attempt sol with time module modification
import time
password = input('enter the password:')
save_password = []
save_password.append(password)
timer = 1
print('password saved')

while True:
  check_password = str(input('want to verify the password(yes/no):'))
  if check_password == 'yes':
    verify_password = input('enter the password for verifying:')
    for i in save_password:
      if i == verify_password:
        print('correct password')
        exit()
      else:
        # timer *= 1
        print('come back after', timer, 'sec')
        time.sleep(timer)
        timer *= 2
  else:
    print('Thank you')
  # exit()
   
# attempt sol 1:
# password = input('enter the password:')
# save_password = []
# save_password.append(password)
# timer = 60
# print('password saved')
# while True:
#   check_password = str(input('want to verify the password(yes/no):'))
#   if check_password == 'yes':
#     verify_password = input('enter the password for verifying:')
#     for i in save_password:
#       if i == verify_password:
#         print('correct password')
#         break
#       else:
#         timer *= 1
#         print('come back after', timer, 'min')
#         exit()  
#   else:
#     print('Thank you')
#   # break
  
# attempt sol 2:
# password = input('enter the password:')
# save_password = []
# save_password.append(password)
# print('password saved')
# # split_password = password.split(' ')
# check_password = str(input('want to verify the password:'))
# if check_password == 'yes':
#   verify_password = input('enter the password for verifying:')
#   for i in save_password:
#     if i == verify_password:
#       print('correct password')
#     else:
#       print('come back after 1 hr')
# else:
#   print('Thank you')
  