#max is 10
Capacity = 10

# initialize lists
AnimalNames = [''] * Capacity
AnimalSpecies = [''] * Capacity
AnimalAges = [0] * Capacity
AnimalWeights = [0.0] * Capacity

AnimalCount = 0


def addAnimal():
    global AnimalCount  

    # check capacity
    if AnimalCount >= Capacity:
        print("The zoo capacity is full (10 animals). Cannot add more.\n")
        return
    
    confirm = "n"
    while confirm == "n":
        # inputs
        name = input("Enter the name: ")
        specie = input("Enter the species: ")
        age = int(input("Enter the age (years): "))
        weight = float(input("Enter the animal's weight (kg): "))
        
        # confirmaion
        print("\nConfirm the animal's registration")
        print(name)
        print(specie)
        print(age)
        print(weight)
        # confirm bit
        confirm = input("Confirm? (y/n): ").strip().lower()

    if confirm == "y":
        i = AnimalCount  # index where next one goes
        AnimalNames[i]   = name
        AnimalSpecies[i] = specie
        AnimalAges[i]    = age
        AnimalWeights[i] = weight
        AnimalCount += 1  
        print(f"\nRegistered '{name}' ({specie}). Total animals: {AnimalCount}/{Capacity}\n")
    else:
        print("\nRegistration cancelled.\n")


def view_all_animals():
    if AnimalCount == 0:
        print("\nNo animals to display.\n")
        return

    print("\n--- Current Animals ---")
    for i in range(AnimalCount):
        print(f"{i+1}. Name: {AnimalNames[i]} | Species: {AnimalSpecies[i]} | "
              f"Age: {AnimalAges[i]} years | Weight: {AnimalWeights[i]} kg")
    print("-------------------------\n")


def show_statistics():
    if AnimalCount == 0:
        print("\nThe zoo is literally empty...\n")
        return
    totalAge = 0
    totalWeight = 0.0


    minAge = AnimalAges[0]
    maxAge = AnimalAges[0]
    minAge_idx = 0
    maxAge_idx = 0

    minWeight = AnimalWeights[0]
    maxWeight = AnimalWeights[0]
    minWeight_idx = 0
    maxWeight_idx = 0

    # loop through all animals and add values up
    for i in range(AnimalCount):
        age = AnimalAges[i]
        weight  = AnimalWeights[i]

        totalAge += age
        totalWeight += weight

        if age < minAge:
            minAge = age
            minAge_idx = i
        if age > maxAge:
            maxAge = age
            maxAge_idx = i

        if weight < minWeight:
            minWeight = weight
            minWeight_idx = i
        if weight > maxWeight:
            maxWeight = weight
            maxWeight_idx = i

    avg_age = totalAge / AnimalCount
    avg_weight = totalWeight / AnimalCount

    # print everything nicely
    print("\n------ Zoo Statistics ------")
    print(f"Animals currently in the zoo: {AnimalCount}")
    print(f"Total weight of all animals: {totalWeight:.2f} kg")
    print(f"Average age: {avg_age:.2f} years")
    print(f"Average weight: {avg_weight:.2f} kg")

    print("\nOldest animal:")
    print(f"  {AnimalNames[maxAge_idx]} ({AnimalSpecies[maxAge_idx]}), "
          f"{AnimalAges[maxAge_idx]} years, {AnimalWeights[maxAge_idx]} kg")

    print("\nYoungest animal:")
    print(f"  {AnimalNames[minAge_idx]} ({AnimalSpecies[minAge_idx]}), "
          f"{AnimalAges[minAge_idx]} years, {AnimalWeights[minAge_idx]} kg")

    print("\nHeaviest animal:")
    print(f"  {AnimalNames[maxWeight_idx]} ({AnimalSpecies[maxWeight_idx]}), "
          f"{AnimalAges[maxWeight_idx]} years, {AnimalWeights[maxWeight_idx]} kg")

    print("\nLightest animal:")
    print(f"  {AnimalNames[minWeight_idx]} ({AnimalSpecies[minWeight_idx]}), "
          f"{AnimalAges[minWeight_idx]} years, {AnimalWeights[minWeight_idx]} kg")
    print("---------------------------\n")


def menu():
    while True:
        print("Zoo Manager")
        print("1. Register a new animal")
        print("2. View animals")
        print("3. Show stats")
        print("4) Done")
        choice = input("Choose your option (1-4): ").strip()

        if choice == "1":
            addAnimal()
        elif choice == "2":
            view_all_animals()
        elif choice == "3":
            show_statistics()
        elif choice == "4":
            print("\nGoodbye!\n")
            break
        else:
            print("\nPlease pick 1-4.\n")



menu()
