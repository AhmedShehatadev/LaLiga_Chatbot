## story_greet_01 <!--- silly user say hi and bye --> 
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* byebye 
   - utter_byebye
   
##byebye
* greetings
   - utter_name   
* byebye 
   - utter_byebye
   
##story_greet_02 <!--- with apperciation -->    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* apperciation
   - utter_apperciation  
* byebye 
   - utter_byebye    

* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet   
* apperciation
   - utter_apperciation  
   
##story_greet_with_goal <!--- goal club history -->    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubs_history
   - action_clubhistory
* apperciation
   - utter_apperciation   
* byebye 
   - utter_byebye
   
##story_greet_with_goal <!--- goal club history -->    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubs_history
   - action_clubhistory
   - utter_affirm_confirm
* affirm
   - utter_greet 
* byebye 
   - utter_byebye
   
##story_greet_with_goal <!--- goal club history -->    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubs_history
   - action_clubhistory  
* byebye 
   - utter_byebye

##story_greet_with_goal <!--- goal club history -->    
* laliga_clubs_history
   - action_clubhistory
* apperciation
   - utter_apperciation
* byebye 
   - utter_byebye   

##story_greet_with_goal <!--- goal club history -->    
* laliga_clubs_history
   - action_clubhistory
   - utter_name
* providename{"username":"lucy"}
   - utter_greet

##story_greet_with_goal <!--- goal club history -->    
* laliga_clubs_history
   - action_clubhistory
* apperciation
   - utter_apperciation
   
##story_greet_with_goal <!--- goal club history -->    
* laliga_clubs_history
   - action_clubhistory
* apperciation
   - utter_apperciation
   - utter_affirm_confirm
* laliga_clubs_history 
   - action_clubhistory 
* apperciation
   - utter_apperciation   
* byebye 
   - utter_byebye

## story_with_goal <!--- stadium information -->
##story_greet_with_goal  <!--- stadium information -->    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubsstadiuminfo_history
   - action_stadiuminfo
* apperciation
   - utter_apperciation   
* byebye 
   - utter_byebye
   
##story_greet_with_goal <!--- goal club history -->    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubsstadiuminfo_history
   - action_stadiuminfo
* byebye 
   - utter_byebye
   
##story_greet_with_goal <!--- goal club history -->    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubsstadiuminfo_history
   - action_stadiuminfo
* byebye 
   - utter_byebye

##story_greet_with_goal <!--- goal club history -->    
* laliga_clubsstadiuminfo_history
   - action_stadiuminfo
* apperciation
   - utter_apperciation
* byebye 
   - utter_byebye   

##story_greet_with_goal <!--- goal club history -->    
* laliga_clubsstadiuminfo_history
   - action_stadiuminfo
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* byebye 
   - utter_byebye    

##story_greet_with_goal <!--- goal club history -->    
* laliga_clubsstadiuminfo_history
   - action_stadiuminfo
* apperciation
   - utter_apperciation
* byebye 
   - utter_byebye
   
##story_greet_with_goal <!--- goal club history -->    
* laliga_clubsstadiuminfo_history
   - action_stadiuminfo
* apperciation
   - utter_apperciation
   - utter_affirm_confirm
* affirm
   - utter_greet
* laliga_clubsstadiuminfo_history
   - action_stadiuminfo
* apperciation
   - utter_apperciation   
* byebye 
   - utter_byebye

<!--- two goals club history and stadium -->    
##story_club_historyandstadium
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubs_history
   - action_clubhistory
* laliga_clubsstadiuminfo_history
   - action_stadiuminfo  
* apperciation
   - utter_apperciation   
* byebye 
   - utter_byebye
   
##story_clubandstadiumhistorywithout_apperciaction
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubs_history{"laligaclubs":"barcelona"}
   - action_clubhistory
* laliga_clubsstadiuminfo_history{"laligaclubs":"barcelona"}
   - action_stadiuminfo    
* byebye 
   - utter_byebye
   
