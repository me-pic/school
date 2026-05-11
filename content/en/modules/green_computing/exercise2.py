"""
## Exercise 2

Calculate the total energy and carbon emissions for the jobs listed in the Slurm log files using the formula given below.

Do not forget to pay attention to the units of each variable!

### Instructions

Replace the `...` by your code. You will need the formulas below:

(1) CPU energy (Wh) = CPU time (hours) x TDP / number of CPU cores

(2) RAM energy (Wh) = Max Memory x VMC x Runtime (hours)

(3) Total energy (kWh) = ((CPU energy + RAM energy) / 1000) x PUE

(4) Carbon emissions (g) = Total energy x VMC x Carbon intensity

The static variables are already define.

NOTE: 1 GB = 1000 MB = 1000000 KB
"""

# Define static variables we'll use below
# Thermal design power - a measure of energy efficiency for our processor
tdp = 200

# Total number of cores on the processor we've used
num_core = 32

# Volatile memory consumption, reflect W of energy used per GB of memory
vmc = 0.3725

# Power use effectiveness, reflecting the energy overheads needed for computing
pue = 1.28

# Carbon intensity, reflecting grams of carbon dioxide emitted per kWh of energy used
carbon_intensity = 177

# Complete your code below
...