from __future__ import division

import numpy as np
import matplotlib.pyplot as plt


from extract_data import *
from utilities import *

# names = ["0", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
names = ["0", "20", "40", "60", "80", "100"]
rates = ['000', '020', '040', '060', '080', '100']


######### Ploting CDFs curves ###########
#
# Plot latencies CDF
def plot_latencies_cdf (numMotes, prefix, x_lim = 40):

    all_latencies = []
    sorted_data   = []
    yvals         = []

    labels = ['No selfisn nodes', '20 % of motes are selfish', '40 % of motes are selfish', '60 % of motes are selfish', '80 % of motes are selfish', 'All nodes are selfish']

    for rate in rates:
        all_latencies.append(extract_all_latencies(rate, numMotes, '1', prefix) + extract_all_latencies(rate, numMotes, '2', prefix) + extract_all_latencies(rate, numMotes, '3', prefix))
        sorted_data.append(np.sort(all_latencies[-1]))
        yvals.append(np.arange(len(sorted_data[-1])) / float(len(sorted_data[-1]) - 1))
        plt.plot(sorted_data[-1], yvals[-1], label=labels.pop(0))


    plt.xlabel("Latency (s)")
    plt.ylabel("CDF")
    plt.xticks(np.arange(0, 44, 4))
    plt.grid(True)
    if (prefix == "R"):
        plt.title('{0} nodes [SA-6TiSCH]'.format(numMotes), fontsize = "10", fontweight="bold")
    else:
        plt.title('{0} nodes [6TiSCH]'.format(numMotes), fontsize = "10", fontweight="bold")

    plt.legend(prop={'size': 8})
    plt.xlim(right=x_lim, left=-2)
    plt.savefig('figs/png/{0}cdf-latency-{1}-motes.png'.format(prefix, numMotes), format='png')
    plt.savefig('figs/eps/{0}cdf-latency-{1}-motes.eps'.format(prefix, numMotes), format='eps')
    plt.show()
    plt.close()
#
#
# Plot latencies CDF and boxes
def plot_latencies_cdf_v3 (x_lim = 40):

    nMotes = [20, 60, 100]

    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(9, 13.5))

    for i in range(len(nMotes)):
        all_latencies = []
        sorted_data = []
        yvals = []
        all_latencies_r = []
        sorted_data_r = []
        yvals_r = []
        labels = ['No selfisn nodes', '20 % of motes are selfish', '40 % of motes are selfish',
                  '60 % of motes are selfish', '80 % of motes are selfish', 'All nodes are selfish']
        for rate in rates:
            all_latencies.append(extract_all_latencies(rate, nMotes[i], '1', "") + extract_all_latencies(rate, nMotes[i], '2', "") + extract_all_latencies(rate, nMotes[i], '3', ""))
            all_latencies_r.append(extract_all_latencies(rate, nMotes[i], '1', "R") + extract_all_latencies(rate, nMotes[i], '2', "R") + extract_all_latencies(rate, nMotes[i], '3', "R"))
            sorted_data.append(np.sort(all_latencies[-1]))
            sorted_data_r.append(np.sort(all_latencies_r[-1]))
            yvals.append(np.arange(len(sorted_data[-1])) / float(len(sorted_data[-1]) - 1))
            yvals_r.append(np.arange(len(sorted_data_r[-1])) / float(len(sorted_data_r[-1]) - 1))
            lab = labels.pop(0)

            axes[0 + i, 0].plot(sorted_data[-1], yvals[-1], label= lab)
            axes[0 + i, 1].plot(sorted_data_r[-1], yvals_r[-1], label= lab)

    for axe in axes.flat:
        axe.yaxis.grid(True)
        axe.set_xlim(right=x_lim, left=-2)
        axe.legend(prop={'size': 8})
        axe.set_xticks(np.arange(0, 44, 4))
        axe.grid(True)

    axes[0, 0].set_ylabel("CDF")
    axes[1, 0].set_ylabel("CDF")
    axes[2, 0].set_ylabel("CDF")

    axes[2, 0].set_xlabel("Latency (s)")
    axes[2, 1].set_xlabel("Latency (s)")

    axes[0, 0].set_title('(A) - 20 nodes [6TiSCH]', fontsize = "10", fontweight="bold")
    axes[0, 1].set_title('(B) - 20 nodes [SA-6TiSCH]', fontsize = "10", fontweight="bold")
    axes[1, 0].set_title('(C) - 60 nodes [6TiSCH]', fontsize="10", fontweight="bold")
    axes[1, 1].set_title('(D) - 60 nodes [SA-6TiSCH]', fontsize="10", fontweight="bold")
    axes[2, 0].set_title('(E) - 100 nodes [6TiSCH]', fontsize="10", fontweight="bold")
    axes[2, 1].set_title('(F) - 100 nodes [SA-6TiSCH]', fontsize="10", fontweight="bold")

    plt.savefig('figs/png/compare-cdf-latency-20-60-100-motes.png', format='png')
    plt.savefig('figs/eps/compare-cdf-latency-20-60-100-motes.eps', format='eps')
    plt.show()
    plt.close()
