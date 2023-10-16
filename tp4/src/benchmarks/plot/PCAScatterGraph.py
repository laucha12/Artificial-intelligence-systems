import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

class PCAGraphs:
    @staticmethod
    def scatter_plot(pca_result,countries):
        pca_df = pd.DataFrame(data=pca_result, columns=["PC1", "PC2"])
        pca_df["Country"] = countries
        plt.figure(figsize=(10, 8))
        plt.scatter(pca_df["PC1"], pca_df["PC2"])
        plt.xlabel("Principal Component 1 (PC1)")
        plt.ylabel("Principal Component 2 (PC2)")
        plt.title("PCA Analysis")
        plt.grid()
        for i, country in enumerate(pca_df["Country"]):
            plt.annotate(country, (pca_df["PC1"][i], pca_df["PC2"][i]))
        plt.show()
    @staticmethod
    def scatter_plot_with_PBI(pc1,pc2, countries):
        pca_df = pd.DataFrame({"PC1": pc1, "PC2": pc2, "Country": countries})
        top_half = pca_df.iloc[:14]
        bottom_half = pca_df.iloc[14:]

        # Create a scatterplot with red for the top half and blue for the bottom half
        plt.figure(figsize=(10, 8))
        plt.scatter(top_half["PC1"], top_half["PC2"], c="red", label="Top Half")
        plt.scatter(bottom_half["PC1"], bottom_half["PC2"], c="blue", label="Bottom Half")
        plt.xlabel("Principal Component 1 (PC1)")
        plt.ylabel("Principal Component 2 (PC2)")
        plt.title("PCA Analysis")
        plt.grid()

        # Annotate points with country names
        for i, country in enumerate(pca_df["Country"]):
            plt.annotate(country, (pca_df["PC1"][i], pca_df["PC2"][i]))

        # Add a legend
        plt.legend(loc="upper right")

        plt.show()
    @staticmethod
    def blox_plot(scaled_data,header):
        pca_df = pd.DataFrame(data=scaled_data, columns=header)
        # Create a box plot using Plotly
        fig = px.box(pca_df, title='Box plot of the variables')
        # Show the plot
        fig.show()
