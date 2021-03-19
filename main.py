pennies = int(input('Enter the number of pennies:'))
quarters = int(input('Enter the number of quarters:'))
nickels = int(input('Enter the number of nickels:'))
dimes = int(input('Enter the number of dimes:'))

pennies_total = pennies * 0.01
nickels_total = nickels * 0.05
quarters_total = quarters *.25
dimes_total = dimes*.1

total_amount = pennies_total+nickels_total+quarters_total+dimes_total

print('Total amount entered: $',format(total_amount, '.2f'),sep='')

if total_amount == 1:
  print('You have exactly one dollar.')
elif total_amount > 1:
  print('The amount entered is more than one dollar.')
else:
  print('The amount entered is less than one dollar.')