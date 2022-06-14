# MBTI_prediction

## Abstract

Myers-Briggers Type Indicator, MBTI in short, is a personality metric which is based on Carl Jung’s theory on psychological types, and consists of 4 axes. We tried to predict one’s MBTI type using NLP techniques, such as word tokenization, regular expression, and tagging, using the dataset in one-to-one Kakaotalk chatting text. We tagged some words that are frequently used in messenger, found particular morphemes using regular expressions, and used statistical techniques for analyzing the result. We collected three or more conversation sets containing the same person, then scored MBTI for each conversation set, and added them up to estimate the person’s MBTI type stochastically.

## Introduction

MBTI, which has spread like a trend in Korea for several years, has recently received so much attention that it has been used by companies to recruit. However, there is a difficulty in solving around 100 problems, and if you want, you can change the results to get the MBTI type you want. We thought that the weaknesses of these MBTI tests could be overcome if a specific MBTI type could be inferred from daily conversations. So, we decided to create an algorithm that infers each MBTI type using KakaoTalk conversations that we use in our daily lives without any decorations

## Theoretical Background/Tools 

### Basic concepts of MBTI   

Myers-Briggers Type Indicator, MBTI in short, is a personality metric which is based on Carl Jung’s theory on psychological types. MBTI is a personality type system that divides every person into 4 personality axes:
Introversion (I) – Extroversion (E)
Intuition (N) – Sensing (S)
Thinking (T) – Feeling (F)
Judging (J) – Perceiving (P)
For example, a person with MBTI labeled as ‘ENFP’ would have traits such as Extroversion, Intuition, Feeling and Perceiving. The words or expressions used by the person may be different depending on the MBTI type. We will focus on this and guess the MBTI type from the conversation of the person.


### Morphological analysis by KoNLPy

KoNLPy is a Python package for Korean information processing and provides functions such as morphological analysis and tagging. KoNLPy offers four natural language processors: Komoran, Hannanum, Kkma, and Okt. Among them, Komoran and Hannanum are fast, but their accuracy is average. Kkma has high accuracy but is very slow. The appropriate morphological analyzer varies to the characteristic of the data to be used (with or without spaces) or the development environment (Python, Java). We collected a lot of data from AI hub, and it took a lot of time to process these data. Among morphological analyzers of KoNLPy, the one with good performance and fast speed was Otk, so we used Okt for all morphological analysis.


### Kakaotalk open dataset in AIHUB

We used Kakaotalk open dataset provided by AIHUB to identify words that ordinary people use a lot in their daily lives. It is basically developed for NLP development of information search, conversation analysis, questioning and answering, and so on. This dataset contains 2 million conversations, and the average number of utterances in each conversation is 16 times. This enormous amount of data is divided into ‘personal and relationship’, ‘beauty and health’, ’food and beverage’, ‘work and occupation’, and ‘event’ etc. according to the topic of the conversation, and we used ‘personal and relationship’ dataset. The ‘personal and relationship’ dataset is a very suitable dataset for our experiments because it contains more comprehensive daily conversations than other datasets.

## Methodology

### 1. Pre - processing of Open dataset

We first went through the data processing process for Kakaotalk open dataset of AIHUB. Kakaotalk open dataset is provided in the from of JSON file, and we extracted 100,000 ‘personal and relationship’ conversations. As a result, about 170,000-length strings could be collected, and we classified all words according to partitions using Okt morphological analyzer of KoNLPy. Table 2 shows examples of words that are used a lot for each part. We thought that the parts of table 2 among the various parts had meaning in the conversation flow, and in this classification, we chose the appropriate words according to MBTI type. We tried to pick words based on our own standards. Table 3 shows the words selected through this process. People with MBTI type E like to meet people, so we thought they would use the words ‘let’s’ or ‘with’ more that people with MBTI type I.  Similarly, we thought that people with MBTI type N would use words that express imagination such as ‘if’, ‘it would be’ more than people with MBTI type S. People with MBTI type F are known to be good at feeling emotional, so they would use words that express empathy such as ‘wow’, ‘ouch’ more than people with MBTI type T. Finally, people with MBTI type J would use words that express planning such as ‘tomorrow’, ‘planning’, ‘promise’ more than people with MBTI type P.

### 2. Pre - processing of personal chatting

Secondly, we went through the data processing process for our personal Kakaotalk dataset. Kakaotalk provides our conversation as a txt file. This file shows who said what and when, and we extracted only the names of people and conversations. We converted this file in to CSV file, and we tagged each person’s words and parts using Okt morphological analyzer of KoNLPy and regular expression.

### 3. Scoring algorithm

 By each axis of MBTI, we tried to count the number of morphemes which is in the category, and also appeared in the chatting text. Then we scored the user’s MBTI of each axis, by calculating the ratio of the count number to other user’s number. We implemented a user DB that stores all user’s score, and tried to update a user’s MBTI score on each comparison.

## Desired behavior

Since we are redeeming the original method of getting MBTI type, which is by answering questions, we did not set up a desired or pre- determined output. However, we thought that the more chat datasets we score, the more accurate MBTI type we get. Therefore, we increased dataset number for a certain limit, which is 3 per user.

## Output

We tried to show the predicted MBTI of users. By making assumption that if ‘E score’ of the user exceeds 50, then the user is ‘E’ type. Otherwise, the user is ‘I’ type. we applied the same standard for each axis of MBTI, and showed the result.

## Conclusion

There were some limitations of our work, which was that we could not get Kakakotalk dataset from other people, which are private, that the accuracy of the other people could not improve much further from just using the chat messages of our own. If we can get datasets from others, we are able to make large network of users, and update the score using chat messages of each other. Also, we could improve our scoring algorithm based on the given network and data, such as using previous MBTI type score while on scoring process, for optimization.
