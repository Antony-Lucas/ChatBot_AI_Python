import json
import logging
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests
from typing import Any, Text, Dict, List, Union

class ActionGetAtendimentos(Action):
    logging.debug(f"==========================================================Resposta da API")
    print("============teste===========")
    def name(self):
        return "action_get_atendimentos"
    
    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        atendimentos = [
            {"nrAtendimento":13919,"nmMedico":"Williams Fernandes Barra","dtEntrada":"2023-11-29","dsConvenio":"Unimed Belém"},
            {"nrAtendimento":13921,"nmMedico":"Williams Fernandes Barra","dtEntrada":"2023-11-29","dsConvenio":"Unimed Belém"},
            {"nrAtendimento":13923,"nmMedico":"Sâmio Pimentel Ferreira","dtEntrada":"2023-11-29","dsConvenio":"Unimed Belém"},
            {"nrAtendimento":13926,"nmMedico":"Sâmio Pimentel Ferreira","dtEntrada":"2023-11-29","dsConvenio":"Aeronáutica"},
            {"nrAtendimento":13927,"nmMedico":"Sâmio Pimentel Ferreira","dtEntrada":"2023-11-29","dsConvenio":"CASSI"},
            {"nrAtendimento":13928,"nmMedico":"LORENA CUNHA CASTRO PATRIOTA","dtEntrada":"2023-11-29","dsConvenio":"Bradesco"},
            {"nrAtendimento":13930,"nmMedico":"Manuel Caitano Dias Ferreira Maia","dtEntrada":"2023-11-29","dsConvenio":"Unimed Belém"},
            {"nrAtendimento":13929,"nmMedico":"LORENA CUNHA CASTRO PATRIOTA","dtEntrada":"2023-11-29","dsConvenio":"Bradesco"}
        ]

        response = "aqui estão alguns atendimentos: \n"
        for atendimento in atendimentos:
            response += f"Nr. Atendimento: {atendimento['nrAtendimento']}, Médico: {atendimento['nmMedico']}, Data: {atendimento['dtEntrada']}, Convênio: {atendimento['dsConvenio']}\n"
            dispatcher.utter_message

        return[]