#variables
weight = 41.5
premium_ground_shipping = 125.00
cost_drone = ""
cost_ground = ""

#ground shipping logic
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20

# ground print logic
print("Ground Shipping: $", cost_ground, "\n")

print("Ground Shipping Premium: $", premium_ground_shipping, "\n")

#drone shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.0
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.0
else:
  cost_drone = weight * 14.25

#drone print logic
print("Drone Shipping: $", cost_drone)
