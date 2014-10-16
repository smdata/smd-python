smd-python
==========

Step 1
```python
# generate some random test data
import SMD
SMD = dreload(SMD)
data = SMD.test_data(10)
types = dict([('index', 'int16' ),('values',dict([('C1','float16'), ('C2','int16')]))])
```

Step 2
```python
# create a representation of a SMD data structure in a python dictionary
SMD = dreload(pySMD)
data = SMD.create(data,types) 
```
