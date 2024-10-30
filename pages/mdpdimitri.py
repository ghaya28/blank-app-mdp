import streamlit as st

# Titre de l'application
st.title("Vérification de mot de passe")

# Champ de saisie pour le mot de passe
saisie_utilisateur = st.text_input("Entrez le mot de passe :", type="password")

# Vérification du mot de passe
if saisie_utilisateur:
    if saisie_utilisateur == 'jedha4ever':
        st.success("Vous avez le bon mot de passe !")
    else:
        st.error("Mot de passe incorrect. Essayez à nouveau.")