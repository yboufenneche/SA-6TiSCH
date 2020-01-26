"""
==================================
The Tipping Problem - The Hard Way
==================================

 Note: This method computes everything by hand, step by step. For most people,
 the new API for fuzzy systems will be preferable. The same problem is solved
 with the new API `in this example <./plot_tipping_problem_newapi.html>`_.

The 'tipping problem' is commonly used to illustrate the power of fuzzy logic
principles to generate complex behavior from a compact, intuitive set of
expert rules.

Input variables
---------------

A number of variables play into the decision about how much to tip while
dining. Consider two of them:

* ``quality`` : Quality of the food
* ``service`` : Quality of the service

Output variable
---------------

The output variable is simply the tip amount, in percentage points:

* ``tip`` : Percent of bill to add as tip


For the purposes of discussion, let's say we need 'high', 'medium', and 'low'
membership functions for both input variables and our output variable. These
are defined in scikit-fuzzy as follows

"""
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Generate universe variables
#   * Quality and service on subjective ranges [0, 10]
#   * Tip has a range of [0, 25] in units of percentage points
x_pr = np.arange(0, 1, 0.001)
x_rsr = np.arange(0, 1, 0.001)
x_selfishness = np.arange(0, 1, 0.001)

# Generate fuzzy membership functions
pr_lo = fuzz.trapmf(x_pr, [0, 0, 0.25, 0.5])
pr_md = fuzz.trimf(x_pr, [0.25, 0.5, 0.75])
pr_hi = fuzz.trapmf(x_pr, [0.5, 0.75, 1, 1])
rsr_lo = fuzz.trapmf(x_rsr, [0, 0, 0.25, 0.5])
rsr_md = fuzz.trimf(x_rsr, [0.25, 0.5, 0.75])
rsr_hi = fuzz.trapmf(x_rsr, [0.5, 0.75, 1, 1])
selfishness_lo = fuzz.trapmf(x_selfishness, [0, 0, 0.333, 0.666])
selfishness_hi = fuzz.trapmf(x_selfishness, [0.333, 0.666, 1, 1])

# Visualize these universes and membership functions
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(x_pr, pr_lo, 'b', linewidth=1.5, label='Pr Low')
ax0.plot(x_pr, pr_md, 'g', linewidth=1.5, label='Pr Medium')
ax0.plot(x_pr, pr_hi, 'r', linewidth=1.5, label='Pr High')
ax0.set_title('Probability')
ax0.legend()

ax1.plot(x_rsr, rsr_lo, 'b', linewidth=1.5, label='RSR Low')
ax1.plot(x_rsr, rsr_md, 'g', linewidth=1.5, label='RSR Medium')
ax1.plot(x_rsr, rsr_hi, 'r', linewidth=1.5, label='RSR High')
ax1.set_title('Request Satisfaction Rate')
ax1.legend()

ax2.plot(x_selfishness, selfishness_lo, 'b', linewidth=1.5, label='Selfishness Low')
ax2.plot(x_selfishness, selfishness_hi, 'r', linewidth=1.5, label='Selfishness High')
ax2.set_title('Selfishness')
ax2.legend()

# Turn off top/right axes
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()
"""
.. image:: PLOT2RST.current_figure

Fuzzy rules
-----------

Now, to make these triangles useful, we define the *fuzzy relationship*
between input and output variables. For the purposes of our example, consider
three simple rules:

1. If the food is bad OR the service is poor, then the tip will be low
2. If the service is acceptable, then the tip will be medium
3. If the food is great OR the service is amazing, then the tip will be high.

Most people would agree on these rules, but the rules are fuzzy. Mapping the
imprecise rules into a defined, actionable tip is a challenge. This is the
kind of task at which fuzzy logic excels.

Rule application
----------------

What would the tip be in the following circumstance:

* Food *quality* was **6.5**
* *Service* was **9.8**

"""

# We need the activation of our fuzzy membership functions at these values.
# The exact values 6.5 and 9.8 do not exist on our universes...
# This is what fuzz.interp_membership exists for!
pr_level_lo = fuzz.interp_membership(x_pr, pr_lo, 0.4)
pr_level_md = fuzz.interp_membership(x_pr, pr_md, 0.4)
pr_level_hi = fuzz.interp_membership(x_pr, pr_hi, 0.4)

