import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def compute_selfishness(pr_value, rsr_value, distance_value):
    """
    Antecedent/Consequent objects
    """
    pr = ctrl.Antecedent(np.arange(0, 1, 0.001), 'pr')
    rsr = ctrl.Antecedent(np.arange(0, 1, 0.001), 'rsr')
    distance = ctrl.Antecedent(np.arange(0, 1, 0.001), 'distance')
    # energy = ctrl.Antecedent(np.arange(0, 100, 1), 'energy')
    selfishness = ctrl.Consequent(np.arange(0, 1, 0.001), 'selfishness')

    """
    Membership functions
    """
    pr['lowPr'] = fuzz.trapmf(pr.universe, [0, 0, 0.25, 0.5])
    pr['mediumPr'] = fuzz.trimf(pr.universe, [0.25, 0.5, 0.75])
    pr['highPr'] = fuzz.trapmf(pr.universe, [0.5, 0.75, 1, 1])

    rsr['lowRsr'] = fuzz.trapmf(rsr.universe, [0, 0, 0.25, 0.5])
    rsr['mediumRsr'] = fuzz.trimf(rsr.universe, [0.25, 0.5, 0.75])
    rsr['highRsr'] = fuzz.trapmf(rsr.universe, [0.5, 0.75, 1, 1])

    distance['near'] = fuzz.trimf(distance.universe, [0, 0, 0.333])
    distance['far'] = fuzz.trapmf(distance.universe, [0, 0.333, 1, 1])

    # energy['crEner'] = fuzz.trapmf(energy.universe, [0, 0, 15, 25])
    # energy['lowEner'] = fuzz.trimf(energy.universe, [15, 30, 45])
    # energy['mediumEner'] = fuzz.trimf(energy.universe, [35, 50, 65])
    # energy['highEner'] = fuzz.trapmf(energy.universe, [55, 70, 100, 100])

    selfishness['veryLowSelfishness']  = fuzz.trapmf(selfishness.universe, [0, 0, 0.1, 0.25])
    selfishness['lowSelfishness']      = fuzz.trimf(selfishness.universe, [0.15, 0.3, 0.45])
    selfishness['mediumSelfishness']   = fuzz.trimf(selfishness.universe, [0.35, 0.5, 0.65])
    selfishness['highSelfishness']     = fuzz.trimf(selfishness.universe, [0.55, 0.7, 0.85])
    selfishness['veryHighSelfishness'] = fuzz.trapmf(selfishness.universe, [0.75, 0.9, 1, 1])


    """
    Fuzzy rules
    """

    rule1 = ctrl.Rule(rsr['lowRsr']     & pr['lowPr']    & distance['near'], selfishness['highSelfishness'])
    rule2 = ctrl.Rule(rsr['lowRsr']     & pr['lowPr']    & distance['far'], selfishness['veryHighSelfishness'])
    rule3 = ctrl.Rule(rsr['lowRsr']     & pr['mediumPr'] & distance['near'], selfishness['mediumSelfishness'])
    rule4 = ctrl.Rule(rsr['lowRsr']     & pr['mediumPr'] & distance['far'], selfishness['highSelfishness'])
    rule5 = ctrl.Rule(rsr['lowRsr']     & pr['highPr']   & distance['near'], selfishness['veryLowSelfishness'])
    rule6 = ctrl.Rule(rsr['lowRsr']     & pr['highPr']   & distance['far'], selfishness['lowSelfishness'])
    rule7 = ctrl.Rule(rsr['mediumRsr']  & pr['lowPr']    & distance['near'], selfishness['highSelfishness'])
    rule8 = ctrl.Rule(rsr['mediumRsr']  & pr['lowPr']    & distance['far'], selfishness['highSelfishness'])
    rule9 = ctrl.Rule(rsr['mediumRsr']  & pr['mediumPr'] & distance['near'], selfishness['lowSelfishness'])
    rule10 = ctrl.Rule(rsr['mediumRsr'] & pr['mediumPr'] & distance['far'], selfishness['mediumSelfishness'])
    rule11 = ctrl.Rule(rsr['mediumRsr'] & pr['highPr']   & distance['near'], selfishness['veryLowSelfishness'])
    rule12 = ctrl.Rule(rsr['mediumRsr'] & pr['highPr']   & distance['far'], selfishness['lowSelfishness'])
    rule13 = ctrl.Rule(rsr['highRsr']   & pr['lowPr']    & distance['near'], selfishness['veryLowSelfishness'])
    rule14 = ctrl.Rule(rsr['highRsr']   & pr['lowPr']    & distance['far'], selfishness['lowSelfishness'])
    rule15 = ctrl.Rule(rsr['highRsr']   & pr['mediumPr'] & distance['near'], selfishness['veryLowSelfishness'])
    rule16 = ctrl.Rule(rsr['highRsr']   & pr['mediumPr'] & distance['far'], selfishness['veryLowSelfishness'])
    rule17 = ctrl.Rule(rsr['highRsr']   & pr['highPr']   & distance['near'], selfishness['veryLowSelfishness'])
    rule18 = ctrl.Rule(rsr['highRsr']   & pr['highPr']   & distance['far'], selfishness['veryLowSelfishness'])


    """
    Control System Creation and Simulation
    """

    selfishness_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
                                           rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18])
    selfEngine = ctrl.ControlSystemSimulation(selfishness_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    selfEngine.input['pr'] = pr_value
    selfEngine.input['rsr'] = rsr_value
    selfEngine.input['distance'] = distance_value

    # Crunch the numbers
    selfEngine.compute()

    # We can view the result as well as visualize it.
    # print selfEngine.output['selfishness']
    # selfishness.view(sim=selfEngine)
    return selfEngine.output['selfishness']

# compute_selfishness(0.8, 0.9, 0.8)

