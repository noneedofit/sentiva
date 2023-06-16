import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
from src.analysis.sent_analysis import get_sentiment_df

def plot_sentiment():

    df = get_sentiment_df()
    df = df.sort_values('sentiment_score', ascending=True)
    df = df.reset_index(drop=True)
    x = df.index
    y = df['sentiment_score']

    fig, ax = plt.subplots()
    
    ax.set_title('Sentiment Analysis', fontsize=14)
    ax.scatter(x, y, c=y, cmap='plasma')
    ax.set_facecolor("white")
    ax.plot(df['sentiment_score'])
    
    cmap = plt.get_cmap('plasma',20)
    norm = mpl.colors.Normalize(vmin=0,vmax=2)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    plt.colorbar(sm, ticks=np.linspace(-1,1,100), 
             boundaries=np.arange(-0.05,2.1,.1))

    plt.show()


plot_sentiment()


