Item_Price = [10.00, 12.00, 15.00, 10.00,
              25.00, 45.00, 50.00, 25.00, 10.0, 12.00]
FoodType = int(input('Enter Food Type'))
price = 0.0
while (FoodType != 0):
    price += Item_Price[FoodType-1]
    FoodType = int(input('Enter Food Type'))
print('Total Price Is ', price)
