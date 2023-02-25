import streamlit as st
import os
import numpy as np
import pandas as pd
import urllib.request
from PIL import Image
import glob


st.set_page_config(
    page_title = "10DaysBalletChallenge",
    page_icon = ":dancers:",
    initial_sidebar_state="expanded",
)

def enable_indexability():
    st.write("<meta name='robots' content='index,follow'>", unsafe_allow_html=True)
    st.write("<meta name='googlebot' content='index,follow'>", unsafe_allow_html=True)

if __name__ == '__main__':
    enable_indexability()
    # Add the rest of your Streamlit app code below

st.markdown('<h1 style="margin-bottom:0rem;margin-top:-4rem;text-align: center">10DaysBalletChallenge</h1>', unsafe_allow_html=True)
st.markdown('<h5 style="color:grey;margin-bottom:0rem;margin-top:-1rem;text-align: center">10 Days Ballet Challenge for all</h5>', unsafe_allow_html=True)




def update_params():
    st.experimental_set_query_params(challenge=st.session_state.day)

md_files = sorted([int(x.strip('Day').strip('.md')) for x in glob.glob1('content',"*.md") ])

# Logo and Navigation
col1, col2, col3 = st.columns((1,4,1))
with col2:
    st.image(Image.open('DALLE.png'))

#st.markdown('# 10 Days of ballet challenge')

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
Welcome to our 10-Days Ballet Challenge! Over the next 10 days, we'll be guiding you through a series of ballet exercises and movements designed to improve your technique, build strength and flexibility, and most importantly, have fun!

Each day of the challenge, we'll be focusing on different aspects of ballet, such as stretching, footwork, or partnering. We'll provide clear instructions and demonstrations for each exercise, as well as tips and modifications for participants of all levels.

To participate in the challenge, all you need to do is follow our Instagram account and use the challenge hashtag when posting your progress. We encourage you to share your experience and progress with your followers, friends, and family.

We'll be offering prizes for those who complete the challenge or share their progress throughout the challenge. The prizes could include a free ballet class, a ballet-related item, or a discount on our company's products or services.

We've also invited popular ballet dancers and fitness influencers to participate in the challenge and share their experience with their followers.

We're excited to have you join us on this journey!

Let's get started!

*Available only for Android and Desktop.

#10DayBalletChallenge
@10DayBalletChallenge
''')


video_file = open('video1.mp4', 'rb')
video_bytes = video_file.read()

st.sidebar.video(video_bytes)



st.sidebar.header('Who we are')

st.sidebar.image(Image.open('photo1.jpeg'))
st.sidebar.markdown('Ivan Ustyuzhaninov')
st.sidebar.markdown('Choreographer/Developer')
st.sidebar.markdown('''
Graduated from the Moscow Bolshoi Ballet Academy and has since become a professional dancer and a professor of choreography with over 10 years of experience. The Bolshoi Ballet Academy is a prestigious institution for classical ballet training, has a strong foundation in classical ballet technique.
As a dancer, performed on stages around the world, showcasing their skills and talent in front of audiences. Have worked with different choreographers and dance companies, gaining valuable experience and insights into different styles and approaches to dance.
As a professor of choreography, has likely taught students of different ages and backgrounds in various countries. Their teaching style and approach may be informed by their experiences as a performer and their training at the Bolshoi Ballet Academy, emphasizing the importance of technical precision and discipline in dance.
Overall, biography suggests that they are a highly skilled and experienced dancer and educator with a passion for sharing their knowledge and love of dance with others. Their training at the Bolshoi Ballet Academy and their years of experience performing and teaching have likely given them a unique perspective on the art of dance.
''')


st.sidebar.image(Image.open('photo2.jpeg'))
st.sidebar.markdown('Aleksandr Filimontsev')
st.sidebar.markdown('Model/Artist')
st.sidebar.markdown('''
Graduated from the prestigious Moscow Bolshoi Ballet Academy, indicating that they have received extensive training in classical ballet. With this training, they have likely developed a deep understanding of technique, artistry, and performance, which they can bring to their work as a dancer.
The individual has also worked in the children's theater Natalia Sats, suggesting that they have experience performing for younger audiences and may have developed skills in engaging and entertaining children through dance.
Furthermore, the individual has participated in many competitions in classical ballet, indicating that they have sought to further their skills and gain recognition in the dance world. This suggests that they are ambitious and dedicated to their craft, and that they have likely had the opportunity to perform in a variety of contexts and settings.
Overall, this biography suggests that the individual is a skilled and accomplished dancer with a strong foundation in classical ballet. They have experience working with children and have sought to improve their skills through competition, indicating that they are dedicated and passionate about their work.
''')


# Define the HTML code for the Buy Me a Coffee button
buy_me_coffee = """
<a href="https://www.buymeacoffee.com/ustyuzhaniX" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 50px; width: 150px;" >
</a>
"""

# Display the Buy Me a Coffee button using the HTML component
st.sidebar.markdown(buy_me_coffee, unsafe_allow_html=True)







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
