class Life:
    def __init__(self):
        self.success = False
        self.alive = True

    def start_life(self):
        print("Life started.")
        
    def make_success(self):
        return self.success

    def try_again(self):
        print("Trying again...")

    def death(self):
        return not self.alive

def main():
    my_life = Life()
    my_life.start_life()
    while not my_life.make_success():
        my_life.try_again()
        if my_life.death():
            print("Life ended.")
            break

if __name__ == "__main__":
    main()
