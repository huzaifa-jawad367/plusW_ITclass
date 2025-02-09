import random  # 1. Import the random module

# 2. Define the list of colors
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime"]

# 3. Generate a random index within the bounds of the colors list
random_index = random.randint(0, len(colors) - 1)

# 4. Select the color at the random index
selected_color = colors[random_index]

# 5. Reverse the selected color string to create the password
reversed_color = selected_color[::-1]

# 6. Print the results
print("Selected Color:", selected_color)
print("Generated Password (Reversed Color):", reversed_color)
