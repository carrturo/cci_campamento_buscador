# Import libraries
import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Campamento Juvenil CCI 2023", page_icon="🐍", layout="wide")
st.title("Campamento Juvenil CCI 2023")

# Connect to the Google Sheet
sheet_id = "1sJhbWrXLmZ1pLoPHi4Pl3W3wQSLxZGXhy-hL_kXoUY4"
sheet_name = "Respuestas"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url, dtype=str).fillna("")

# https://docs.google.com/spreadsheets/d/1sJhbWrXLmZ1pLoPHi4Pl3W3wQSLxZGXhy-hL_kXoUY4/edit?usp=sharing

# Use a text_input to get the keywords to filter the dataframe
text_search = st.text_input("Search", value="")
text_search = text_search.upper()

# Filter the dataframe using masks
m1 = df["Nombre Completo - Registro"].str.contains(text_search)
m2 = df["Identidad - Registro"].str.contains(text_search)
m3 = df["Nombre Completo - Abono"].str.contains(text_search)
m4 = df["Identidad - Abono"].str.contains(text_search)
df_search = df[m1 | m2 | m3 | m4]

# Another way to show the filtered results
# Show the cards
N_cards_per_row = 3
if text_search:
    for n_row, row in df_search.reset_index().iterrows():
        i = n_row%N_cards_per_row
        if i==0:
            st.write("---")
            cols = st.columns(N_cards_per_row, gap="large")
        # draw the card
        with cols[n_row%N_cards_per_row]:
            if len(f"{row['Nombre Completo - Registro'].strip()}") != 0 :
                st.caption(f"Registro")
                st.markdown(f"**{row['Nombre Completo - Registro'].strip()}**")
                st.markdown(f"*{row['Identidad - Registro'].strip()}*")
                st.markdown(f"**{row['Fecha de Pago - Registro']}**")
                st.markdown(f"**{row['Metodo de Pago - Registro']}**")
                st.markdown("Lps. " + f"**{row['¿De cuanto es el abono inicial?']}**")
                st.markdown(f"**{row['Número de Recibo de Pago - Registro']}**")
            if len(f"{row['Nombre Completo - Abono'].strip()}") != 0 :
                st.caption(f"Abono")
                st.markdown(f"**{row['Nombre Completo - Abono'].strip()}**")
                st.markdown(f"*{row['Identidad - Abono'].strip()}*")
                st.markdown(f"**{row['Fecha de Pago - Abono']}**")
                st.markdown(f"**{row['Metodo de Pago - Abono']}**")
                st.markdown("Lps. " + f"**{row['¿De cuanto es el abono? - Abono']}**")
                st.markdown(f"**{row['Número de Recibo de Pago - Abono']}**")