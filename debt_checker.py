import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

# --- Data ---
data_dict = {
    'Deadline': ['14/11/25', '21/11/25', '14/11/25', '21/11/25', '28/11/25', '28/11/25', '28/11/25'],
    'Amount (#)': [172375, 172375, 172375, 172375, 57460, 57460, 57460],
    'Amount Paid (#)': [0, 0, (9480 + 100000 - 40200 + 50000), 0, 0, 0, 0]
}
#Convert to date format
data_dict['Deadline'] = pd.to_datetime(data_dict['Deadline'],dayfirst=True)

# Compute balance automatically
data_dict['Balance (#)'] = np.array(data_dict['Amount (#)']) - np.array(data_dict['Amount Paid (#)'])

# Member names (used as DataFrame index)
names = ['Senator', 'Sister', 'Nurse', 'Sunshine', 'Austin', 'Confidence', 'Victor']

# Create DataFrame
df = pd.DataFrame(data_dict, index=names)

# --- Streamlit App ---
st.title("💰 Burial Levy Checker")

#Deadline reminder
for name in names:
    str_pay_day = str(df.loc[[name],'Deadline']).split('-')[2]
    str_to_day = str(date.today()).split('-')[2]
    if str_pay_day < str_to_day:
        st.subheader('⚠️ {}! your burial levy is over due.\nKindly make payment!'.format(name))

# Dropdown to choose member
selected_name = st.selectbox("Select your name:", names)

# Display payment details
if selected_name:
    st.subheader(f"Payment details for **{selected_name}**")
    st.table(df.loc[[selected_name]])

# Optional: Show all data (for admin view)
with st.expander("📊 View all member records"):
    st.write('Total amount realized so far = {} / {}'.
             format(sum(df['Amount Paid (#)']),sum(df['Amount (#)'])))
    st.dataframe(df)











