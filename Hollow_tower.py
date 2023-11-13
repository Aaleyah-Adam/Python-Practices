def draw_hollow_a_tower(height):
    width = 2 * height - 1

    for i in range(1, height + 1):
        if i == height:
            print("A" * width)
        else:
            print(" " * (height - i) + "A" + " " * (2 * (i - 1) - 1) + "A")


height = int(input("Enter the height of the hollow A tower: "))
draw_hollow_a_tower(height)
