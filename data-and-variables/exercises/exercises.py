# 1. Declare and assign the variables here:
space_shuttle_name = "Determination"
shuttle_speed_mph = 17500
distance_to_mars_km = 225000000
distance_to_moon_km = 384400
m_per_km = 0.621
# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(space_shuttle_name))
print(type(shuttle_speed_mph))
print(type(distance_to_mars_km))
print(type(distance_to_moon_km))
print(type(m_per_km))

# Code your solution to exercises 3 and 4 here:
m_to_mars = distance_to_mars_km * m_per_km
hrs_to_mars = m_to_mars / shuttle_speed_mph
days_to_mars = hrs_to_mars / 24

print(f"{space_shuttle_name} will take {days_to_mars} to reach Mars.")

# Code your solution to exercise 5 here
m_to_moon = distance_to_moon_km * m_per_km
hrs_to_moon = m_to_moon / shuttle_speed_mph
days_to_moon = hrs_to_moon / 24

print(f"{space_shuttle_name} will take {days_to_moon} to reach the Moon.")
