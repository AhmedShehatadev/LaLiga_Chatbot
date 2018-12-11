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
import wikipediaapi

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
        #----- wiki extraction ----
        out = "As a bot i am still learning, Can you rephrase you quistion"  
        if clubname is not None:  
         if "club" not in clubname:
           clubname = clubname + " " + "club"   
         wiki_wiki = wikipediaapi.Wikipedia('en')
                      
         wiki_wiki = wikipediaapi.Wikipedia('en')
         page_py = wiki_wiki.page(Wiki.search(clubname)[0])
         if page_py.exists():
            out = " " 
            out = page_py.summary[0:300].split('/n')[0]
            # Get the history
            historysection = page_py.section_by_title("History")
            out = out + ". REGARDING HISTORY :" + historysection.sections[0].text.split('\n')[0] 
        
        #--end of wiki extraction---
        dispatcher.utter_message(out) #send the message back to ,image_url_club = "alex"  the usercluppage.images[0]
        #dispatcher.utter_template("action_clubhistory",tracker,image_url_club = page_py.images[0] )
        return []
        
## Action action_stadiuminfo
class Action_stadiuminfo(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_stadiuminfo"

    def run(self, dispatcher, tracker, domain):
       # what your action should do
       # to be modified by Nltk to get capacity if needed
       out = "huh! Are you asking about team stadium can you try help me by asking in another way :)" 
       stadium = tracker.get_slot("laligaclubs")
       stadium = stadium.lower()
       if stadium is not None: 
        if "stadium" not in stadium:
           stadiumname = stadium + " stadium" 
        wiki_wiki = wikipediaapi.Wikipedia('en')
           
        # prepare out from wiki summary   
        page_py = wiki_wiki.page(Wiki.search(stadium)[0])
        if page_py.exists():
            out = " "
            number = random.randint(5890,123123)
            lstofoption = [". and the size of the stadium is ," + str(number),".the capacity is " + str(number),". stadium can take "+str(number)]
            secure_random = random.SystemRandom() # to be removed- just for now 
            concat = secure_random.choice(lstofoption)
            out = page_py.summary[0:300].split('/n')[0]
            out = out + concat + " Person "
   
       dispatcher.utter_message(out) #send the message back to the user
       #dispatcher.utter_message("Please click this image " + stadiumpage.images[0])
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
        out = "do you mean " + nameofplayer + " , yes He plays in alot of positions in the team and scored alot"
        dispatcher.utter_message(out) #send the message back to the user)
        return []
class Action_greeting(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_utter_greetwithname"

    def run(self, dispatcher, tracker, domain):
        nameofplayer = tracker.get_slot("players")
        out = "nice to you meet you boss. how can i help?"
        # got_results_via_crawling_info_about_rewards to be used
        username = tracker.get_slot("username")
        if username is not None: 
         # team one from slot + team 2 from slot plus score -score
         out = "nice to you meet you " + username + ". how can i help?"
        dispatcher.utter_message(out) #send the message back to the user)
        return []
class Action_default_fallback(Action):
  def name(self):
      return "action_default_fallback"

  def run(self, dispatcher, tracker, domain):
      from rasa_core.events import UserUtteranceReverted

      dispatcher.utter_template("utter_default", tracker,
                              silent_fail=True)

      return [UserUtteranceReverted()]        