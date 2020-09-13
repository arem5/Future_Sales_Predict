# Future_Sales_Predict
Compare Linear Regressin and CNN for Future Sales Predict <br/>
[Compatation Link from Kaggle](https://www.kaggle.com/c/competitive-data-science-predict-future-sales/data) <br/>
<br/>
## DATA DESCRIPTION 

*input*        :daily historical sales data and a test set (Note: list of shops and products slightly changes every month)  <br/>
*output*       :total amount of products sold in every shop for the test set  <br/>
  <br/>
*sales_train.csv*         :the training set. Daily historical data from January 2013 to October 2015.  <br/>
*test.csv*                 :the test set. You need to forecast the sales for these shops and products for November 2015.  <br/>
*sample_submission.csv*    :a sample submission file in the correct format.  <br/>
*items.csv*                :supplemental information about the items/products. <br/>
*item_categories.csv*      :supplemental information about the items categories. <br/>
*shops.csv*                :supplemental information about the shops.  <br/>


## VARAİBLE NAME AND DESCRIPTION

**sales_train.csv** <br/>
<br/>
*date*			              :date in format dd/mm/yyyy <br/>
*date_block_num*		      :a consecutive month number, used for convenience. January 2013 is 0, February 2013 is 1,..., October 2015 is 33 <br/>
*shop_id*			            :unique identifier of a shop  <br/>
*item_id*			            :unique identifier of a product  <br/>
*item_price*		          :current price of an item  <br/>
*item_cnt_day*		        :number of products sold. You are predicting a monthly amount of this measure  <br/>
<br/>
**test.csv** <br/>
<br/>
*ID*			                :an Id that represents a (Shop, Item) tuple within the test set <br/>
*shop_id*			            :unique identifier of a shop <br/>
*item_id*			            :unique identifier of a product <br/>
<br/>
**sample_submission.csv**<br/>
<br/>
*ID*			               :an Id that represents a (Shop, Item) tuple within the test set <br/>
*item_cnt_day*	       :number of products sold. You are predicting a monthly amount of this measure <br/>
<br/>
**item_categories.csv**<br/>
<br/>
*item_category_name*	  :name of item category <br/>
*item_category_id*	    :unique identifier of item category <br/>
<br/>
**shops.csv**<br/>
<br/>
*shop_name*		          :name of shop <br/>
*shop_id*			          :unique identifier of a shop <br/>
<br/>
<br/>
## DATA EXPLORATION<br/>
<br/>
In the data there ara 33 months between two date and there are 60 shops.We can see the sales performance of all shops on the graphs for 33 months. <br/>
We can see an increase on sales every 12th month. <br/>
<br/>
![Graphs about Data](https://github.com/arem5/Future_Sales_Predict/blob/master/result/DataExp.png) 

<br/>
<br/>
# TRAIN <br/> 
 <br/>
I compare two method in this project for "Predict Future Sales" . <br/>
1) *Linear* *Regression*  <br/>
2) *Convolution Neural Network* <br/>
<br/>
<br/>
You can see the predict result in *'result'* folder.  <br/>
<br/>
![CNN_Acc](https://github.com/arem5/Future_Sales_Predict/blob/master/result/Cnn_model_acc.png)  <br/>
![CNN_Loss](https://github.com/arem5/Future_Sales_Predict/blob/master/result/Cnn_model_loss.png) <br/>
![Lr_Acc](https://github.com/arem5/Future_Sales_Predict/blob/master/result/Linear_model_acc.png) <br/>
![Lr_Loss](https://github.com/arem5/Future_Sales_Predict/blob/master/result/Linear_model_Loss.png) <br/>
<br/>
I make dataset with <br/>
"item_cnt_day" values with the same id are added together and filled substituted 0 for "NaN" values . <br/>
After I have Merged "shop_id" and "item_id" in test and train dataset and have occoured dataset for  
train with "LinearRegression" and "Convolution Neural Network". 


