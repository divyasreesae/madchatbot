from chatterbot.logic import LogicAdapter
from api_call import getUserData,get_credits,get_class_history,getCredit
class CreditLogicAdapter(LogicAdapter):
    rstatement = ""
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['credit']
        if all(x in statement.text.split() for x in words):
            self.rstatement = statement
            return True
        else:
            return False

    

    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        import requests
        from api_call import getUserData,get_credits,get_class_history,getCredit
        temperature=""
        print(self.rstatement)
        temperature= getCredit(self.rstatement)
        try:
           
            confidence = 1
        except:
            confidence = 0
        response = Statement(text='Credit {}'.format(temperature))
        response.confidence = confidence
        return response
    


class ClassHistoryLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['class history']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False
    eclass = ""
    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        import requests 
        temperature = ""
        try:
           temperature= getClassesHistory(input_statement)
           confidence = 1
        except:
            confidence = 0
        response_statement = Statement(text ='Class History {}'.format(temperature))
        return confidence, response_statement
    
    def getClassesHistory(strg):
        data = getUserData()['users']
        user =Enumerable(data).where(lambda i:i['name'].find(strg.split()[0],0,len(i['name']))>0).first()
        print(user['id'])
        nclasshistory = get_class_history(user['id'])
        return nclasshistory