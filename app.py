import streamlit as st
import pandas as pd

# Store expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = []

st.title("Expense Tracker")

menu = ["Add Expense", "View Expenses"]

choice = st.sidebar.selectbox("Menu", menu)

# Add Expense
if choice == "Add Expense":

    name = st.text_input("Expense Name")

    category = st.selectbox(
        "Category",
        ["Food", "Travel", "Shopping", "Bills"]
    )

    amount = st.number_input("Amount", min_value=0)

    if st.button("Add"):

        st.session_state.expenses.append(
            [name, category, amount]
        )

        st.success("Expense Added")

# View Expenses
elif choice == "View Expenses":

    if len(st.session_state.expenses) == 0:

        st.warning("No Expenses Added")

    else:

        df = pd.DataFrame(
            st.session_state.expenses,
            columns=["Expense", "Category", "Amount"]
        )

        st.dataframe(df)

        total = df["Amount"].sum()

        st.subheader(f"Total Expense = ₹{total}")
