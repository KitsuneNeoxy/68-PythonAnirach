def Display_Heroes(heroes):
    print(heroes)

def Add_Heroes(heroes,hero):
    heroes.append(hero)
    Display_Heroes(heroes)
    
def Insert_Heroes(heroes,InsHero,Position):
    H = heroes
    Ins = str(InsHero)
    Pos = int(Position) - 1
    
    H.insert(Pos,Ins)
    Display_Heroes(heroes)

def Remove_Heroes(heroes,Rem):
    if Rem in heroes:
        heroes.remove(Rem)
    Display_Heroes(heroes)

def Display_Sort_Heroes(heroes,choice):
    choice = str(choice).lower()
    if choice == "ascending":
        Display_Heroes(sorted(heroes))
    elif choice == 'descending':
        Display_Heroes(sorted(heroes, reverse=True))

    
heroes = ['Ironman', 'Thor', "Hulk", 'Spiderman']


print("Display Hero:")
Display_Heroes(heroes)

print("Add Heroes:")
Add_Heroes(heroes,"Teletubbies")

print("Insert Hero:")
Insert_Heroes(heroes,"Dogman",1)

print("Remove Hero:")
Remove_Heroes(heroes,"Hulk")

print("Display Ascending:")
Display_Sort_Heroes(heroes,"Ascending")

print("Display Descending:")
Display_Sort_Heroes(heroes,"Descending")