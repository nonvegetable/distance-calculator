import APICall
from DistanceCalculate import calculate_distance

# Take user inputs
place1 = input("Enter place 1: ")
place2 = input("Enter place 2: ")

# Make a call to the API to get the coordinates
coord1 = APICall.api_call(place1)
coord2 = APICall.api_call(place2)

# Calculate the distance
distance = calculate_distance(coord1, coord2)

# Print the final output
print(f"\nThe distance between {place1} and {place2} is {distance:.2f} kilometers.")
