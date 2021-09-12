class Animal:
    def __init__(self, group, name):
        self.group = group
        self.name = name
    
    #dispaplay animal
    def display(self):
        print("Animal type: " + self.group)
        print("Name: " + self.name)

#main
animal1 = Animal("dog", "fago")
animal1.group.title()
animal1.name.title()
animal1.display()
print(animal1.__class__)