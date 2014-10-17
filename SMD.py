def read_json(filename):
	#smd.read_json(filename): Loads a SMD structure from JSON formated .smd file
	print('read_jason')
	import json
	json_data = open(filename).read()
	smd = json.loads(json_data)
	return smd

def isvalid(dataset):
	#smd.isvalid(dataset): Checks if supplied struct is a valid SMD instance.	
	#This only looks to see if the correct fields are present it has not been
	#generalized to ensure that the correct data type is present in each field
	#The output will indicate which parts of the data structure do not conform
	#to the expected format 
	print('isvalid')

	
	# Check if the top level fields in exist
	if "id" in dataset.keys():
  		TopID = 1
	else:
  		TopID = 0
	
	#if "Types" in dataset.keys():
	if "types" in dataset.keys():
  		TopTypes = 1
	else:
  		TopTypes = 0
  		
	if "attr" in dataset.keys():
  		TopAttr = 1;
  		if "data_package" in dataset["attr"].keys():
  			TopDataPackage = 1
		else:
  			TopDataPackage = 0	
	else:
  		TopAttr = 0	
	
	if "data" in dataset.keys():
  		TopData = 1
	else:
  		TopData = 0
  		
	ValidID = [];
	ValidDataAttr = [];
	ValidIndex = [];
	ValidValude = [];

	for i in range(0, len(dataset["data"])):
				#print i
		try:

			# Check if "id" are okay			
			if len(dataset["data"][i]["id"])==32:
				ValidID.append(1)
			else:
				ValidID.append(0)
			
			# Check if "attr" exists			
			if "attr" in dataset["data"][i].keys():
  				ValidDataAttr.append(1)
  				#print ValidDataAttr
			else:
  				ValidDataAttr.append(0)
  				
  			# Check if "index" exists	
  			# Currently time
  			if "index" in dataset["data"][i].keys():		
			#if "time" in dataset["data"][i].keys():
  				ValidIndex.append(1)
  				#print ValidDataAttr
			else:
  				ValidIndex.append(0)
  				
  			# Check if "values" exists	
  			# Currently signal		
			if "values" in dataset["data"][i].keys():
			#if "signal" in dataset["data"][i].keys():
  				ValidValude.append(1)
  				#print ValidDataAttr
			else:
  				ValidValude.append(0)	

		except:
 	       		print i
 	   		#pass
	
	
	ValidSMD = dict([('TopID', TopID),
					 ('TopTypes',TopTypes),
					 ('TopAttr', TopAttr),
					 ('TopDataPackage', TopDataPackage),
					 ('TopData', TopData),
					 ('ValidID', ValidID), 
					 ('ValidDataAttr', ValidDataAttr), 
					 ('ValidIndex', ValidIndex), 
					 ('ValidValude', ValidValude)])
	
	return ValidSMD
	
def filter(dataset):
	#smd.filter(dataset): Returns a filtered dataset by matching id and attr values, 
	#or by applying a custom function with boolean output to each trace.

	print('filter')
	return dataset
	
def merge_data(*arg):
	#smd.merge(data1, data2, ...): Returns a merged dataset containing all traces in 
	#multiple datasets.
	#A new top level 'id' is generated that should be unique to this dataset
    import hashlib
    import json
    import cPickle as pickle
    
    print('merge')

    MergedData = arg[0].copy()
    for j in range(1,len(arg)):
        tl = len(arg[j]['data'])
        print len(MergedData['data'])
        print len(arg[j]['data'])
        for k in range(0,tl):
            TempData = arg[j]['data'][k]
            MergedData['data'].append(TempData)

	data_md5 = hashlib.md5(json.dumps(pickle.dumps(MergedData), sort_keys=True)).hexdigest()
	MergedData['id'] = data_md5

    return MergedData
	
def write_json(filename, dataset):
	#smd.write_json(filename, dataset): Saves a SMD structure as JSON
    import json
    import numpy
	
    class NumpyAwareJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, numpy.ndarray) and obj.ndim == 1:
                return obj.tolist()
            return json.JSONEncoder.default(self, obj)
	
	print('write_json')
    #j=json.dumps(dataset,cls=NumpyAwareJSONEncoder)
    j=json.dumps(dataset,cls=NumpyAwareJSONEncoder, sort_keys=True, indent=4, separators=(',', ': '))

    f=open((filename+'.smd'),"w")
    f.write(j)
    f.close()
	
	
def create(data, types): 
	#smd.create(filename, dataset): Creates valid SMD dict from data and specified data types
    print('create')    
    import hashlib
    import json
    import cPickle as pickle
    import numpy as np

	# generates a hash id based on all the input data
    data_md5 = hashlib.md5(json.dumps(pickle.dumps(data), sort_keys=True)).hexdigest()
    tid = data_md5

    SMD = dict([('id', tid ),('attr',{"data_package":'pySMD'}),('types',types),('data',[])])
		
    for j in range(0,len(data)):
        tid = hashlib.md5(json.dumps(pickle.dumps(data[j]), sort_keys=True)).hexdigest()
        DataTypes = dict.items(types['values'])
        TempDict = types['values'].keys()
        TempDict = dict.fromkeys(TempDict)
        
        for k in range(0,len(types['values'])):
            TempDict[DataTypes[k][0]]  = np.array(np.hstack(data[j][k,:]), dtype=DataTypes[k][1])

        index = range(0, len(data[j][0,:]))
        index = np.array(index, dtype=types['index'])

        TempData = dict([('id', tid ),('index', np.hstack(index)),('values', TempDict),('attr','')])
        SMD['data'].append(TempData)
       
    return SMD


def test_data(ntraces):	
	#smd.testdata(ntraces): generated ntraces of randomly generated two channel data for 
	#test cases
	import random
	import numpy as np
	data = []
	for i in range(0,10):
		tdata = []
		for j in range(100):
			tdata.append(random.gauss(1,5))
		data.append(np.vstack((tdata,tdata)))

	return data
