# Amazon Research Scientist Challenge


## General Overview

You are required to complete 2 challenges of the given 3 challenges below. Please select one challenge from Challenge 1 and Challenge 2. Completing Challenge 3 is required.
Return the results to us in the next three days.

## Additional Notes for the Candidate

- Please document your work and provide us the results along with commented code
- The candidate’s work will not be used for commercial purposes outside of the interview process
- We are interested in the both the thought process and approach
- Bonus points for well communicated and presented results
- Use any format you like including PowerPoint, Word doc, excel files, Jupyter notebooks etc.
- All data and included scenarios are fictitious


## Challenge 1: Price Optimization
A pricing experiment was conducted by Amazon.com.au with the main aim of increasing revenue. In the experiment, users were grouped into two groups: A (66% of the user base) and B (33% of user base). Group A users were offered a cheaper price while group B users received a higher price.

### Business Questions
What is your recommendation to the company in terms of setting an optimum price for their product?
What are your main findings looking at the data? What is your overall view into user behavior, especially focusing on actionable insights that might increase conversion rate?
Can you optimize the number of days that the test is run? After how many days would you have stopped the test? Why?

### Data Details
Table 1: test_results
- **user_id**: the Id of the user. Can be joined to user_id in user_table 
- **timestamp**: the date and time when the user first hit the webpage. It is in user local time 
- **source**: marketing channel that led to the user coming to the site. It can be:
  - ads - ["google", "facebook", "bing", "yahoo", "other"]. That is, user coming from google ads, yahoo ads, etc. 
  - seo - ["google", "facebook", "bing", "yahoo", "other"]. That is, user coming from google search, yahoo,  facebook, etc.
  - friend_referral : user coming from a referral link of another user
  - direct_traffic: user coming by directly typing the address of the site on the browser
- **device**: Can be mobile or web 
- **operative_system**: user operative system.
- **test**: (i.e. 1 -> higher price) and  (0 -> old lower price) 
- **price**: the price the user sees.
- **converted**: 1 -> bought the product - 0 -> left the site without buying it.

Table 2: user_table
- **user_id**: the Id of the user. Can be joined to user_id in test_results table
- **city**: the city where the user is located. Comes from the user ip address
- **country**: in which country the city is located 
- **lat**: city latitude - should match user city
- **long**: city longitude - should match user city


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


## Challenge 3: Understanding user and product interaction
Amazon’s employee travel provider has asked you to review how users interact with their online travel website.
They store their data in JSON files. Each row in these files lists all the different cities that have been searched for by a user within the same session (as well as some other info about the user).

### Business Questions
- There was a bug in the code and one country didn't get logged. Can you guess which country? How?
- For each city, find the most likely city to be also searched for within the same session.
- Travel sites are browsed by two kinds of users. Users who are actually planning a trip and users who just dream about a vacation. The first group obviously has a much higher purchasing intent. Users planning a trip often search for cities close to each other, while users who search for cities far away from each other are often just dreaming about a vacation (or a great work trip!). Based on this idea, come up with an algorithm that clusters sessions into two groups: high intent and low intent.

### Data Details
Table 1: city_search
- **session_id**: session id.
- **unix_timestamp**: unix timestamp of session start time
- **cities**: the unique cities which were searched within the same session
- **user**:
  - user_id: the id of the user
  - joining_date: when the user created the account
  - country: where the user is based
