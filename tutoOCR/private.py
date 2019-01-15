class CoffeeMachine:
    WATER_LEVEL = 100

    def _start_machine(self): # protected
        # Start the machine
        if self.WATER_LEVEL > 20:
            return True
        else:
            print("Please add water!")
            return False

    def __boil_water(self): # private
        return "boiling..."

    def make_coffee(self):
        # Make a new coffee!
        if self._start_machine():
            self.WATER_LEVEL -= 20
            print(self.__boil_water())
            print("Coffee is ready!")


machine = CoffeeMachine()
#for i in range(0, 5):
#  machine.make_coffee()

print("Make Coffee: Public", machine.make_coffee())
print("Start Machine: Protected", machine._start_machine())
print("Boil Water: Private", machine.__boil_water()) # error
print("Boil Water: Private", machine._CoffeeMachine__boil_water()) # fonctionne
