import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 240671999 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
        alpha = 0.03
        count = np.array([x_success, y_success])
        nobs = np.array([x_cnt, y_cnt])
        z,p = proportions_ztest(count, nobs, value=0, alternative='two-sided')
    
        if p < alpha:
            return True
        else:
            return False
