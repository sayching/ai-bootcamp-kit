# create a Class which has three methods:

class IOContainer:
    var = None

    def read_input(self):
        self.var = input("enter any input")

    def print_message(self):
        if self.var is None:
            print("Nothing to display")
        else:
            print(self.var)

    def reset_message(self):
        self.var = None


obj = IOContainer()
obj.read_input()
obj.print_message()
obj.reset_message()
obj.print_message()
