from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
    ISO_639 = 'en_core_web_sm'
    ENGLISH_NAME = 'Portuguese'


chatbot = ChatBot("BotNico", tagger_language=ENGSM)

conversa = [
    "Coe",
    "Eai, tranquilo",
    "Tranquilo",
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)
chatbot.get_response("Coe")
print(chatbot.get_response())