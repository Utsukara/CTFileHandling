
# Objective:
# This assignment is aimed at challenging your skills in advanced data processing and 
# analysis using Python. It encompasses a broad range of topics, including file handling, 
# regular expressions, data structures, and complex problem-solving, at a medium-hard difficulty 
# level.

# Task 1: Travel Blog Sentiment Analysis:

# Problem Statement:
# Perform sentiment analysis on a collection of travel blog entries stored in travel_blogs.txt. 
# Identify and count the occurrences of positive words 
# (e.g., "amazing", "enjoy", "beautiful") and negative words (e.g., "bad", "disappointing", "poor").
# - Dataset Example:
# Travel Blog Entries:

# 1. "Our recent trip to the mountains was amazing! The scenery was breathtaking and we enjoyed every moment of it."

# 2. "The beach vacation was wonderful. We relaxed by the shore and soaked up the sun."

# 3. "The city tour was a bit disappointing. The guide wasn't very knowledgeable, and the attractions were overcrowded."

# 4. "Exploring the countryside was a unique experience. The landscapes were stunning, but the accommodations were poor."

# 5. "Despite the rain, our visit to the waterfall was memorable. The cascading water was mesmerizing."

# 6. "We had high hopes for the safari adventure, but it turned out to be lackluster. The wildlife sightings were scarce."

# 7. "The food on our trip was excellent. We sampled delicious local cuisine at every stop."

# 8. "The historical tour was enlightening. We learned so much about the culture and heritage of the region."

# 9. "Overall, our travel experience was fantastic. We made unforgettable memories and can't wait for our next adventure!"
# Code Example:
def analyze_blog_sentiments(blog_file):
    # Implement sentiment analysis logic on the blog file
    positive_words = ["amazing", "enjoy", "beautiful", "wonderful", "relaxed", "memorable", "excellent", "fantastic", "unforgettable"]
    negative_words = ["disappointing", "poor", "lackluster", "scarce", "overcrowded"]
    try:
        with open(blog_file, 'r') as file:
            data = file.read()
            positive_count = sum(data.count(word) for word in positive_words)
            negative_count = sum(data.count(word) for word in negative_words)
            print("Positive Words Count:", positive_count)
            print("Negative Words Count:", negative_count)
    except FileNotFoundError:
        print("The specified file does not exist.")
    except Exception as e:
        print("An error occurred:", e)

blog_file = "travel_blogs.txt"
analyze_blog_sentiments(blog_file)

# Expected Outcome:
# A summary report indicating the number of positive and negative words in the travel blogs, demonstrating the ability to process text data and apply basic sentiment analysis.