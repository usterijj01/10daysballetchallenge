import streamlit as st
import os
import numpy as np
import pandas as pd
import urllib.request
from PIL import Image
import glob


st.set_page_config(
    page_title = "10DaysOfBalletChallenge",
    page_icon = ":dancers:",
    initial_sidebar_state="expanded",
)


def update_params():
    st.experimental_set_query_params(challenge=st.session_state.day)

md_files = sorted([int(x.strip('Day').strip('.md')) for x in glob.glob1('content',"*.md") ])

# Logo and Navigation
col1, col2, col3 = st.columns((1,4,1))
with col2:
    st.image(Image.open('screenshot.jpg'))

st.markdown('# 10 Days of ballet challenge')

days_list = [f'Day {x}' for x in md_files]

query_params = st.experimental_get_query_params()

if query_params and query_params["day"][0] in days_list:
    st.session_state.day = query_params["day"][0]

selected_day = st.selectbox('Start the Challenge 👇', days_list, key="day", on_change=update_params)

with st.expander("About the #10DaysOfBalletChallenge"):
    st.markdown('''
    The **#10DaysOfBalletChallenge** is a Ballet challenge designed to help you improve your skills in classical ballet technique.

    Particularly, you'll be able to learn with:
    - Tips
    - Exemples
    - Live experience of the real artist
    ''')

# Sidebar
st.sidebar.header('About')
st.sidebar.markdown('''
Welcome to our 10-Days Ballet Challenge! Over the next 10 days, we'll be guiding you through a series of ballet exercises and movements designed to improve your technique, build strength and flexibility, and most importantly, have fun!

Each day of the challenge, we'll be focusing on different aspects of ballet, such as stretching, footwork, or partnering. We'll provide clear instructions and demonstrations for each exercise, as well as tips and modifications for participants of all levels.

To participate in the challenge, all you need to do is follow our Instagram account and use the challenge hashtag when posting your progress. We encourage you to share your experience and progress with your followers, friends, and family.

We'll be offering prizes for those who complete the challenge or share their progress throughout the challenge. The prizes could include a free ballet class, a ballet-related item, or a discount on our company's products or services.

We've also invited popular ballet dancers and fitness influencers to participate in the challenge and share their experience with their followers.

We're excited to have you join us on this journey!

Let's get started!

*Available only for Android and Desktop.

#10DayBalletChallenge
#BalletFitness
#StrongFoundation
''')
st.sidebar.header('Who we are')
st.sidebar.image(Image.open('screenshot.jpg'))
st.sidebar.markdown('Exercice master')
st.sidebar.image(Image.open('screenshot.jpg'))
st.sidebar.markdown('Developer')
st.sidebar.image(Image.open('screenshot.jpg'))
st.sidebar.markdown('Model/Artist')

#audio_file = open('content/audiog/01-faixa-1.ogg','rb') #enter the filename with filepath

#audio_bytes = audio_file.read() #reading the file

#st.audio(audio_bytes, format='audio/ogg') #displaying the audio


# Display content
for i in days_list:
    if selected_day == i:
        st.markdown(f'# {i}')
        j = i.replace(' ', '')
        with open(f'content/{j}.md', 'r') as f:
            st.markdown(f.read())
        if os.path.isfile(f'content/figures/{j}.csv') == True:
            st.markdown('---')
            st.markdown('### Music')
            df = pd.read_csv(f'content/figures/{j}.csv', engine='python')
            for i in range(len(df)):
                st.audio(f'content/audiog/{df.audio[i]}')
                st.info(f'{df.figure[i]}: {df.caption[i]}')
