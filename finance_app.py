import streamlit as st
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Personal Finance Toolkit",
    page_icon="💰",
    layout="centered"
)

# --- CSS FOR STYLING ---
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 2rem;
    }
    .disclaimer-container {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 5px;
        margin-top: 50px;
        border-left: 4px solid #f1c40f;
        font-size: 0.85rem;
        color: #444;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #888;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #eee;
    }
    .footer a {
        color: #4CAF50;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. GLOBAL SETTINGS (Currency Selector) ---
st.sidebar.title("⚙️ Settings")
currency_choice = st.sidebar.selectbox(
    "Select Currency", 
    ["₹ INR", "$ USD", "€ EUR", "£ GBP"]
)
curr = currency_choice.split()[0] 

# --- 2. DEFINE THE TOOLS MAP ---
TOOLS = {
    "home": "Home",
    "doubling": "Rule of 72 (Doubling)",
    "tripling": "Rule of 114 (Tripling)",
    "quadrupling": "Rule of 144 (Quadrupling)",
    "inflation": "Rule of 70 (Inflation)",
    "allocation": "The 110 Rule (Asset Allocation)",
    "emergency": "The 3-6 Rule (Emergency Fund)",
    "budget": "50-30-20 Rule (Budgeting)",
    "retirement": "The 4% Rule (Retirement)",
    "car": "20-4-10 Rule (Car Buying)"
}

# --- 3. HANDLE DEEP LINKING ---
query_params = st.query_params
default_tool = "Home"

if "tool" in query_params:
    requested_key = query_params["tool"]
    if requested_key in TOOLS:
        default_tool = TOOLS[requested_key]

options = list(TOOLS.values())
default_index = options.index(default_tool)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📚 Finance Toolkit")
selected_rule = st.sidebar.radio(
    "Select a Calculator:",
    options,
    index=default_index 
)

# --- HELPER FUNCTIONS ---
def show_disclaimer():
    st.markdown("""
        <div class="disclaimer-container">
        <strong>⚠️ IMPORTANT DISCLAIMER</strong>
        <br><br>
        <strong>1. Educational Use Only (Global):</strong> This tool is designed strictly for educational and informational purposes. The calculations provided are based on general financial rules of thumb and do not constitute specific investment advice, financial planning, or a recommendation to buy/sell any financial instruments.
        <br><br>
        <strong>2. SEBI Disclosure (For Indian Users):</strong> I am <strong>not</strong> a SEBI Registered Investment Advisor (RIA). No content on this application should be construed as investment advice under SEBI (Investment Advisers) Regulations, 2013. Please consult a qualified financial professional before making any financial decisions.
        </div>
    """, unsafe_allow_html=True)

# --- PAGE LOGIC ---

if selected_rule == "Home":
    st.markdown('<div class="main-header">💰 Personal Finance Toolkit</div>', unsafe_allow_html=True)
    st.write(f"""
    ### 👋 Welcome!
    Select a tool from the sidebar to start planning your financial future.
    
    **Current Currency:** **{currency_choice}** (Change in sidebar)
    
    **💡 Quick Links:**
    * 🚗 [Car Buying Planner](?tool=car)
    * 🏖️ [Retirement Planner](?tool=retirement)
    * 📈 [Doubling Rule](?tool=doubling)
    """)
    st.info("👈 Use the sidebar menu to navigate.")

elif selected_rule == "Rule of 72 (Doubling)":
    st.title("Rule of 72 📈")
    st.markdown("**Find out how many years it takes to DOUBLE your money.**")
    st.latex(r"Years = \frac{72}{Interest Rate}")
    
    rate = st.number_input("Expected Annual Return (%)", min_value=1.0, max_value=100.0, value=10.0)
    years = 72 / rate
    st.success(f"At {rate}%, your money will **DOUBLE** in approx **{years:.1f} years**.")

elif selected_rule == "Rule of 114 (Tripling)":
    st.title("Rule of 114 🚀")
    st.markdown("**Find out how many years it takes to TRIPLE your money.**")
    st.latex(r"Years = \frac{114}{Interest Rate}")
    
    rate = st.number_input("Expected Annual Return (%)", min_value=1.0, max_value=100.0, value=10.0)
    years = 114 / rate
    st.success(f"At {rate}%, your money will **TRIPLE** in approx **{years:.1f} years**.")

elif selected_rule == "Rule of 144 (Quadrupling)":
    st.title("Rule of 144 💰")
    st.markdown("**Find out how many years it takes to QUADRUPLE (4x) your money.**")
    st.latex(r"Years = \frac{144}{Interest Rate}")
    
    rate = st.number_input("Expected Annual Return (%)", min_value=1.0, max_value=100.0, value=10.0)
    years = 144 / rate
    st.success(f"At {rate}%, your money will **QUADRUPLE** in approx **{years:.1f} years**.")

elif selected_rule == "Rule of 70 (Inflation)":
    st.title("Rule of 70 💸")
    st.markdown("**Find out how fast Inflation HALVES your money's purchasing power.**")
    st.latex(r"Years = \frac{70}{Inflation Rate}")
    
    inflation = st.number_input("Inflation Rate (%)", min_value=1.0, max_value=50.0, value=6.0)
    years = 70 / inflation
    st.warning(f"At {inflation}% inflation, your money will lose **HALF its value** in **{years:.1f} years**.")

elif selected_rule == "The 110 Rule (Asset Allocation)":
    st.title("The 110 Rule ⚖️")
    st.markdown("**Determine how much Equity (Stocks) you should hold.**")
    st.latex(r"Equity \% = 110 - Age")
    
    age = st.slider("Your Age", 18, 100, 25)
    equity = 110 - age
    debt = 100 - equity
    if equity < 0: equity = 0
    if debt > 100: debt = 100
    
    col1, col2 = st.columns(2)
    col1.metric("Equity (Stocks)", f"{equity}%")
    col2.metric("Debt (Bonds/FD)", f"{debt}%")
    
    df = pd.DataFrame({'Allocation': [equity, debt]}, index=['Equity', 'Debt'])
    st.bar_chart(df)

elif selected_rule == "The 3-6 Rule (Emergency Fund)":
    st.title("The 3-6 Rule 🛡️")
    st.markdown("**Calculate the Emergency Fund you need.**")
    
    expense = st.number_input(f"Monthly Expenses ({curr})", min_value=0, value=25000, step=500)
    min_fund = expense * 3
    max_fund = expense * 6
    st.info(f"You should save between **{curr}{min_fund:,.0f}** and **{curr}{max_fund:,.0f}**.")

elif selected_rule == "50-30-20 Rule (Budgeting)":
    st.title("50-30-20 Rule 📊")
    st.markdown("**The classic budgeting framework.**")
    
    income = st.number_input(f"Monthly Income (After Tax) ({curr})", min_value=0, value=50000, step=1000)
    needs = income * 0.50
    wants = income * 0.30
    savings = income * 0.20
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Needs (50%)", f"{curr}{needs:,.0f}")
    c2.metric("Wants (30%)", f"{curr}{wants:,.0f}")
    c3.metric("Savings (20%)", f"{curr}{savings:,.0f}")

elif selected_rule == "The 4% Rule (Retirement)":
    st.title("The 4% Rule 🏖️")
    st.markdown("**Safe annual withdrawal from retirement corpus.**")
    
    corpus = st.number_input(f"Total Retirement Corpus ({curr})", min_value=0, value=1000000, step=10000)
    safe_withdrawal = corpus * 0.04
    monthly = safe_withdrawal / 12
    st.success(f"Safe Withdrawal: **{curr}{safe_withdrawal:,.0f}/year** ({curr}{monthly:,.0f}/month).")

elif selected_rule == "20-4-10 Rule (Car Buying)":
    st.title("20-4-10 Rule 🚗")
    st.markdown("**How much Car can you afford?**")
    
    income = st.number_input(f"Monthly Income ({curr})", min_value=0, value=80000, step=1000)
    loan_rate = st.number_input("Car Loan Interest Rate (%)", value=9.0)
    
    max_emi = income * 0.10
    r = (loan_rate / 100) / 12
    n = 4 * 12
    max_loan = max_emi * (1 - (1 + r)**(-n)) / r
    max_price = max_loan / 0.8
    down_payment = max_price * 0.2
    
    st.divider()
    st.subheader(f"🚗 Max Budget: {curr}{max_price:,.0f}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Max EMI (10%)", f"{curr}{max_emi:,.0f}")
    col2.metric("Down Payment", f"{curr}{down_payment:,.0f}")
    col3.metric("Max Loan", f"{curr}{max_loan:,.0f}")

# --- DISPLAY DISCLAIMER & AUTHOR ---
st.divider()
show_disclaimer()

# 👇 YOUR DETAILS
MY_NAME = "Kevin Joseph"
MY_LINKEDIN = "https://www.linkedin.com/in/kevin-joseph-in/"

st.markdown(
    f"""
    <div class="footer">
        Made  by <a href="{MY_LINKEDIN}" target="_blank">{MY_NAME}</a>
    </div>
    """,
    unsafe_allow_html=True
)
