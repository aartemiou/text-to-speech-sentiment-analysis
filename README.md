# Text-to-Speech App with Sentiment Analysis

This project is a proof-of-concept application that combines Text-to-Speech (TTS) with Sentiment Analysis. The app converts text input to speech, adjusting the tone of voice based on the detected sentiment of the text (positive, negative, or neutral).

Read the full article on LinkedIn: [Building a Simple Text to Speech App with Sentiment Analysis](https://www.linkedin.com/pulse/building-simple-text-speech-app-sentiment-analysis-artemakis-artemiou-fgxsc/)

## Features
- **Text-to-Speech (TTS)**: Uses the `pyttsx3` library to convert text into spoken words.
- **Sentiment Analysis**: Leverages the `TextBlob` library to analyze the sentiment of the input text.
- **Emotion Modulation**: Adjusts speech parameters like rate, volume, and pitch based on the sentiment to convey positive, neutral, or negative tones.

## Prerequisites

### 1. Install Required Libraries
Install the following libraries to set up the application:
```bash
pip install pyttsx3
pip install textblob
pip install nltk
```

### 2. Download TextBlob Corpora
TextBlob requires additional corpora to perform sentiment analysis. Download them by running:
```bash
python -m textblob.download_corpora
```

### 3. Usage
Run the app with:
```
python app.py
```
The application will prompt you to enter text to speak aloud with sentiment-adjusted tone. Type 'q' to quit the app.

### 4. Libraries Used
1. pyttsx3: Provides text-to-speech capabilities, allowing spoken output from text input.
2. TextBlob: Performs sentiment analysis on text to determine if the sentiment is positive, neutral, or negative.
3. nltk: Required by TextBlob to access linguistic datasets for sentiment analysis.

### 5. Example Output
Here's how the app works:

1. User Input: The app prompts the user to enter a text input, for example: "I am very happy today!"
2. Sentiment Analysis: The app uses TextBlob to analyze the sentiment of the input text.
- If the sentiment is positive, the app speaks the text with an enthusiastic tone.
- If the sentiment is negative, it speaks with a more somber tone.
- If the sentiment is neutral, it maintains a neutral tone.
3. Text-to-Speech Output: The app speaks the text aloud with adjusted voice parameters.

### 6. License
This project is licensed under the MIT License - see the LICENSE file for details.

### 7. Author
Artemakis Artemiou  
AI Leader | Automation Architect | Database Expert | Former Microsoft MVP | Scaled Scrum Master | Published Author & Speaker
