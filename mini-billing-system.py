class Item:
    def __init__(self,name,price,qty):
        self.name=name
        self.price=price
        self.qty=qty

    def total(self):
        return self.price * self.qty

class Bill:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_bill(self):
        total = 0
        print("\nName\tQty\tPrice\tAmount")
        for i in self.items:
            amt = i.total()
            total += amt
            print(f"{i.name}\t{i.qty}\t{i.price}\t{amt}")
        discount = 0
        if total > 500:
            discount = total * 0.10
        print(f"Discount:\t\t\t{discount}")
        print(f"Total:\t\t\t\t{total-discount}")

def main():
    bill = Bill()
    while True:
        name = input("Item name (or 'done'): ")
        if name.lower() == 'done':
            break
        price = float(input("Price: "))
        qty = int(input("Quantity: "))
        bill.add_item(Item(name, price, qty))
    bill.display_bill()

main()
