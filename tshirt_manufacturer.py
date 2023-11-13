def calculate_costs(size, material):
    prices = {
        ("Small", "Polyester"): 8,
        ("Small", "Cotton"): 10,
        ("Medium", "Polyester"): 12,
        ("Medium", "Cotton"): 13.50,
        ("Large", "Polyester"): 15,
        ("Large", "Cotton"): 16,
        ("Extra-Large", "Polyester"): 18,
        ("Extra-Large", ""): 20
        }
    return prices[(size, material)]


def bubble_sort(tshirts):
    n = len(tshirts)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if tshirt[j] > tshirt [j+1]:
                tshirt[j], tshirt [J+1] = tshirt[j+1], tshirt[j]

num_tshirts = int(input("How many tshirts would you like to order?"))
tshirts = []

# Loop to get the size and material of each t-shirt from the user
for i in num_tshirts:
    print(f"Enter details for shirt #{i + 1}:")
    size = input("Size? (Small, Medium, Large, Extralarge)")
    material = input("Material? (Polyester or Cotton)")
    cost = calculate_costs(size, material)
    tshirts.append((size, material, cost))

bubble_sort(tshirts)

totalcost = 0
sizecost = {"Small":0, "Medium":0, "Large":0, "Extra-Large":0}

for shirt in tshirts:
    totalcost = totalcost + tshirts[2]
    sizecost[shirt[0]] += shirt[2]

print("\nSorted T-Shirts:")
for t_shirt in tshirts:
    print(f"Size: {t_shirt[0]}, Material: {t_shirt[1]}, Cost: ${t_shirt[2]}")

print(f"\nTotal Cost: ${totalcost}")
print("Cost by Size:")
for size, cost in sizecost.items():
    print(f"{size}: ${cost}")
