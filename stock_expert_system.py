import streamlit as st

def short_term_strategy(parameters):
    # Implement short-term investment strategy logic
    return "Short-term: Buy" if parameters["volatility"] > 0.5 and parameters["volume"] > 100000 and parameters["pe_ratio"] < 20 else "Short-term: Hold"

def mid_term_strategy(parameters):
    # Implement mid-term investment strategy logic
    return "Mid-term: Buy" if parameters["growth_rate"] > 0.1 and parameters["debt_to_equity"] < 0.5 and parameters["sector_pe_ratio"] < 25 else "Mid-term: Hold"

def long_term_strategy(parameters):
    # Implement long-term investment strategy logic
    return "Long-term: Buy" if parameters["competitive_advantage"] and parameters["pe_ratio"] < 15 else "Long-term: Hold"

def main():
    st.title("Stock Investment Advisor")

    strategy = st.radio("Select Investment Strategy:", ("Short-term", "Mid-term", "Long-term"))

    st.subheader("Enter Company Parameters:")

    parameters = {}
    if strategy == "Short-term":
        parameters["volatility"] = st.slider("Volatility", min_value=0.0, max_value=1.0, step=0.01, value=0.5)
        parameters["volume"] = st.number_input("Volume", min_value=0, step=10000, value=100000)
        parameters["pe_ratio"] = st.number_input("P/E Ratio", min_value=0, step=1, value=15)
    elif strategy == "Mid-term":
        parameters["growth_rate"] = st.slider("Growth Rate", min_value=0.0, max_value=1.0, step=0.01, value=0.5)
        parameters["debt_to_equity"] = st.slider("Debt to Equity", min_value=0.0, max_value=1.0, step=0.01, value=0.5)
        parameters["sector_pe_ratio"] = st.number_input("Sector P/E Ratio", min_value=0, step=1, value=20)
    elif strategy == "Long-term":
        parameters["competitive_advantage"] = st.checkbox("Competitive Advantage")
        parameters["pe_ratio"] = st.number_input("P/E Ratio", min_value=0, step=1, value=12)

    if st.button("Submit"):
        if strategy == "Short-term":
            result = short_term_strategy(parameters)
        elif strategy == "Mid-term":
            result = mid_term_strategy(parameters)
        elif strategy == "Long-term":
            result = long_term_strategy(parameters)
        
        st.write("Recommendation:", result)

if __name__ == "__main__":
    main()