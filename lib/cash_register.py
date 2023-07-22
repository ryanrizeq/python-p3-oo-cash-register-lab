#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0.0):
    self.discount = discount
    self.total = total
    self.items = []
    self.prices = []
  
  def add_item(self, item, price, quantity=1):
    self.total += (price * quantity)

    i = 0
    while i < quantity:
      self.items.append(item)
      self.prices.append(price)
      i += 1

  def apply_discount(self):
    if (self.discount == 0):
      print("There is no discount to apply.")
    else:
      self.total -= (self.total * (self.discount / 100))
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    i = -1
    if self.items[-1] == self.items[-2]:
      self.total -= (self.prices[-1] + self.prices[-2])
    else:
      self.total -= self.prices[-1]
    