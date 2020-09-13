# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:52:42 2020

@author: Emre
"""
import math
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from Methods import loadData

train, test, submission, items, itemCategory, shops = loadData()

#Data Exploration

grouped = pd.DataFrame(train.groupby(['shop_id', 'date_block_num'])['item_cnt_day'].sum().reset_index())
fig, axes = plt.subplots(nrows=5, ncols=2, sharex=True, sharey=True, figsize=(16,20))
num_graph = 10
id_per_graph = math.ceil(grouped.shop_id.max() / num_graph)
count = 0
for i in range(5):
    for j in range(2):
        sns.pointplot(x='date_block_num', y='item_cnt_day', hue='shop_id', data=grouped[np.logical_and(count*id_per_graph <= grouped['shop_id'], grouped['shop_id'] < (count+1)*id_per_graph)], ax=axes[i][j])
        count += 1

