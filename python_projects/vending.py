
milk_price = 50
curd_price = 30

print("welcome to the vending machine")
item = input("Would you like to buy Milk, Curd or Both: ")
if item == "Milk":
    print("Thankyou for your selection")
    milk_qty = int(input("Kindely enter the quantity in liters: "))
    milk_cost = milk_qty * milk_price
    print("kindely enter Rupees" + str(milk_cost) + "below")
    cus_paid = int(input("kindely enter the amount to be paid: "))
    if cus_paid == milk_cost:
        print("Thankyou, please collect" + item)


    elif item == "Curd":
        print("Thankyou for your selected" + item + "for purchase")
        curd_qty = int(input("Kindely enter the quantity in liters: "))
        curd_cost = curd_qty * curd_price
        print("kindely enter Rupees" + str(curd_cost) + "below")
        cus_paid = int(input("kindely enter the amount to be paid: "))
        if cus_paid == curd_cost:
            print("Thankyou, please collect" + item)

        elif item == "Both":
            print("Thankyou for your selected" + item + "milk and curd")
            milk_qty = int(input("Kindely enter the quantity in liters: "))
            milk_cost = milk_qty * milk_price

            curd_qty = int(input("Kindely enter the quantity in liters: "))
            curd_cost = curd_qty * curd_price
            total_cost = curd_cost + milk_cost
            print("kindely enter Rupees" + str(total_cost) + "below")
            cus_paid = int(input("kindely enter the amount to be paid: "))
            if cus_paid == total_cost:
                print("Thankyou, please collect" + item)
            else:
                print("wrong entry please check")
    else:
        print("I dont know your entry please make currect entry")



# milk_price = 50
# curd_price = 30




# while True:
#     print("welcome to the vending machine")
#     item = input("Would you like to buy Milk, Curd or Both: ")
#     item = item.lower()
#     volume_qty = [0.5, 1, 5]
#     milk_price_list = [25, 50, 250]
#     curd_price_list = [15, 30, 150]

#     milk_cost = 0
#     curd_cost = 0
#     if item == 'milk':
#         cus_choice = input("would you have any choices on packet. Avalible packets are for 0.5L, 1L, 5L. please enter yes / No: ")
#         if cus_choice == "yes":
#             select = input((("Qty of 0.5L pack: "), ("Qty of 1L pack: "), ("Qty of 5L pack: ")))
#             for i in range(0,len(milk_price_list)):
#                 price = int(select[i] * int(milk_price_list[i]))
#                 milk_cost = milk_cost + milk_price

#             else:
#                 print("Thankyou for your selection")
#                 milk_qty = int(input("Kindely enter the quantity in liters: "))
#                 milk_cost = milk_qty * milk_price
#                 print("kindely enter Rupees " + str(milk_cost) + " below")
#                 cus_paid = int(input("kindely enter the amount to be paid: "))
#                 if cus_paid == milk_cost:
#                     print("Thankyou, please collect" + item)
#                 else:
#                     print('wrong entry, please check')

#     elif item == 'curd':
#         cus_choice = input("would you have any choices on packet. Avalible packets are for 0.5L, 1L, 5L. please enter yes / No")
#         if cus_choice == "yes":
#             select = input((("Qty of 0.5L pack: "), ("Qty of 1L pack: "), ("Qty of 5L pack: ")))
#             for i in range(0,len(curd_price_list)):
#                 price = int(select[i] * int(curd_price_list[i]))
#                 curd_cost = curd_cost + curd_price

#         else:
#             print("Thankyou for your selected" + item + "for purchase")
#             curd_qty = int(input("Kindely enter the quantity in liters: "))
#             curd_cost = curd_qty * curd_price
#             print("kindely enter Rupees" + str(curd_cost) + "below")
#             cus_paid = int(input("kindely enter the amount to be paid: "))
#             if cus_paid == curd_cost:
#                 print("Thankyou, please collect" + item) 

        
