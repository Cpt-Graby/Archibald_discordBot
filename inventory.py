class Item:
    def __init__(self, name: str, qty: int):
        """
        Initializes an Item object.
        Args:
            name (str): The name of the item.
            qty (int): The initial quantity of the item.
        """
        self.name = name
        self.qty = qty
        self.qty_sold = 0
        self.alias = []


class Inventory:
    def __init__(self):
        """
        Initializes an Inventory object.
        """
        self.inventory = {}
        self.alias = []

    def add_item(self, nameup: str, qty: int):
        """
        Adds items to the inventory of an item.
        Args:
            nameup (str): The name of the item to add.
            qty (int): The quantity of the item to add.
        """
        name = nameup.lower()
        if qty < 0:
            pass
        if name in self.inventory:
            print("Already exists.\n")
            self.inventory[name].qty_sold += qty
            print(f"Qty: {qty} added.\n")
            pass
        item = Item(name, qty)
        self.inventory[name] = item

    def achat_item(self, nameup: str, qty: int = 1):
        """
        Increases the quantity sold of an item.
        Args:
            nameup (str): The name of the item.
            qty (int): The quantity to add to the quantity sold. Default is 1.
        """
        name = nameup.lower()
        if (qty < 0):
            pass
        if name not in self.inventory:
            print("Does not exist")
            pass
        self.inventory[name].qty_sold += qty

    def correct_error(self, nameup: str, qty: int = 1):
        """
        Corrects the quantity sold of an item.
        Args:
            nameup (str): The name of the item.
            qty (int): The quantity to subtract from the quantity sold. Default is 1.
        """
        name = nameup.lower()
        if (qty < 0):
            pass
        if name not in self.inventory:
            print("Does not exist")
            pass
        if self.inventory[name].qty_sold - qty >= 0:
            self.inventory[name].qty_sold -= qty

    def __str__(self):
        """
        Returns a string representation of the inventory.
        Returns:
            str: The inventory items and their quantities sold.
        """
        new_bilan = ""
        for key in self.inventory.keys():
            new_bilan += f"{key}: {self.inventory[key].qty_sold}\n"
        return new_bilan

    def reset_inventory(self):
        """
        Resets the quantities sold of all items in the inventory.
        """
        for key in self.inventory.keys():
            self.inventory[key].qty_sold = 0
    
    def item_exists(self, nameup: str) -> bool:
        """
        Vérifie si un élément existe dans l'inventaire.
        Args:
            nameup (str): Le nom de l'élément à vérifier.
        Returns:
            bool: True si l'élément existe dans l'inventaire, False sinon.
        """
        name = nameup.lower()
        return name in self.inventory
