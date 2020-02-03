import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def compute_selfishness(pr_value, rsr_value):
    """
    Antecedent/Consequent objects
    """
    pr = ctrl.Antecedent(np.arange(0, 1, 0.001), 'pr')
    rsr = ctrl.Antecedent(np.arange(0, 1, 0.001), 'rsr')
    distance = ctrl.Antecedent(np.arange(0, 10, 1), 'distange')
    energy = ctrl.Antecedent(np.arange(0, 100, 1), 'energy')
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

    distance['near'] = fuzz.trapmf(distance.universe, [0, 0, 2, 4])
    distance['far'] = fuzz.trapmf(distance.universe, [2, 4, 10, 10])

    energy['crEner'] = fuzz.trapmf(energy.universe, [0, 0, 15, 25])
    energy['lowEner'] = fuzz.trimf(energy.universe, [15, 30, 45])
    energy['mediumEner'] = fuzz.trimf(energy.universe, [35, 50, 65])
    energy['highEner'] = fuzz.trapmf(energy.universe, [55, 70, 100, 100])

    selfishness['lowSelfishness'] = fuzz.trapmf(selfishness.universe, [0, 0, 0.333, 0.666])
    selfishness['highSelfishness'] = fuzz.trapmf(selfishness.universe, [0.333, 0.666, 1, 1])

    """
    Fuzzy rules
    """

    rule1 = ctrl.Rule(pr['lowPr'] & rsr['lowRsr'], selfishness['highSelfishness'])
    rule2 = ctrl.Rule(pr['lowPr'] & rsr['mediumRsr'], selfishness['highSelfishness'])
    rule3 = ctrl.Rule(pr['lowPr'] & rsr['highRsr'], selfishness['lowSelfishness'])
    rule4 = ctrl.Rule(pr['mediumPr'] & rsr['lowRsr'], selfishness['highSelfishness'])
    rule5 = ctrl.Rule(pr['mediumPr'] & rsr['mediumRsr'], selfishness['lowSelfishness'])
    rule6 = ctrl.Rule(pr['mediumPr'] & rsr['highRsr'], selfishness['lowSelfishness'])
    rule7 = ctrl.Rule(pr['highPr'] & rsr['lowRsr'], selfishness['lowSelfishness'])
    rule8 = ctrl.Rule(pr['highPr'] & rsr['mediumRsr'], selfishness['lowSelfishness'])
    rule9 = ctrl.Rule(pr['highPr'] & rsr['highRsr'], selfishness['lowSelfishness'])

    """
    Control System Creation and Simulation
    """

    selfishness_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
    selfEngine = ctrl.ControlSystemSimulation(selfishness_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    selfEngine.input['pr'] = pr_value
    selfEngine.input['rsr'] = rsr_value

    # Crunch the numbers
    selfEngine.compute()

    # We can view the result as well as visualize it.
    # print selfEngine.output['selfishness']
    # selfishness.view(sim=selfEngine)
    return selfEngine.output['selfishness']

