from flask import Flask, render_template, send_file
import pandas as pd
import pickle
import io

app = Flask(__name__)

# Load your processed wallet scoring DataFrame
with open("wallet_scoring.pkl", "rb") as f:
    wallet_features = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download")
def download_csv():
    top_1000 = wallet_features.sort_values(by="normalized_score", ascending=False).head(1000)
    output = io.StringIO()
    top_1000[["wallet", "normalized_score"]].to_csv(output, index=False)
    output.seek(0)

    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype="text/csv",
        as_attachment=True,
        download_name="top_1000_wallets.csv"
    )

@app.route("/wallet-analysis")
def wallet_analysis():
    sorted_wallets = wallet_features.sort_values(by="normalized_score", ascending=False)

    top_wallets = sorted_wallets.head(5)
    bottom_wallets = sorted_wallets.tail(5)

    cols = [
        "wallet",
        "normalized_score",
        "repay_to_borrow_ratio",
        "deposit_to_withdraw_ratio",
        "liquidation_ratio",
        "sum_deposit",
        "sum_repay",
        "count_borrow",
        "count_repay",
        "count_liquidation"
    ]

    top_data = top_wallets[cols].to_dict(orient="records")
    bottom_data = bottom_wallets[cols].to_dict(orient="records")

    return render_template("wallet_analysis.html", top_data=top_data, bottom_data=bottom_data)

if __name__ == "__main__":
    app.run(debug=True)
