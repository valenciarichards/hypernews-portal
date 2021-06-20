def tallest_people(**names_and_heights):
    largest = {}
    max_height = max(names_and_heights.values())
    for name, height in names_and_heights.items():
        if height == max_height:
            largest[name] = height
    for name, height in sorted(largest.items()):
        print(f"{name} : {height}")
