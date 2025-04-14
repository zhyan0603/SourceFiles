import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

data_1978 = np.load('des_Li_1978.npy') 
data_802 = np.load('des_Li_802.npy')   
data_25 = np.load('des_Li_25.npy')    

combined_data = np.vstack((data_1978, data_802, data_25)) 

labels_1978 = np.zeros(data_1978.shape[0])  
labels_802 = np.ones(data_802.shape[0])     
labels_25 = np.full(data_25.shape[0], 2)   

combined_labels = np.hstack((labels_1978, labels_802, labels_25)) 

pca = PCA(n_components=2)  
reduced_data = pca.fit_transform(combined_data) 

fig = plt.figure(figsize=(6, 4.5), dpi=150)
gs = fig.add_gridspec(5, 5, hspace=0.05, wspace=0.05)

ax_scatter = fig.add_subplot(gs[1:5, 0:4])

ax_hist_x = fig.add_subplot(gs[0, 0:4], sharex=ax_scatter)
ax_hist_y = fig.add_subplot(gs[1:5, 4], sharey=ax_scatter)

colors = ['#9DBAD2', '#F8BC7E', '#A9CA70']
labels_name = [r'NEP$_{std}$', r'NEP$_{802}$', r'NEP$_{25}$'] 

for i in range(3):
    ax_scatter.scatter(reduced_data[combined_labels == i, 0],  
                       reduced_data[combined_labels == i, 1],  
                       c=colors[i], s=15, label=labels_name[i], alpha=0.6)
    sns.kdeplot(reduced_data[combined_labels == i, 0], ax=ax_hist_x, color=colors[i], fill=True, alpha=0.4)
    sns.kdeplot(reduced_data[combined_labels == i, 1], ax=ax_hist_y, color=colors[i], fill=True, alpha=0.4, vertical=True)

ax_scatter.set_xlabel('Principal Component 1')
ax_scatter.set_ylabel('Principal Component 2')
ax_scatter.legend()

ax_hist_x.set_yticks([])
ax_hist_y.set_xticks([])
ax_hist_x.set_xticks([])
ax_hist_y.set_yticks([])

plt.show()
#plt.savefig('Figure5_PCA.png', dpi=600)