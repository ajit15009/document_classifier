import csv
from proposal_sample import proposal

def read_training_data():
	data=[]
	with open('check.csv',newline='') as csvfile:
		spam=csv.reader(csvfile,dialect='excel',delimiter=',',quotechar='"')
		for row in spam:
			data.append(row)
	return data

def process_data(data):
	labels=data[0]
	list_of_samples=[]
	data=data[1:]
	for i in range(len(data)):
		x=proposal(data[i])
		list_of_samples.append(x)
	return labels,list_of_samples

data=read_training_data()
labels,data=process_data(data)
for i in range(len(data)):
	print(data[i])