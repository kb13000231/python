ls= list()
def change(amount):
  if amount%7 !=0:
      amount -= 5
      ls.append(5)
      change(amount)
      return ls
  elif amount==0:
      return ls
  else:
      amount -= 7
      ls.append(7)
      change(amount)
      return ls
print(change(25))
