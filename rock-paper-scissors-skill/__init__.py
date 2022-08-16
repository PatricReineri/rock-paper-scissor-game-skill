import random
import time
from mycroft import MycroftSkill, intent_handler


class RockPaperScissors(MycroftSkill):

    def __init__(self):
        MycroftSkill.__init__(self)
        self.rps = ['Paper', 'Rock', 'Scissors']
        self.URock = False
        self.UPaper = False
        self.UScissors = False
        self.CRock = False
        self.CPaper = False
        self.CScissors = False



         
    def computer_choice(self):
        mylist = ['Paper', 'Rock', 'Scissors']
        selection = random.choice(mylist)
        if(selection ==  'Rock'):
            self.CRock = True
        elif (selection  ==  'Paper'):
            self.CPaper = True
        elif  (selection  ==  'Scissors'):
            self.CScissors = True
        else : self.speak_dialog('Error: invalid choice')


    @intent_handler('scissors.pap.rock.intent')
    def handle_request_scissorsPaperRock(self):
        self.speak_dialog('Yeah, i am ready to play')
        selection = self.ask_selection(self.rps, 'Choose..')
        self.speak_dialog('scissors.pap.rock', {'type': selection})

        if(selection  ==  'Rock'):
            self.URock = True
        elif (selection  ==  'Paper'):
            self.UPaper = True
        elif  (selection  ==  'Scissors'):
            self.UScissors = True
        else : self.speak_dialog('Error: invalid choice')
        
        time.sleep(2)
        self.speak_dialog('Well, now it is my turn to choose')
        time.sleep(3)
        mylist = ['Paper', 'Rock', 'Scissors']
        selections = random.choice(mylist)
        if(selections ==  'Rock'):
            self.CRock = True
            self.speak_dialog('scissors.p.r', {'choice': selections})
        elif (selections  ==  'Paper'):
            self.CPaper = True
            self.speak_dialog('scissors.p.r', {'choice': selections})
        elif  (selections  ==  'Scissors'):
            self.CScissors = True
            self.speak_dialog('scissors.p.r', {'choice': selections})
        else : self.speak_dialog('Error: invalid choice')

        if((self.CPaper and self.UPaper) or( self.CRock and self.URock) or (self.CScissors and self.UScissors)):
            self.speak_dialog('That is a draw')
        elif ((self.CPaper  and self.UScissors ) or
              (self.CRock and self.UPaper )  or 
              (self.CScissors and self.URock )):
            self.speak_dialog('Congratulations, you win')
        else :
            self.speak_dialog('Oh yes, i win')
       




def create_skill():
    return RockPaperScissors()

