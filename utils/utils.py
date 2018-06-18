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


def plot_video_language(video_features, hot_idx):
    languages, language_counts = np.unique(video_features['video_language'][hot_idx], return_counts=True)
    languages = np.concatenate((np.expand_dims(languages, axis=1), np.expand_dims(language_counts, axis=1)), axis=1)

    print('%d languages:' % languages.shape[0])
    print([lang for lang in zip(languages[:,0], languages[:,1])])

    # Plot
    plt.figure(figsize=(16,6))
    plt.subplot(1,2,1)
    plt.bar(range(languages.shape[0]), languages[:,1], tick_label=[str(lang) for lang in zip(languages[:,0])])
    plt.title('Video Languages', fontsize=18)
    plt.xlabel('Countries', fontsize=14)
    plt.ylabel('Occurrences (#)', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    languages_norm = languages
    languages_norm[:,1] = languages[:,1] / len(hot_idx)

    plt.subplot(1,2,2)
    plt.bar(range(languages.shape[0]), languages_norm[:,1], tick_label=[str(lang) for lang in zip(languages_norm[:,0])])
    plt.title('Video Languages', fontsize=18)
    plt.xlabel('Countries', fontsize=14)
    plt.ylabel('Occurrences (%)', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()

    return

def plot_video_date(video_features, hot_idx):
    date, date_counts = np.unique(video_features['video_upload_date'][hot_idx], return_counts=True)
    date = np.concatenate((np.expand_dims(date, axis=1), np.expand_dims(date_counts, axis=1)), axis=1)

    print('%d dates:' % date.shape[0])
    print([day for day in zip(date[:,0], date[:,1])])

    # Plot
    plt.figure(figsize=(16,6))
    plt.subplot(1,2,1)
    plt.bar(range(date.shape[0]), date[:,1], tick_label=[str(day) for day in zip(date[:,0])])
    plt.title('Video Upload Date', fontsize=18)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Occurrences (#)', fontsize=14)
    plt.xticks(fontsize=12, rotation=45)
    plt.yticks(fontsize=12)

    date_norm = date
    date_norm[:,1] = date[:,1] / len(hot_idx)

    plt.subplot(1,2,2)
    plt.bar(range(date.shape[0]), date_norm[:,1], tick_label=[str(day) for day in zip(date_norm[:,0])])
    plt.title('Video Upload Date', fontsize=18)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Occurrences (%)', fontsize=14)
    plt.xticks(fontsize=12, rotation=45)
    plt.yticks(fontsize=12)
    plt.show()

    return

def plot_video_quality(video_features, hot_idx):
    quality, quality_counts = np.unique(video_features['video_quality'][hot_idx], return_counts=True)
    quality = np.concatenate((np.expand_dims(quality, axis=1), np.expand_dims(quality_counts, axis=1)), axis=1)

    print('%d different qualities:' % quality.shape[0])
    print([qual for qual in zip(quality[:,0], quality[:,1])])

    # Plot
    plt.figure(figsize=(16,6))
    plt.subplot(1,2,1)
    plt.bar(range(quality.shape[0]), quality[:,1], tick_label=[str(qual) for qual in zip(quality[:,0])])
    plt.title('Video Quality', fontsize=18)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Occurrences (#)', fontsize=14)
    plt.xticks(fontsize=12, rotation=45)
    plt.yticks(fontsize=12)

    quality_norm = quality
    quality_norm[:,1] = quality[:,1] / len(hot_idx)

    plt.subplot(1,2,2)
    plt.bar(range(quality.shape[0]), quality_norm[:,1], tick_label=[str(qual) for qual in zip(quality_norm[:,0])])
    plt.title('Video Quality', fontsize=18)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Occurrences (%)', fontsize=14)
    plt.xticks(fontsize=12, rotation=45)
    plt.yticks(fontsize=12)
    plt.show()

    return
