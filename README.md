# End‑to‑End Machine Learning Project for Data Science

This repository implements a complete **end‑to‑end Machine Learning workflow**, including data preprocessing, model training, model persistence, and a **Flask web application** for making real‑time predictions.

This project can be used as a template for building and deploying ML models that serve predictions via an API or a web interface.

---

## Project Structure
```
mlproject/
│
├── artifacts/ # Saved models / preprocessors
├── notebook/ # Exploratory notebooks
├── src/
│ ├── exception.py # Custom exception code
│ ├── logger.py # Logging configuration
│ └── pipeline/
│ ├── predict_pipeline.py # Code for prediction pipeline
│
├── templates/ # HTML templates for Flask UI
├── app.py # Flask application entry point
├── requirements.txt # Python dependencies
├── setup.py # Package configuration
└── README.md # This file
```



---

## 🚀 Features

✔ Builds a trained ML model and preprocessor  
✔ Includes modular code for training, evaluation, and prediction  
✔ REST API + web interface via **Flask**  
✔ Easily extendable for new datasets or models

---

## How It Works

1. **Data Input**  
   • Users submit features via a web form.  
2. **Preprocessing**  
   • A saved scikit‑learn preprocessor scales and encodes the input.  
3. **Model Inference**  
   • A trained model makes predictions on new inputs.  
4. **Output**  
   • Results are displayed dynamically in the web UI.

The ML pipeline code is implemented in `src/pipeline/predict_pipeline.py`.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Negar‑Erfanian/mlproject.git
   cd mlproject
   ```

2. Create and activate a Python environment:
```bash
  python3 ‑m venv venv
  source venv/bin/activate
  ```
3. Install dependencies:

  ```bash
  pip install ‑r requirements.txt
  ```
