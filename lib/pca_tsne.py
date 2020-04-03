import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

def pca_tsne(X, y, plot_2d = True, plot_3d = True, plot_tsne = True, n_components = 3, perplexity = [5,50,95]):

        df = X
        features = list(df.columns.values)
        df['y']=y

        pca = PCA(n_components=n_components)
        pca_result = pca.fit_transform(X)

        df['pca-one'] = pca_result[:,0]
        df['pca-two'] = pca_result[:,1]
        df['pca-three'] = pca_result[:,2]

        print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))

        if plot_2d :
            plt.figure(figsize=(14,10))
            sns.scatterplot(
            x="pca-one", y="pca-two",
            hue="y",
            palette=sns.color_palette("hls", 7),
            data=df,
            legend="full",
            alpha=0.3
            )
            plt.show()

        if plot_3d :
            ax = plt.figure(figsize=(14,10)).gca(projection='3d')
            ax.scatter(
            xs=df["pca-one"],
            ys=df["pca-two"],
            zs=df["pca-three"],
            c=df['y'],
            cmap='tab10'
            )
            ax.set_xlabel('pca-one')
            ax.set_ylabel('pca-two')
            ax.set_zlabel('pca-three')
            plt.show()

        if plot_tsne :
            for perp in perplexity:
                tsne = TSNE(n_components=2, verbose=0, perplexity=perp, n_iter=300)
                tsne_results = tsne.fit_transform(df[features].values)
                df['tsne-2d-one'] = tsne_results[:,0]
                df['tsne-2d-two'] = tsne_results[:,1]
                print('Perplexity = ',perp)
                plt.figure(figsize=(14,10))
                sns.scatterplot(
                x="tsne-2d-one", y="tsne-2d-two",
                hue="y",
                palette=sns.color_palette("hls", 7),
                data=df,
                legend="full",
                alpha=0.3
                )
                plt.show()
