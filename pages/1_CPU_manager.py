import streamlit as st
import psutil as ps
import numpy as np;
import time

st.set_page_config(page_title="CPU Manager", page_icon="🖥️")
st.markdown("# CPU Manager")

tab1, tab2, tab3 = st.tabs(["CPU Times", "Especif Times", "Stats"])

with tab1:
    place1=st.empty()
    place2=st.empty()
    place3=st.empty()

with tab2:
    place4=st.empty()
    place5=st.empty()

with tab3:
    place6=st.empty()
    place7=st.empty()
    place8=st.empty()

#st.sidebar.header("CPU Manager")


for x in range(150): 
    timesOfCPU = ps.cpu_times()
    timesOfCPUPercent = ps.cpu_times_percent(interval=1, percpu=False)
    place1.markdown(
        f'''
        ### User:
        ###### Tempo dos processos normais em execução no modo de usuário.
        ##### {timesOfCPU.user}
        ##### {timesOfCPUPercent.user}
        '''
    )

    place2.markdown(
        f'''
        ### System:
        ###### Tempo gasto pelos processos em execução no modo Kernel
        ##### {timesOfCPU.system}
        ##### {timesOfCPUPercent.system}
        '''
    )

    place3.markdown(
        f'''
        ### Idle:
        ###### Tempo ocioso gasto, ou seja, sem fazer nenhum processo
        ##### {timesOfCPU.idle}
        ##### {timesOfCPUPercent.idle}
        '''
    )

    place4.markdown(
        f'''
        ### Iowait:
        ###### Tempo gasto esperando a conclusão da E/S. Não é contabilizado em contador de tempo IDLE
        ##### {timesOfCPU.iowait}
        ##### {timesOfCPUPercent.iowait}
        '''
    )

    place5.markdown(
        f'''
        ### Thread:
        ###### Número de núcleos
        ##### {ps.cpu_count(logical=True)}
        ###### Número de núcleos físicos
        ##### {ps.cpu_count(logical=False)}
        '''
    )

    place6.markdown(
        f'''
        ### Trocas de Contexto:
        ###### Número de trocas de contexto desde a inicialização
        ##### {ps.cpu_stats().ctx_switches}
        '''
    )

    place7.markdown(
        f'''
        ### Interrupções:
        ###### Número de interrupções desde a inicialização
        ##### {ps.cpu_stats().interrupts}
        '''
    )

    place8.markdown(
        f'''
        ### Trocas de Contexto:
        ###### Número de trocas de contexto desde a inicialização
        ##### {ps.cpu_stats().ctx_switches}
        '''
    )