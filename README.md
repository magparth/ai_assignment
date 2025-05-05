
# Wallet Analysis System - Internship Submission

This repository contains the code and model developed as part of my internship assignment for analyzing wallet behavior. The core functionality of this system is based on a scoring model that evaluates wallets based on their financial activity and presents insights using a web interface.

## Table of Contents

* [Project Overview](#project-overview)
* [Installation](#installation)
* [Usage](#usage)
* [Model Details](#model-details)
* [System Architecture](#system-architecture)
* [Dependencies](#dependencies)


## Project Overview

This project aims to analyze wallet behaviors, scoring them based on several financial metrics. The analysis is performed using the `wallet_scorer.ipynb` Jupyter notebook, which calculates the scores based on real-time data and provides a detailed comparison of the top and bottom wallets. The results are displayed in an interactive web interface.Also you get to donload the ids of top 1000 wallets and their respective scores.

### Key Features:

* **Wallet Scoring**: The system calculates wallet scores based on repayment behavior, deposit activity, liquidation risk, and other key financial metrics.
* **Top and Bottom Wallets**: The analysis compares the top 5 and bottom 5 wallets to highlight the best and worst-performing wallets.
* **Web Interface**: The results are presented in an intuitive, responsive web dashboard with tables and observations.

## Installation

To run this system locally, follow the steps below:

### Step 1: Clone the repository

Clone the repository to your local machine using:

```bash
git clone https://github.com/<your-username>/wallet-analysis-system.git
```

Navigate into the project folder:

```bash
cd wallet-analysis-system
```

### Step 2: Set up a Python virtual environment

Create and activate a virtual environment:

* For **Windows**:

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

* For **macOS/Linux**:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Step 3: Install dependencies

Install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 4: Run the model

The core model logic is implemented in the Jupyter notebook `wallet_scorer.ipynb`. To test the model:

1. Open the `wallet_scorer.ipynb` notebook in Jupyter or any compatible environment.
2. Execute the cells to run the wallet scoring analysis.

### Step 5: Set up the web interface

The web interface is powered by Flask and uses dynamic data to display the results.

To start the web application, run:

```bash
python app.py
```

The application will be hosted on `http://127.0.0.1:5000/`.

## Usage

After running the system, visit `http://127.0.0.1:5000/` to view the following:

* **Top 5 Wallets**: These wallets demonstrate responsible financial behavior with high scores, low liquidation risk, and consistent repayment activity.
* **Bottom 5 Wallets**: These wallets show poor performance, lacking repayment behavior and having high liquidation counts.
* **Observations**: Key insights that validate the scoring model's effectiveness.

## Model Details

The wallet scoring model is implemented in `wallet_scorer.ipynb` and includes the following key components:

1. **Data Processing**: The model processes wallet-related data to calculate metrics like repayment ratio, deposit/withdraw ratio, and liquidation ratio.
2. **Wallet Scoring**: Wallets are scored based on these metrics, and the scores are normalized for comparison.
3. **Analysis**: The system calculates the top and bottom 5 wallets based on the scores and displays them in the web interface.
4. **Model Validation**: The results of the model are compared to expected financial behavior patterns to validate the effectiveness of the scoring algorithm.

### Key Metrics:

* **Repay/Borrow Ratio**: The ratio of repayments to borrowings.
* **Deposit/Withdraw Ratio**: The ratio of deposits to withdrawals.
* **Liquidation Ratio**: The risk factor indicating how often a wallet is liquidated.
* **Wallet Score**: A normalized score that reflects the wallet's overall financial behavior.

## System Architecture

The system is composed of two main components:

1. **Model**: Developed in `wallet_scorer.ipynb` to perform the scoring and data analysis.
2. **Web Interface**: A Flask-based web application that presents the results of the analysis in a user-friendly format.

## Dependencies

This project requires the following Python packages:

* Flask
* pandas
* numpy
* jinja2
* bootstrap

You can install all dependencies using:

```bash
pip install -r requirements.txt
```



### Steps to Run the System Locally:

1. Clone the repository using `git clone`.
2. Set up a Python virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the model in `wallet_scorer.ipynb` for the analysis.
5. Start the Flask app using `python app.py`.
6. Open the application at `http://127.0.0.1:5000/` to view the wallet analysis.

