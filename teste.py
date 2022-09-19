from tkinter.filedialog import Open
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download


conversa = []

class ENGSM():
    ISO_639 = 'en_core_web_sm'
    ENGLISH_NAME = 'Portuguese'
        
class Chatter():

    def __init__(self) -> None:
        ENGSM()
        self.chatbot = ChatBot("BotNico", tagger_language=ENGSM)
        self.trainer = ListTrainer(self.chatbot)

    def get_response(self, mensagem) -> str:
        self.populate_conversa(mensagem)
        self.train()
        message = self.chatbot.get_response(mensagem)
        return message

 
    def populate_conversa(self, message) -> None:
        if message in conversa:
            return print('Já tem, meu nobre')
        else:
            conversa.append(message)
            print(f'Nova conversa inserida: {message}')

        with open('conversa.txt', 'w') as f:
            for i in conversa:
                f.writelines(i + '\n')

        print(f'Histórico de conversa recuperado, total: {len(conversa)}' )

    def train(self):
        self.trainer.train(conversa)
        
    def massive_train(self):
        carga = []
        with open('carga_pesada.txt', 'r') as f:
            aux = f.readlines()
            for i in aux:
                print(i)
                carga.append(i)
        for i in carga:
            print(i)
            self.chatbot.get_response(i)