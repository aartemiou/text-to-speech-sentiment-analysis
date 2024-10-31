# Import necessary libraries
import pyttsx3
from textblob import TextBlob

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to adjust speech based on sentiment
def speak_with_emotion(text, sentiment):
    # Set default voice parameters
    voice_params = {
        'rate': 175,  # Normal speech rate
        'volume': 1.0,  # Normal volume
        'pitch': 50  # Normal pitch (custom pitch handling may vary)
    }

    # Adjust voice parameters based on sentiment
    if sentiment.polarity > 0:
        # Positive sentiment: enthusiastic tone
        voice_params['rate'] = 185
        voice_params['volume'] = 1.2
        engine.say("You said: " + text)
        engine.say("Great to hear that!")

    elif sentiment.polarity < 0:
        # Negative sentiment: somber tone
        voice_params['rate'] = 150
        voice_params['volume'] = 0.8
        engine.say("You said: " + text)
        engine.say("I'm sorry to hear that.")

    else:
        # Neutral sentiment: default tone
        engine.say("You said: " + text)

    # Apply the voice parameters to the engine
    engine.setProperty('rate', voice_params['rate'])
    engine.setProperty('volume', voice_params['volume'])
    engine.runAndWait()

# Main program loop
def main():
    print("Text-to-Speech App with Sentiment Analysis")
    print("Type 'q' to quit.")
    
    while True:
        # Get user input
        text = input("Enter text to speak (or 'q' to quit): ")
        if text.lower() == 'q':
            break
        
        # Perform sentiment analysis
        sentiment = TextBlob(text).sentiment
        speak_with_emotion(text, sentiment)
    
    # Shut down the engine when finished
    engine.stop()
    print("Application closed.")

if __name__ == "__main__":
    main()
