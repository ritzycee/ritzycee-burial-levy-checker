import streamlit as st
import pandas as pd
import numpy as np

# --- Data ---
data_dict = {
    'Deadline': ['14/11/25', '21/11/25', '14/11/25', '21/11/25', '28/11/25', '28/11/25', '28/11/25'],
    'Amount (#)': [172375, 172375, 172375, 172375, 57460, 57460, 57460],
    'Amount Paid (#)': [0, 0, (9480 + 90000), 0, 0, 0, 0]
}

# Compute balance automatically
data_dict['Balance (#)'] = np.array(data_dict['Amount (#)']) - np.array(data_dict['Amount Paid (#)'])

# Member names (used as DataFrame index)
names = ['Senator', 'Sister', 'Nurse', 'Sunshine', 'Austin', 'Confidence', 'Victor']

# Create DataFrame
df = pd.DataFrame(data_dict, index=names)

# --- Streamlit App ---
st.title("💰 Burial Levy Checker")

# Dropdown to choose member
selected_name = st.selectbox("Select your name:", names)

# Display payment details
if selected_name:
    st.subheader(f"Payment details for **{selected_name}**")
    st.table(df.loc[[selected_name]])

# Optional: Show all data (for admin view)
with st.expander("📊 View all member records"):
    st.write('Total amount realized = {} / {}'.
             format(sum(df['Amount Paid (#)']),sum(df['Amount (#)'])))
    st.dataframe(df)




