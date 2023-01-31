import streamlit as st
from chatterbot import ChatBot
import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

nlp = spacy.load("en_core_web_sm")
chatbot = ChatBot("Streamlit Bot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")

if st.button("Talk to Chatbot"):
    st.write("Chatbot: ", chatbot.get_response(st.text_input("You: ")))