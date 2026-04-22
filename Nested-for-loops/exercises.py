def print_pyramid(height):
    for i in range(height):
        for j in range(i+1):
            print("*", end="")
        print()


print_pyramid(5)