rsr_level_lo = fuzz.interp_membership(x_rsr, rsr_lo, 0.1)
rsr_level_md = fuzz.interp_membership(x_rsr, rsr_md, 0.1)
rsr_level_hi = fuzz.interp_membership(x_rsr, rsr_hi, 0.1)

# Now we take our rules and apply them.
active_rule1 = np.fmin(pr_level_lo, rsr_level_lo)
active_rule2 = np.fmin(pr_level_lo, rsr_level_md)
active_rule3 = np.fmin(pr_level_lo, rsr_level_hi)
active_rule4 = np.fmin(pr_level_md, rsr_level_lo)
active_rule5 = np.fmin(pr_level_md, rsr_level_md)
active_rule6 = np.fmin(pr_level_md, rsr_level_hi)
active_rule7 = np.fmin(pr_level_hi, rsr_level_lo)
active_rule8 = np.fmin(pr_level_hi, rsr_level_md)
active_rule9 = np.fmin(pr_level_hi, rsr_level_hi)

# Now we apply this by clipping the top off the corresponding output
# membership function with `np.fmin`

self_activation_hi = np.fmin(active_rule1, selfishness_hi)
self_activation_hi = np.fmin(active_rule2, selfishness_hi)
self_activation_hi = np.fmin(active_rule4, selfishness_hi)

self_activation_lo = np.fmin(active_rule3, selfishness_lo)
self_activation_lo = np.fmin(active_rule5, selfishness_lo)
self_activation_lo = np.fmin(active_rule6, selfishness_lo)
self_activation_lo = np.fmin(active_rule7, selfishness_lo)
self_activation_lo = np.fmin(active_rule8, selfishness_lo)
self_activation_lo = np.fmin(active_rule9, selfishness_lo)


selfishness0 = np.zeros_like(x_selfishness)

# Visualize this
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.fill_between(x_selfishness, selfishness0, self_activation_lo, facecolor='b', alpha=0.7)
ax0.plot(x_selfishness, selfishness_lo, 'b', linewidth=0.5, linestyle='--', )
ax0.fill_between(x_selfishness, selfishness0, self_activation_hi, facecolor='b', alpha=0.7)
ax0.plot(x_selfishness, selfishness_hi, 'r', linewidth=0.5, linestyle='--')
ax0.set_title('Output membership activity')

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

"""
.. image:: PLOT2RST.current_figure

Rule aggregation
----------------

With the *activity* of each output membership function known, all output
membership functions must be combined. This is typically done using a
maximum operator. This step is also known as *aggregation*.

Defuzzification
---------------
Finally, to get a real world answer, we return to *crisp* logic from the
world of fuzzy membership functions. For the purposes of this example
the centroid method will be used.

The result is a tip of **20.2%**.
---------------------------------
"""

# Aggregate all three output membership functions together
aggregated = np.fmax(self_activation_lo, self_activation_hi)

# Calculate defuzzified result
selfishness = fuzz.defuzz(x_selfishness, aggregated, 'centroid')
print("Selfishness = " + str(selfishness))
selfishness_activation = fuzz.interp_membership(x_selfishness, aggregated, selfishness)  # for plot

# Visualize this
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(x_pr, pr_lo, 'b', linewidth=0.5, linestyle='--', )
ax0.plot(x_selfishness, selfishness_hi, 'r', linewidth=0.5, linestyle='--')
ax0.fill_between(x_selfishness, selfishness0, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([selfishness, selfishness], [0, selfishness_activation], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Aggregated membership and result (line)')

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

"""
.. image:: PLOT2RST.current_figure

Final thoughts
--------------

The power of fuzzy systems is allowing complicated, intuitive behavior based
on a sparse system of rules with minimal overhead. Note our membership
function universes were coarse, only defined at the integers, but
``fuzz.interp_membership`` allowed the effective resolution to increase on
demand. This system can respond to arbitrarily small changes in inputs,
and the processing burden is minimal.

"""
