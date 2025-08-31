confirm = 'n'
while confirm == 'n':
    AnimalName = input("Enter the name: ")
    AnimalSpecies = input("Enter the species: ")
    AnimalAge = int(input("Enter the age (years): "))
    AnimalWeight = float(input("Enter the animals's weight (kg.): "))
    print(f"Confirm the animal's registration\n{AnimalName}\n{AnimalSpecies}\n{AnimalAge}\n{AnimalWeight}")
    confirm = input("Confirm? (y/n)").lower()

