# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:18:51 2020

@author: Emre
"""
import pandas as pd
from keras.models import Sequential
from keras.layers import  Dense, Conv1D, MaxPooling1D, Flatten

def createLinearModel():
    model = Sequential()
    model.add(Dense(100, input_dim=33, activation='relu'))
    model.add(Dense(1))

    model.compile(loss='mse',optimizer='adam',metrics=['acc'])

    return model


def createConvolutionalModel():
    model = Sequential()
    model.add(Conv1D(filters=128, kernel_size=2, activation='relu', input_shape=(33,1)))
    model.add(Conv1D(filters=128, kernel_size=2, activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(1))

    model.compile(loss='mse',optimizer='adam',metrics=['acc'])

    return model

def loadData():
    train = pd.read_csv('data/sales_train.csv')
    test = pd.read_csv('data/test.csv')
    submission = pd.read_csv('data/sample_submission.csv')
    items = pd.read_csv('data/items.csv')
    itemCategory = pd.read_csv('data/item_categories.csv')
    shops = pd.read_csv('data/shops.csv')
    
    return train, test, submission, items, itemCategory, shops

# Data preprocessing
def dataProcess(train, test):
    
    # reset data type of 'date to date frame
    train['date'] = pd.to_datetime(train['date'],format = '%d.%m.%Y') 

    # merge rows with same shop_id and item_id
    dataset = train.pivot_table(index = ['shop_id','item_id'],values = ['item_cnt_day'],columns = ['date_block_num'],fill_value = 0,aggfunc='sum')
    dataset.reset_index(inplace=True)
    print(dataset) #shop id ye göre sıtalanmış iteem id ve aylık satışar sıralanmış

    # join with test table to see matching for store and item
    dataset = pd.merge(test, dataset, on=['shop_id', 'item_id'], how='left')
    dataset.fillna(0, inplace=True)
    print(dataset)

    # drop id as well because ID = index
    dataset.drop(['shop_id','item_id','ID'], inplace=True, axis=1)
    print(dataset)

    return dataset
