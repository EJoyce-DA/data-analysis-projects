# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.
fuel_level = 0
astronauts_on_board = 0
current_altitude = 0




# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 

while fuel_level <= 5000 or fuel_level > 30000:
    fuel_level = int(input("Enter Starting Fuel Level: "))
   

# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
  
while astronauts_on_board <=0: 
    astronauts_on_board = int(input("Enter Number of Astronauts on Board: "))
    if astronauts_on_board <=7:
       print(f"Crew on board: {astronauts_on_board}. Begin launch.")
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.

while fuel_level - 100 * astronauts_on_board >= 0:
    current_altitude += 50
    fuel_level -= 100 * astronauts_on_board
    print(f"The shuttle gained an altitude of {current_altitude} km and has {fuel_level} kg of fuel left.")



# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.


# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”

if current_altitude >= 2000:
  ending = "Orbit achieved!"
else:
  ending = "Failed to reach orbit."
print(f"The shuttle gained an altitude of {current_altitude} km and has {fuel_level} kg of fuel left. {ending}")