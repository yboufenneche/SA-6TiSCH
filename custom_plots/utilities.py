# **
# ** Compute the mean of three different runs
# ** Ignore motes that didn't join the network (negative values)
# **
def mean_runs (list1, list2, list3):
    result = []
    for i in range(len(list1)):
        denominator = 3
        s = 0
        if (list1[i] < 0):
            denominator = denominator - 1
        else:
            s = s + list1[i]

        if (list2[i] < 0):
            denominator = denominator - 1
        else:
            s = s + list2[i]

        if (list3[i] < 0):
            denominator = denominator - 1
        else:
            s = s + list3[i]

        if (denominator > 0):
            e = s/denominator
            result.append(e)

    return  result

#
# Purificate a list (omit entires with negative values)
#
def pur(list):
    result = []
    for i in range(len(list)):
        if list[i] < 0:
            result.append(list[i])

    return result

#
# Find the mean of positive values in a list
#
def mean_pos(list):
    s = 0
    denominator = 0
    for i in range (len(list)):
        if (list[i] >= 0 ):
            s = s + list[i]
            denominator = denominator + 1

    return (s/denominator)

#
#
#
def ylims(numMotes, ax1, ax2, ax3 = None, ax4 = None, ax5 = None, ax6 = None):
    try:
        if (numMotes == 20):
            ax1.set_ylim([0, 13])
            ax2.set_ylim([0, 13])
            ax3.set_ylim([0.6, 1.05])
            ax4.set_ylim([0.6, 1.05])
            ax5.set_ylim([0, 13])
            ax6.set_ylim([0, 13])
        elif (numMotes == 60):
            ax1.set_ylim([0, 21])
            ax2.set_ylim([0, 21])
            ax3.set_ylim([0.1, 1.05])
            ax4.set_ylim([0.1, 1.05])
            ax5.set_ylim([0, 13])
            ax6.set_ylim([0, 13])
        else:
            ax1.set_ylim([0, 35])
            ax2.set_ylim([0, 35])
            ax3.set_ylim([0, 1.05])
            ax4.set_ylim([0, 1.05])
            ax5.set_ylim([0, 13])
            ax6.set_ylim([0, 13])
    except:
        print("Axe not existing !")


# ***
# Normalize an array
# ***
def normalize (tab):
    data = np.array(tab)
    normalized = []
    _min = np.min(tab)
    _max = np.max(tab)
    for x in data:
        normalized.append((x-_min)/(_max-_min))

    return normalized