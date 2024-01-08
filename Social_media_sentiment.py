import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score

# Function to categorize sentiment scores as positive, negative, or neutral
def categorize_sentiment(score):
    if score > 0.2:
        return 'Positive'
    elif score < -0.2:
        return 'Negative'
    else:
        return 'Neutral'

# Function to generate  tweets
def generate_tweets():
    tweets = [
        "Tonight's sky is mesmerizing, filled with twinkling stars!",
        "Gazing at the clear sky, feeling grateful for the beauty above.",
        "The stars are so vivid tonight, it's absolutely breathtaking!",
        "Clear skies mean a perfect night for stargazing!",
        "Feeling peaceful under the brilliantly shining stars tonight.",
        "Mesmerized by the twinkling stars in the crystal-clear sky tonight.",
        "Tonight's celestial canvas is painted with dazzling stars!",
        "Under this radiant sky, each star tells a story of its own.",
        "The night sky's clarity unveils the secrets of the universe tonight!",
        "The sparkling stars tonight are like diamonds in the clear sky!",
        "The bright stars in the clear night sky are a sight to behold!",
        "In awe of the sparkling stars against the clear night backdrop!",
        "The starry night sky ignites a sense of wonder within.",
        "Under this sky's clarity, dreams seem within reach tonight.",
        "Each star twinkling tonight is a reminder of endless possibilities.",
        "Tonight's sky whispers secrets, each star a silent storyteller.",
        "Wrapped in the tranquility of the star-lit, clear night sky.",
        "The stars tonight seem like they're dancing in the clear sky!",
        "Lost in contemplation under the gleaming stars tonight.",
        "Tonight's sky resembles a shimmering tapestry of stars!",
        "The stars' brilliance in the clear sky is a celestial spectacle!",
        "The sky's clarity tonight reveals the universe's vastness.",
        "Beneath this starry sky, peace fills the heart.",
        "Tonight's stars shine as beacons of hope in the clear sky.",
        "The starry canopy above is a vision of sheer magnificence tonight."
    ]
    return tweets

# Function to plot sentiment analysis results
def plot_sentiment_analysis(sentiment_data):
    df = pd.DataFrame(sentiment_data)
    fig, ax = plt.subplots()
    df.plot(kind='bar', ax=ax)
    ax.set_xticklabels(df['Sentiment'])
    ax.set_ylabel('Sentiment Score')
    ax.set_title('Sentiment Analysis Results')
    st.pyplot(fig)

# Streamlit UI
def main():
    st.title('Social Media Sentiment Analysis')

    option = st.sidebar.selectbox('Choose an option', ('Analyze Text', 'Fetch Tweets', 'Visualization'))

    if option == 'Analyze Text':
        st.subheader('Enter Text for Sentiment Analysis')
        text_input = st.text_area('Enter text or tweet:')
        if st.button('Analyze'):
            if text_input:
                sentiment_score = analyze_sentiment(text_input)
                sentiment_category = categorize_sentiment(sentiment_score)
                st.write(f'Sentiment: {sentiment_category}')
            else:
                st.warning('Please enter some text.')

    elif option == 'Fetch Tweets':
        st.subheader('Fetch Tweets Related to a Word')
        word_input = st.text_input('Enter a tweet:')
        if st.button('Fetch'):
            if word_input:
                st.write(f"Fetching tweets related to '{word_input}'...")
                # You can add code here to fetch tweets related to the input word
                # For demonstration purposes, generating  tweets
                tweets = generate_tweets()
                st.write(' Tweets:')
                for tweet in tweets:
                    st.write(f"- {tweet}")
            else:
                st.warning('Please enter a word.')

    elif option == 'Visualization':
        st.subheader('Visualization of Sentiment Analysis Results')
        #  Data for visualization
        sentiment_data = {'Sentiment': ['Positive', 'Negative', 'Neutral'],
                          'Score': [0.8, -0.6, 0.1]}  # Example scores, replace with your data
        plot_sentiment_analysis(sentiment_data)

if __name__ == "__main__":
    main()
