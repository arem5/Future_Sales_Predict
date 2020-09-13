# Future_Sales_Predict
Compare Linear Regressin and CNN for Future Sales Predict 

DATA DESCRIPTION 

input        :daily historical sales data and a test set (Note: list of shops and products slightly changes every month)
output       :total amount of products sold in every shop for the test set


sales_train.csv          :the training set. Daily historical data from January 2013 to October 2015.
test.csv                 :the test set. You need to forecast the sales for these shops and products for November 2015.
sample_submission.csv    :a sample submission file in the correct format.
items.csv                :supplemental information about the items/products.
item_categories.csv      :supplemental information about the items categories.
shops.csv                :supplemental information about the shops.


VARAİBLE NAME AND DESCRIPTION

sales_train.csv

date			              :date in format dd/mm/yyyy
date_block_num		      :a consecutive month number, used for convenience. January 2013 is 0, February 2013 is 1,..., October 2015 is 33
shop_id			            :unique identifier of a shop
item_id			            :unique identifier of a product
item_price		          :current price of an item
item_cnt_day		        :number of products sold. You are predicting a monthly amount of this measure



test.csv
ID			                :an Id that represents a (Shop, Item) tuple within the test set
shop_id			            :unique identifier of a shop
item_id			            :unique identifier of a product


sample_submission.csv

ID			               :an Id that represents a (Shop, Item) tuple within the test set
item_cnt_day		       :number of products sold. You are predicting a monthly amount of this measure

item_categories.csv
item_category_name	  :name of item category
item_category_id	    :unique identifier of item category

shops.csv
shop_name		          :name of shop
shop_id			          :unique identifier of a shop


DATA EXPLORATION

In the data there ara 33 months between two date and there are 60 shops.We can see the sales performance of all shops on the graphs for 33 months.
We can see an increase on sales every 12th month.


TRAIN
I compare two method in this project for "Predict Future Sales" .
1) Linear Regression 
2) Convolution Neural Network

You can see the result in 'result' folder.

I make dataset with 'sales

'item_cnt_day' values with the same id are added together and filled substituted 0 for 'NaN'values . 
After I have Merged shop_id and item_id in test and train dataset and have occoured dataset for 
train with 'Linear Regression' and 'Convolution Neural Network'. 


