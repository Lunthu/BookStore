# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 21:22:23 2016

@author: Victor
"""

import pandas as pd
import numpy as np

def set_tour_data(data, tour_number):
    current_tour = pd.DataFrame(data[tour_number])
    current_tour.columns = ['Date', 'Home', 'Score', 'Guest', 'Viewers']
    buffer = pd.DataFrame(current_tour['Score'].str.split(' : ', 1).tolist(), columns = ['Home Score', 'Guest Score'])
    current_tour['Home Score'] = buffer['Home Score']
    current_tour['Guest Score'] = buffer['Guest Score']
    current_tour['Home Score'] = pd.to_numeric(current_tour['Home Score'], errors = 'coerce')
    current_tour['Guest Score'] = pd.to_numeric(current_tour['Guest Score'], errors = 'coerce')
    current_tour['Difference'] = (current_tour['Home Score'] - current_tour['Guest Score'])
    current_tour['Winner'] = current_tour['Difference'].apply(lambda x: 'H' if x >0 else 'D' if x==0 else 'G')
    current_tour = current_tour.drop(labels = ['Date', 'Viewers'], axis = 1, inplace = False)
    return current_tour
    
def set_result_data(path):
    result_data = pd.read_excel(io = str(path))
    result_data['Home Eugene'] = pd.to_numeric(result_data['Home Eugene'], errors = 'coerce')
    result_data['Guest Eugene'] = pd.to_numeric(result_data['Guest Eugene'], errors = 'coerce')
    result_data['Home Victor'] = pd.to_numeric(result_data['Home Victor'], errors = 'coerce')
    result_data['Guest Victor'] = pd.to_numeric(result_data['Guest Victor'], errors = 'coerce')
    result_data['Difference Eugene'] = result_data['Home Eugene'] - result_data['Guest Eugene']
    result_data['Difference Victor'] = result_data['Home Victor'] - result_data['Guest Victor']
    result_data['Winner Eugene'] = result_data['Difference Eugene'].apply(lambda x: 'H' if x >0 else 'D' if x==0 else 'G')
    result_data['Winner Victor'] = result_data['Difference Victor'].apply(lambda x: 'H' if x >0 else 'D' if x==0 else 'G')
    return result_data
    
def set_score_table(analyze_data, result_data):
    score_table = pd.DataFrame(columns = ['Home', 'Guest', 'Score', 'Eugene Prediction', 'Victor Prediction','Eugene Winner', 'Victor Winner', 'Eugene Difference', 'Victor Difference', 'Eugene Accurate Score', 'Victor Accurate Score','Eugene Result', 'Victor Result'])
    score_table['Home'] = analyze_data['Home']
    score_table['Guest'] = analyze_data['Guest']
    score_table['Score'] = analyze_data['Score']
    score_table['Eugene Winner'] =  (analyze_data['Winner']==result_data['Winner Eugene'])
    score_table['Victor Winner'] =  (analyze_data['Winner']==result_data['Winner Victor'])
    score_table['Eugene Difference'] = (analyze_data['Difference']==result_data['Difference Eugene'])   
    score_table['Victor Difference'] = (analyze_data['Difference']==result_data['Difference Victor'])
    score_table['Eugene Accurate Score'] = ((analyze_data['Home Score']==result_data['Home Eugene']) & (analyze_data['Guest Score']==result_data['Guest Eugene']))
    score_table['Victor Accurate Score'] = ((analyze_data['Home Score']==result_data['Home Victor']) & (analyze_data['Guest Score']==result_data['Guest Victor']))
    
    return score_table


def counting_scores(score_table, result_data, name):
    dfLength = len(score_table)-1
    i = 0
    while i <=dfLength:
        if score_table['{0} Accurate Score'.format(name)][i]==True:
            score_table['{0} Result'.format(name)][i] = 3
        elif ((score_table['{0} Difference'.format(name)][i]==True) & (analyze_data['Winner'][i]=='D')):
            score_table['{0} Result'.format(name)][i] = 1.5
        elif ((score_table['{0} Difference'.format(name)][i]==True) & ((analyze_data['Winner'][i]=='H')|(analyze_data['Winner'][i]=='G'))):
            score_table['{0} Result'.format(name)][i] = 2
        elif score_table['{0} Winner'.format(name)][i]==True:
            score_table['{0} Result'.format(name)][i] = 1
        else:
            score_table['{0} Result'.format(name)][i] = 0
        score_table['{0} Prediction'.format(name)][i] = (str(result_data['Home {0}'.format(name)][i]) + ' : ' + str(result_data['Guest {0}'.format(name)][i]))
        i+=1
    return score_table

data_read = pd.read_html('http://www.sports.ru/epl/calendar/?s=5540', encoding = 'utf8')
print ('print number of tour')
j = 2
analyze_data = set_tour_data(data_read, j)
path = 'D:/DB/epl/epl_data_tour_5_2016-17.xls'
result_data = set_result_data(path)
final_data = set_score_table(analyze_data, result_data)
final_data = counting_scores(final_data, result_data, 'Eugene')
final_data = counting_scores(final_data, result_data, 'Victor')

print ('Eugene Score: ', final_data['Eugene Result'].sum(), 'Victor Score: ', final_data['Victor Result'].sum())

    
