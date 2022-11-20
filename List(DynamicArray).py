expenses = [['January', 'February', 'March', 'April', 'May'],
           [2200, 2350, 2600, 2130, 2190]]
print('\nOriginal List:\t', expenses)
print(f'\nThe Amount Of February Is Rs.{expenses[1][1]- expenses[1][0]} More Than Amount Of January. \tAnd Total Expenses Of {expenses[0][0]}, {expenses[0][1]} & {expenses[0][2]} Is Rs.{expenses[1][0]+expenses[1][1]+expenses[1][2]}.')

amount = eval(input("\nEnter The Amount To Be Search.:\t"))
if amount in expenses[1][:]:
    print(f"Yes Amount Rs.{amount} Exist In The List.")
else:
    print(f"No, Amount Rs.{amount} Doesn't Exist In The List.")

expenses[0].append('June')
expenses[1].append(1980)
print("\nFirst Updated List After Addition of June's Expenses:\t", expenses)

expenses[1][3] =  expenses[1][3] - 200
print("\nSecond Updation List After Updation of April's Expenses By Deduction Of Rs.200:\t", expenses)

heros=['Spider Man','Thor','Hulk','IronMan','Captain America']
print("\nOriginal Heros List:\t", heros, "\tLength Of list:\t", len(heros))

heros.append('Black Panther')
print("\nFirst Updated List After Black Panther Addition:\t", heros, "\tLength Of list:\t", len(heros))

heros.remove('Black Panther')
heros.insert(3,'Black Panther')
print(f"\nSecond Updated List After Black Panther Shift To {heros[3]} Position:\t", heros)

heros[1:3] = ['Doctor Strange']
print("\nThird Updated List After Replacing Thor & Hulk From Doctor Strange:\t", heros)

print("\nList Before Sorting:\t", heros)
heros.sort()
print("Fourth Updated List After Sorting:\t", heros)