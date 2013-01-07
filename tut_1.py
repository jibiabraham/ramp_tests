import pandas
from ramp import *

training_data = pandas.read_csv('data/train.csv')
print training_data

context = DataContext(store='~/data/insults/ramp', data=training_data)
base_config = Configuration(target='Insult', metrics=[metrics.AUC()],)