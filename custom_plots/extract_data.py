from __future__ import division

import json
import numpy as np

from utilities import *
#*
# This file serves to extract data (kpis) from json files containainig simulation logs
# Author: Yassine Boufenneche
#*

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# selfishness_rates = ["000", "010", "020", "030", "040", "050", "060", "070", "080", "090", "100"]
selfishness_rates = ["000", "020", "040", "060", "080", "100"]

# ***
# Extract latencies of all sent packets of the whole network for a specific selfishness rate from .dat.kpi file
# ***
def extract_all_latencies (self_rate, numMotes, numRun, prefix):
    with open('kpis/{0}{1}_{2}_exec_numMotes_{3}.dat.kpi'.format(prefix, numRun, self_rate, numMotes)) as source:
        row_data = json.load(source)

    all_latencies = []

    for moteId in range(1, numMotes):
        try:
            current = row_data["0"][str(moteId)]["latencies"]
            all_latencies =  all_latencies + current
            #print (sum(current)/len(current))
        except:
            print(
                "No values for latencies --> NumRun : {0} & NumMotes : {1} & SelfRate : {2} & Mote : {3}".format(
                    numRun, numMotes, self_rate, moteId))

    return all_latencies

# ***
# Extract lifetimes of each mote for a specific selfishness rate from .dat.kpi file
# ***
def extract_lifetimes_AA_years (self_rate, numMotes, numRun, prefix):
    with open('kpis/{0}{1}_{2}_exec_numMotes_{3}.dat.kpi'.format(prefix, numRun, self_rate, numMotes)) as source:
        row_data = json.load(source)

    lifetime_AA_years = []
    
    for moteId in range(1, numMotes):
        try:
            current = row_data["0"][str(moteId)]["lifetime_AA_years"]
            lifetime_AA_years.append(current)
            #print (sum(current)/len(current))
        except:
            lifetime_AA_years.append(-1)
            print("No value for lifetime_AA_years --> NumRun : {0} & NumMotes : {1} & SelfRate : {2} & Mote : {3}".format(
                numRun, numMotes, self_rate, moteId))

    return lifetime_AA_years

# ***
# Mean lifetime_AA_years for all selfishness rates
# ***
def all_lifetime_AA_years(numMotes, numRun, prefix):
    all = []
    for rate in selfishness_rates:
        all.append(mean_pos(extract_lifetimes_AA_years(rate, numMotes, numRun, prefix)))

    return all

# ***
# Extract mean pdr of the whole network for a specific selfishness rate from .dat.kpi file
# ***
def extract_pdr (self_rate, numMotes, numRun, prefix):
    with open('kpis/{0}{1}_{2}_exec_numMotes_{3}.dat.kpi'.format(prefix, numRun, self_rate, numMotes)) as source:
        row_data = json.load(source)

    pdr = row_data["0"]["global-stats"]["e2e-upstream-delivery"][0]["value"]

    return pdr

# Mean pdr of the whole network for all selfishness rates and a given run
def all_pdrs(numMotes, numRun, prefix):
    all = []
    for rate in selfishness_rates:
        all.append(extract_pdr(rate, numMotes, numRun, prefix))

    return all

# Mean joining time of the whole network for all selfishness rates and a given run
def all_joins(numMotes, numRun, prefix):
    all = []
    for rate in selfishness_rates:
        all.append(mean_pos(join_every_mote(rate, numMotes, numRun, prefix)))

    return all

# Mean Sync time of the whole network for all selfishness rates and a given run
def all_syncs(numMotes, numRun, prefix):
    all = []
    for rate in selfishness_rates:
        all.append(mean_pos(sync_every_mote(rate, numMotes, numRun, prefix)))

    return all


# ***
# Extract a value of global kpi (of the whole network) for a specific selfishness rate from .dat.kpi file
# ***
def extract_global(kpi_name, kpi_property, self_rate, numMotes, numRun, prefix):
    with open('kpis/{0}{1}_{2}_exec_numMotes_{3}.dat.kpi'.format(prefix, numRun, self_rate, numMotes)) as source:
        row_data = json.load(source)

    value = row_data["0"]["global-stats"][kpi_name][0][kpi_property]
    return value

# ***
# Extract values of a global kpi for all selfishness rates
# ***
def all_global(kpi_name, kpi_property, numMotes, numRun, prefix):
    all = []
    for rate in selfishness_rates:
        all.append(extract_global(kpi_name, kpi_property, rate, numMotes, numRun, prefix))

    return all

#
# Compute throughputs of the whole network for all selfishness rates
#
def all_throughput (numSlotframes, numMotes, numRun, prefix):
    data = all_global("app_packets_received", "total", numMotes, numRun, prefix)
    throughputs = []
    for x in data:
        throughputs.append(x*0.01 / numSlotframes*101)

    return  throughputs

