from rasa_core_sdk import Action

import pandas as pd
import requests

scores_data = pd.read_csv("data/EPL_Set.csv")

class WinsAction(Action):
    def name(self):
        return "action_get_results"

    def run(self, dispatcher, tracker, domain):
        team = tracker.get_slot('team')
        season = tracker.get_slot('season').replace(' ', '')

        results_season = scores_data[scores_data.Season == season]
        home_wins = len(results_season[(results_season.HomeTeam == team) & (results_season.FTR == 'H')])
        away_wins = len(results_season[(results_season.AwayTeam == team) & (results_season.FTR == 'A')])
        dispatcher.utter_message("{} won {} games in the {} season".format(team, home_wins + away_wins, season))

class PresenceAction(Action):
    def name(self):
        return "action_check_presence"
    
    def run(self, dispatcher, tracker, domain):
        team = tracker.get_slot('team')

        presence = len(scores_data[scores_data.HomeTeam == team]) > 0

        if presence is True:
            dispatcher.utter_message("{} have played in the Premier League!".format(team))
        else:
            dispatcher.utter_message("{} have not played in the Premier League!".format(team))