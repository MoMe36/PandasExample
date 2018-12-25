import pandas as pd
import numpy as np 
import csv 
import glob 
import os 


def make_csv(nb, values=  100): 

	try: 
		os.makedirs('test_csv') 
	except: 
		pass 

	for i in range(nb): 
		x = np.random.uniform(0.,1., (values)).tolist() 
		with open('test_csv/{}.csv'.format(i), 'w') as file: 
			writer = csv.writer(file) 
			for xx in x: 	
				writer.writerow([xx]) 

make_csv(3) 

dfs = [] 

files = glob.glob('test_csv/*.csv')

for f in files: 
	df = pd.read_csv(f, header = None) 
	dfs.append(df) 

df = pd.concat(dfs, axis = 1) 
print(df.head())
