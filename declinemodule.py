import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from datetime import datetime
import math
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

class decline_curve_analysis:
	def __init__(self, uwi):
		self.uwi = uwi


	def dca_match(self):

		filepath = ''

		mainDF = pd.read_csv(filepath)
		mainDF = mainDF.set_index('UWI')
		mainDF.replace(to_replace = 0, value =0.01)

		df_working = mainDF.loc[self.uwi]
		df_working["Days"] = np.arange(len(df_working))

		# this is the dca function
		# use curve_fit on dca_func to find best b value for each iteration on t1
		def dca_func(x, b):
			histMatch = q2 / np.power( ( 1 + ( b * di * (x - t2) ) ), (1/b) )
			return histMatch

		xdata = df_working[df_working['Days'] > 0]['Days']

		ydata = df_working[df_working['Days'] > 0]['Oil Rate (bbl/d)']

		t1=t2=df_working["Days"].max()
		q2=df_working["Oil Rate (bbl/d)"][t2]

		results_dict = {"t1":[],"b":[], "di":[], "error":[]}

		#loop backwarsd from last day of prod and calculate di for each 120 day interval
		#then use optimization function to find optimal b value for given di
		while t1 > 120:
			t1=t1-30
			q1=df_working["Oil Rate (bbl/d)"][t1]

			# calc di based on t2 (fixed) and t1 (iterated)
			di = (1/(t2-t1)) * (np.log(q1/q2))
			if (di == float("inf")) or (di == float("-inf")) or (di<=0):
				# skip iterations that result in a bad di value
				continue

			try:
				# match the decline to the data
				popt, pcov = curve_fit(dca_func, xdata, ydata, bounds=(0, 1))
				b = tuple(popt)[0].round(3)
				p_sigma = np.sum(abs(df_working["Oil Rate (bbl/d)"] - (q2 / np.power( ( 1 + ( b * di * (df_working["Days"] - t2) ) ), (1/b) ))))
				results_dict["t1"].append(t1)
				results_dict["b"].append(b)
				results_dict["di"].append(di)
				results_dict["error"].append(round(float(p_sigma),3))
			except ValueError:
				pass


		# to find t1, b, di parameters with mininmum error
		ix = 0
		min = results_dict["error"][0]
		for i in range(len(results_dict["error"])):
			if results_dict["error"][i] < min:
				min = results_dict["error"][i]
				ix = i

		t1 = results_dict["t1"][ix]
		b = results_dict["b"][ix]
		di = results_dict["di"][ix]
		error = results_dict["error"][ix]
		
		if b != 0:
		    df_working["histMatch"] = q2 / np.power( ( 1 + ( b * di * (df_working["Days"] - t2) ) ), (1/b) )
		else:
		    df_working["histMatch"] = q2 * np.exp(-di*(df_working["Days"] - t2))

		return df_working, t1, t2, b, di, error


