import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Análise de Renda",
    page_icon="https://img.freepik.com/vetores-premium/lupa-de-linha-fina-como-icone-de-visao-geral-de-escrutinio-de-renda-plana-tendencia-lineart-exame-simples-ou-lucro-logotipo-golpe-arte-web-design-isolado-no-conceito-branco-de-pictograma-de-inspecao-ou-simbolo-de-pesquisa_775815-407.jpg",
    # layout="wide",
)

# Estilo da página
st.markdown("""
<style>
    h1 {
        color: #26547C;
        text-align: left;
    }
    h2 {
        color: #407FB7;
        border-bottom: 1px solid #407FB7;
    }
    h3 {
        color: #4A90E2;
        text-align: center;    
    }
    p {
        color: #333333;
    }
</style>
""", unsafe_allow_html=True)


# Função para criar os gráficos lineplot
def create_lineplot(data, x, y, hue, hue_order):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=x, y=y, hue=hue, data=data, ax=ax, hue_order=hue_order, palette="Set2") #add palette
    ax.tick_params(axis='x', rotation=45, labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel(' ', fontsize=12)
    ax.set_ylabel('Renda', fontsize=12)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.6)
    return fig

# Função para criar os gráficos barplot
def create_barplot(data, x, y, hue_order):
    fig, ax = plt.subplots(figsize=(10,6))
    sns.barplot(x=x, y=y, data=data, ax=ax, hue_order=hue_order, palette="Set3")
    ax.tick_params(axis='x', rotation=0, labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel(' ', fontsize=12)
    ax.set_ylabel('Renda', fontsize=12)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.6)
    return fig


# Importando os dados
df = pd.read_csv('./input/previsao_de_renda.csv')

# Legendas das figuras------------------------------------------------------------------------------------
texto_sexo="""É possível visualizar claramente a disparidade salarial entre os gêneros. 
Os homens possuem aproximadamente o dobro da renda das mulheres, incluindo o erro."""
texto_pi="""Apesar de ter sido indicada pela análise de regressão do Patsy, o gráfico de linha não mostra nenhuma
diferença significativa de renda entre os clientes que possuem imóvel e os que não possuem."""
texto_pv="""O gráfico mostra que os clientes que possuem veículo apresentam de forma geral uma renda 
maior do que os clientes sem veículo. Esse fator não foi escolhido na análise do Patsy."""
texto_edu="""Ao longo do tempo pode-se ver que a escolaridade não é um fator determinante para a renda,
ao contrário do que seria imaginável. Para o ensino secundário e superior completo, observa-se uma 
menor variação do valor da renda ao longo do tempo, enquanto as outras categorias possuem variação maior."""
texto_tr="""Sobre o tipo de renda, os pensionistas apresentam renda sistematicamente menor do que as 
outras categorias, isso é explicado pelo fato do valor recebido pelos pensionistas ser limitado pelo 
teto da Previdência Social."""
texto_ec="""O estado civil mostra uma variação gradual entre as categorias, com destaque para os viúvos,
que possuem menor renda, e os casados que possuem maior renda de forma geral. As outras categorias variam
entre essas duas."""

texto_sexo2="""Novamente podemos ver a grande diferença da renda entre mulheres e homens. O gráfico apresenta
o valor médio da renda para todos os dados, divididos pelo sexo. A renda média masculina incluindo o erro
é maior do que o dobro da renda média feminina."""
texto_pi2="""Podemos ver que considerando o erro, os valores da renda média para os clientes que possuem
e não possuem imóvel são estatisticamente iguais."""
texto_pv2="""Já para a posse de veículo, a renda é aproximadamente 35% maior do que a renda dos clientes que 
não possuem veículo."""
texto_edu2="""A escolaridade não tem uma relação direta com a renda, sendo que o maior grau de educação, 
a pós-graduação, apresenta a menor renda (com bastante erro), enquanto as maiores rendas são representadas
pelo ensino secundário, e superior completo. O ensino superior incompleto estatisticamente compara-se ao
ensino primário."""
texto_tr2="""O servidor público apresenta maior renda entre as categorias, enquanto o pensionista apresenta a menor."""
texto_ec2="""Como visto nos gráficos de linha, aqui também vemos que os casados apresentam maior renda entre
todos os outros, e os viúvos apresentam menor renda."""

# Lista de variáveis usadas no loop--------------------------------------------------------------------------
variables = [
    {'var': 'sexo', 'hue_order': ['M', 'F'], 'title': 'Sexo vs Renda', 'texto1':texto_sexo, 'texto2':texto_sexo2},
    {'var': 'posse_de_imovel', 'hue_order': [True, False], 'title': 'Posse de Imóvel vs Renda', 'texto1':texto_pi, 'texto2':texto_pi2},
    {'var': 'posse_de_veiculo', 'hue_order': [True, False], 'title': 'Posse de Veículo vs Renda','texto1':texto_pv, 'texto2':texto_pv2},
    {'var': 'educacao', 'hue_order': None, 'title': 'Escolaridade vs Renda','texto1':texto_edu, 'texto2':texto_edu2},
    {'var': 'tipo_renda', 'hue_order': None, 'title': 'Tipo de Renda vs Renda','texto1':texto_tr, 'texto2':texto_tr2},
    {'var': 'estado_civil', 'hue_order': None, 'title': 'Estado Civil vs Renda','texto1':texto_ec, 'texto2':texto_ec2}     
]

# Título da página---------------------------------------------------------------------------------------
st.title('Análise Exploratória da Previsão de Renda')

# Gráficos de Linha---------------------------------------------------------------------------------------
st.header('Parte 1 - Gráficos ao longo do tempo:')#Subtitulo
st.write('A análise ao longo do tempo por meio de gráficos de linha é uma poderosa técnica para visualizar tendências e padrões temporais nos dados. Ao traçar a evolução de uma variável ao longo de diferentes períodos, podemos identificar flutuações sazonais, padrões de crescimento ou declínio e eventos incomuns.')
# Loop para criar os gráficos de linha
for var in variables:
    st.markdown(f"### {var['title']}")
    fig = create_lineplot(data=df, x='data_ref', y='renda', hue=var['var'], hue_order=var['hue_order'])
    st.pyplot(fig)
    st.write(var['texto1'])

# Gráficos de Barra-------------------------------------------------------------------------------
st.header('Parte 2 - Análise Bivariada:')#Subtitulo
st.write('A análise bivariada é uma abordagem estatística fundamental que examina a relação entre duas variáveis em um conjunto de dados. Por meio dessa análise, buscamos compreender como as mudanças em uma variável estão associadas às mudanças em outra variável.')
#Loop para criar os gráficos de barra
for var in variables:
    st.markdown(f"### {var['title']}")
    fig = create_barplot(x=var['var'], y='renda', data=df, hue_order=var['hue_order'])
    st.pyplot(fig)
    st.write(var['texto2'])                     
