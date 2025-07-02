Mutual Fund Analysis
This project performs exploratory data analysis (EDA) on Indian mutual fund stock data, specifically the Nifty 50 closing prices. The goal is to visualize stock trends and clean the dataset for further financial modeling.

🧰 Features
Cleans and fills missing values using pandas

Visualizes stock trends using plotly

Reads CSV input data dynamically from the /data folder

Easy to extend with new indicators, models, or datasets

📁 Project Structure
bash
Copy
Edit


🧪 Requirements
Install Python packages from the provided requirements file:

bash
Copy
Edit
pip install -r "stock analysis requirements.txt"
Or install individually:

bash
Copy
Edit
pip install pandas plotly
▶️ Running the Project
From the project root, activate your virtual environment and run:

bash
Copy
Edit
python analysis.py
This will:

Load and clean the dataset

Display basic info and trends

Plot stock price movements of all Nifty 50 companies

🔮 Future Enhancements
Add interactive dashboards using Dash or Streamlit

Integrate fundamental/technical indicators

Perform statistical or ML-based forecasting
