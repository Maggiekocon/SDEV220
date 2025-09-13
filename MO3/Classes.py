
class Vehicle():
    def __init__(self, type):
        self.type=type


class Automobile(Vehicle):
    def __init__(self, type=None, year=None, make=None, model=None, doors=None, roof=None):
        super().__init__(type)
        self.year= year
        self.make=make
        self.model=model
        self.doors=doors
        self.roof=roof
            
    def get_attributes(self):
        self.type = input("Enter Vehicle type: ")
        if (self.type.upper() == 'AUTOMOBILE') or (self.type.upper() =="CAR"):
            self.year = input("Enter the your automobile's year: ")
            self.make = input("Enter the your automobile's make: ")
            self.model = input("Enter the your automobile's model: ")
            self.doors = int(input("Enter the number of doors your automobile has: "))
            while (self.doors%2 != 0) or (self.doors < 2):
                raise ValueError('You must have an even number of doors')
                self.doors = input()
            self.roof = input("Enter your automobile's roof type: ")
            '''
            # for some reason this does not work
            while (self.roof != 'solid') or self.roof != 'sun':
                raise ValueError('roof type must be solid or sun roof')
                self.roof = input()
            '''

    def display(self):
        print(f"""
              Vehicle type: {self.type}""")
        if (self.type.upper() == 'AUTOMOBILE') or (self.type.upper() =="CAR"):
            print(f"""
            Year: {self.year}
            Make: {self.make}
            Model: {self.model}
            Doors: {self.doors}
            Roof: {self.roof}
            """)

my_Automobile = Automobile()
my_Automobile.get_attributes()
my_Automobile.display()



'''
class Plant:
    def __init__(self, name, type, color, major_nutrient):
        self.name=name
        self.type=type
        self.color=color
        self.major_nutrient=major_nutrient

#myPlant=Plant('Cactus','Plantae','green','sun')
#print(myPlant.name)

name=input()
type=input()
color=input()
major_nutrient=input()

newplant = ({name},{type},{color},{major_nutrient})
'''


