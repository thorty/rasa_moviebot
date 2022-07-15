# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from pathlib import Path
from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


# class ActionCheckExistence(Action):
#     knowledge = Path("data/pokemons.txt").read_text().split("\n")

#     def name(self) -> Text:
#         return "action_check_existence"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         for blob in tracker.latest_message['entities']:
#             print(tracker.latest_message)
#             if blob['entity'] == 'pokemon_name':
#                 name = blob['value'].lower()
#                 if name in self.knowledge:
#                     dispatcher.utter_message(text=f"Japp, {name} ist ein pokemon.")
#                 else:
#                     dispatcher.utter_message(
#                         text=f"Ich kenne keinen {name}, entweder der ist neu oder es gibt ihn nicht!")
#         return []
