# FraudSense_AI 🎃 - Spooky Edition

FraudSense_AI is an AI-powered web application designed to detect fraudulent text and URLs from user-uploaded images with a Halloween-inspired theme. Users can upload images containing suspicious text, and the app extracts and evaluates the text and any associated URL for legitimacy. With engaging visuals, confidence scoring, and eerie sound effects, FraudSense_AI makes fraud detection informative and fun.


## Features
1. **Image Text Extraction:** Extracts text from user-uploaded images using OCR and assesses its legitimacy.
2. **URL Analysis:** Evaluates the provided URLs for legitimacy using a custom-trained machine learning model.
3. **Confidence Score Visualization:** Displays results with a confidence score in a spooky-themed pie chart.
4. **Halloween-Themed UI:** Engages users with creepy visuals, animations, and sound effects.

## Built With
1. **Languages/Frameworks:** Python, Flask, HTML, CSS
2. **Libraries:** OpenCV, Tesseract OCR, scikit-learn, matplotlib


## Datasets: Custom phishing datasets for text and URL classification
1. https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset - For URL Validation
2. https://www.kaggle.com/datasets/shashwatwork/phishing-dataset-for-machine-learning - For Text Spam Classification
3. **textspamdata.csv:** Contains SMS messages labeled as "ham" (legitimate) or "spam". Used for training the Phishing Text Classifier.
4. **URL_dataset_phishing.csv:** Contains URLs with extracted features for phishing and legitimate classification. Used for training the URL classifier.

## 1. Installation
### 1.1. Clone the Repository

```bash
git clone https://github.com/yourusername/FraudSense_AI.git
cd FraudSense_AI
```
### 1.2. Install Required Dependencies
```bash
pip install -r requirements.txt
```

## 2. Usage
### 2.1. Run the Flask Application
```bash
python app.py
```


### 2.2. Using FraudSense_AI
1. **Upload an Image:** Upload an image containing potentially suspicious text, such as SMS or email screenshots.
2. **Enter URL (Optional):** Optionally, enter a URL associated with the text for further analysis.
3. **Click Analyze with FraudSense:** Check for fraudulent content in the uploaded image.
4. **View Results:** See the analysis result with a confidence score and spooky visuals.




## License and Usage Rights

This project was created for HackUNT 2024 and is licensed under the HackUNT 2024 DevPost License. This license allows for personal, educational, and demonstration use. Redistribution or commercial use without permission is prohibited.
For further details on usage rights, please refer to the [DevPost HackUNT 2024 guidelines](https://hackunt-2024.devpost.com/rules) or contact the project author.


# 👻 Happy fraud hunting! 🎃


