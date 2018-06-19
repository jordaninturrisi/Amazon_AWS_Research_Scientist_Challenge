
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
