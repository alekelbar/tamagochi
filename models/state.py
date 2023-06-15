from abc import ABC, abstractclassmethod


class State(ABC):

    @abstractclassmethod
    def play(self) -> None:
        """
        This method is called when user select play option from
        the panel options
        """
        pass

    @abstractclassmethod
    def feed(self) -> None:
        """
        This method is called when user select feed option from
        the panel options
        """
        pass

    @abstractclassmethod
    def sleep(self) -> None:
        """
        This method is called when user select sleep option from
        the panel options
        """
        pass

    @abstractclassmethod
    def howAreYou(self) -> None:
        """
        This method is called when user select 'how are you' option from
        the panel options
        """
        pass

    @abstractclassmethod
    def setTamagochi(self, tamagochi) -> None:
        """
        This method is called when tamagochi state is changed
        """
        pass
