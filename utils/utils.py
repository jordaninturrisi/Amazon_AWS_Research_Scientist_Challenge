import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot1(kmeans, counts, counts_norm, dict, labels):
    # label = [num for num in range(kmeans.n_clusters)]

    # Plot the results
    plt.figure(figsize=(16,4))
    plt.suptitle('Explore Clustered Data', fontsize=20)

    plt.subplot(1, 2, 1)
    for i in set(kmeans.labels_):
        index = kmeans.labels_ == i
        plt.semilogy(np.mean(counts_norm[index, :], axis=1), np.mean(counts[index, :], axis=1), 'o', label=labels[i])
        print('%s:          Average Normalised Count: %5.2f          Average Daily Count: %.0f' % (labels[i], np.mean(counts_norm[dict[i]]), np.mean(counts[dict[i]])))
    plt.ylabel('Average Counts', fontsize=16)
    plt.xlabel('Average Normalised Count', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)

    plt.subplot(1, 2, 2)
    series1 = list(np.mean(counts_norm[dict[0]], axis=1))
    series2 = list(np.mean(counts_norm[dict[1]], axis=1))
    series = [series1, series2]
    plt.hist(series, histtype='bar', log=True, bins=15, label=labels)
    plt.ylabel('Occurrences', fontsize=16)
    plt.xlabel('Average Normalised Count', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)
    plt.show()

    return


def plot2(kmeans, counts, counts_norm, dict, labels):

    # Plot the results
    plt.figure(figsize=(16,4))
    plt.suptitle('Explore Clustered Data', fontsize=20)

    plt.subplot(1, 2, 1)
    for i in set(kmeans.labels_):
        index = kmeans.labels_ == i
        plt.semilogx(np.mean(counts_norm[index, :], axis=1), np.mean(counts[index, :], axis=1), 'o', label=labels[i])
        print('%s:          Average Normalised Count: %5.2f          Average Daily Count: %.0f' % (labels[i], np.mean(counts_norm[dict[i]]), np.mean(counts[dict[i]])))
    plt.ylabel('Average Counts', fontsize=16)
    plt.xlabel('Average Normalised Count', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)

    plt.subplot(1, 2, 2)
    series1 = list(np.mean(counts[dict[0]], axis=1))
    series2 = list(np.mean(counts[dict[1]], axis=1))
    series = [series1, series2]
    plt.hist(series, histtype='bar', log=True, bins=15, label=labels)
    plt.ylabel('Occurrences', fontsize=16)
    plt.xlabel('Average Normalised Count', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)
    plt.show()

    return
