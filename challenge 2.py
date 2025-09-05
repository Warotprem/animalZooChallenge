Capacity = 10

AnimalNames = [''] * Capacity
AnimalSpecies = [''] * Capacity
AnimalAges = [0] * Capacity
AnimalWeights = [0.0] * Capacity

AnimalCount = 0

def addAnimal():
    if AnimalCount >= Capacity:
        print("The zoo capacity is full (10 animals). Cannot add more.\n")
        return
    confirm = "n"
    while confirm == "n":
        name = input("Enter the name: ")
        specie = input("Enter the species: ")
        age = int(input("Enter the age (years): "))
        weight = float(input("Enter the animal's weight (kg): "))
        print("\nConfirm the animal's registration")
        print(name)
        print(specie)
        print(age)
        print(weight)
        confirm = input("Confirm? (y/n): ").strip().lower()
        