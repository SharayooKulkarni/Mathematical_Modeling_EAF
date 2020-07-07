# Mathematical_Modeling_EAF

 Main aim of this project is to reduce the Specific power consumption of EAF. 
 
 In this I have yearly EAF data with 250 features. Based on the given profiles , an appropriate statistical filter can be designed to remove unecessary features. 
 
 For this, the correlation between each of the feature is obtained with the target feature. Here using a technique called Wrapper Method , I feed the features to the selected Machine Learning algorithm and based on the model performance I add/remove the features.
 
 So I selected most important 20 features to build a model. I have applied Linear Regression model and plot the predicted values with Actual values which gives quite good prediction.
 
 Currently I am applying Genetic Algorithm with constraint optimization to reduce the Specific Power Consumption.
