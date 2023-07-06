import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.gridspec as gridspec


def generate_z_values(x, y):
    z = np.sin(x) * np.cos(y)
    return z


def add_colorbar(fig, cmap, z_values):
    cbar_axes = fig.add_axes([0.92, 0.1, 0.02, 0.8]) 
    norm = mpl.colors.Normalize(vmin=np.min(z_values), vmax=np.max(z_values))
    scalar_mappable = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    scalar_mappable.set_array(z_values)
    colorbar = plt.colorbar(scalar_mappable, cax=cbar_axes, ticks=np.linspace(np.min(z_values), np.max(z_values), 5),
                            boundaries=np.linspace(np.min(z_values), np.max(z_values), 10))


def scatter_plot(*dataframes):
    num_subplots = len(dataframes)
    fig = plt.figure(figsize=(8 + num_subplots, 4))
    grid_spec = gridspec.GridSpec(1, num_subplots + 1, width_ratios=[1] * num_subplots + [0.05])
    colormap = plt.get_cmap('viridis')

    for i, df in enumerate(dataframes):
        df = df[df['sentiment_score'] != 0]
        df = df.reset_index(drop=True)

        x = df.index
        y = df['sentiment_score']
        X, Y = np.meshgrid(x, y)
        z_values = generate_z_values(X, Y)

        subplot = fig.add_subplot(grid_spec[0, i])
        subplot.set_title('Sentiments Scattered', fontsize=14)
        subplot.scatter(x, y, c=y, cmap=colormap)
        subplot.set_xlabel('Index')
        subplot.set_ylabel('Sentiment Score')
        subplot.set_facecolor('#F0F0F0')
        subplot.axhline(0, color='black', linestyle='dotted')

    add_colorbar(fig, colormap, z_values)
    plt.tight_layout()
    plt.show()


def heatmap_plot(*dataframes):
    num_subplots = len(dataframes)
    fig = plt.figure(figsize=(8 + num_subplots, 4))
    grid_spec = gridspec.GridSpec(1, num_subplots + 1, width_ratios=[1] * num_subplots + [0.05])
    colormap = plt.get_cmap('plasma')

    for i, df in enumerate(dataframes):
        df = df[df['sentiment_score'] != 0]
        df = df.reset_index(drop=True)

        x = df.index
        y = df['sentiment_score']
        X, Y = np.meshgrid(x, y)
        Z = generate_z_values(X, Y)

        subplot = fig.add_subplot(grid_spec[0, i], projection='3d')
        subplot.set_title('Sentiments Heatmapped', fontsize=14)
        subplot.plot_surface(X, Y, Z, cmap=colormap, edgecolor='none')
        subplot.set_xlabel('Index')
        subplot.set_ylabel('Sentiment Score')
        subplot.set_zlabel('Value')

    add_colorbar(fig, colormap, Z)

    plt.tight_layout()
    plt.show()
