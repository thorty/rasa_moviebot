# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from pathlib import Path
from typing import Any, Text, Dict, List
import logging

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

from .utils.create_db import read_db

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


class ValidateMoviefilterForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_moviefilter_form"

    movie_df = read_db("actions/data/movies.dat")

    print(movie_df)
