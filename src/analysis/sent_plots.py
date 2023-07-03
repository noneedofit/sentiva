import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def generate_z_values(x, y):
    # Generate z values based on x and y coordinates
    z = np.sin(x) * np.cos(y)
    return z

def plot_sentiment(df):
    df = df.sort_values('sentiment_score', ascending=True)
    df = df.reset_index(drop=True)
    x = df.index
    y = df['sentiment_score']
    X, Y = np.meshgrid(x, y)
    z = generate_z_values(X, Y)

    fig = plt.figure()
    ax_scatter = fig.add_subplot(121)
    ax_heatmap = fig.add_subplot(122, projection='3d')
    ax_cbar = fig.add_axes([0.92, 0.1, 0.02, 0.8])  # Colorbar axes position

    ax_scatter.set_title('Sentiment Analysis (Scatter Plot)', fontsize=14)
    ax_scatter.scatter(x, y, c=y, cmap='plasma')
    ax_scatter.set_xlabel('Index')
    ax_scatter.set_ylabel('Sentiment Score')

    ax_heatmap.set_title('Sentiment Analysis (3D Heatmap)', fontsize=14)
    ax_heatmap.plot_surface(X, Y, z, cmap='plasma', edgecolor='none')
    ax_heatmap.set_xlabel('Index')
    ax_heatmap.set_ylabel('Sentiment Score')
    ax_heatmap.set_zlabel('Value')  # Set a string as the z-label

    cmap = plt.get_cmap('plasma')
    norm = mpl.colors.Normalize(vmin=np.min(z), vmax=np.max(z))
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    colorbar = plt.colorbar(sm, cax=ax_cbar, ticks=np.linspace(-1, 1, 5), boundaries=np.linspace(-1, 1, 10))

    
    plt.show()
