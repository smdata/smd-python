smd-python
==========

Step 1
```python
# load the SMD python package
import SMD
SMD = dreload(SMD)
```

Step 2
```python
# generate some random test data and identiy the data types
data = SMD.test_data(10)
types = dict([('index', 'int16' ),('values',dict([('C1','float16'), ('C2','int16')]))])
```

Step 3
```python
# create a representation of a SMD data structure in a python dictionary
data = SMD.create(data,types) 
```

Data manipulations supported by the SMD-python package
```python
# check that the data diction is valid SMD format
ValidSMD = SMD.isvalid(data)
print(ValidSMD)
```

```python
# saves a SMD dictionary into valid JSON file
SMD.write_json('TestSave', data)
```

```python
# load .smd data into a valid SMD python dictionary
data = SMD.read_json('TestSave.smd')
```

```python
# deep coppy the data sets to be combined
import copy
ds1 = copy.deepcopy(data)
ds2 = copy.deepcopy(data)
ds3 = copy.deepcopy(data)
# merge the data sets using merge_data 
MergedData = SMD.merge_data(ds1, ds2, ds3)
```

