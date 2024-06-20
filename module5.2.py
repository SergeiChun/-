class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors (self,floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


lodge = House()
lodge.setNewNumberOfFloors(2)
print(lodge.numberOfFloors)