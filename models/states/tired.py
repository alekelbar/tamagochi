from models.tamagochi import Tamagochi, State
from helpers.say import say


class Tired(State):
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
        say("No quiero comer")
        print("No quiero comer... \n")

    def sleep(self) -> None:
        """
        This method is called when user select sleep option from
        the panel options
        """
        say("Buenas noches!")
        print("Durmiendo... \n")
        from models.states.sleeping import Sleeping
        self.tamagochi.setState(Sleeping())

    def howAreYou(self) -> None:
        """
        This method is called when user select 'how are you' option from
        the panel options
        """
        say("Estoy Cansado")
        print("Estoy Cansado... :( \n")
