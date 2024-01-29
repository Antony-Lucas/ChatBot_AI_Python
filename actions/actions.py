import json
import logging
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests
from typing import Any, Text, Dict, List, Union

class ActionGetAtendimentos(Action):
    print("============teste da API===========")    

    def name(self) -> Text:
        return "action_get_atendimentos"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
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

        intent = tracker.latest._message['intent']['name']

        if intent == 'informacoes_atendimento':
            # Lógica para extrair informações do atendimento com base nos parâmetros fornecidos
            nr_atendimento = tracker.latest_message['entities'][0]['value']
            info_atendimento = next((atendimento for atendimento in atendimentos if atendimento["nrAtendimento"] == nr_atendimento), None)

            if info_atendimento:
                # Se encontrou o atendimento, envie as informações para o usuário
                dispatcher.utter_message(f"Informações do atendimento {nr_atendimento}: {info_atendimento}")
            else:
                # Se não encontrou o atendimento, informe ao usuário
                dispatcher.utter_message(f"Atendimento {nr_atendimento} não encontrado.")

        elif intent == 'quantidade_atendimentos':
            # Lógica para calcular a quantidade de atendimentos e enviar ao usuário
            quantidade_atendimentos = len(atendimentos)
            dispatcher.utter_message(f"Total de atendimentos: {quantidade_atendimentos}")

        elif intent == 'medico_atendimentos':
            # Lógica para extrair informações do médico e enviar ao usuário
            nome_medico = tracker.latest_message['entities'][0]['value']
            atendimentos_medico = [atendimento for atendimento in atendimentos if atendimento["nmMedico"] == nome_medico]

            if atendimentos_medico:
                # Se encontrou atendimentos do médico, envie as informações para o usuário
                dispatcher.utter_message(f"Atendimentos do Dr. {nome_medico}: {atendimentos_medico}")
            else:
                # Se não encontrou atendimentos do médico, informe ao usuário
                dispatcher.utter_message(f"Atendimentos do Dr. {nome_medico} não encontrados.")

        return []