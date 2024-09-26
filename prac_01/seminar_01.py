# Tax problem
gst = False
item_price = float(input("Item price: "))
gst_input = input("Does it have GST (Y/N)? ").upper()
if gst_input == "Y":
    gst = True
elif gst_input == "N":
    pass
else:
    print("Error")
    gst_input = input("Does it have GST (Y/N)? ").upper()
if gst:
    item_price = item_price * 1.1
print(f"The final price is ${item_price:.2f}")
