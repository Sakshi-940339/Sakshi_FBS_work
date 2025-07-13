total= 0
for i in range(1,6):
    price=float(input("Enter a price of product ({i}):"))

    total += price 
    gst = total * 0.18
    total_bill = total + gst

    print(f"total ammount before GST : Rs{gst:.2f} ")
    print(f"GST (18%):Rs{gst:.2f} ")
    print(f"total bill after   GST : Rs{total_bill: .2f}")