import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from src.analysis.sent_analysis import get_sentiment_df

def plot_sentiment():
    df = get_sentiment_df()
    df = df.sort_values('sentiment_score', ascending=True)
    df = df.reset_index(drop=True)

    x = df.index 
    y = df['sentiment_score']
    df['sentiment_score'].plot()
    plt.show()