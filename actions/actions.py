import json
import logging
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests
from typing import Any, Text, Dict, List, Union
import re

class ActionGetAtendimentos(Action):
    print("============teste da API===========")    

    def name(self) -> Text:
        return "action_get_atendimentos"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        api_url = "http://localhost:8080/bot/getAtendimentos"
        response = requests.get(api_url)
        # Imprimir o conteúdo completo da mensagem do usuário
        print("Conteúdo da mensagem:", tracker.latest_message)
        
        if response.status_code == 200:
            # Extrair os dados da resposta JSON
            atendimentos = response.json()
            
            # Extrair o nome do médico usando a entidade
            entities = tracker.latest_message.get('entities')
            if entities:
                for entity in entities:
                    if entity['entity'] == 'nmMedico':
                        nome_medico = entity['value']
            
                        atendimentos_medico = [atendimento for atendimento in atendimentos if atendimento["nmMedico"] == nome_medico]
                        if atendimentos_medico:
                            numeros_atendimentos = [str(atendimento["nrAtendimento"]) for atendimento in atendimentos_medico]
                            dispatcher.utter_message(f"Atendimentos do Dr. {nome_medico}: {atendimentos_medico}")
                        else:
                            dispatcher.utter_message(f"Atendimentos do Dr. {nome_medico} não encontrados.")
            else:
                dispatcher.utter_message("Por favor, forneça o nome do médico.")
        else:
            # Se houver um erro na solicitação, envie uma mensagem de erro
            dispatcher.utter_message("Ocorreu um erro ao obter os dados da API.")
        
        return []