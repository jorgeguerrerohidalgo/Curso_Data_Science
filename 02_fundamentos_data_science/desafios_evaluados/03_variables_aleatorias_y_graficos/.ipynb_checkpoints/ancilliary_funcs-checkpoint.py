import matplotlib.pyplot as plt 
import scipy.stats as stats
import numpy as np

def fetch_descriptives(dataframe):
    for key, value in dataframe.iteritems():
       print(value.describe())
    


def fetch_null_cases(dataframe, var, print_list=False):
    tmp = dataframe
    tmp['flagnull'] = tmp[var].isnull()
    count_na = 0
    for i, r in tmp.iterrows(): 
        if r['flagnull'] is True:
            count_na += 1
            if print_list is True:
                print( r['cname'])
    print("\nCasos perdidos para {0}:\nCantidad de Casos: {1}\nPorcentaje de la muestra {2}".format(var, count_na, (count_na/len(tmp))*100))
    if print_list is True:
        print("Países sin registros de {0}\n".format(var))
        

def plot_histograma(df,columna, df_total,media_df_peque= False, media_df_total= False):
    temporal = df[columna].dropna()
    plt.hist(temporal, color='grey')
    plt.grid(True)
    plt.title(columna)
    if media_df_peque is True:
        plt.axvline(np.mean(temporal), color='dodgerblue')
    if media_df_total is True:
        plt.axvline(np.mean(df_total[columna]), color='red')
        

def dotplot(df, plot_var, plot_by, global_stat = False, statistic = 'mean'):
    tmp_df = df.loc[:, [plot_by, plot_var]]
    if statistic is 'mean':
        tmp_group_stat = tmp_df.groupby(plot_by)[plot_var].mean()
    if statistic is 'median':
        tmp_group_stat = tmp_df.groupby(plot_by)[plot_var].median()
        plt.plot(tmp_group_stat.values, tmp_group_stat.index, 'o',color='grey')
    if global_stat is True and statistic is 'mean':
        plt.axvline(df[plot_var].mean(), color='tomato', linestyle='--')
    if global_stat is True and statistic is 'median': 
        plt.axvline(df[plot_var].median(), color='tomato',linestyle='--')