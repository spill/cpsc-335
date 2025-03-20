# main.py
# Author: Ryan Trinh
# License: MIT License
# Contact: rtrinh02@csu.fullerton.edu

def find_preferred_starting_city(city_distances, fuel, mpg):


    total_fuel_balance = 0  #fuel balance
    current_fuel_balance = 0  #current segment
    starting_city = 0  #starting city

    # Iterate over each city to determine if the current segment can be completed.
    for i in range(len(city_distances)):
        # Calculate the net gain in miles after refueling and traveling to the next city.
        net_gain = (fuel[i] * mpg) - city_distances[i]
        
        total_fuel_balance += net_gain
        current_fuel_balance += net_gain

        if current_fuel_balance < 0:
            starting_city = i + 1
            current_fuel_balance = 0

    #If the total fuel balance isnt non-neg, return the starting city.
    return starting_city

# Sample execution of the algorithm
if __name__ == "__main__":
    city_distances = [5, 25, 15, 10, 15]  
    fuel = [1, 2, 1, 0, 3]                
    mpg = 10                             

    # Compute and display the preferred starting city.
    result = find_preferred_starting_city(city_distances, fuel, mpg)
    print(f"Preferred Starting City: {result}")
