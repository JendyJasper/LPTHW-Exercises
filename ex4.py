# get the total number of available crs
cars = 100
#fet the number of space in a car
space_in_a_car = 4.0
#get number of drivers
drivers = 30
#get number of passenger
passengers = 90
#get number of cars not driven by subtracting the number of drivers from the number of cars
cars_not_driven = cars - drivers
#get number of cars driven by simply understnding the number of drivers
cars_driven = drivers
#get the number of capacity by multiplying the number of cars driven by the space in a car
carpool_capacity = cars_driven * space_in_a_car
#get the number of average passengers by dividing the number of passengers by the number of cars drivers
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "passengers today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"