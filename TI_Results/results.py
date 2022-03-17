import numpy as np
import matplotlib.pyplot as plt
import csv

folder = "extended"

results_file = folder + "_results.csv"


def uncAddition(A=1., B=1., sigmaA=0., sigmaB=0., a=1., b=1., sigmaAB=0.):
    f = (a * A) + (b * B)
    sigmaf = np.sqrt((a * sigmaA)**2
                     + (b * sigmaB)**2
                     + (2 * a * b * sigmaAB))
    return f, sigmaf


def integrate(x, data, errors):
    # Data: is ab nx1 array that contains n number of f values
    # while errors contains  their absolute standard deviation
    # x:    is the independent variable of the f values
    # Obviously x and f should have the same number of rows
    integralAve = 0.
    integralStd = 0.
    for i in range(1, len(data)):
        trapzPartAve, trapzPartStd = uncAddition(A=data[i - 1],
                                                 sigmaA=errors[i - 1],
                                                 a=(x[i] - x[i - 1]) / 2.0,
                                                 B=data[i],
                                                 sigmaB=errors[i],
                                                 b=(x[i] - x[i - 1]) / 2.0)
        integralAve += trapzPartAve
        integralStd += trapzPartStd

    return integralAve, integralStd


with open(results_file, "w", newline="", encoding='utf8') as results:
    fieldnames = ["n-ALA", "Free_eng", "error"]
    csv_writer = csv.DictWriter(results, fieldnames=fieldnames)
    csv_writer.writeheader()  # Write headers for each column

    for i in range(1, 11):

        if i < 10:

            dHdl_file = "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/0" + \
                str(i) + "ALA/" + folder + "/L01_v1/dHdl_test.dat"

            data = np.loadtxt(dHdl_file, delimiter=",")

            x = data[:, 0]
            y = data[:, 1]
            y_err_pre = data[:, 2]

            y_err = np.nan_to_num(y_err_pre)

            Integral, Error = integrate(x, y, y_err)

            # with open(results_file, "w", newline="", encoding='utf8') as results:
            #     fieldnames = ["n-ALA", "Free_eng", "error"]
            #     csv_writer = csv.DictWriter(results, fieldnames=fieldnames)
            #     csv_writer.writeheader()  # Write headers for each column

            csv_writer.writerow(
                {"n-ALA": i, "Free_eng": Integral, "error": Error})

        if i == 10:

            dHdl_file = "/home/ignacio/DonElias/DiegoArmando/NPT.Lambda/10ALA/" + \
                folder + "/L01_v1/dHdl_test.dat"

            data = np.loadtxt(dHdl_file, delimiter=",")

            x = data[:, 0]
            y = data[:, 1]
            y_err_pre = data[:, 2]

            y_err = np.nan_to_num(y_err_pre)

            Integral, Error = integrate(x, y, y_err)

            # with open(results_file, "w", newline="", encoding='utf8') as results:
            #     fieldnames = ["n-ALA", "Free_eng", "error"]
            #     csv_writer = csv.DictWriter(results, fieldnames=fieldnames)
            #     csv_writer.writeheader()  # Write headers for each column

            csv_writer.writerow(
                {"n-ALA": i, "Free_eng": Integral, "error": Error})


data_1 = np.loadtxt("helix_results.csv", skiprows=1, delimiter=",")
data_2 = np.loadtxt("extended_results.csv", skiprows=1, delimiter=",")

# x = data_1[:, 0]
# y = data_1[:, 1]
# y_err = data_1[:, 2]

# i = data_1[:, 0]
# j = data_1[:, 1]
# y_err = data_1[:, 2]

plt.style.use("seaborn-whitegrid")

plt.title("Gibbs Free Energy -$\u0394G_{cav}$ / Alanine")
plt.plot(data_1[:, 0], data_1[:, 1], color="k", label="Helix")
plt.errorbar(data_1[:, 0], data_1[:, 1], yerr=data_1[:, 2], color='k', linewidth=1, marker='o',
             mfc='none', markersize=7, markeredgewidth=1)

plt.plot(data_2[:, 0], data_2[:, 1], color="r", label="Extended")
plt.errorbar(data_2[:, 0], data_2[:, 1], yerr=data_2[:, 2], color='r', linewidth=1, marker='o',
             mfc='none', markersize=7, markeredgewidth=1)

plt.xlabel("n-ALA")
plt.ylabel("-$\u0394G_{cav}$  " + r"$[kJ mol^{-1}]$", fontsize=11)


# # plt.text(1, y[0], "     (1," + str("{:.2f}".format(y[0])) + ")")
# # plt.text(4, y[3], "     (5," + str("{:.2f}".format(y[3])) + ")")
# # plt.text(5, y[4], "     (5," + str("{:.2f}".format(y[4])) + ")")
# #plt.text(10, y[9], "     (10," + str("{:.2f}".format(y[9])) + ")")

plt.legend(loc="upper right")
plt.show()
