import streamlit as st

st.set_page_config(
    page_title="SGP",
    page_icon="⌨︎",
)

st.sidebar.success("Gerenciadores")
st.title("Sistema Gerenciador de Processos")
st.write("Bem vindo ao SGP, você é capaz de monitorar os processos de seu computador através deste sistema")
st.markdown(
    """
    ---
### Clique no menu lateral para selecionar o tipo de processo que você quer verificar

---

"""
)