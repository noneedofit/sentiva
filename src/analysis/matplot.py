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
    
    cmap = plt.get_cmap('plasma',10)
    norm = mpl.colors.Normalize(vmin=0,vmax=2)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    plt.colorbar(sm, ticks=(-1.0, -0.95, -0.9, -0.85, -0.8, -0.75, -0.7, -0.65, -0.6, -0.55, -0.5, -0.45, -0.4, -0.35, -0.3, -0.25, -0.2, -0.15, -0.1, -0.05, 0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0), 
                 boundaries=np.arange(-1,2.1,.1))

    plt.show()


plot_sentiment()


