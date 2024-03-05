# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# pacotes
import pandas as pd

#carregando dados
pokemon = pd.read_csv("C:/Users/20191enpro0027/Downloads/pokemon_data.csv")

#descrição dos dados
pokemon.describe()

#selecionar colunas especificas
pokemon_2 = pokemon[['Name', 'Type 1', 'Type 2']]

#Filtrar por tipo do pokemon
pokemon_fogo = pokemon.loc[pokemon['Type 1'] == 'Fire']

pokemon_fogo2 = pokemon[pokemon.iloc[:,2] == 'Fire']

pokemon_fogo3 = pokemon.loc[(pokemon['Type 1'] == 'Fire') | (pokemon['Type 2'] == 'Fire')]

#Ordenação
pokemon_ataque = pokemon.sort_values('Attack', ascending = True)

#Estatísticas de agregação
pokemon_grupo = pokemon.groupby(['Type 1'])
pokemon_grupo['Attack'].mean()
pokemon_grupo['Attack'].std()
pokemon_grupo['Attack'].median()

