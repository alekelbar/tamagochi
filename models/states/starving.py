from models.tamagochi import Tamagochi, State
from helpers.say import say


class Starving(State):

    tamagochi: Tamagochi

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
        say("No quiero jugar")
        print("No quiero jugar... :( \n")

    def feed(self) -> None:
        """
        This method is called when user select feed option from
        the panel options
        """
        say("Estoy comiendo")
        print("Comiendo... \n")
        from models.states.boring import Boring
        self.tamagochi.setState(Boring())

    def sleep(self) -> None:
        """
        This method is called when user select sleep option from
        the panel options
        """
        say("No quiero domir")
        print("No quiero dormir... \n")

    def howAreYou(self) -> None:
        """
        This method is called when user select 'how are you' option from
        the panel options
        """
        say("Estoy hambriento")
        print("Estoy hambriento... :( \n")
