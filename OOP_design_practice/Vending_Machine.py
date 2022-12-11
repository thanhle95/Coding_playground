"""
Design Vending machine
"""

from enum import Enum
from collections import Counter
import random


class Coin(Enum):
    PENNIE = 1
    NICKEL = 5
    DIM = 10
    QUARTER = 25


class Item(Enum):
    COKE = 25
    PEPSI = 35
    WATER = 10


class Inventory:
    def __init__(self):
        self.inventory: dict[str, int] = dict()

    def get_quantity(self, item):
        value = self.inventory.get(item)
        return value if value is not None else 0

    def add(self, item, quantity = 1):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def deduct(self, item, quantity = 1):
        if (item in self.inventory) and (self.get_quantity(item) > 0):
            self.inventory[item] -= quantity
        else:
            print(f"{item.name} out of quantity, Please contact service for help")

    def has_item(self, item):
        return self.get_quantity(item) > 0

    def clear(self):
        self.inventory = dict()

    def display(self):
        print(f"{self.__class__} had {self.inventory.items()}")


class VendingMachine:
    item_inventory: Inventory = Inventory()
    coin_inventory: Inventory = Inventory()
    current_items: list[Item] = []
    current_balance: int = 0
    cart_price: int = 0
    total_sale: int = 0

    def __init__(self):
        for c in Coin:
            self.coin_inventory.add(c, 100)
        for i in Item:
            self.item_inventory.add(i, 20)

    def select_item(self, item: Item):
        total_price = 0
        if self.item_inventory.has_item(item):
            self.current_items.append(item)
            self.cart_price = self.cart_price + item.value
            print(f"Cart: {self.current_items}")
            print(f"Total price: {self.cart_price}")
            print(f"Balance: {self.current_balance}")
        else:
            print("ITEM SOLD OUT, GET THE FUCK OUT!")

    def check_out(self):
        if self.cart_price > self.current_balance:
            print(f"Please insert more {self.cart_price - self.current_balance} and check out again")
        else:
            for item in self.current_items:
                self.item_inventory.deduct(item)

            self.total_sale = self.cart_price
            self.current_balance = self.current_balance - self.cart_price
            self.cart_price = 0
            self.current_items = []
            self.refund()

    def insert_coin(self, coin):
        self.current_balance = self.current_balance + coin.value
        self.coin_inventory.add(coin)
        print(f"Inserted {coin.name}")
        print(f"Balance: {self.current_balance}")

    def refund(self) -> None:
        """
        Refund less coin as posible
        """
        refund_coin = []

        while self.current_balance > 0:
            if self.current_balance > 25:
                self.current_balance = self.current_balance - 25
                self.coin_inventory.deduct(Coin.QUARTER)
                refund_coin.append(Coin.QUARTER)
            elif self.current_balance > 10:
                self.current_balance = self.current_balance - 10
                self.coin_inventory.deduct(Coin.DIM)
                refund_coin.append(Coin.DIM)
            elif self.current_balance > 5:
                self.current_balance = self.current_balance - 5
                self.coin_inventory.deduct(Coin.NICKEL)
                refund_coin.append(Coin.NICKEL)
            else:
                self.current_balance = self.current_balance - 1
                self.coin_inventory.deduct(Coin.PENNIE)
                refund_coin.append(Coin.PENNIE)
        print(f"Refund amount {Counter(refund_coin).items()}")

    def restart(self):
        self.current_items = []
        self.refund()

    def display(self):
        self.item_inventory.display()
        self.coin_inventory.display()
        print(f"Total Sale: {self.total_sale}")

if __name__ == '__main__':
    vending = VendingMachine()
    vending.display()
    for _ in range(10):
        vending.insert_coin(random.choice(list(Coin)))
    vending.select_item(Item.COKE)

    vending.check_out()
    vending.display()

    print("#################################")
    for _ in range(5):
        vending.insert_coin(random.choice(list(Coin)))

    for _ in range(5):
        vending.select_item(random.choice(list(Item)))

    vending.check_out()
    vending.display()