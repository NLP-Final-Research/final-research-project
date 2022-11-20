# Natural Language Processing: Final Project Proposal 
Yeonie Heo (sh5874)
Oyungerel Amarsanaa (oa853)
Jennifer Zheng (lz2278)

## 01 Introduction & Research Question
We have decided to use the annotation and evaluating techniques we learned this semester in order to analyze data from social media concerning a current event: the United States elections of 2022. Based on the fact that Twitter is a platform with high activity and people are not restricted in sharing and displaying their political views, we chose to use tweet data from Twitter. 
We are developing an evaluation project to extract features from tweets and analyze the interests, utterances, and sentiments of tweet writers. We believe that Twitter users from different political parties express their political positions in a variety of ways. As a result of annotating the features of tweet texts, we hope to be able to further develop a Political Party Identifier based on the annotations and then, evaluate the precision and accuracy of our identifier on predicting tweet writers’ political stances. 

## 02 Literatures Reviews

How does this article relate to our research?
Quantising Opinions for Political Tweets Analysis 

This paper is one of the first papers that analyzed Twitter users’ political perspectives in 2010. This paper is relevant to our research as it provides insights about how to collect data on Twitter users’ political perspectives: using hashtags and relevant keywords associated with each political party. The paper collected their data from Twitter API and implemented a lexicon based approach which assigns a score +1 and -1 to any matched positive and negative word respectively based on a sentiment lexicon. For each political party, the paper counted the total number of positive and negative mentions to this specific party across all the tweets to define and calculate ‘bias measure’. The slight distinctions of bias measure for diverse sentiment analysis methods show that activities on Twitter cannot be used to predict the popularity of election parties. Building on their focus on sentiment analysis and using keywords to identify Twitter users’ political perspectives, we became interested in how Natural Language Processing techniques we learned this semester (POS tags, regular expressions) on top of sentiment analysis can better contribute to categorizing tweets into corresponding political parties. 
An Annotated Corpus of Film Dialogue for Learning and Characterizing Character Style

This paper discusses a film script annotation project that is used to develop a personage generator which will identify film characters based on sentences feeded into the model. Despite the fact that our project involves political speech while this paper deals with film scripts, we have gained a lot of insights by looking at how the researchers train the features. To train the features, they used approaches such as LIWC, SentiWordNet, POS tagger, and self-written scripts to annotate features ranging from the basic, polarity, merge ratio, passive sentence ratio, to LIWC Word Categories. That said, we may refer to this paper for a variety of ways to construct the features of data for our project. Furthermore, this research is highly relevant as the end goal of our project is to train a political party personage identifier based on the past data. 
Political Tendency Identification in Twitter using Sentiment Analysis Techniques

This paper describes an approach to identify political stances of Twitter users based on the polarity of the political entities mentioned in the tweets. The dataset used comprises 68,000 Spanish tweets written by influential people in public spheres within a period of 4 months. Each tweet is tagged with varying polarity in 6 ways – N (negative), N+ (intense negative), P (positive), P+ (intense positive), NEU (neutral), None (no polarity) and assigned polarity values of -1/+1/0 respectively. The polarity of the political tendencies are also taken into account by assigning -1/+1/0 and both scores are combined to come up with a political tendency score to identify the political orientation of each user. The paper is highly relevant to our project as it gives an insight on creating the training set and identifying the political polarity of tweets using named entities. Differentiating factors of this paper include the dataset which consists of Spanish language tweets written by influential figures, political stance identification of users instead of the tweets themselves, as well as classifying political stance into 4 different groups (Center, Left, Right, Undefined).
Identifying Stance by Analyzing Political Discourse on Twitter

In this paper, a novel approach is discussed for modeling the tweets of potential presidential candidates. They categorizes sixteen potential issues that will be discussed in the political tweets such as Abortion, Drugs, Religion, Education, etc. After that, they analyze issues-related words or terms to determine the speakers' positions. The purpose of deepening down its analysis of tweets surrounded by political topics is to model both the content of posted messages as well as the social context in which they are generated, and to suggest a joint model that captures both aspects. In order to achieve this, they compiled a list of frequently occurring keywords for each issue, with an average of seven keywords per issue. Using ISideWith.com, they then annotated the party stances of politicians. 
Finally, they analyze their positions on each issue. Certainly, this method of analyzing issues can be beneficial to our project. 
Beyond Binary Labels: Political Ideology Prediction of Twitter Users