#

#
# Plot latencies CDF
def plot_latencies_cdf_v2 (numMotes, x_lim = 40):

    all_latencies = []
    sorted_data   = []
    yvals         = []

    all_latencies_r = []
    sorted_data_r   = []
    yvals_r         = []

    labels = ['No selfisn nodes', '20 % of motes are selfish', '40 % of motes are selfish', '60 % of motes are selfish', '80 % of motes are selfish', 'All nodes are selfish']
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 4.5))

    for rate in rates:
        all_latencies.append(extract_all_latencies(rate, numMotes, '1', "") + extract_all_latencies(rate, numMotes, '2', "") + extract_all_latencies(rate, numMotes, '3', ""))
        all_latencies_r.append(extract_all_latencies(rate, numMotes, '1', "R") + extract_all_latencies(rate, numMotes, '2', "R") + extract_all_latencies(rate, numMotes, '3', "R"))
        sorted_data.append(np.sort(all_latencies[-1]))
        sorted_data_r.append(np.sort(all_latencies_r[-1]))
        yvals.append(np.arange(len(sorted_data[-1])) / float(len(sorted_data[-1]) - 1))
        yvals_r.append(np.arange(len(sorted_data_r[-1])) / float(len(sorted_data_r[-1]) - 1))
        lab = labels.pop(0)

        axes[0].plot(sorted_data[-1], yvals[-1], label= lab)
        axes[1].plot(sorted_data_r[-1], yvals_r[-1], label= lab)

    for axe in axes:
        axe.set_xlabel("Latency (s)")
        axe.set_xticks(np.arange(0, 44, 4))
        axe.grid(True)
        axe.legend(prop={'size': 8})
        axe.set_xlim(right=x_lim, left=-2)

    axes[0].set_ylabel("CDF")
    axes[0].set_title('{0} nodes [6TiSCH]'.format(numMotes), fontsize = "10", fontweight="bold")
    axes[1].set_title('{0} nodes [SA-6TiSCH]'.format(numMotes), fontsize = "10", fontweight="bold")

    plt.savefig('figs/png/compare-cdf-latency-{0}-motes.png'.format(numMotes), format='png')
    plt.savefig('figs/eps/compare-cdf-latency-{0}-motes.eps'.format(numMotes), format='eps')
    plt.show()
    plt.close()
#
#
#

# Plot CDF latencies for 6TiSCH and SA-6TiSCH for a given selfishness rate in the same figure
def plot_compare_cdf_latency(numMotes, rate, x_lim = 42):
    all_latencies1 = extract_all_latencies(rate, numMotes, "1", "R") + extract_all_latencies(rate, numMotes, "2", "R") + extract_all_latencies(rate, numMotes, "3", "R")
    all_latencies2 = extract_all_latencies(rate, numMotes, "1", "") + extract_all_latencies(rate, numMotes, "2", "") + extract_all_latencies(rate, numMotes, "3", "")
    sorted_data1 = np.sort(all_latencies1)
    sorted_data2 = np.sort(all_latencies2)
    _yvals1 = np.arange(len(sorted_data1)) / float(len(sorted_data1) - 1)
    _yvals2 = np.arange(len(sorted_data2)) / float(len(sorted_data2) - 1)
    plt.xlabel("Latency (s)")
    plt.ylabel("CDF")
    plt.plot(sorted_data1, _yvals1, color='blue', label='SA-6TiSCH')
    plt.plot(sorted_data2, _yvals2, color='red', label='6TiSCH')

    plt.xticks(np.arange(0, 44, 4))
    plt.grid(True)
    plt.title('{0} nodes [selfishness rate = {1} % ]'.format(numMotes, rate))
    plt.legend(prop={'size': 8})
    plt.xlim(right=x_lim, left=-2)
    plt.savefig('figs/png/compare-cdf-latency-{0}-motes-self-rate-{1}.png'.format(numMotes, rate), format='png')
    plt.savefig('figs/eps/compare-cdf-latency-{0}-motes-self-rate-{1}.eps'.format(numMotes, rate), format='eps')
    plt.show()
    plt.close()

