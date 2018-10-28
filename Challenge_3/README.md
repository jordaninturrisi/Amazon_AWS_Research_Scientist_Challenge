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
