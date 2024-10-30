import streamlit as st
st.title("verification de mot passe")
password = "jedha4ever"
saisie_utilisateur=st.text_input("veuillez saisir le mdp")
if saisie_utilisateur != password:
    st.write("erreur,mdp incorrecte")
    saisie_utilisateur=st.text_input("veuillez re-saisir le mdp")
else:
    st.write("correct")