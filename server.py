from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)  

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    if response is None or response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is:\n"
        f"  anger: {response['anger']:.3f}\n"
        f"  disgust: {response['disgust']:.3f}\n"
        f"  fear: {response['fear']:.3f}\n"
        f"  joy: {response['joy']:.3f}\n"
        f"  sadness: {response['sadness']:.3f}\n"
        f"  The dominant emotion is: {response['dominant_emotion']}"
    )

if __name__ == "__main__":
    app.run(debug=True)  
