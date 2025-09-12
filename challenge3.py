# max is 10
Capacity = 10

# initialize lists
AnimalNames = [''] * Capacity
AnimalSpecies = [''] * Capacity
AnimalAges = [0] * Capacity
AnimalWeights = [0.0] * Capacity

AnimalCount = 0

def addAnimalDetails(name, specie, age, weight):
    # No checks here ,keeping it simple
    global AnimalCount
    i = AnimalCount
    AnimalNames[i]   = name
    AnimalSpecies[i] = specie
    AnimalAges[i]    = age
    AnimalWeights[i] = weight
    AnimalCount += 1

def findAnimalIndexByName(searching_name):
    target = searching_name.strip().lower()
    if target == "":
        return -1
    for i in range(AnimalCount):
        if AnimalNames[i].strip().lower() == target:
            return i
    return -1




# validation input things (loop until ok)
def getValidName(prompt_text):
    while True:
        s = input(prompt_text).strip()
        if len(s) > 0:
            return s
        print("please enter something")

def getValidAge(prompt_text):
    # must be int between 1 and 50
    while True:
        t = input(prompt_text).strip()
        try:
            v = int(t) 
            if 1 <= v <= 50:
                return v
            else:
                print("age must be 1-50")
        except ValueError:
            print("age has to be a whole number")

def getValidWeight(prompt_text):
    # must be float between 0.1 and 1000
    while True:
        t = input(prompt_text).strip()
        try:
            v = float(t)
            if 0.1 <= v <= 1000:
                return v
            else:
                print("weight must be between 0.1 and 1000 kg.")
        except ValueError:
            print("weight needs to be a number")

def addAnimal():
    global AnimalCount  
    if AnimalCount >= Capacity:
        print("The zoo capacity is full (10 animals). Cannot add more.\n")
        return
    
    confirm = "n"
    while confirm == "n":
        # inputs with validation
        name = getValidName("Enter the name: ")
        specie = getValidName("Enter the species: ")
        age = getValidAge("Enter the age (years 1-50): ")
        weight = getValidWeight("Enter the animal's weight (kg 0.1-1000): ")
        
        print("\nConfirm the animal's registration")
        print(name)
        print(specie)
        print(age)
        print(weight)
        confirm = input("Confirm? (y/n): ").strip().lower()

    if confirm == "y":
        addAnimalDetails(name, specie, age, weight)
        print(f"\nRegistered '{name}' ({specie}). Total animals: {AnimalCount}/{Capacity}\n")
    else:
        print("\nRegistration cancelled.\n")


def view_all_animals():
    if AnimalCount == 0:
        print("\nNo animals to display.\n")
        return

    print("\nCurrent Animals ")
    for i in range(AnimalCount):
        print(f"{i+1}. Name: {AnimalNames[i]} | Species: {AnimalSpecies[i]} | "
              f"Age: {AnimalAges[i]} years | Weight: {AnimalWeights[i]} kg")
    print("\n")


def show_statistics():
    if AnimalCount == 0:
        print("\nThe zoo is empty...\n")
        return
    totalAge = 0
    totalWeight = 0.0

    # init mins/maxes from first one
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
    print("\nZoo Statistics")
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



def feedAnimal(name):
    # using case-insensitive search
    idx = findAnimalIndexByName(name)
    if idx == -1:
        print(f"could not find '{name}' to feed. maybe typo?")
    else:

        print(f"{AnimalNames[idx]} the {AnimalSpecies[idx]} has been fed. yum.")


# function: random health check (returns a string)
def checkHealth(name):

    import random
    idx = findAnimalIndexByName(name)
    if idx == -1:
        return "Unknown (animal not found)"
    # do some pretend randomness
    status = random.choice(["Healthy", "Sick", "Injured"])
    return status


def searchAnimal():
    if AnimalCount == 0:
        print("\nzoo empty, nothing to search.\n")
        return
    q = input("Search by name: ")
    idx = findAnimalIndexByName(q)
    if idx == -1:
        print("no match. try different case/spelling?")
    else:
        # show the animal we found
    
        print(f"found it: {AnimalNames[idx]} | {AnimalSpecies[idx]} | age {AnimalAges[idx]} | {AnimalWeights[idx]} kg")



def menu():
    while True:
        print("Zoo Manager")
        print("1. Register a new animal")
        print("2. View animals")
        print("3. Show stats")
        print("4. Search by name (case-insensitive)")
        print("5. Feed an animal")
        print("6. Health check")
        print("7) Done")
        choice = input("Choose your option (1-7): ").strip()

        if choice == "1":
            addAnimal()
        elif choice == "2":
            view_all_animals()
        elif choice == "3":
            show_statistics()
        elif choice == "4":
            searchAnimal()
        elif choice == "5":
            name = input("which animal to feed? ")
            feedAnimal(name)
        elif choice == "6":
            name = input("which animal to check? ")
            result = checkHealth(name)
            print(f"health status: {result}")
        elif choice == "7":
            print("\nGoodbye!\n")
            break
        else:
            print("\nPlease pick 1-7.\n")

menu()
