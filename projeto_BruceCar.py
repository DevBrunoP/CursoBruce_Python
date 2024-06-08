import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime, timedelta

#Criando um dicionário com preços de manutenção
precos_manutencao = {
    "Troca de óleo": 50,
    "Filtro de ar": 20,
    "Pastilhas de freio": 80,
    "Bateria": 100,
    "Alinhamento": 60
}

#Criando um dicionário com tempo de manutenção
tempo_manutencao = {
    "Troca de óleo": 30,
    "Filtro de ar": 15,
    "Pastilhas de freio": 45,
    "Bateria": 60,
    "Alinhamento": 40
}

################################################################################################
# Criação da tabela de preços com base nos dicionários de precos_manutencao e tempo_manutencao #
################################################################################################

# Através dos dicionários é criada a tabela
data = {"Serviços":list(precos_manutencao.keys()), "Valor manutenção (R$)": list(precos_manutencao.values()), "Tempo manutenção (min)": list(tempo_manutencao.values())}
tabela_servicos = pd.DataFrame(data=data)

#########################
# Definição das funções #
#########################

# Função que soma os valores do dicionário com base no serviço de manutenção que o cliente escolher
def soma_lista(lista_de_servicos: list, pedido_servico: list) -> str:
    return sum(list(map(lambda x: lista_de_servicos.get(x), pedido_servico)))

# Função que irá formatar os mintuos caso forem menores que 60min, se não formata e transforma em horas
def formata_horario(minutos: int) -> str:
    if minutos >= 60: 
        horas = minutos // 60 # Converte os minutos para horas
        minutos_restantes = minutos % 60 # Coleta o resto da divisão do parâmetro minutos
        horas_formatadas = f"0{horas}:{str(minutos_restantes).zfill(2)} h" # Utiliza as duas variáveis acima para criar as horas_formatadas
    else:
        horas_formatadas = f"{minutos} min" # Se os minutos forem menores que 60, apenas é formatado os minutos
    return horas_formatadas 

# Função que adiciona a duração da manutenção na Ordem ser Serviço
def adicionar_minutos(minutos:float) -> str:
    agora = datetime.now() # Obtém a data e a hora atuais
    novo_horario = agora + timedelta(minutes=minutos) # Adiciona a quantidade de minutos especificada
    data_atual_formatada = agora.strftime("%d/%m/%Y")  # Converte da data no formato dd/mm/YY
    novo_horario_formatado = novo_horario.strftime("%H:%M") # Converte o horário no formato hh:mm

    return f"{data_atual_formatada} às {novo_horario_formatado}" # Retorna a data e a hora formatada e converte para str

#####################################
# Criação dos componentes da página #
#####################################

st.set_page_config(page_title = "Projeto Bruce")
st.title("BRUCE_CAR Auto Center :car:")
st.header("Olá, seja bem vindo a nossa página oficial!")
st.divider()
with st.container(): # Container: sobre
    st.subheader("Quem nós somos? :sparkles:")
    st.markdown("""Nós somos a BRUCE_CAR Auto Center, uma empresa com mais de 20 anos de experiência em manutenção de automóveis, atendendo clientes em todo o Brasil. 
                Nosso compromisso com a qualidade e a satisfação do cliente nos tornou referência na categoria, garantindo que seu veículo receba o melhor cuidado possível. 
                Nossa equipe de técnicos altamente qualificados está sempre pronta para realizar desde serviços básicos de manutenção até reparos complexos, utilizando as mais avançadas tecnologias e peças de alta qualidade. 
                Na BRUCE_CAR Auto Center, valorizamos a transparência, a confiança e a excelência, e estamos dedicados a manter seu veículo em perfeitas condições. 
                Venha nos visitar e experimente o atendimento diferenciado que só nós podemos oferecer :stuck_out_tongue_winking_eye:""")    
with st.container(): # Container: Tabela de preços
    st.subheader("Tabela de preços :dollar:")
    st.table(tabela_servicos) # Utilização da tabela

with st.container(): # Container: Atendimento virtual
    st.subheader("Atendimento virtual :technologist:")
    options = list(precos_manutencao.keys()) # Coletando todas as "chaves" de algum dos dicionários para ser as opções do dropdown

    # Criando o dropdown com os seviços oferecidos
    selected_option = st.multiselect(
        'Como podemos te ajudar hoje?', 
        options,
        placeholder="Selecione o tipo de manutenção",
        help='Escolha o serviço de manutenção'
    )
    # Utilizando o soma_lista para verificar os tempo da manutenção em minutos
    minutos_manutencao = soma_lista(tempo_manutencao, selected_option)
    
    col1, col2 = st.columns(2)
    with col1:
        if selected_option != []: # Foi escolhido alguma opoção? Caso sim é utilizado a função soma_lista para verificar o valor total
            st.metric(label="Custo da manutenção", value= f"R$ {soma_lista(precos_manutencao, selected_option)}")
        else: # Não foi escolhido nenhuma opção, então é definido um valor padrão de "R$ 0" para ser exibido ao usuário
            st.metric(label="Custo da manutenção", value= "R$ 0")
    
    with col2:
        if selected_option != []: # Foi escolhido alguma opoção? Caso sim é utilizado a função formata_horario para verificar o tempo total da manutenção
            st.metric(label="Tempo da manutenção", value= formata_horario(minutos_manutencao))
        else: # Não foi escolhido nenhuma opção, então é definido um valor padrão de "0 min" para ser exibido ao usuário
            st.metric(label="Tempo da manutenção", value= "0 min") 

    st.divider()
    col3, col4 = st.columns(2)
    pedido_gerado = False # Utilizo essa variável para verirficar se o pedido foi gerado e utiliá-lo ao final do código, incialmente é definido como False

    with col3:
        
        if selected_option != []: # Só irá aparecer o botão de "Gerar pedido caso tenha sido selecionado algum serviço"
            if st.button(label="Gerar pedido", type="primary"):
                with col4:
                    with st.spinner("Criando pedido... :hourglass_flowing_sand:"): # Indicação visual do carregamento do pedido para o usuário
                        time.sleep(random.randint(1,5)) # Coloquei um intervalo aleatório para parecer mais um cenário real
                        pedido_gerado = True # Pedido foi gerado! Irá mostrar o st.sucess no final com as informações de conclusão do pedido
        else:
            st.button(label="Gerar pedido", disabled=True) # Não foi selecionado nenhum serviço :( Botão fica desabilitado!
    if pedido_gerado:
        numero_pedido = random.randint(1, 3000) # Número do pedido aleatório
        st.success(f"""Pedido gerado com sucesso! :sparkles:
                   \n Ordem de serviço nº **{numero_pedido}** :clipboard:
                   \n Prazo de conclusão: **{adicionar_minutos(minutos_manutencao)}** :clock5:""") # Mensagem de sucesso do pedido com algumas informações de conclusão
