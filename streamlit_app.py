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

if query_params and query_params["challenge"][0] in days_list:
    st.session_state.day = query_params["challenge"][0]

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
Classical ballet is a form of dance that originated in the courts of Renaissance Italy and was later developed further in France and Russia. It is a highly stylized and technical form of dance that often tells a story through movement, music, and stage design.

Classical ballet is characterized by a set of specific techniques and movements, such as pointe work (dancing on the tips of the toes), turns, leaps, and graceful arm movements. The choreography in classical ballet is typically designed to showcase the dancers' technical skills and their ability to convey emotions and tell a story through movement.

Famous classical ballets include "Swan Lake," "The Nutcracker," "Giselle," and "The Sleeping Beauty." Classical ballet is still widely performed today and is considered an important part of the history of dance.


''')

# Display content
for i in days_list:
    if selected_day == i:
        st.markdown(f'# {i}')
        j = i.replace(' ', '')
        with open(f'content/{j}.md', 'r') as f:
            st.markdown(f.read())
        #if os.path.isfile(f'content/figures/{j}.csv') == True:
        #    st.markdown('---')
        #    st.markdown('### Figures')
        #    df = pd.read_csv(f'content/figures/{j}.csv', engine='python')
        #    for i in range(len(df)):
        #        st.image(f'content/images/{df.img[i]}')
        #        st.info(f'{df.figure[i]}: {df.caption[i]}')
