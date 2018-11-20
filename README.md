# Sports LaLiga_Chatbot
﻿# Rasa Stack starter-pack

Looked through the [Rasa NLU](http://rasa.com/docs/nlu/) and [Rasa Core](http://rasa.com/docs/core/) documentation and ready to build your first intelligent assistant? We have some resources to help you get started! This repository contains the foundations of your first custom assistant. This starter-pack is also accompanied by a step-by-step video tutorial, which you can find [here](https://youtu.be/lQZ_x0LRUbI). 

This project comes with training data and testing as well as pre-trained model.

I would recommend downloading this packages before getting started 

The Current version of this Chatbot lets you build a simple conversational assistant which is capable of handling up LaLiga Conversation 


<p align="center">
  Please Have Look at those two sample conversation :
</p>
<p align="left">
  <img src="https://github.com/AhmedShehatadev/LaLiga_Chatbot/blob/master/conv1.png">
</p>

Clone this repo to get started:

```
git clone https://github.com/AhmedShehatadev/LaLiga_Chatbot.git
```
## Setup and installation

If you haven’t installed Rasa NLU and Rasa Core yet,   
```
pip install -r requirements.txt
`''

## What’s in this project?

This LaLiga project contains some training data and the main files which you can use as the basis of your first custom assistant. It also has the usual file structure of the assistant built with Rasa Stack. This starter-pack consists of the following files:

### Files for training the Rasa NLU model

- **data/training.json** file contains training examples and testing example... of 10 intents 
   and chatito tool data sample data of how we created the rasa nlu data using this tool [here](https://rodrigopivi.github.io/Chatito/) 
	
	- action_stadiuminfo   i.e what is the size of madrid stadium -- > To ask about laliga conversation
	- utter_name	       i.e my name is alex   --> you have intent to give the bot your name
	- utter_greet	       i.e Hello wusp bot    --> you have intent to Say hey to the bot 
	- utter_byebye	       i.e bye bye bot       --> you have intent to  say bye to that bot 
	- utter_apperciation 	i.e Thank you bot        --> you have intent to  thx the bot 
	- action_clubhistory    i.e what is the history of barcelona       --> you have intent to get knwoledge about specific team 
	- action_gameresult  i.e what was the score of barcelona and espanyol game --> you have intent to get knwoledge about game score 
	- action_players_prizes  i.e did messi won the best goal keeper before --> you have intent to get game results
	- action_playerstoclubinfo i.e do messi play in this position 
	- utter_affirm_confirm    i.e sure bot ,, i agree bot  --> you have intent to say yes
	- action_default_fallback
	
- **Tensorflow_Embedding** file contains the configuration of the Rasa NLU pipeline: 
  I did conver multiintent to include in the config but will do so in later versions
```text
language: "en"

pipeline:
- name: "tokenizer_whitespace"
- name: "ner_crf"
- name: "ner_synonyms"
- name: "intent_featurizer_count_vectors"
- name: "intent_classifier_tensorflow_embedding"
```	

### Files for training the Rasa Core model

- **data/stories.md** file contains some training stories which represent the conversations between a user and the assistant.
Example of a story is : 
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubs_history{"laligaclubs":"barcelona"}
   - action_clubhistory
* laliga_clubsstadiuminfo_history{"laligaclubs":barcelona}
   - action_stadiuminfo
* laliga_rewardstoplayers{"soccerposition":"goalkeeper","players":"messi"}
   - action_players_prizes
* apperciation
   - utter_apperciation
* byebye 
   - utter_byebye

- **domain.yml** file describes the domain of the assistant which includes intents, entities, slots, templates and actions the assistant should be aware of.  
- **CustomAction.py** file contains the code of a custom actions:
  We have 5 different custom action which retrieve responses mainly for intent that need custom action i.e club history but is not needed for intent like greeeting as we can provide in the template of domain file since it is simple text ... 
  
  The custom action out response are being retrieved differently for each intent for example (Action_clubhistory via wiki api call that retrieve page on the mentioned club from wiki and summarize the history) but for some intent like (player reward since it is specific result i luckily found some table that i used web crawler to retrieve specific info i need) 
using import requests
from bs4 import BeautifulSoup 

- **endpoints.yml** file contains the webhook configuration for custom action.

## How to use this starter-pack?
1. You can train the Rasa NLU model by running:  
```make train-nlu```  
This will train the Rasa NLU model and store it inside the `/models/current/nlu` folder of your project directory.

2. Train the Rasa Core model by running:  
```make train-core```  
This will train the Rasa Core model and store it inside the `/models/current/dialogue` folder of your project directory.

3. Start the server for the custom action by running:  
```make action-server```  
This will start the server for emulating the custom action.

4. Test the assistant by running:  
```make cmdline```  
This will load the assistant in your terminal for you to chat.

## What's next?
This starter-pack lets you build a simple assistant which can tell Chuck Norris jokes. It's pretty fun, but there is so much more you can do to make a really engaging and cool assistant. Here are some ideas of what you can do to take this assistant to the next level:  
- **Use the Rasa NLU [training data file](https://forum.rasa.com/t/grab-the-nlu-training-dataset-and-starter-packs/903) which you downloaded previously from the Rasa Community Forum**. This dataset contains quite a few interesting intents which will enable your assistant to handle small talk. To use it, append the training examples to `data/nlu_data.md` file, retrain the NLU model and see how your assistant learns new skills.
- Enrich `data/nlu_data.md` file with the custom intents you would like your assistant to understand. Retrain the NLU model using the command above and see you assistant improving with every run!  
- Enrich `data/stories.md` file with more training stories with different dialogue turns, intents and actions.  
- Implement more custom action inside the `actions.py` file and add them to stories data as well as the domain file.   


Let us know how you are getting on with Rasa Stack and what have you built! Join the [Rasa Community Forum](https://forum.rasa.com) and share your experience with us!

