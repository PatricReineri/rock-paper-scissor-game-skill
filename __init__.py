from mycroft import MycroftSkill, intent_handler


class RockPaperScissorGame(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('game.scissor.paper.rock.intent')
    def handle_game_scissor_paper_rock(self, message):
        self.speak_dialog('game.scissor.paper.rock')


def create_skill():
    return RockPaperScissorGame()

