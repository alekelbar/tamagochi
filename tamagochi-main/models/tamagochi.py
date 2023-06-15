from models.state import State


class Tamagochi():
    state: State

    def __init__(self) -> None:
        from models.states.boring import Boring
        self.setState(Boring())

    def setState(self, state: State):
        self.state = state
        self.state.setTamagochi(self)

    def play(self) -> None:
        """
        This method is called when user select play option from
        the panel options
        """
        self.state.play()

    def feed(self) -> None:
        """
        This method is called when user select feed option from
        the panel options
        """
        self.state.feed()

    def sleep(self) -> None:
        """
        This method is called when user select sleep option from
        the panel options
        """
        self.state.sleep()

    def howAreYou(self) -> None:
        """
        This method is called when user select 'how are you' option from
        the panel options
        """
        self.state.howAreYou()