Published comparably recently, this paper describes an approach to predict Twitter users’ political ideology using a 7-point scale (Very conservative, Conservative, Moderately Conservative, Moderate, Moderately Liberal, Liberal, Very Liberal). The fact that the paper tries to take into account Twitter users with not-so-much obvious or open political ideologies makes it an interesting example to examine. A unique aspect of this paper is that it uses original data collected through primary research methods by conducting questionnaires from 3938 users. It also uses a dataset consisting of 13651 users with plainly apparent political views to facilitate differentiation from previous academic research. The paper uses a broad range of linguistic features, some of which we will be using in our project including LIWC and Unigrams. For analysis, the paper explores the relationship between language use and political ideological groups by doing comparison in 3 ways:  comparing the 2 political extremes, 2 political moderates and as well as moderates versus extremes. The paper offers a relevant insight for our project regardless of the differences in dataset as well as the primary focus on non-overt tweets because it establishes a useful framework of creating differentiation between political ideologies.  

## 03 Methods, Strategies & 04 Evaluation Plan
The final objective of this research is to develop a Political Party Identifier that will predict the political stances of Twitter writers based on the features that are automatically extracted from tweet posts using our written scripts. To achieve this goal, we have divided the project into three main phases: a) data collection, b) features extraction & model training and c) model testing & evaluation. 

### PART I: Data Collections
The first step is to write scripts and collect relevant data using Twitter API. To ensure the certainty of political stance of each tweet and stance, we will only collect tweets with hashtags, #supportbiden and #supporttrump, using the Twitter API. Those tweets with #supportbiden would be considered to hold left or centered-left political views, while those with #supporttrump would be regarded to hold right or centered-right political views. 

### PART II: Feature Extractions & Training Model
Next, we will write scripts that automate the extraction of features from tweets, which will be used for training the political party identifier model later. For the model training, we would use 80% of the collected tweets. 
For the purpose of identifying the noun groups of the tweets, we will use POS tagger as we believe nouns are the most likely to describe the political topics and issues the tweet writers are interested in. The filtered noun groups of the tweets will be made into a “political issue list” that will contain popular topics within the two parties, such as education, religion, abortion, and etc. Along with the “political issue list”, we will identify the “political entities,’’ mentioned in the tweets, such as names and acronyms of political parties, and their respective political polarities. The merged list of extracted “political issue list” and “political entities” will be called “topics-list”.
Given the “topics-list”, we will conduct LIWC to expand the list of preferred topics or events for each political party. As a result, we will be able to cover a broader range of vocabulary, content, and subject areas of tweet writers’ interests. 
In each tweet, we will identify topic-related words and track their occurrences. As a result of collecting the occurrences, a unique vector will be formed that will be used for training the identifier model. 
To evaluate the positive and negative emotions and recognitions associated with tweets, we will conduct the overall sentiment analysis for each tweet. Using the occurrence vector as weights, we will be reconstructing the ‘weighted-sentiment-by-topic’ by multiplying the occurrence and the overall sentiment analysis for each topic that appeared. 

### PART III: Testing Model
Second, we will test the Political Party Identifier model with the 20% of the collected tweets that aren’t used in PART II. 
We will perform the identical sentiment analysis to yield the sentiment score features and count the topic-related word occurrences features for each test tweet. We will then be able to provide the predictions for each tweet writer's political party by plugging the features into the model trained in the training stage.   
As we already know the preferred political party of the testing tweets from the data collection, we will be able to calculate the Accuracy, Recall, and F-measure in relation to our system output and answers. This will allow us to objectively evaluate the performance of our Political Party Identifier model. 
In addition to the internal evaluation, we will externally compare the F-measure of our system to existing work in Literature Reviews and verify the means to improve the accuracy of Political Party Identifiers. 
