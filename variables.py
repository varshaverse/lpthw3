# Variables

cars = 100 #intializes variable cars to a value of 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers # stores value of cars not driven by subtracting cars value and drivers value
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven 
print("\n")

print("There are", cars, "cars available.") # prints the final value of cars as well the other variables
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
print("\n")