##
##story_clubandstadiumhistorywithout_apperciaction
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_playerstoclubinfo_history{"players":"messi"}
   - action_playerstoclubinfo
* laliga_clubs_history{"laligaclubs":"barcelona"}
   - action_clubhistory    
* apperciation
   - utter_apperciation
* byebye 
   - utter_byebye

##story20   
* laliga_playerstoclubinfo_history{"laligaclubs":"barcelona","players":"messi","soccerposition":"goalkeeper"}
   - action_playerstoclubinfo
* laliga_clubs_history{"laligaclubs":"barcelona"}
   - action_clubhistory    
* apperciation
   - utter_apperciation
* byebye 
   - utter_byebye

#story 21
* laliga_playerstoclubinfo_history{"laligaclubs":"barcelona","players":"messi","soccerposition":"goalkeeper"}
   - action_playerstoclubinfo  
* apperciation
   - utter_apperciation
* laliga_clubs_history{"laligaclubs":"barcelona"}
   - action_clubhistory
* apperciation
   - utter_apperciation   
* byebye 
   - utter_byebye

#story 22   
* laliga_playerstoclubinfo_history{"laligaclubs":"barcelona","players":"messi","soccerposition":"goalkeeper"}
   - action_playerstoclubinfo  
* apperciation
   - utter_apperciation
* laliga_clubs_history{"laligaclubs":"barcelona"}
   - action_clubhistory
* apperciation
   - utter_apperciation   
* byebye 
   - utter_byebye


#story 23
* laliga_playerstoclubinfo_history{"laligaclubs":"barcelona","players":"messi","soccerposition":"goalkeeper"}
   - action_playerstoclubinfo  
* apperciation
   - utter_apperciation
* laliga_clubs_history{"laligaclubs":"barcelona"}
   - action_clubhistory
* apperciation
   - utter_apperciation   
* byebye 
   - utter_byebye

#story 24   
* laliga_playerstoclubinfo_history{"laligaclubs":"barcelona","players":"messi","soccerposition":"goalkeeper"}
   - action_playerstoclubinfo 
* apperciation
   - utter_apperciation
* laliga_clubs_history{"laligaclubs":"barcelona"}
   - action_clubhistory
* apperciation
   - utter_apperciation   
* byebye 
   - utter_byebye

#story 24 
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet  
* laliga_match_result{"laligaclubs":"barcelona","laligaclubs":"real madrid"}
   - action_gameresult
* apperciation
   - utter_apperciation 
* byebye 
   - utter_byebye      
   
#story 25   
* laliga_match_result{"laligaclubs":"barcelona","laligaclubs":"real madrid"}
   - action_gameresult 
* apperciation
   - utter_apperciation 
* byebye 
   - utter_byebye

#story 26    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_rewardstoplayers{"soccerposition":"goalkeeper","players":"messi"}
   - action_players_prizes   
* laliga_match_result{"laligaclubs":"barcelona","laligaclubs":"real madrid"}
   - action_gameresult
* apperciation
   - utter_apperciation 
* byebye 
   - utter_byebye    

#story 27 
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet  
* laliga_rewardstoplayers{"soccerposition":"goalkeeper","players":"messi"}
   - action_players_prizes
* apperciation
   - utter_apperciation 
* byebye 
   - utter_byebye      
   
#story 28   
* laliga_rewardstoplayers{"soccerposition":"goalkeeper","players":"messi"}
   - action_players_prizes
* apperciation
   - utter_apperciation 
* byebye 
   - utter_byebye

#story 29    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubs_history{"laligaclubs":"barcelona"}
   - action_clubhistory   
* laliga_rewardstoplayers{"soccerposition":"goalkeeper","players":"messi"}
   - action_players_prizes
* apperciation
   - utter_apperciation 
* byebye 
   - utter_byebye



#story 26    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_rewardstoplayers{"soccerposition":"goalkeeper","players":"messi"}
   - action_players_prizes   
