from models.state import State

statesImages = {
    "boring": "https://images.emojiterra.com/google/android-12l/512px/1f971.png",
    "sleeping": "https://w7.pngwing.com/pngs/953/690/png-transparent-bedroom-emoji-emoticon-rest-sleep-sleeping-emoji-icon-thumbnail.png",
    "starving": "https://cdn-icons-png.flaticon.com/512/742/742880.png",
    "tired": "https://images.emojiterra.com/google/android-11/512px/1f62b.png"
}


class Tamagochi():
    state: State

    def setImageUrl(self):
        from models.states.boring import Boring
        from models.states.sleeping import Sleeping
        from models.states.starving import Starving
        from models.states.tired import Tired

        if isinstance(self.state, Boring):
            self.socketio.emit(
                'url', statesImages['boring'])

        if isinstance(self.state, Sleeping):
            self.socketio.emit(
                'url', statesImages['sleeping'])

        if isinstance(self.state, Starving):
            self.socketio.emit(
                'url', statesImages['starving'])

        if isinstance(self.state, Tired):
            self.socketio.emit(
                'url', statesImages['tired'])

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

    def setSocket(self, socket):
        self.socketio = socket