# Plot kpi with reaction and without reaction on the same figure for three different numbers of motes
def plot_compare (kpi_name, data1, data2, data3, data4, data5, data6, _xlabel, _ylabel, y_lim1, y_lim2):
    plt.xlabel(_xlabel)
    plt.ylabel(_ylabel)
    plt.plot(names, data1, "r-o", label="6TiSCH (20 nodes)")
    plt.plot(names, data2, "b-o", label = "SA-6TiSCH (20 nodes)")
    plt.plot(names, data3, "r-^", label="6TiSCH (60 nodes)")
    plt.plot(names, data4, "b-^", label="SA-6TiSCH (60 nodes)")
    plt.plot(names, data5, "r-D", label="6TiSCH (100 nodes)")
    plt.plot(names, data6, "b-D", label="SA-6TiSCH (100 nodes)")
    plt.ylim([y_lim1, y_lim2])
    plt.grid(True)
    plt.legend(prop={'size': 8})
    plt.savefig('figs/png/{0}-20-60-100-motes.png'.format(kpi_name), format='png')
    plt.savefig('figs/eps/{0}-20-60-100-motes.eps'.format(kpi_name), format='eps')
    plt.show()
    plt.close()

# Plot kpi on the same figure for three different numbers of motes
def plot_curves (kpi_name, data1, data2, data3, _xlabel, _ylabel, y_lim1, y_lim2):
    plt.xlabel(_xlabel)
    plt.ylabel(_ylabel)
    plt.plot(names, data1, "r-o", label= "20 nodes")
    plt.plot(names, data2, "r-D", label = "60 nodes")
    plt.plot(names, data3, "r-^", label= "100 nodes")
    plt.ylim([y_lim1, y_lim2])
    plt.grid(True)
    plt.legend(prop={'size': 8})
    plt.savefig('figs/png/{0}-20-60-100-motes.png'.format(kpi_name), format='png')
    plt.savefig('figs/eps/{0}-20-60-100-motes.eps'.format(kpi_name), format='eps')
    plt.show()
    plt.close()
#
#
#
def plot_box (kpi_name1, kpi_property1, unit1, kpi_name2, kpi_property2, unit2, sixtisch1, sa_sixtisch1, sixtisch2, sa_sixtisch2, numMotes):
    # plt.xlabel("Selfishness rate (%)")
    # plt.ylabel("{0} {1} {2}".format(kpi_property, kpi_name, unit))
    # plt.grid(True)
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(9, 9))

    bplot1 = axes[0, 0].boxplot(sixtisch1, labels = names)
    axes[0, 0].set_title('{0} motes [6TiSCH]'.format(numMotes), fontsize = "10", fontweight="bold")
    axes[0, 0].set_ylabel("{0} {1} {2}".format(kpi_property1, kpi_name1, unit1))

    bplot2 = axes[0, 1].boxplot(sa_sixtisch1, labels=names)
    axes[0, 1].set_title('{0} motes [SA-6TiSCH]'.format(numMotes), fontsize = "10", fontweight="bold")
    # axes[0, 1].set_ylabel("{0} {1} {2}".format(kpi_property1, kpi_name1, unit1))


    bplot3 = axes[1, 0].boxplot(sixtisch2, labels=names)
    # axes[1, 0].set_title('{0} motes [6TiSCH]'.format(numMotes))
    axes[1, 0].set_ylabel("{0} {1} {2}".format(kpi_property2, kpi_name2, unit2))
    axes[1, 0].set_xlabel("Selfishness rate (%)")

    bplot4 = axes[1, 1].boxplot(sa_sixtisch2, labels=names)
    # axes[1, 1].set_title('{0} motes [SA-6TiSCH]'.format(numMotes))
    # axes[1, 1].set_ylabel("{0} {1} {2}".format(kpi_property2, kpi_name2, unit2))
    axes[1, 1].set_xlabel("Selfishness rate (%)")

    ylims(numMotes, kpi_name1, axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1])

    for ax in axes.flat:
        ax.yaxis.grid(True)

    plt.savefig('figs/png/{0}-{1}-boxes-{2}-motes.png'.format(kpi_name1, kpi_name2, numMotes), format = 'png')
    plt.savefig('figs/eps/{0}-{1}-boxes-{2}-motes.eps'.format(kpi_name1, kpi_name2, numMotes), format = 'eps')
    plt.show()
    plt.close()

