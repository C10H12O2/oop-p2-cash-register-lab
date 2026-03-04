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
    
  def apply_discount(self):
    if self.discount > 0:
      self.total = self.total * (1 - (self.discount / 100))
      return self.total
    else:
      return self.total
    
  def void_last_transaction(self):
    if self.previous_transactions:
      last_transaction = self.previous_transactions.pop()
      
      if last_transaction["item"] in self.items:
        self.items.remove(last_transaction["item"])
        
        self.total -= (last_transaction["price"] * last_transaction["quantity"])
      else:
        print("There is no transactions to void.")
