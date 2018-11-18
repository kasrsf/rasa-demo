## Greet
* greet 
    - utter_greet

## Thanks
* thanks
    - utter_np

## Goodbye
* goodbye
    - utter_goodbye

## Path 1
* greet
    - utter_greet
* results_query
    - utter_what_team
* inform{"team":"arsenal"}
    - utter_what_season
* inform{"season":"1996-97"}
    - action_get_results
* thanks
    - utter_np
* goodbye
    - utter_goodbye

## Path 2 
* results_query{"team": "tottenham"}
    - utter_what_season
* inform{"season":"2005-06"}
    - action_get_results
* thanks
    - utter_np

## Path 3
* presence_check{"team": "watford"}
    - action_check_presence
* thanks
    - utter_np

## Path 4
* results_query{"team": "manchester utd", "season": "1997-98"}
    - action_get_results
* thanks
    - utter_np