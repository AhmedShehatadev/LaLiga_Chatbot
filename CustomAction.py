from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action
import wikipedia as Wiki
import random
from playerewards import get_via_crawling_info_about_rewards

logger = logging.getLogger(__name__)

## action club history
class Action_clubhistory(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_clubhistory"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #request = requests.get('http://api.icndb.com/jokes/random').json() #make an apie call
        #joke = request['value']['joke'] #extract a joke from returned json response
        #tracker
        clubname = tracker.get_slot("laligaclubs")
        clubname = clubname.lower()
        if "club" not in clubname:
           clubname = clubname + " " + "club"       
        
        cluppage = Wiki.page(clubname)
        out = Wiki.summary(clubname, sentences=1)
        dispatcher.utter_message(out) #send the message back to ,image_url_club = "alex"  the usercluppage.images[0]
        dispatcher.utter_template("action_clubhistory",tracker,image_url_club = cluppage.images[0] )
        return []
        
## Action action_stadiuminfo
class Action_stadiuminfo(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_stadiuminfo"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        # to be modified by Nltk to get capacity if needed
        stadium = tracker.get_slot("laligaclubs")
        stadium = stadium.lower()
        if "stadium" not in stadium:
           stadiumname = stadium + " stadium" 
        stadiumpage = Wiki.page(stadiumname)
        number = random.randint(5890,123123)
        lstofoption = [". and the size of the stadium is ," + str(number),".the capacity is " + str(number),". stadium can take "+str(number)]
        secure_random = random.SystemRandom() # to be removed by nltk so i can get from wiki the word capacity if needed
        concat = secure_random.choice(lstofoption)
        # wiki api to get info
        out = Wiki.summary(stadiumname, sentences=1)
        dispatcher.utter_message(stadiumname + " " + out + concat ) #send the message back to the user
        dispatcher.utter_message("Please click this image " + stadiumpage.images[0])
        return []
'''        
# action_gameresult  
#To be implemented after purchasing
https://market.mashape.com/heisenbug/
la-liga-live-scores#match-scorers 
api for live and previous scores
'''
class Action_gameresult(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_gameresult"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #request = requests.get('http://api.icndb.com/jokes/random').json() #make an apie call
        #joke = request['value']['joke'] #extract a joke from returned json response
        #tracker
        # team one from slot + team 2 from slot plus score -score
        laligaclubs = tracker.get_slot("laligaclubs")
        score1 = random.randint(0,5)
        score2= random.randint(0,4)
        out = "The game of the " + laligaclubs + " ended " + str(score1) + " - " + str(score2)
        dispatcher.utter_message(out) #send the message back to the user
        return []
class Action_players_prizes(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_players_prizes"

    def run(self, dispatcher, tracker, domain):
        # get_via_crawling_info_about_rewards to be used
        # what your action should do
        #request = requests.get('http://api.icndb.com/jokes/random').json() #make an apie call
        #joke = request['value']['joke'] #extract a joke from returned json response
        #tracker
        # team one from slot + team 2 from slot plus score -score
        nameofplayer = tracker.get_slot("players")
        response = get_via_crawling_info_about_rewards(nameofplayer)
        
        if response == "":
          out = "The player you mentioned seems that he did not recieve any gifts"
        else:
          position,playername = response.split("|")
          out = "Yes! " + playername +  " recieved the " + position
        dispatcher.utter_message(out) #send the message back to the user
        return []
class Action_playerstoclubinfo(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_playerstoclubinfo"

    def run(self, dispatcher, tracker, domain):
        nameofplayer = tracker.get_slot("players")
        # got_results_via_crawling_info_about_rewards to be used

        # team one from slot + team 2 from slot plus score -score
        out = "do you mean" + nameofplayer + ",yes He plays in alot of positions in the team and scored alot"
        dispatcher.utter_message(out) #send the message back to the user
        #dispatcher.utter_message(nameofplayer)
        return []         