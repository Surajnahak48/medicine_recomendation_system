# Medicine Recommendation System

## Overview
The **Medicine Recommendation System** is a machine learning-based web application designed to predict diseases based on user-input symptoms. It provides detailed descriptions of predicted diseases and recommends relevant medications, precautions, diet plans, and workouts.

## Features
<!-- - Accepts user symptoms in natural language (e.g., "continuous sneezing" instead of "continuous_sneezing"). -->
- Uses a trained machine learning model for disease prediction.
- Provides disease descriptions and recommended precautions.
- Suggests suitable medications, dietary plans, and workouts.
- User-friendly web interface built using Flask.

## Installation
### Prerequisites
Ensure you have Python installed on your system.

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Surajnahak48/medicine_recomendation_system.git
   cd medicine-recommendation-system
   ```
2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```sh
   python main.py
   ```
4. Open your browser and go to:
   ```sh
   http://127.0.0.1:5000/
   ```

## How to Use
1. Enter symptoms separated by commas (e.g., `itching, skin rash, nodal skin eruptions`).
2. Click on the **Predict** button.
3. View the predicted disease, its description, and the recommended treatment options.

## Project Structure
```
medicine-recommendation-system/
│-- datasets/            # Contains symptom-disease datasets
│-- models/              # Trained machine learning model
│-- templates/           # HTML templates for Flask
│-- main.py              # Flask web application
│-- requirements.txt     # Dependencies
│-- README.md            # Documentation
```

## Contributing
You are welcome to contribute by:
- Adding more symptoms and diseases to the dataset.
- Improving UI/UX for better user experience.
- Enhancing machine learning model accuracy.

## License
This project is licensed under the MIT License.

---
**Author:** Suraj Nahak