#
# Extract the avrage latency of every mote for a specific selfishness rate from .dat.kpi file
#
def avg_latency_every_mote (self_rate, numMotes, numRun, prefix):
    with open('kpis/{0}{1}_{2}_exec_numMotes_{3}.dat.kpi'.format(prefix, numRun, self_rate, numMotes)) as source:
        row_data = json.load(source)

    latencies = []

    for moteId in range(1, numMotes):
        try:
            current = row_data["0"][str(moteId)]["latency_avg_s"]
            latencies.append(current)
        except:
            latencies.append(-1)
            print("No value for latency_avg_s --> NumRun : {0} & NumMotes : {1} & SelfRate : {2} & Mote : {3}".format(numRun, numMotes, self_rate, moteId))
        #print (sum(current)/len(current))

    return latencies

#
# Extract the PDR of every mote for a specific selfishness rate from .dat.kpi file
#
def pdr_every_mote (self_rate, numMotes, numRun, prefix):
    with open('kpis/{0}{1}_{2}_exec_numMotes_{3}.dat.kpi'.format(prefix, numRun, self_rate, numMotes)) as source:
        row_data = json.load(source)

    pdrs = []

    for moteId in range(1, numMotes):
        try:
            current = row_data["0"][str(moteId)]["upstream_reliability"]
            pdrs.append(current)
        except:
            pdrs.append(-1)
            print("No value for upstream_relaibilty --> NumRun : {0} & NumMotes : {1} & SelfRate : {2} & Mote : {3}".format(numRun, numMotes, self_rate, moteId))
        #print (sum(current)/len(current))

    return pdrs

#
# Extract the number of packets received from every mote for a specific selfishness rate from .dat.kpi file
#
def pkts_received_every_mote (self_rate, numMotes, numRun, prefix):
    with open('kpis/{0}{1}_{2}_exec_numMotes_{3}.dat.kpi'.format(prefix, numRun, self_rate, numMotes)) as source:
        row_data = json.load(source)

    num_packets_recieved = []

    for moteId in range(1, numMotes):
        try:
            current = row_data["0"][str(moteId)]["upstream_num_rx"]
            num_packets_recieved.append(current)
        except:
            num_packets_recieved.append(-1)
            print("No value for upstream_num_rx")
        #print (sum(current)/len(current))

    return num_packets_recieved

#
# Convert a list of numbers of received_packets to a list of throughputs
#
def throughputs (packets_received, numSlotframes):
    throughputs = []
    for x in packets_received:
        throughputs.append(x / (0.01 * numSlotframes * 101))

    return throughputs


def lifetimes_AA_years_every_mote (self_rate, numMotes, numRun, prefix):
    with open('kpis/{0}{1}_{2}_exec_numMotes_{3}.dat.kpi'.format(prefix, numRun, self_rate, numMotes)) as source:
        row_data = json.load(source)

    lifetime = []

    for moteId in range(1, numMotes):
        try:
            current = row_data["0"][str(moteId)]["lifetime_AA_years"]
            lifetime.append(current)
            #print (sum(current)/len(current))
        except:
            lifetime.append(-1)
            print("No value for lifetime_AA_years --> NumRun : {0} & NumMotes : {1} & SelfRate : {2} & Mote : {3}".format(
            numRun, numMotes, self_rate, moteId))

    return lifetime

#
# Extract the Join Time of every mote for a specific selfishness rate from .dat.kpi file
#
def join_every_mote (self_rate, numMotes, numRun, prefix):
    with open('kpis/{0}{1}_{2}_exec_numMotes_{3}.dat.kpi'.format(prefix, numRun, self_rate, numMotes)) as source:
        row_data = json.load(source)

    joins = []

    for moteId in range(1, numMotes):
        try:
            current = row_data["0"][str(moteId)]["join_time_s"]
            joins.append(current)
        except:
            joins.append(-1)
            print("No value for join_time_s --> NumRun : {0} & NumMotes : {1} & SelfRate : {2} & Mote : {3}".format(numRun, numMotes, self_rate, moteId))
        #print (sum(current)/len(current))

    return joins

#
# Extract the Sync Time of every mote for a specific selfishness rate from .dat.kpi file
#
def sync_every_mote (self_rate, numMotes, numRun, prefix):
    with open('kpis/{0}{1}_{2}_exec_numMotes_{3}.dat.kpi'.format(prefix, numRun, self_rate, numMotes)) as source:
        row_data = json.load(source)

    syncs = []

    for moteId in range(1, numMotes):
        try:
            current = row_data["0"][str(moteId)]["sync_time_s"]
            syncs.append(current)
        except:
            syncs.append(-1)
            print("No value for sync_time_s --> NumRun : {0} & NumMotes : {1} & SelfRate : {2} & Mote : {3}".format(numRun, numMotes, self_rate, moteId))
        #print (sum(current)/len(current))

    return syncs