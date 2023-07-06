basket = [
    {
        'Product': 'Leather wallet',
        'Unit Price':1100,
        'GST %': 18,
        'Quantity': 1
    },
    {
        'Product': 'Umbrella',
        'Unit Price': 900,
        'GST %': 12,
        'Quantity': 4
    },
    {
        'Product': 'Cigarette',
        'Unit Price': 200,
        'GST %': 28,
        'Quantity': 3
    },
    {
        'Product': 'Honey',
        'Unit Price': 100,
        'GST %': 0,
        'Quantity': 2
    }
]

max_gst_product = None
max_gst_amount = 0

for product in basket:
    gst_amount = (product['Unit Price'] * product['GST %']) / 100 * product['Quantity']
    
    if gst_amount > max_gst_amount:
        max_gst_amount = gst_amount
        max_gst_product = product['Product']

print("Product with maximum GST amount:", max_gst_product)

total_amount = 0

for product in basket:
    unit_price = product['Unit Price']
    gst_amount = (unit_price * product['GST %']) / 100
    quantity = product['Quantity']
    
    if unit_price >= 500:
        discount = (5 * unit_price) / 100
        unit_price -= discount
    
    total_amount += (unit_price + gst_amount) * quantity

print("Total amount to be paid to the shopkeeper:", total_amount)


