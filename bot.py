import requests
import json
import teste

class Telegram_Bot:

    def __init__(self):
<<<<<<< HEAD
        token = '5403052208:AAHaGaU9dQhyAuhHgcSMnBDCOcpADuZIqTM'
=======
        token = ''
>>>>>>> f0c5f5b87e47c2fc51197faa3f2e1e1090aa68d9
        self.url_base = f'https://api.telegram.org/bot{token}/'
        self.chatter = teste.Chatter()
        self.chatter.massive_train()

    def Start(self):
        update_id = None
        while True:
            atualizacao = self.get_new_messages(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"].lower())
                    ##usuario = str(dado["message"]["from"]["username"])
                    chat_id = dado["message"]["from"]["id"]
                    firstmessage = int(
                        dado["message"]["message_id"]) == 1
                    response = self.create_response(
                        mensagem, firstmessage)
                    self.responder(response, chat_id)

    # Get messages
    def get_new_messages(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Create response
    def create_response(self, mensagem, firstmessage):
        message = None
        
        if firstmessage == True or mensagem in ('/start', '/menu'):
            message = f'''        
            vai a merda'''

        else:
            message = self.chatter.get_response(mensagem)

        return message

    # Send response
    def responder(self, response, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={response}'
        requests.get(link_requisicao)

if __name__ == '__main__':
    a = Telegram_Bot()
    a.Start()
