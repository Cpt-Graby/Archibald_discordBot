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
        """
        add_item permet de rajouter des elements dans l'inventaire de l'item.
        """
        if (qty < 0):
            pass
        if (name in self.inventory):
            print("Already exist.\n")
            self.inventory[name].qty_sold += qty
            print(f"Qty:{qty} added.\n")
            pass
        item = Item(name, qty)
        self.inventory[name] = item

    def achat_item(self, name: str, qty: int = 1):
        if (qty < 0):
            pass
        if (name not in self.inventory):
            print("Does not exist")
            pass
        self.inventory[name].qty_sold += qty

    def correct_error(self, name: str, qty: int = 1):
        if (qty < 0):
            pass
        if (name not in self.inventory):
            print("Does not exist")
            pass
        if (self.inventory[name].qty_sold - qty >= 0):
            self.inventory[name].qty_sold -= qty

    def __str__(self):
        new_bilan = ""
        for key in self.inventory.keys():
            new_bilan += f"{key} : {self.inventory[key].qty_sold}\n"
        return (new_bilan)

    def reset_inventory(self):
        print(f"{self}")
        for key in self.inventory.keys():
            self.inventory[key].qty_sold = 0
