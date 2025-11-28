weight = 41.5

#Ground shipping
def ground_shipping(weight):
    if weight <= 0:
      print("Please enter a valid positive weight.")
    elif weight <= 2:
      return weight * 1.5 + 20.0
    elif weight <= 6:
      return weight * 3.0 + 20.0
    elif weight <= 10:
      return weight * 4.0 + 20.0
    else:
      return weight * 4.75 + 20.0
cost_ground = ground_shipping(weight)

#Premium shipping
cost_ground_premium = 125.00

#Drone shipping
def drone_shipping(weight):
  if weight <= 0:
    print("Please enter a valid positive weight.")
  elif weight <= 2:
    return weight * 4.5
  elif weight <= 6:
    return weight * 9.0
  elif weight <= 10:
    return weight * 12.0
  else:
    return weight * 14.25
cost_drone_shipping = drone_shipping(weight)

print(f"Ground shipping cost of the package is: {cost_ground:.2f}€.")
print(f"Ground premium shipping cost of the package is: {cost_ground_premium:.2f}€.")
print(f"Ground shipping cost of the package is: {cost_drone_shipping:.2f}€.")

#Cheaper shipping
if cost_ground < cost_ground_premium and cost_ground < cost_drone_shipping:
  shipping_cost = cost_ground
elif cost_ground_premium < cost_ground and cost_ground_premium < cost_drone_shipping:
  shipping_cost = cost_ground_premium
else:
  shipping_cost = cost_drone_shipping

print(f"The cheapest shipping method is: {shipping_cost:.2f}€.")