from models.tamagochi import Tamagochi, State
from helpers.say import say


class Boring(State):

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
        say("Estoy jugando")
        print("Estoy jugando... :) \n")
        from models.states.tired import Tired
        self.tamagochi.setState(Tired())

    def feed(self) -> None:
        """
        This method is called when user select feed option from
        the panel options
        """
        say("No quiero comer")
        print("No quiero comer :(... \n")

    def sleep(self) -> None:
        """
        This method is called when user select sleep option from
        the panel options
        """
        say("No quiero dormir")
        print("No quiero dormir... \n")

    def howAreYou(self) -> None:
        """
        This method is called when user select 'how are you' option from
        the panel options
        """
        say("Estoy aburrido")
        print("Estoy aburrido... :( \n")
