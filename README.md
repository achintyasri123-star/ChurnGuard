# Churn Guard

Churn Guard is a customer churn-risk analysis dashboard that helps identify customers who may be likely to leave a service. It reads customer data from a CSV file, calculates a risk score using customer-related parameters, and displays the results in an easy-to-understand Streamlit dashboard.

## Features

* Customer churn-risk analysis
* Identifies high-risk customers
* Displays risk percentages and customer information
* Supports customer data through CSV files
* Built with Python, Pandas, and Streamlit
* Includes a sample `demo.csv` file showing the required data format

## Project Structure

```text
Churn-Guard/
│
├── ChurnGuard.py
├── Demo_Datasets_Sturcture.csv
├── README.md
└── requirements.txt
```

## Input Data

Churn Guard expects customer information in CSV format.

The included `demo.csv` file is provided as a sample dataset. It shows the structure, column names, and type of information that should be provided to the application.

You can use `demo.csv` as a template when creating your own dataset.

### Example `demo.csv`

```csv
CustomerID,Age,MonthlyCharges,TechSupport
1001,25,45.50,No
1002,42,89.99,Yes
1003,31,72.00,No
1004,56,95.50,Yes
```

### Required Data

The CSV should contain the columns expected by the Churn Guard scoring logic.

| Column           | Description                                |
| ---------------- | ------------------------------------------ |
| `CustomerID`     | Unique identifier for the customer         |
| `Age`            | Customer's age                             |
| `MonthlyCharges` | Customer's monthly service charge          |
| `TechSupport`    | Whether the customer has technical support |

Keep the column names and data format consistent with `demo.csv`. If you modify the columns, the scoring logic may need to be modified as well.

## How Churn Guard Works

Churn Guard evaluates customer information using predefined scoring conditions.

Each relevant customer parameter contributes to the customer's overall risk score. The score is then converted into a percentage and used to classify customers according to their churn risk.

The application uses the project's defined scoring logic to calculate risk.

## Running the Project

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Then start the Streamlit application:

```bash
streamlit run ChurnGuard.py
```

The dashboard will open in your browser.

## Using Your Own Dataset

1. Open `Demo_Dataset_Sturcture.csv`.
2. Use it as a template for your customer dataset.
3. Replace the sample customer records with your own data.
4. Keep the required column names unchanged.
5. Place the CSV where the application expects the input file.
6. Run Churn Guard.

## Purpose

Churn Guard is designed as a simple and understandable way to demonstrate how customer data can be analyzed to identify customers who may need attention before they leave a service.

## Technologies

* Python
* Pandas
* Streamlit
* NumPy

## Note

`demo.csv` is included specifically to demonstrate the input format required by Churn Guard. It is a sample dataset and should not be treated as real customer data.
