class encapsulation:
    def __init__(self):
        self.name="Sandeep"
        self.age="19"
    def get_name(self):
        print(self.name)
    def set_name(self,value):
        self.name=value
obj=encapsulation()
obj.get_name()