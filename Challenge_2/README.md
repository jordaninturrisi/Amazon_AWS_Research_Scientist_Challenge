## Challenge 2: Recommendation Engine for Prime Video
Today, videos shown to new users on Prime Video’s home page are manually chosen. You need to implement a recommendation engine to increase the conversation rate.

### Business Questions
- Classify each video into the following buckets:
  - "Hot" - means trending up. These videos are candidates to be shown.
  - "Stable and Popular" - video view counts are flat, but very high. These videos are candidates to be shown too.
  - "Everything else" - these videos won't be shown.
- What are the main characteristics of the "hot videos"?
- After having identified the characteristics of the hot videos, how would you use this information from a product standpoint?

### Data Details
Table 1: video_count
- **video_id**: unique video id
- **count**: total count of views for the specific video_id on the specific date 
- **date**: the date that these views occurred


Table 2: video_features
- **video_id**: video id, unique by video and joinable to the video id in the other table
- **video_length**: length of the video in seconds 
- **video_language**: language of the video, as selected by the user when they uploaded the video
- **video_upload_date**: when the video was uploaded 
- **video_quality**: quality of the video. It can be [ 240p, 360p, 480p, 720p, 1080p]
