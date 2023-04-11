import pandas as pd
import numpy as np


chat_id = 240671999 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
        alpha = 0.03
        count = np.array([x_success, y_success])
        nobs = np.array([x_cnt, y_cnt])
        stat, pval = proportions_ztest(count, nobs, alternative='smaller')
    
        if pval < alpha:
            return True
        else:
            return False
