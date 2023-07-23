# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from pathlib import Path
from typing import Any, Text, Dict, List
import logging
import random

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

from .utils.read_db import search_genre, search_year

logger = logging.getLogger(__name__)


class ActionCheckExistence(Action):
    def name(self) -> Text:
        return "action_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        logger.debug("action_fallback triggerd")
        dispatcher.utter_message(response="utter_restart_with_button")
        return []

class ActionSearchGenre(Action):
    def name(self) -> Text:
        return "action_search_genre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        logger.info("I'm here")
        try:
            logger.info("I'm also here")
            logger.info(tracker)
            logger.info(tracker.latest_message)
            for blob in tracker.latest_message['entities']:
                logger.info(blob)
                if blob['entity'] == 'genre':
                    genre = blob['value']
                    genreList = search_genre(genre)
                    logger.info(len(genreList))
                    
                    dispatcher.utter_message(text=f"Ich habe {len(genreList)} Filme, gefunden, ich schlage dir einen zufälligen aus der Liste vor:")
                    randomMovie = random.choice(genreList)
                    dispatcher.utter_message(text=f"{randomMovie[1]}, herausgekommen im Jahr {randomMovie[2]}.")
        except Exception as e:
            logger.error(e)
        else:
            return []
