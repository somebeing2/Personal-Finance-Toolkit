#  Personal Finance Toolkit

**Personal Finance Toolkit** is a comprehensive suite of interactive financial calculators designed for universal financial planning.

Unlike static spreadsheets, this app features a **Dynamic Currency Selector** (supports USD, INR, EUR, GBP) and **Deep Linking** capabilities, making it a flexible tool for users worldwide to visualize wealth growth, budget effectively, and plan for retirement.

**Live App:** [Insert your Streamlit App Link Here]

---

### Included Tools

The toolkit features **10+ calculators** organized into three key pillars:

####  Wealth & Growth
* **Rule of 72, 114 & 144:** Instantly calculate the time required to Double (2x), Triple (3x), or Quadruple (4x) your investment at any interest rate.
* **Rule of 70:** Visualizes the impact of inflation on purchasing power over time.

####  Safety & Allocation
* **The 110 Rule:** A dynamic asset allocation model (Equity vs. Debt) based on age.
* **The 3-6 Rule:** Calculates the precise Emergency Fund range needed based on monthly expenses.

####  Budgeting & Lifestyle
* **20-4-10 Car Rule:** A "Reverse Affordability" calculator that determines your maximum car budget based on income and loan terms.
* **50-30-20 Rule:** The classic framework for balancing Needs, Wants, and Savings.
* **The 4% Rule:** Estimates the safe annual withdrawal rate from a retirement corpus to ensure longevity.

---

###  Key Features

* **Universal Currency Support:** Users can toggle between **USD ($), INR (₹), EUR (€), and GBP (£)** instantly via the sidebar.
* **Deep Linking System:** Share specific tools directly with URL parameters (e.g., `/?tool=car` opens the Car Calculator immediately).
* **Responsive Interface:** Clean, mobile-friendly design built with Streamlit's latest components.
* **Privacy First:** All calculations are performed client-side in the browser session. No data is stored.
###  Tech Stack

* **Frontend:** Streamlit (Python Web Framework)
* **Logic:** Python (Financial formulas, Time Value of Money calculations)
* **Visualization:** Pandas & Streamlit Charts

### How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/Personal-Finance-Toolkit.git](https://github.com/yourusername/Personal-Finance-Toolkit.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the app:**
    ```bash
    streamlit run finance_app.py
    ```

---
## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

*Disclaimer: This tool is for educational purposes only and does not constitute financial advice. Please consult a qualified financial professional before making investment decisions.*
