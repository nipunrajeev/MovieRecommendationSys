
import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    index = movies_list[movies_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for j in distances[1:6]:
        recommended_movies.append(movies_list.iloc[j[0]].title)
    return recommended_movies

similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_list = pickle.load(open('movie_dict.pkl', 'rb'))
movies_list = pd.DataFrame(movies_list)

st.title('Which Movie Next ?')
selected_movie = st.selectbox(
    "Which movie would you like to watch?",
    movies_list['title'].values,
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)
