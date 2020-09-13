# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 00:17:32 2020

@author: Emre
"""

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

from Methods import loadData, createLinearModel, dataProcess, createConvolutionalModel

train, test, submission, items, itemCategory, shops = loadData()

#Convert to dataset train and test data (Preprocess)
dataset = dataProcess(train, test)

# split into training set and test set
X = np.expand_dims(dataset.values[:,:-1], axis=2)
y = dataset.values[:,-1:]


X_test = np.expand_dims(dataset.values[:,1:], axis=2)
Linear_model = createLinearModel()
Linear_model.summary()

Cnn_model = createConvolutionalModel()
Cnn_model.summary()

Cnn_history =Cnn_model.fit(X, y, validation_split=0.33, batch_size=512, epochs=30)
Linear_history = Linear_model.fit(X[:,:,0], y, validation_split=0.33, batch_size=512, epochs=60)


#Linear Graph
plt.title('Linear_model accuracy')
plt.plot(Linear_history.history['val_acc'])
plt.plot(Linear_history.history['acc'])
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['Val_Acc','Accuracy'], loc='upper left')
plt.show()

plt.title('Linear_model Loss')
plt.plot(Linear_history.history['val_loss'])
plt.plot(Linear_history.history['loss'])
plt.ylabel('Loss')
plt.xlabel('epoch')
plt.legend(['Val_Loss','Loss'], loc='upper left')
plt.show()


#Predict and save predict amount Linear 
submission=Linear_model.predict(X_test[:,:,0])
submission=submission.clip(0,20)
submission=pd.DataFrame({'ID':test['ID'], 'item_cnt_month':submission.ravel()})
submission.to_csv('result/linear_predicts.csv',index=False)

#Cnn Graph

plt.title('Cnn_model accuracy')
plt.plot(Cnn_history.history['val_acc'])
plt.plot(Cnn_history.history['acc'])
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['Val_Acc','Accuracy'], loc='upper left')
plt.show()

plt.title('Cnn_model Loss')
plt.plot(Cnn_history.history['val_loss'])
plt.plot(Cnn_history.history['loss'])
plt.ylabel('Loss')
plt.xlabel('epoch')
plt.legend(['Val_Loss','Loss'], loc='upper left')
plt.show()

submission=Cnn_model.predict(X_test)
submission=submission.clip(0,20)
submission=pd.DataFrame({'ID':test['ID'], 'item_cnt_month':submission.ravel()})
submission.to_csv('result/convolution_predicts.csv',index=False)


