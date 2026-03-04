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
    
    for _ in range(quantity):
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
      print("There is no discount to apply.")
      return self.total
    
def void_last_transaction(self):
        if self.previous_transactions:
            last = self.previous_transactions.pop()
            
            self.total -= (last["price"] * last["quantity"])
            
            for _ in range(last["quantity"]):
                if last["item"] in self.items:
                    self.items.remove(last["item"])
        else:
            print("There is no transaction to void.")
