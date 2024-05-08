# importing Randomforest 
from sklearn.ensemble import AdaBoostRegressor 
from sklearn.ensemble import RandomForestRegressor 

# creating model 
m1 = RandomForestRegressor() 

# separating class label and other attributes 
train1 = train.drop(['air_quality_index'], axis=1) 
target = train['air_quality_index'] 

# Fitting the model 
m1.fit(train1, target) 
'''RandomForestRegressor(bootstrap=True, ccp_alpha=0.0, criterion='mse', 
					max_depth=None, max_features='auto', max_leaf_nodes=None, 
					max_samples=None, min_impurity_decrease=0.0, 
					min_impurity_split=None, min_samples_leaf=1, 
					min_samples_split=2, min_weight_fraction_leaf=0.0, 
					n_estimators=100, n_jobs=None, oob_score=False, 
					random_state=None, verbose=0, warm_start=False)'''

# calculating the score and the score is 97.96360799890066% 
m1.score(train1, target) * 100

# predicting the model with other values (testing the data) 
# so AQI is 123.71 
m1.predict([[123, 45, 67, 34, 5, 0, 23]]) 

# Adaboost model 
# importing module 

# defining model 
m2 = AdaBoostRegressor() 

# Fitting the model 
m2.fit(train1, target) 

'''AdaBoostRegressor(base_estimator=None, learning_rate=1.0, loss='linear', 
				n_estimators=50, random_state=None)'''

# calculating the score and the score is 96.15377360010211% 
m2.score(train1, target)*100

# predicting the model with other values (testing the data) 
# so AQI is 94.42105263 
m2.predict([[123, 45, 67, 34, 5, 0, 23]])
