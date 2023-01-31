import matplotlib as plt
import streamlit as st
import random
from datetime import datetime
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import streamlit as st
from streamlit_option_menu import option_menu
import spacy
from collections import Counter
import glob
import json
import en_core_web_sm
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


image=[ {"name": "2.png", "likes": 0},{"name": "3.png", "likes": 0},{"name": "Sonia Monteiro Imobiliary.png", "likes": 0},{"name": "star.png", "likes": 0}]

# Create an empty dictionary to store the number of likes per day of the week
likes_per_day = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
days_of_week = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

days_of_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

# Create a list to store the likes per day of the week
likes_per_day = [0, 0, 0, 0, 0, 0, 0]

# Create a list to store the date of the like
date_likes = []

now=[]
# Create a function to display the histogram of likes per day of the week
st.title("                        O MEU PORTFOLIO")

def main():
    st.set_page_config(page_title="O MEU PORTEFOLIO", page_icon=":guardsman:", layout="centered")


    # 1. as sidebar menu
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", 'Settings'],
                               icons=['house', 'gear'], menu_icon="cast", default_index=1)


    # 2. horizontal menu
    selected2 = option_menu(None, ["Home", "ART", "Design", 'Video', "3D", "IoT", "Gallery"],
                            icons=['house', 'cloud-upload', "list-task", 'gear'],
                            menu_icon="cast", default_index=0, orientation="horizontal")


    # 3. CSS style definitions
    selected3 = option_menu(None, ["Home", "ART", "Design", 'Video' "3D", "IoT", "Gallery"],
                            icons=['house', 'cloud-upload', "list-task", 'gear'],
                            menu_icon="cast", default_index=0, orientation="horizontal",
                            styles={
                                "container": {"padding": "0!important", "background-color": "#fafafa"},
                                "icon": {"color": "orange", "font-size": "25px"},
                                "nav-link": {"font-size": "25px", "text-align": "left", "margin": "0px",
                                             "--hover-color": "#eee"},
                                "nav-link-selected": {"background-color": "green"}})
    # Create the responsive menu
    menu = ["Home", "About Me", "Art", "Design", "Video", "3D", "IoT", "Graphics"]
    choice = st.markdown("Select a page", menu)
    st.markdown("""
    <style>
    .menu-item {
        padding: 10px;
        font-size: 20px;
        color: green;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

    # you can add more elif for the other options
    # for each option you can show the gallery and the chatbot or the graph histogram


    # Show the appropriate page based on the user's menu choice
    if choice == "Home":
        st.title("Welcome to my Web App!")

    elif choice == "About Me":
        st.title("Sobre Mim")
        st.write("My name is Paulo  Monteiro and I am a web developer.")

    elif choice == "Art":
        st.title("Art Gallery")
        # create the gallery with 8 images and a like counter with 5 stars
        for i in range(1):
            # code to display the image
            st.image("image" + str(i) + "3.png", caption='Art ' + str(i), use_column_width=True)
            # create a star rating
            star_rating = st.rating(label='picture nice???', min_value=0, max_value=5, step=1)
            # count likes
            likes_per_day[i] = star_rating
        st.write("Likes per day of the week")


        # Add the other pages
    elif choice == "Design":
        st.title("Design Gallery")
        # create the gallery with 8 images and a like counter with 5 stars
        for i in range(1):
            # code to display the image
            st.image("image" + str(i) + "Sonia Monteiro Imobiliary.png", caption='Design ' + str(i),
                     use_column_width=True)
            # create a star rating
            star_rating = st.rating(label='star.png', min_value=0, )

    elif choice == "IoT":
        st.title("IoT Gallery")
        # create the gallery with 8 images and a like counter with 5 stars
        for i in range(1):
            # code to display the image
            st.image("image" + str(i) + "2.png", caption='IoT ' + str(i), use_column_width=True)
            # create a star rating
            star_rating = st.rating(label='star.png', min_value=0, )

#nlp = spacy.load("en_core_web_sm")
#chatbot = ChatBot("chatbot Paulo")

#trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train("chatterbot.corpus.english.greetings",
              #"chatterbot.corpus.english.conversations")

#if st.button("Talk to Chatbot"):
    #st.write("Chatbot: ", nlp.get_response(st.text_input("Paulo: ")))

def display_menu():
    menu = ["Home", "About", "Art", "Design", "Video", "3D", "IoT", "Graphics"]
    choice = st.selectbox("Select an option", menu)
    if choice == "Home":
        st.title("Welcome to My Gallery")
        st.write("This is a sample application to showcase a gallery of images and a chart of likes per day of the week.")
    elif choice == "About":
        st.title("About Me")
        st.write("My name is Paulo and I Like to Develop Web Apllications.")
    elif choice == "Art":
        display_images("Art")
    elif choice == "Design":
        display_images("Design")
    elif choice == "Video":
        display_images("Video")
    elif choice == "3D":
        display_images("3D")
    elif choice == "IoT":
        display_images("IoT")
    elif choice == "Graphics":
        display_images("Graphics")
display_menu()

# Create a function to display the images
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Video")
   st.image ("/Users/paulomonteiro/PycharmProjects/Portefolio2/3.png")
   button_1 = st.button("Gosto", key="abnormal")
with col2:
   st.header("Design")
   st.image("/Users/paulomonteiro/PycharmProjects/Portefolio2/2.png")

   button_2 = st.button("Gosto", key="cool")
with col3:
   st.header("ART")
   st.image("/Users/paulomonteiro/PycharmProjects/Portefolio2/2.png")
   button_3 = st.button("Gosto", key="psy ")


# Allow only .csv and .xlsx files to be uploaded
#uploaded_file = st.bar_chart("Topicosbwem.csv", type=["csv", "xlsx"])

# Check if file was uploaded
#if uploaded_file:
    # Check MIME type of the uploaded file
   # if uploaded_file.type == "text/csv":
     #   df = pd.read_csv(uploaded_file)
   # else:

      # df = pd.read_excel(uploaded_file)



chart_data= pd.read_csv('/Users/paulomonteiro/PycharmProjects/Portefolio2/Topicosbem.csv', sep=',')
# Work with the dataframe
st.dataframe(chart_data.head(15))
columns=(['Length','Height','Width','Frequency','Word',])

chart_data = pd.DataFrame(
    np.random.randn(20, 5),
    columns=['Length','Height','Width','Frequency','Word'])
st.bar_chart(chart_data)

chart_data = pd.DataFrame(
    np.random.randn(20, 5),
    columns=['Length','Height','Width','Frequency','Word'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='Length', y='Frequency', size='Height', color='Word', tooltip=['Length','Height','Width','Frequency','Word'])

st.altair_chart(c, use_container_width=True)





def display_images(category):
    st.title(category)
    for i in range(3):
        st.image(random.choice(["/Users/paulomonteiro/PycharmProjects/Portefolio2/star.png", "/Users/paulomonteiro/PycharmProjects/Portefolio2/3.png", "/Users/paulomonteiro/PycharmProjects/Portefolio2/2.png", "/Users/paulomonteiro/PycharmProjects/Portefolio2/Sonia Monteiro Imobiliary.png"]), caption=image[i], width=450,)
        st.write("Likes: ", image[i]["likes"])
        st.write("")
        if button_1==st.button('Gosto', key='abnormal' ):
                image[i]["likes"] += 1
                now = datetime.now()
                date_likes.append(now.weekday())
        if button_2==st.button("Gosto", key='cool'):
                image[i]["likes"] += 1
                now = datetime.now()
                date_likes.append(now.weekday())
        if button_3==st.button("Gosto", key='psy'):
                image[i]["likes"] += 1
                now = datetime.now()
                date_likes.append(now.weekday())

display_images("Design")


def display_histogram():
    # Count the number of likes per day of the week
    for date in date_likes:
        day_of_week = date.weekday()
        likes_per_day[day_of_week] += 1
    # Display the histogram
    plt.bar(list(days_of_week.values()), likes_per_day)
    plt.title("Likes per Day of the Week")
    plt.xlabel("Day of the Week")
    plt.ylabel("Number of Likes")
st.pyplot()
st.bar_chart()


