#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: func.py
Author: Daniel Mardones
Email: daniel[dot]mardones[dot]s[at]gmail[dot]com
Github: https://github.com/Denniels
Description: Funciones para prueba modulo DataSciens
"""

#import argparse
#import time
#import os
#from collections import Counter
#import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import scipy.stats as stats
import seaborn as sns
#from scipy.stats import norm
#from scipy.stats import t
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings(action="ignore")
colors = ["tomato", "darkgoldenrod", "limegreen", "dodgerblue", "sienna", "slategray"]

def summary_drop(data):

    """Funcion que entrega un summary de un dataframe completo.
    Args:
        data (DataFrame): Conjunto de datos
    Returns:
        pd.DataFrame: con todas las variables del df
    """
    tipos = pd.DataFrame({'tipo': data.dtypes},index=data.columns)
    na = pd.DataFrame({'nulos': data.isna().sum()}, index=data.columns)
    na_prop = pd.DataFrame({'porc_nulos':data.isna().sum()/data.shape[0]}, index=data.columns)
    ceros = pd.DataFrame({'ceros':[data.loc[data[col]==0,col].shape[0] for col in data.columns]}, index= data.columns)
    ceros_prop = pd.DataFrame({'porc_ceros':[data.loc[data[col]==0,col].shape[0]/data.shape[0] for col in data.columns]}, index= data.columns)
    summary = data.describe(include='all').T

    summary['dist_IQR'] = summary['75%'] - summary['25%']
    summary['limit_inf'] = summary['25%'] - summary['dist_IQR']*1.5
    summary['limit_sup'] = summary['75%'] + summary['dist_IQR']*1.5

    summary['outliers'] = data.apply(lambda x: sum(np.where((x<summary['limit_inf'][x.name]) | (x>summary['limit_sup'][x.name]),1 ,0)) if x.name in summary['limit_inf'].dropna().index else 0)


    return pd.concat([tipos, na, na_prop, ceros, ceros_prop, summary], axis=1).sort_values('tipo')


def dist_box(data):
    """Funcion que imprime grafico de las distribuciones de un 
    dataframe completo.
    Args:
        data (DataFrame): Conjunto de datos
    Returns:
        distplots: con todas las variables del df
    """
    Name=data.name.upper()
    fig,(ax_box,ax_dis) = plt.subplots(nrows=2,sharex=True,gridspec_kw = {"height_ratios": (.25, .75)},figsize=(8, 5))
    mean=data.mean()
    median=data.median()
    mode=data.mode().tolist()[0]
    sns.set_theme(style="white")
    fig.suptitle("Distribución para "+ Name  , fontsize=18, fontweight='bold')
    sns.boxplot(x=data,showmeans=True, orient='h',color="tan",ax=ax_box)
    ax_box.set(xlabel='')

    sns.despine(top=True,right=True,left=True) 
    sns.distplot(data,kde=False,color='red',ax=ax_dis)
    ax_dis.axvline(mean, color='r', linestyle='--',linewidth=2)
    ax_dis.axvline(median, color='g', linestyle='-',linewidth=2)
    plt.legend({'Media':mean,'Mediana':median})