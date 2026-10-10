age = int(input('enter your age:'))
on_day = str((input('on day:')))
num_tickets = int(input('enter the ticket count:'))

total = num_tickets * 190
discount_apply = total - 190
if age <= 18:
    if on_day == 'sunday':
        print('total amount(discount applied):', discount_apply)
    else:
        print('total amount:', total)
elif age > 18:
    if on_day == 'saturday':
        print('total amount(discount applied):', discount_apply)
    else:
        print('total amount:', total)
     

    