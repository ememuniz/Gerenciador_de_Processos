import streamlit as st
import psutil as ps
import numpy as np;
import time

st.set_page_config(page_title="Memory Manager", page_icon="🖥️")
st.markdown("# Memory Manager")

tab1,tab2 = st.tabs(["Stats","stats2"])

with tab1:
    place1=st.empty()
    place2=st.empty()
    place3=st.empty()
with tab2:
    place4=st.empty()
    place5=st.empty()


for x in range(150): 
    memoryStats=ps.virtual_memory()

    place1.markdown(
        f'''
        ### Memória Total:
        ###### Memória Física Total
        ##### {memoryStats.total}
        '''
    )

    place2.markdown(
        f'''
        ### Memória Disponível:
        ###### Memória Disponível para uso, calculado baseado em várias métricas
        ##### {memoryStats.available}
        '''
    )

    place3.markdown(
        f'''
        ### Memória em Uso(%):
        ###### Memória para uso, calculado baseado em várias métricas
        ##### {memoryStats.percent}
        '''
    )

    place4.markdown(
        f'''
        ### Memória Buffer:
        ###### Cache para coisas como metadados do sistema de arquivos
        ##### {memoryStats.buffers}
        '''
    )

    place5.markdown(
        f'''
        ### Memória Cached:
        ###### Cache para varias coisas
        ##### {memoryStats.buffers}
        '''
    )

    #o comando que ativa o venv é 'source .venv/bin/activate' 