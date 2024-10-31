# Text-to-Speech App with Sentiment Analysis

This project is a proof-of-concept application that combines Text-to-Speech (TTS) with Sentiment Analysis. The app converts text input to speech, adjusting the tone of voice based on the detected sentiment of the text (positive, negative, or neutral).

Read the full article on LinkedIn: [Building a Simple Text to Speech App with Sentiment Analysis](https://www.linkedin.com/pulse/building-simple-text-speech-app-sentiment-analysis-artemakis-artemiou-fgxsc/)

## Features
- **Text-to-Speech (TTS)**: Uses the `pyttsx3` library to convert text into spoken words.
- **Sentiment Analysis**: Leverages the `TextBlob` library to analyze the sentiment of the input text.
- **Emotion Modulation**: Adjusts speech parameters like rate, volume, and pitch based on the sentiment to convey positive, neutral, or negative tones.

## Prerequisites

### 1. Install Required Libraries
To get started, install the required libraries using:
```bash
pip install -r requirements.txt
