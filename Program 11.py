cube_dict = {}

for i in range(1, 6):
    cube = i ** 3
    cube_dict[i] = cube

# Print the dictionary using a loop
print("Dictionary of numbers and their cubes:")
for key, value in cube_dict.items():
    print(f"Key: {key}, Cube: {value}")
