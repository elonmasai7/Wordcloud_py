import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud

# Create a dictionary of word frequencies
word_freq = {'apple': 10, 'banana': 15, 'cherry': 20, 'durian': 5, 'elderberry': 12}

# Sort the word frequencies in descending order
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)



# Create a WordCloud object
wordcloud = wordcloud.WordCloud(font_path=font_path, width=800, height=600, background_color="white")

# Generate the word cloud
wordcloud.generate_from_frequencies(dict(sorted_word_freq))

# Display the word cloud
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# Import the input data
data = input("Enter your input data: ")

# Preprocess the data
data = data.lower()  # Convert the data to lowercase
data = "".join(char for char in data if char.isalpha() or char.isspace())  # Remove non-alphabetic and non-whitespace characters
data = " ".join(word for word in data.split() if word not in STOPWORDS)  # Remove common stopwords

# Analyze the data
word_freq = {}  # Dictionary to store word frequencies
for word in data.split():
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Sort the word frequencies in descending order
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=600, background_color="white").generate_from_frequencies(dict(sorted_word_freq))

# Display the word cloud
plt.imshow(wordcloud)
plt.axis("off")
plt.show()