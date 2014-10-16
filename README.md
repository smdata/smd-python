smd-python
==========

```matlab
% initialize smd structure
dataset = smd.create(data, {'state', 'observation'})
% add global attributes 
dataset.attr.description = 'example data: mixture of 3 gaussians with equal occupancy';
dataset.attr.state_mean = state_mean;
dataset.attr.state_noise = state_noise;
dataset.attr.max_length = max_length;
