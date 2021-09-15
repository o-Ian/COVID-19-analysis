import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


df_covid = pd.read_csv('Covid_datas.csv', index_col='Unnamed: 0').sort_values(by=['date'], ignore_index=True)

# Removing countrys in dictatorships
df_remove = df_covid.loc[(df_covid['location'] == 'China') | (df_covid['location'] == 'Russia')
                         | (df_covid['location'] == 'Uzbekistan') | (df_covid['location'] == 'Turkmenistan')
                         | (df_covid['location'] == 'Myanmar') | (df_covid['location'] == 'Vietnam')
                         | (df_covid['location'] == 'Iran') | (df_covid['location'] == 'Syria')
                         | (df_covid['location'] == 'Turkey') | (df_covid['location'] == 'Afhhanistan')
                         | (df_covid['location'] == 'Cuba') | (df_covid['location'] == 'Venezuela')
]

df_covid = df_covid.drop(df_remove.index)

df_covid_pos_vacina = pd.DataFrame()

correlation = df_covid.corr()

correlation.to_csv('Correlações_geral.csv')

# Condition to catch only the data after vaccination has started
df_covid_pos_vacina = df_covid.iloc[:63556]

# Doing the correlations after vaccination has started
df_covid_pos_vacina.to_csv('Covid_data_pos_vac.csv')

correlation_pos_vac = df_covid_pos_vacina.corr()

correlation_pos_vac.to_csv('Correlações_pos_vac.csv')

# Configuration of correlation image
plt.subplots(figsize=(20, 15))

correlation_graph = sn.heatmap(correlation, annot=True, fmt='.2f', linewidth=.5)

correlation_graph.set_yticklabels(correlation_graph.get_yticklabels(), fontsize=8)

correlation_graph.set_xticklabels(correlation_graph.get_xticklabels(), fontsize=5)

plt.show()


# Final steps
df_covid.to_csv('Covid_datas.csv')

df_covid_pos_vacina.to_csv('Covid_data_pos_vac.csv')
