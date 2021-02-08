from mycroft import MycroftSkill, intent_file_handler


class DarinsPirate(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pirate.darins.intent')
    def handle_pirate_darins(self, message):
        self.speak_dialog('pirate.darins')


def create_skill():
    return DarinsPirate()

