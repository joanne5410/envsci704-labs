# Calculate the volume of a rectangular estuary (length x width x depth)
length = 5000   # metres
width = 800     # metres
depth = 3.5     # metres
volume = length * width * depth
print(f"Estuary volume: {volume} m^3")

# Simulate 10 days of exponential population growth
population = 100
rate = 0.05
history = [population]

for day in range(10):
    population = population + rate * population
    history.append(round(population, 1))

print(history)

# Write a function that converts temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

# Test it
for temp in [0, 15, 25, 37]:
    print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")

    import matplotlib.pyplot as plt

days = list(range(len(history)))
plt.plot(days, history, "o-")
plt.xlabel("Day")
plt.ylabel("Population")
plt.title("Exponential growth")
plt.show()

