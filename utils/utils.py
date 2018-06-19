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




def get_counts(video_features, idx):
    unique, counts = np.unique(video_features[idx], return_counts=True)
    unique = np.concatenate((np.expand_dims(unique, axis=1), np.expand_dims(counts, axis=1)), axis=1)
    return unique

def expand_data(feat, feat_all):
    new_feat = []
    new_feat = feat_all
    new_feat[:,1] = 0

    for i in range(len(feat)):
        ind = np.where(feat_all[:,0] == str(feat[i,0]))[0][0]
        new_feat[ind,1] = feat[i,1]

    return new_feat

def count_normalise(video_features, hot_idx, popular_idx, else_idx, all_idx):

    feat_all = get_counts(video_features, all_idx)
    feat_all_norm = feat_all[:,1] / len(all_idx)

    feat_hot = get_counts(video_features, hot_idx)
    feat_hot = expand_data(feat_hot, feat_all)
    feat_hot_norm = (feat_hot[:,1] + 1e-5 )/ len(hot_idx)

    feat_pop = get_counts(video_features, popular_idx)
    feat_pop = expand_data(feat_pop, feat_all)
    feat_pop_norm = feat_pop[:,1] / len(popular_idx)

    feat_else = get_counts(video_features, else_idx)
    feat_else = expand_data(feat_else, feat_all)
    feat_else_norm = feat_else[:,1] / len(else_idx)

    num_feat = feat_all.shape[0]
    labels = [str(feat) for _, feat in enumerate(feat_all[:,0])]

    return feat_hot_norm, feat_pop_norm, feat_else_norm, feat_all_norm, num_feat, labels

def plot_video_length(video_features, hot_idx, popular_idx, else_idx, all_idx):

    series1 = video_features[hot_idx]
    series2 = video_features[popular_idx]
    series3 = video_features[else_idx]
    series4 = video_features[all_idx]
    series = [series1, series2, series3, series4]
    labels = ['hot', 'pop', 'else', 'all']
    colors = ['red', 'blue', 'green', 'black']

    plt.figure(figsize=(16,6))
    plt.title('Video Length', fontsize=20)
    plt.xlabel('Length', fontsize=16)
    plt.ylabel('Occurrences (%)', fontsize=16)

    plt.hist(series, bins=5, histtype='bar', align='mid', rwidth=0.75, density=True, color=colors, label=labels)

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    plt.legend(fontsize=14)
    plt.show()

    return


def plot_video_language(video_features, hot_idx, popular_idx, else_idx, all_idx):

    feat_hot_norm, feat_pop_norm, feat_else_norm, feat_all_norm, num_feat, labels = count_normalise(video_features, hot_idx, popular_idx, else_idx, all_idx)
    width=0.2

    plt.figure(figsize=(16,6))
    plt.title('Video Languages', fontsize=20)
    plt.xlabel('Language', fontsize=16)
    plt.ylabel('Occurrences (%)', fontsize=16)

    plt.bar(np.arange(num_feat)-1.5*width, feat_hot_norm, width, color='r', tick_label=labels, label='Hot')
    plt.bar(np.arange(num_feat)-0.5*width, feat_pop_norm, width, color='b', tick_label=labels, label='Popular')
    plt.bar(np.arange(num_feat)+0.5*width, feat_else_norm, width, color='g', tick_label=labels, label='Everything Else')
    plt.bar(np.arange(num_feat)+1.5*width, feat_all_norm, width, color='black', tick_label=labels, label='All')

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    plt.legend(fontsize=14)
    plt.show()

    return

def plot_video_date(video_features, hot_idx, popular_idx, else_idx, all_idx):

    feat_hot_norm, feat_pop_norm, feat_else_norm, feat_all_norm, num_feat, labels = count_normalise(video_features, hot_idx, popular_idx, else_idx, all_idx)

    width=0.2

    plt.figure(figsize=(16,6))
    plt.title('Video Upload Date', fontsize=20)
    plt.xlabel('Date', fontsize=16)
    plt.ylabel('Occurrences (%)', fontsize=16)

    plt.bar(np.arange(num_feat)-1.5*width, feat_hot_norm, width, color='r', tick_label=labels, label='Hot')
    plt.bar(np.arange(num_feat)-0.5*width, feat_pop_norm, width, color='b', tick_label=labels, label='Popular')
    plt.bar(np.arange(num_feat)+0.5*width, feat_else_norm, width, color='g', tick_label=labels, label='Everything Else')
    plt.bar(np.arange(num_feat)+1.5*width, feat_all_norm, width, color='black', tick_label=labels, label='All')

    plt.xticks(fontsize=14, rotation=90)
    plt.yticks(fontsize=14)

    plt.legend(fontsize=14)
    plt.show()

    return

def plot_video_quality(video_features, hot_idx, popular_idx, else_idx, all_idx):
    feat_hot_norm, feat_pop_norm, feat_else_norm, feat_all_norm, num_feat, labels = count_normalise(video_features, hot_idx, popular_idx, else_idx, all_idx)

    width=0.2

    plt.figure(figsize=(16,6))
    plt.title('Video Quality', fontsize=20)
    plt.xlabel('Quality', fontsize=16)
    plt.ylabel('Occurrences (%)', fontsize=16)

    plt.bar(np.arange(num_feat)-1.5*width, feat_hot_norm, width, color='r', tick_label=labels, label='Hot')
    plt.bar(np.arange(num_feat)-0.5*width, feat_pop_norm, width, color='b', tick_label=labels, label='Popular')
    plt.bar(np.arange(num_feat)+0.5*width, feat_else_norm, width, color='g', tick_label=labels, label='Everything Else')
    plt.bar(np.arange(num_feat)+1.5*width, feat_all_norm, width, color='black', tick_label=labels, label='All')

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    plt.legend(fontsize=14)
    plt.show()

    return