#
#
#
def plot_box_v2 (kpi, ylabel, sixtisch1, sa_sixtisch1, sixtisch2, sa_sixtisch2, sixtisch3, sa_sixtisch3):

    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(9, 13.5))

    bplot1 = axes[0, 0].boxplot(sixtisch1, labels = names)
    axes[0, 0].set_title('(A) - 20 motes [6TiSCH]', fontsize = "10", fontweight="bold")
    axes[0, 0].set_ylabel(ylabel)

    bplot2 = axes[0, 1].boxplot(sa_sixtisch1, labels=names)
    axes[0, 1].set_title('(B) - 20 motes [SA-6TiSCH]', fontsize = "10", fontweight="bold")


    bplot3 = axes[1, 0].boxplot(sixtisch2, labels=names)
    axes[1, 0].set_ylabel(ylabel)
    axes[2, 0].set_xlabel("Selfishness rate (%)")
    axes[1, 0].set_title('(C) - 60 motes [6TiSCH]', fontsize="10", fontweight="bold")

    bplot4 = axes[1, 1].boxplot(sa_sixtisch2, labels=names)
    axes[2, 1].set_xlabel("Selfishness rate (%)")
    axes[1, 1].set_title('(D) - 60 motes [SA-6TiSCH]', fontsize="10", fontweight="bold")

    bplot5 = axes[2, 0].boxplot(sixtisch3, labels=names)
    axes[2, 0].set_ylabel(ylabel)
    axes[2, 0].set_xlabel("Selfishness rate (%)")
    axes[2, 0].set_title('(E) - 100 motes [6TiSCH]', fontsize="10", fontweight="bold")

    bplot6 = axes[2, 1].boxplot(sa_sixtisch3, labels=names)
    axes[2, 1].set_title('(F) - 100 motes [SA-6TiSCH]', fontsize="10", fontweight="bold")
    axes[2, 1].set_xlabel("Selfishness rate (%)")


    # ylims(numMotes, kpi_name1, axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1])

    for ax in axes.flat:
        ax.yaxis.grid(True)

    plt.savefig('figs/png/{}-boxes-20-60-100-motes.png'.format(kpi), format = 'png')
    plt.savefig('figs/eps/{}-boxes-20-60-100-motes.eps'.format(kpi), format = 'eps')
    plt.show()
    plt.close()
#
#
def plot_box_v3 (kpi, ylabel, sixtisch1, sixtisch2, sixtisch3):

    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(6, 18))

    bplot1 = axes[0].boxplot(sixtisch1, labels = names)
    axes[0].set_title('(A) - 20 motes', fontsize = "10", fontweight="bold")
    axes[0].set_ylabel(ylabel)

    bplot2 = axes[1].boxplot(sixtisch2, labels=names)
    axes[1].set_ylabel(ylabel)
    axes[1].set_title('(B) - 60 motes', fontsize="10", fontweight="bold")

    bplot3 = axes[2].boxplot(sixtisch3, labels=names)
    axes[2].set_ylabel(ylabel)
    axes[2].set_xlabel("Misbehavior rate (%)")
    axes[2].set_title('(C) - 100 motes', fontsize="10", fontweight="bold")

    # ylims(numMotes, kpi_name1, axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1])

    for ax in axes.flat:
        ax.yaxis.grid(True)

    plt.savefig('figs/png/{}-boxes-6tisch-20-60-100-motes.png'.format(kpi), format = 'png')
    plt.savefig('figs/eps/{}-boxes-6tisch-20-60-100-motes.eps'.format(kpi), format = 'eps')
    plt.show()
    plt.close()

# *************************************************************************************

def pdrs_all_runs(nMotes):
    return mean_runs(all_pdrs(nMotes, "1", ""),
                     all_pdrs(nMotes, "2", ""),
                     all_pdrs(nMotes, "3", ""))

def pdrs_all_runs_r(nMotes):
    return mean_runs(all_pdrs(nMotes, "1", "R"),
                     all_pdrs(nMotes, "2", "R"),
                     all_pdrs(nMotes, "3", "R"))

