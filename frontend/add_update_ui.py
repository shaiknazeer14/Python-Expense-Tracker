import streamlit as st
from datetime import datetime

def add_update_tab():
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility="collapsed")

    # ✅ Dummy data (with float amounts)
    existing_expenses = [
        {"amount": 1200.0, "category": "Rent", "notes": "Monthly house rent"},
        {"amount": 300.0, "category": "Food", "notes": "Lunch with friends"},
        {"amount": 500.0, "category": "Shopping", "notes": "T-shirt & shoes"},
    ]

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        expenses = []
        for i in range(5):
            if i < len(existing_expenses):
                amount = float(existing_expenses[i]['amount'])  # Ensure float
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(
                    label="Amount", min_value=0.0, step=1.0, value=amount,
                    key=f"amount_{i}", label_visibility="collapsed"
                )
            with col2:
                category_input = st.selectbox(
                    label="Category", options=categories, index=categories.index(category),
                    key=f"category_{i}", label_visibility="collapsed"
                )
            with col3:
                notes_input = st.text_input(
                    label="Notes", value=notes,
                    key=f"notes_{i}", label_visibility="collapsed"
                )

            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

        # ✅ FIXED: submit button with label
        submit_button = st.form_submit_button(label="Submit Expenses")
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]
            st.success("✅ Demo mode: Expenses accepted (not saved to backend)")