* laliga_playerstoclubinfo_history{"laligaclubs":"barcelona","players":"messi","soccerposition":"goalkeeper"}
   - action_playerstoclubinfo
* apperciation
   - utter_apperciation 
* byebye 
   - utter_byebye    

#story 27 
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet  
* laliga_playerstoclubinfo_history{"laligaclubs":"barcelona","players":"messi","soccerposition":"goalkeeper"}
   - action_playerstoclubinfo
* apperciation
   - utter_apperciation 
* byebye 
   - utter_byebye      
   
#story 28   
* laliga_playerstoclubinfo_history{"laligaclubs":"barcelona","players":"messi","soccerposition":"goalkeeper"}
   - action_playerstoclubinfo
* apperciation
   - utter_apperciation 
* byebye 
   - utter_byebye

#story 29    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_playerstoclubinfo_history{"laligaclubs":"barcelona","players":"messi","soccerposition":"goalkeeper"}
   - action_playerstoclubinfo  
* laliga_rewardstoplayers{"soccerposition":"goalkeeper","players":"messi"}
   - action_players_prizes
* apperciation
   - utter_apperciation 
* byebye 
   - utter_byebye


* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* apperciation
   - utter_apperciation  
* byebye 
   - utter_byebye    

##story_greet_with_goal <!--- goal club history -->    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubsstadiuminfo_history{"laligaclubs":barcelona}
   - action_stadiuminfo
* apperciation
   - utter_apperciation   
* byebye 
   - utter_byebye
   
##story_greet_with_goal <!--- goal club history -->    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubsstadiuminfo_history{"laligaclubs":barcelona}
   - action_stadiuminfo
   - utter_affirm_confirm
* affirm
   - utter_greet 
* byebye 
   - utter_byebye
   
##story_greet_with_goal <!--- goal club history -->    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubsstadiuminfo_history{"laligaclubs":barcelona}
   - action_stadiuminfo 
* byebye 
   - utter_byebye

#story 28   
* laliga_clubsstadiuminfo_history{"laligaclubs":barcelona}
   - action_stadiuminfo 
* apperciation
   - utter_apperciation 
* byebye 
   - utter_byebye

#story 29    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubs_history{"laligaclubs":"barcelona"}
   - action_clubhistory
* laliga_clubsstadiuminfo_history{"laligaclubs":barcelona}
   - action_stadiuminfo
* apperciation
   - utter_apperciation 
* byebye 
   - utter_byebye

#story 30    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_clubs_history{"laligaclubs":"barcelona"}
   - action_clubhistory
* laliga_rewardstoplayers{"soccerposition":"goalkeeper","players":"messi"}
   - action_players_prizes
* apperciation
   - utter_apperciation 
* byebye 
   - utter_byebye

#story 29    
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_rewardstoplayers{"soccerposition":"goalkeeper","players":"messi"}
   - action_players_prizes
* apperciation
   - utter_apperciation 
* byebye 
   - utter_byebye

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

* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_match_result{"laligaclubs":"barcelona","laligaclubs":"real madrid"}
   - action_gameresult 
* laliga_clubsstadiuminfo_history{"laligaclubs":barcelona}
   - action_stadiuminfo
* apperciation
   - utter_apperciation
* byebye 
   - utter_byebye  

* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet   
* laliga_match_result{"laligaclubs":"barcelona","laligaclubs":"real madrid"}
   - action_gameresult    
* byebye 
   - utter_byebye

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

* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet
* laliga_match_result{"laligaclubs":"barcelona","laligaclubs":"real madrid"}
   - action_gameresult 
* laliga_clubsstadiuminfo_history{"laligaclubs":barcelona}
   - action_stadiuminfo
* apperciation
   - utter_apperciation
* byebye 
   - utter_byebye  
* greetings
   - utter_name
* providename{"username":"lucy"}
   - utter_greet   
* laliga_match_result{"laligaclubs":"barcelona","laligaclubs":"real madrid"}
   - action_gameresult    
* byebye 
   - utter_byebye    