def throughputs_all_runs(nMotes):
    return mean_runs(all_throughput(15000, nMotes, "1", ""),
                     all_throughput(15000, nMotes, "2", ""),
                     all_throughput(15000, nMotes, "3", ""))

def throughputs_all_runs_r(nMotes):
    return mean_runs(all_throughput(15000, nMotes, "1", "R"),
                     all_throughput(15000, nMotes, "2", "R"),
                     all_throughput(15000, nMotes, "3", "R"))

def min_life_all_runs(nMotes):
    return mean_runs(all_global("network_lifetime", "min", nMotes, "1", ""),
                     all_global("network_lifetime", "min", nMotes, "2", ""),
                     all_global("network_lifetime", "min", nMotes, "3", ""))

def min_life_all_runs_r(nMotes):
    return mean_runs(all_global("network_lifetime", "min", nMotes, "1", "R"),
                     all_global("network_lifetime", "min", nMotes, "2", "R"),
                     all_global("network_lifetime", "min", nMotes, "3", "R"))

def aa_life_all_runs(nMotes):
    return mean_runs(all_lifetime_AA_years(nMotes, "1", ""),
                     all_lifetime_AA_years(nMotes, "2", ""),
                     all_lifetime_AA_years(nMotes, "3", ""))

def aa_life_all_runs_r(nMotes):
    return mean_runs(all_lifetime_AA_years(nMotes, "1", "R"),
                     all_lifetime_AA_years(nMotes, "2", "R"),
                     all_lifetime_AA_years(nMotes, "3", "R"))

def joins_all_runs(nMotes):
    return mean_runs(all_joins(nMotes, "1", ""),
                     all_joins(nMotes, "2", ""),
                     all_joins(nMotes, "3", ""))

def joins_all_runs_r(nMotes):
    return mean_runs(all_joins(nMotes, "1", "R"),
                     all_joins(nMotes, "2", "R"),
                     all_joins(nMotes, "3", "R"))

def syncs_all_runs(nMotes):
    return mean_runs(all_syncs(nMotes, "1", ""),
                     all_syncs(nMotes, "2", ""),
                     all_syncs(nMotes, "3", ""))

def syncs_all_runs_r(nMotes):
    return mean_runs(all_syncs(nMotes, "1", "R"),
                     all_syncs(nMotes, "2", "R"),
                     all_syncs(nMotes, "3", "R"))


#*************************************      Generating plots      **********************

def call_plots ():

    # jointime_by_1000 = []
    # jointime_all_runs = mean_runs(all_global("joining-time", "mean", numMotes, "1", ""),
    #                               all_global("joining-time", "mean", numMotes, "2", ""),
    #                               all_global("joining-time", "mean", numMotes, "3", ""))
    #
    # for x in jointime_all_runs:
    #     jointime_by_1000.append(x / 1000)
    #
    # r_jointime_by_1000 = []
    # jointime_all_runs_r = mean_runs(all_global("joining-time", "mean", numMotes, "1", "R"),
    #                                 all_global("joining-time", "mean", numMotes, "2", "R"),
    #                                 all_global("joining-time", "mean", numMotes, "3", "R"))
    #
    # for x in jointime_all_runs_r:
    #     r_jointime_by_1000.append(x / 1000)


    # ************************************************************************************
    # plot_compare("pdr",
    #              pdrs_all_runs(20), pdrs_all_runs_r(20),
    #              pdrs_all_runs(60), pdrs_all_runs_r(60),
    #              pdrs_all_runs(100), pdrs_all_runs_r(100),
    #              "Selfishness rate (%)", "PDR",
    #              0.3, 1.05)
    #
    # plot_compare("throughput",
    #              throughputs_all_runs(20), throughputs_all_runs_r(20),
    #              throughputs_all_runs(60), throughputs_all_runs_r(60),
    #              throughputs_all_runs(100), throughputs_all_runs_r(100),
    #              "Selfishness rate (%)", "Throughput (packet/s)",
    #              3, 33)
    #
    # # plot_compare("min-lifetime",
    # #              min_life_all_runs(20), min_life_all_runs_r(20),
    # #              min_life_all_runs(60), min_life_all_runs_r(60),
    # #              min_life_all_runs(100), min_life_all_runs_r(100),
    # #              "Selfishness rate (%)", "Network lifetime (min)")
    #
    # plot_compare("avg-lifetime",
    #              aa_life_all_runs(20),  aa_life_all_runs_r(20),
    #              aa_life_all_runs(60),  aa_life_all_runs_r(60),
    #              aa_life_all_runs(100), aa_life_all_runs_r(100),
    #              "Selfishness rate (%)", "Average network lifetime (years)",
    #              2.5, 6)

    plot_curves("join",
                 joins_all_runs(20),
                 joins_all_runs(60),
                 joins_all_runs(100),
                 "Misbehavior rate (%)", "Joining time",
                 300, 2600)

    plot_curves("sync",
                 syncs_all_runs(20),
                 syncs_all_runs(60),
                 syncs_all_runs(100),
                 "Selfishness rate (%)", "Synchronization time",
                 300, 3000)



