'''
'	CrowdTruth Configuration File
'	Version 0.1
'''

class Configuration():

	# collection name
	name = 'ControCurator'

	# inputColumns to use
	inputColumns = []
	# outputColumns to use
	outputColumns = []


	# units to use
	units = []
	# workers to use
	workers = []
	# jobs to use
	jobs = []


	def processUnit(self, unit):
		return True

	def processWorker(self, worker):
		return True

	'''
	'	customize the judgments before being processed
	'''
	def processJudgments(self, judgments):
		judgments['controversy'] = judgments.apply(lambda row: ','.join([col+'-'+row[col] for col in self.output.keys()]), axis=1)
		judgments.drop(self.output.keys(), axis=1, inplace=True)

		return judgments


	'''
	'	customize the results
	'''
	def processResults(self, results):
		import pandas as pd
		from scipy.stats import chi2_contingency
		import itertools

		# pearson_correlation
		#results['annotations'].columns = [c.replace('output.','') for c in results['annotations'].columns]
		results['correlations'] = pd.DataFrame()
		for col in results['annotations'].columns:
			#results['annotations'][col].apply(lambda x: str(x))
			# corr freq
			answers = results['judgments'][col].value_counts().keys()
			for a in answers:
				#print results['judgments'][col].apply(lambda x: 1 if x == a else 0)
				results['correlations'][col.replace('output.','')+'.'+a] = results['judgments'][col].apply(lambda x: 1 if x == a else 0)
		
		#results['correlations'] = results['judgments'][results['annotations'].columns].reset_index()
		results['correlations'] = results['correlations'].corr(method='pearson')
		results['correlations'] = results['correlations'].sort_index(axis=1).sort_index(axis=0)


		# independence test
		# chisq with p
		df = results['judgments'][results['annotations'].columns]
		results['independence'] = pd.DataFrame(index=results['annotations'].columns,columns=results['annotations'].columns)
		combinations = list(itertools.combinations(results['annotations'].columns,2))
		for cola, colb in combinations:
			#print cola, colb
			confusion_matrix = pd.crosstab(df[cola], df[colb])
			contingency = chi2_contingency(confusion_matrix)
			
			chisq, p = contingency[:2]
			results['independence'][cola][colb] = 'chisq = {}, p = {}'.format(chisq, p)
			results['independence'][colb][cola] = 'chisq = {}, p = {}'.format(chisq, p)

		return results

