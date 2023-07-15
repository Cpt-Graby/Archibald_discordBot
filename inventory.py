class Item:
    def __init__(self, name: str, qty: int):
        self.name = name
        self.qty = qty
        self.qty_sold = 0

class Inventory:
    def __init__(self):
        self.inventory = {}
        pass

    def add_item(self, name: str, qty: int):
        if (name in self.inventory):
            print("Already exist")
            pass
        item = Item(name, qty)
        self.inventory[name] = item

    def achat_item(self, name):
        if (name not in self.inventory):
            print("Does exist")
            pass
        self.inventory[name].qty_sold += 1

    def __str__(self):
        new_bilan = ""
        for key in self.inventory.keys():
            new_bilan += f"{key} : {self.inventory[key].qty_sold}\n"
        return (new_bilan)

    def reset_inventory(self):
        print(f"{self}")
        for key in self.inventory.keys():
            self.inventory[key].qty_sold = 0
