# Import libraries
import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Cena de Gala Conmemorativa 25 Aniversario", page_icon="🐍", layout="wide")
st.title("CCI Cena de Gala Conmemorativa 25 Aniversario")

# Connect to the Google Sheet
sheet_id = "1syDzr3Xly7fl2XdzO3J38uZc8fgd_wi8-wOjp4a9Re0"
sheet_name = "Respuestas"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url, dtype=str).fillna("")

# https://docs.google.com/spreadsheets/d/1syDzr3Xly7fl2XdzO3J38uZc8fgd_wi8-wOjp4a9Re0/edit?usp=sharing

# Use a text_input to get the keywords to filter the dataframe
text_search = st.text_input("Search", value="")
text_search = text_search.upper()

# Filter the dataframe using masks
m1 = df["Nombre Completo"].str.contains(text_search)
m2 = df["Identidad"].str.contains(text_search)
m3 = df["Número de Teléfono"].str.contains(text_search)
df_search = df[m1 | m2 | m3]

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
                st.caption(f"Abono")
                st.markdown(f"**{row['Nombre Completo'].strip()}**")
                st.markdown(f"*{row['Identidad'].strip()}*")
                st.markdown(f"*{row['Número de Teléfono'].strip()}*")
                st.markdown(f"**{row['Metodo de Pago']}**")
                st.markdown("Lps. " + f"**{row['Monto']}**")