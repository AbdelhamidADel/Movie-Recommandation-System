import streamlit as st
import pickle
from pandas import DataFrame
import requests
import base64

def fectch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f0d2435c75b4b0663a372fccaf03b4a8&language=en-US")
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in movie_list:
        movie_id = movies_list.iloc[i[0]].id
        recommended_movie_names.append(movies_list.iloc[i[0]
        ].title)
        recommended_movie_posters.append(fectch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters
file = open("Movies.pkl",'rb')
movies_list = pickle.load(file)

file2=open('Movie_Recommendation.pkl', 'rb')
world_data = ast.literal_eval(file2.read())
similarity = similarity(world_data)

movies_list = DataFrame(movies_list)
#----------------------------------------------------------------
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('Cover_Project.jfif')
#------------------------------------------------------------------ 
st.title("Movie Recommandation System")
option = st.selectbox("Select Movie Name", movies_list['title'].values)
 

if st.button("Recommend"):
    names, posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

