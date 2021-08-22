from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from flask import Flask, render_template, request, jsonify
from api_call import getUserData,get_credits,get_class_history,getCredit
from py_linq import Enumerable


def getresult(strg):
   
    bot = ChatBot('assistant',
            logic_adapters=[
            {
                'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                'input_text': 'Help me!',
                'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
            },
            {
            'import_path': 'customadapter.CreditLogicAdapter'
            },
            {
            'import_path': 'customadapter.ClassHistoryLogicAdapter'
            },
            {
            'import_path': 'chatterbot.logic.BestMatch',
            "statement_comparison_function": "chatterbot.comparisons.jaccard_similarity",
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
            }
           
        ],
            read_only = True,
            preprocessors=['chatterbot.preprocessors.clean_whitespace',
                        'chatterbot.preprocessors.unescape_html',
                        'chatterbot.preprocessors.convert_to_ascii']
                        )
    trainer = ListTrainer(bot)
    trainer.train("chatterbot.corpus.english.greetings")
    response = bot.get_response(strg)
    
    return str(response)
    
