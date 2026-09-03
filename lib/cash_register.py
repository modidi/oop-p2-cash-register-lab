#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, value):
    if type(value) == int and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")

  def add_item(self, item, price, quantity=1):
    self.total += price * quantity

    for _ in range(quantity):
      self.items.append(item)

    self.previous_transactions.append({
      "item": item,
      "price": price,
      "quantity": quantity
    })

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total = self.total - (self.total * self.discount / 100)
      self.total = int(self.total)
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    if self.previous_transactions:
      transaction = self.previous_transactions.pop()

      item = transaction["item"]
      price = transaction["price"]
      quantity = transaction["quantity"]

      self.total -= price * quantity

      for _ in range(quantity):
        self.items.remove(item)