def lists_latencies(numMotes, prefix):
    return[mean_runs(extract_all_latencies("000", numMotes, 1, prefix),
                     extract_all_latencies("000", numMotes, 2, prefix),
                     extract_all_latencies("000", numMotes, 3, prefix)),
           mean_runs(extract_all_latencies("020", numMotes, 1, prefix),
                     extract_all_latencies("020", numMotes, 2, prefix),
                     extract_all_latencies("020", numMotes, 3, prefix)),
           mean_runs(extract_all_latencies("040", numMotes, 1, prefix),
                     extract_all_latencies("040", numMotes, 2, prefix),
                     extract_all_latencies("040", numMotes, 3, prefix)),
           mean_runs(extract_all_latencies("060", numMotes, 1, prefix),
                     extract_all_latencies("060", numMotes, 2, prefix),
                     extract_all_latencies("060", numMotes, 3, prefix)),
           mean_runs(extract_all_latencies("080", numMotes, 1, prefix),
                     extract_all_latencies("080", numMotes, 2, prefix),
                     extract_all_latencies("080", numMotes, 3, prefix)),
           mean_runs(extract_all_latencies("100", numMotes, 1, prefix),
                     extract_all_latencies("100", numMotes, 2, prefix),
                     extract_all_latencies("100", numMotes, 3, prefix))]

def lists_avg_latencies(numMotes, prefix):
    return [
        mean_runs(avg_latency_every_mote("000", numMotes, 1, prefix),
                  avg_latency_every_mote("000", numMotes, 2, prefix),
                  avg_latency_every_mote("000", numMotes, 3, prefix)),
        mean_runs(avg_latency_every_mote("020", numMotes, 1, prefix),
                  avg_latency_every_mote("020", numMotes, 2, prefix),
                  avg_latency_every_mote("020", numMotes, 3, prefix)),
        mean_runs(avg_latency_every_mote("040", numMotes, 1, prefix),
                  avg_latency_every_mote("040", numMotes, 2, prefix),
                  avg_latency_every_mote("040", numMotes, 3, prefix)),
        mean_runs(avg_latency_every_mote("060", numMotes, 1, prefix),
                  avg_latency_every_mote("060", numMotes, 2, prefix),
                  avg_latency_every_mote("060", numMotes, 3, prefix)),
        mean_runs(avg_latency_every_mote("080", numMotes, 1, prefix),
                  avg_latency_every_mote("080", numMotes, 2, prefix),
                  avg_latency_every_mote("080", numMotes, 3, prefix)),
        mean_runs(avg_latency_every_mote("100", numMotes, 1, prefix),
                  avg_latency_every_mote("100", numMotes, 2, prefix),
                  avg_latency_every_mote("100", numMotes, 3, prefix))]

def lists_pdrs (numMotes, prefix):
    return [
        mean_runs(pdr_every_mote("000", numMotes, 1, prefix),
                  pdr_every_mote("000", numMotes, 2, prefix),
                  pdr_every_mote("000", numMotes, 3, prefix)),
        mean_runs(pdr_every_mote("020", numMotes, 1, prefix),
                  pdr_every_mote("020", numMotes, 2, prefix),
                  pdr_every_mote("020", numMotes, 3, prefix)),
        mean_runs(pdr_every_mote("040", numMotes, 1, prefix),
                  pdr_every_mote("040", numMotes, 2, prefix),
                  pdr_every_mote("040", numMotes, 3, prefix)),
        mean_runs(pdr_every_mote("060", numMotes, 1, prefix),
                  pdr_every_mote("060", numMotes, 2, prefix),
                  pdr_every_mote("060", numMotes, 3, prefix)),
        mean_runs(pdr_every_mote("080", numMotes, 1, prefix),
                  pdr_every_mote("080", numMotes, 2, prefix),
                  pdr_every_mote("080", numMotes, 3, prefix)),
        mean_runs(pdr_every_mote("100", numMotes, 1, prefix),
                  pdr_every_mote("100", numMotes, 2, prefix),
                  pdr_every_mote("100", numMotes, 3, prefix))]


