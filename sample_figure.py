#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


# In[3]:


#input raw RNAseq readcount data 
#source: https://ay-lab-tools.lji.org/sle/index.php
df = pd.read_csv('GSE149050_Bulk_Human_RawCounts.csv', index_col = 0, nrows=200)


# In[4]:


#sort dataframe by count values to filter out non-transcribed genes
df2 = df.sort_values(by = ['025_S1073a_IFNpos_T'], ascending=False)


# In[9]:


#for simplicity, select top 20 genes to display
df3 = df2.head(20)
df3


# In[8]:


#generate a cluster heatmap of the 20 most transcribed genes for three representative healthy T cell populations
sb_plot = sb.clustermap(df3.iloc[:, 0:3], col_cluster = False, figsize = (10,10), cbar_pos = (1, 0.2, 0.08, 0.5))

#save figure
sb_plot.savefig("test_clustermap.png")


# In[ ]:





# In[ ]:




