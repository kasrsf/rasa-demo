from rasa_core_sdk import Action

class SampleAction(Action):
    def name(self):
        return "action_sample_action"

    def run(self, dispatcher, tracker, domain):
        slot = tracker.get_slot('slot')
        
        dispatcher.utter_message("slot value = {}".format(slot))