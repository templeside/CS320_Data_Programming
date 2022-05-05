# project: p7
# submitter: cjhon
# partner: none
# hours: 10

import pandas as pd
import os
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate

class UserPredictor:
    lr = LogisticRegression()

    def fit(self, train_users, train_logs, train_y):
        logs_seconds = train_logs.groupby(['user_id']).sum()
        train_users_seconds = train_users.merge(logs_seconds, on='user_id', how='left')
        train_users_seconds['seconds'] = train_users_seconds['seconds'].fillna(0)
        
        self.lr.fit(train_users_seconds[["seconds"]],train_y[['y']] )
        cv_results = cross_validate(self.lr, train_users_seconds[["seconds"]],train_y[['y']], cv=3)


    def predict(self, test_users, test_logs):
        logs_seconds = test_logs.groupby(['user_id']).sum()
        test_users_seconds = test_users.merge(logs_seconds, on='user_id', how='left')
        test_users_seconds['seconds'] = test_users_seconds['seconds'].fillna(0)
       
        return self.lr.predict(test_users_seconds[['seconds']])
        