def lists_throughputs (numMotes, prefix, numSlotframes):
    return [
        mean_runs(throughputs(pkts_received_every_mote("000", numMotes, 1, prefix), 15000),
                  throughputs(pkts_received_every_mote("000", numMotes, 2, prefix), 15000),
                  throughputs(pkts_received_every_mote("000", numMotes, 3, prefix), 15000)),
        mean_runs(throughputs(pkts_received_every_mote("020", numMotes, 1, prefix), 15000),
                  throughputs(pkts_received_every_mote("020", numMotes, 2, prefix), 15000),
                  throughputs(pkts_received_every_mote("020", numMotes, 3, prefix), 15000)),
        mean_runs(throughputs(pkts_received_every_mote("040", numMotes, 1, prefix), 15000),
                  throughputs(pkts_received_every_mote("040", numMotes, 2, prefix), 15000),
                  throughputs(pkts_received_every_mote("040", numMotes, 3, prefix), 15000)),
        mean_runs(throughputs(pkts_received_every_mote("060", numMotes, 1, prefix), 15000),
                  throughputs(pkts_received_every_mote("060", numMotes, 2, prefix), 15000),
                  throughputs(pkts_received_every_mote("060", numMotes, 3, prefix), 15000)),
        mean_runs(throughputs(pkts_received_every_mote("080", numMotes, 1, prefix), 15000),
                  throughputs(pkts_received_every_mote("080", numMotes, 2, prefix), 15000),
                  throughputs(pkts_received_every_mote("080", numMotes, 3, prefix), 15000)),
        mean_runs(throughputs(pkts_received_every_mote("100", numMotes, 1, prefix), 15000),
                  throughputs(pkts_received_every_mote("100", numMotes, 2, prefix), 15000),
                  throughputs(pkts_received_every_mote("100", numMotes, 3, prefix), 15000))]


def lists_lifetime_AA (numMotes, prefix):
    return[
        mean_runs(lifetimes_AA_years_every_mote("000", numMotes, 1, prefix),
                  lifetimes_AA_years_every_mote("000", numMotes, 2, prefix),
                  lifetimes_AA_years_every_mote("000", numMotes, 3, prefix)),
        mean_runs(lifetimes_AA_years_every_mote("020", numMotes, 1, prefix),
                  lifetimes_AA_years_every_mote("020", numMotes, 2, prefix),
                  lifetimes_AA_years_every_mote("020", numMotes, 3, prefix)),
        mean_runs(lifetimes_AA_years_every_mote("040", numMotes, 1, prefix),
                  lifetimes_AA_years_every_mote("040", numMotes, 2, prefix),
                  lifetimes_AA_years_every_mote("040", numMotes, 3, prefix)),
        mean_runs(lifetimes_AA_years_every_mote("060", numMotes, 1, prefix),
                  lifetimes_AA_years_every_mote("060", numMotes, 2, prefix),
                  lifetimes_AA_years_every_mote("060", numMotes, 3, prefix)),
        mean_runs(lifetimes_AA_years_every_mote("080", numMotes, 1, prefix),
                  lifetimes_AA_years_every_mote("080", numMotes, 2, prefix),
                  lifetimes_AA_years_every_mote("080", numMotes, 3, prefix)),
        mean_runs(lifetimes_AA_years_every_mote("100", numMotes, 1, prefix),
                  lifetimes_AA_years_every_mote("100", numMotes, 2, prefix),
                  lifetimes_AA_years_every_mote("100", numMotes, 3, prefix))]


def lists_joins (numMotes, prefix):
    return [
        mean_runs(join_every_mote("000", numMotes, 1, prefix),
                  join_every_mote("000", numMotes, 2, prefix),
                  join_every_mote("000", numMotes, 3, prefix)),
        mean_runs(join_every_mote("020", numMotes, 1, prefix),
                  join_every_mote("020", numMotes, 2, prefix),
                  join_every_mote("020", numMotes, 3, prefix)),
        mean_runs(join_every_mote("040", numMotes, 1, prefix),
                  join_every_mote("040", numMotes, 2, prefix),
                  join_every_mote("040", numMotes, 3, prefix)),
        mean_runs(join_every_mote("060", numMotes, 1, prefix),
                  join_every_mote("060", numMotes, 2, prefix),
                  join_every_mote("060", numMotes, 3, prefix)),
        mean_runs(join_every_mote("080", numMotes, 1, prefix),
                  join_every_mote("080", numMotes, 2, prefix),
                  join_every_mote("080", numMotes, 3, prefix)),
        mean_runs(join_every_mote("100", numMotes, 1, prefix),
                  join_every_mote("100", numMotes, 2, prefix),
                  join_every_mote("100", numMotes, 3, prefix))]


