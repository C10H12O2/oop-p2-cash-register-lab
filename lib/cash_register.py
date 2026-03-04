#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.items = []
    self.total = 0
    self.previous_transactions = []
    
  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, value):
    if isinstance(value, int) and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not a valid discount")
      
  def add_item(self, item, price, quantity=1):
    self.total += (price * quantity)
    self.items.append(item)
    transaction = {
      "item": item,
      "price": price,
      "quantity": quantity
    }
    self.previous_transactions.append(transaction)
    

