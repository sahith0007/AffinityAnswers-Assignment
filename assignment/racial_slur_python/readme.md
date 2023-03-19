# Degree of Profanity
## Introduction
This Python code is designed to analyze tweets in a given file for the presence of certain words that may indicate the use of racial slurs. The code categorizes the degree of profanity of a tweet based on the number of times such words appear in it. This degree of profanity is then used to classify the tweet as Normal, Moderate or High.
## Installation
This code requires Python 3.x to run. The following modules are used:
* No additional modules required.
## Usage
The function degree_of_hate takes a file name as input and analyzes each tweet in the file for the presence of certain words that may indicate the use of racial slurs. The function then calculates the degree of profanity for each tweet and classifies it as Normal, Moderate or High based on the count of such words.
## Input
The input parameter is the file name in which the tweets are stored.
### Assumptions on input file
* Tweets: The file will contain a collection of tweets, which are short messages that express an individual's thoughts or opinions on a particular topic. Each tweet is typically limited to 280 characters.
* Usernames: The file may contain the usernames of the individuals who posted the tweets. These usernames typically begin with the "@" symbol and are used to identify the user on the social media platform.
* Every tweet is seperated by empty line.
## Output
The output is the degree of profanity and classification of each tweet in the file. The degree of profanity is classified as Normal, Moderate or High.
## Example
```python
degree_of_hate("demo.txt")
```
The output of the above code will be as follows:
```bash
@user1-Normal
@user2-Moderate
@user3-High
```
