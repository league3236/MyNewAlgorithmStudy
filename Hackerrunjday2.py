#round()

def solve(meal_cost, tip_percent, tax_percent):
  tip = meal_cost*(tip_percent/100)
  tax = meal_cost*(tax_percent/100)

  return round(meal_cost+tip+tax)
  
print(solve(10.25, 17, 5))
