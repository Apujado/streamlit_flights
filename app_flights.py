import pandas as pd
df_flights = pd.read_csv("C:/Users/pujad/OneDrive - APS Consult/Documents/FORMATION/Wild Code School/streamlit_flights/streamlit_flights/flights.csv", sep=',')
df_flights.head()

import streamlit as st
st.title("Flights Data Analysis")
st.write("Ceci est une petite app pour manipuler les données et créer des graphiques.")

st.selectbox("Sélectionne le dataset", ["flights"])

st.write(pd.DataFrame(df_flights))

st.write("Choisissez la colonne X")
x_col = st.selectbox("Selectionne la colonne X", df_flights.columns)

y_col = st.selectbox("Selectionne la colonne Y", df_flights.columns)

graph_type = st.selectbox("Quel graphique veux-tu utiliser? ", ["scatter_chart","line_chart","bar_chart"])

import matplotlib.pyplot as plt
def plot_graph(x, y, graph_type):
    plt.figure(figsize=(10, 5))
    if graph_type == "scatter_chart":
        plt.scatter(x, y)
    elif graph_type == "line_chart":
        plt.plot(x, y)
    elif graph_type == "bar_chart":
        plt.bar(x, y)
    else:
        st.write("Graphique non reconnu")
    
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Graphique des données de vol")
    st.pyplot(plt)

plot_graph(df_flights[x_col], df_flights[y_col], graph_type)

import seaborn as sns
corr_matrix = df_flights.select_dtypes(include=['number']).corr()
show_corr = st.checkbox("Afficher la matrice de corrélation", value = False)
if show_corr:
    st.write("Ma matrice de corrélation:")
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap="rocket", ax=ax)
    st.pyplot(fig)