def lists_syncs (numMotes, prefix):
    return [
        mean_runs(sync_every_mote("000", numMotes, 1, prefix),
                  sync_every_mote("000", numMotes, 2, prefix),
                  sync_every_mote("000", numMotes, 3, prefix)),
        mean_runs(sync_every_mote("020", numMotes, 1, prefix),
                  sync_every_mote("020", numMotes, 2, prefix),
                  sync_every_mote("020", numMotes, 3, prefix)),
        mean_runs(sync_every_mote("040", numMotes, 1, prefix),
                  sync_every_mote("040", numMotes, 2, prefix),
                  sync_every_mote("040", numMotes, 3, prefix)),
        mean_runs(sync_every_mote("060", numMotes, 1, prefix),
                  sync_every_mote("060", numMotes, 2, prefix),
                  sync_every_mote("060", numMotes, 3, prefix)),
        mean_runs(sync_every_mote("080", numMotes, 1, prefix),
                  sync_every_mote("080", numMotes, 2, prefix),
                  sync_every_mote("080", numMotes, 3, prefix)),
        mean_runs(sync_every_mote("100", numMotes, 1, prefix),
                  sync_every_mote("100", numMotes, 2, prefix),
                  sync_every_mote("100", numMotes, 3, prefix))]


def call_boxes():

    # plot_box_v2("latency", "Latency (s)",
    #             lists_avg_latencies(20, ""),
    #             lists_avg_latencies(20, "R"),
    #             lists_avg_latencies(60, ""),
    #             lists_avg_latencies(60, "R"),
    #             lists_avg_latencies(100, ""),
    #             lists_avg_latencies(100, "R"))
    #
    # plot_box_v2("pdr", "PDR",
    #             lists_pdrs(20, ""),
    #             lists_pdrs(20, "R"),
    #             lists_pdrs(60, ""),
    #             lists_pdrs(60, "R"),
    #             lists_pdrs(100, ""),
    #             lists_pdrs(100, "R")
    #             )
    #
    # plot_box_v2("throughput", "Throughput (packet/s)",
    #             lists_throughputs(20, "", 15000),
    #             lists_throughputs(20, "R", 15000),
    #             lists_throughputs(60, "", 15000),
    #             lists_throughputs(60, "R", 15000),
    #             lists_throughputs(100, "", 15000),
    #             lists_throughputs(100, "R", 15000),
    #             )
    #
    # plot_box_v2("lifetime", "Network lifetime (years)",
    #             lists_lifetime_AA(20, ""),
    #             lists_lifetime_AA(20, "R"),
    #             lists_lifetime_AA(60, ""),
    #             lists_lifetime_AA(60, "R"),
    #             lists_lifetime_AA(100, ""),
    #             lists_lifetime_AA(100, "R")
    #             )

    plot_box_v3("join", "Joining time",
                lists_joins(20, ""),
                lists_joins(60, ""),
                lists_joins(100, "")
                )

    plot_box_v3("sync", "Sync time",
                lists_syncs(20, ""),
                lists_syncs(60, ""),
                lists_syncs(100, "")
                )

# **********************************************************************************************

# plot_latencies_cdf_v3(40)
# call_plots()
# call_boxes()

# print("pdrs 20     : {0}".format(pdrs_all_runs(20)))
# print("pdrs 60     : {0}".format(pdrs_all_runs(60)))
# print("pdrs 100    : {0}".format(pdrs_all_runs(100)))
# print("pdrs 100 (R): {0}".format(pdrs_all_runs_r(100)))
# print('***')
# print("throughput 20     : {0}".format(throughputs_all_runs(20)))
# print("throughput 60     : {0}".format(throughputs_all_runs(60)))
# print("throughput 100    : {0}".format(throughputs_all_runs(100)))
# print("throughput 100 (R): {0}".format(throughputs_all_runs_r(100)))

print(joins_all_runs(20))
print(joins_all_runs(60))
print(joins_all_runs(100))



