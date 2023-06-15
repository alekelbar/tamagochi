import threading
from models.tamagochi import Tamagochi, State
from helpers.say import say


class Sleeping(State):

    tamagochi: Tamagochi

    def __init__(self) -> None:
        super().__init__()
        t = threading.Timer(5, self.wakeup)
        t.start()

    def wakeup(self):
        from models.states.starving import Starving
        say("Buenos días")
        print("\n Waking up! \n")
        self.tamagochi.setState(Starving())

    def setTamagochi(self, tamagochi: Tamagochi) -> None:
        """
        This method is called when tamagochi state is changed
        """
        self.tamagochi = tamagochi

    def play(self) -> None:
        """
        This method is called when user select play option from
        the panel options
        """
        print("... \n")

    def feed(self) -> None:
        """
        This method is called when user select feed option from
        the panel options
        """
        print("... \n")

    def sleep(self) -> None:
        """
        This method is called when user select sleep option from
        the panel options
        """
        print("... \n")

    def howAreYou(self) -> None:
        """
        This method is called when user select 'how are you' option from
        the panel options
        """
        print("... \n")
