"""
A practice project from CodeAcademy
"""
def cost_ground_shipping (weight):
  flat_charge = 20.00
  if weight <= 2:
    return flat_charge + weight * 1.5
  elif weight <= 6:
    return flat_charge + weight * 3.0
  elif weight <= 10:
    return flat_charge + weight * 4.0
  else:
    return flat_charge + weight * 4.75

def cost_drone_shipping (weight):
   if weight <= 2:
    return weight * 4.5
   elif weight <= 6:
    return weight * 9.0
   elif weight <= 10:
    return weight * 12.0
   else:
    return weight * 14.25

cost_premium_ground_shipping = 125

def cost_compare (weight):
  total = min([cost_ground_shipping(weight), cost_drone_shipping (weight), cost_premium_ground_shipping])
  method = ""
  if total == cost_premium_ground_shipping:
    method = "Premium Ground Shipping"
  elif total == cost_ground_shipping(weight):
    method = "Ground Shipping"
  else:
    method = "Drone Shipping"

  print ( "The cheapest shipping method is {}".format(method) )
  print ( "The total cost is {}".format(total) )

def get_weight ():
  
  weight = float(raw_input("How heavy is your package(in Pounds): "))
  return weight

def weight_cost_selector ():
  weight = get_weight()
  cost_compare(weight)

if True:
  weight_cost_selector()
