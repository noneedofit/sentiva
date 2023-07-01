import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def plot_sentiment(df):

    df = df.sort_values('sentiment_score', ascending=True)
    df = df.reset_index(drop=True)
    x = df.index
    y = df['sentiment_score']

    fig, axes = plt.subplots() 
    
    axes.set_title('Sentiment Analysis', fontsize=14)
    axes.scatter(x, y, c=y, cmap='plasma')
    axes.set_facecolor("white")
    axes.plot(df['sentiment_score'])
    
    cmap = plt.get_cmap('plasma')
    norm = mpl.colors.Normalize(vmin=min(y), vmax=max(y))
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    colorbar = plt.colorbar(sm, ticks=np.linspace(-1,1,5), boundaries=np.linspace(-1,1,10))

    plt.show()