import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng


st.set_page_config(
    page_title="Customer Churn Intelligence",
    layout="wide"
)

st.markdown("""
<style>
    .block-container {
        max-width: 100%;
        padding: 0.5rem 1rem;
    }
</style>
""", unsafe_allow_html=True)


col1, col2, col3, col4 = st.columns([2, 2, 2, 2])

with col1:
    st.write("Pinlens")

with col4:
    st.write("🟢 Model Online")


st.title("Customer Churn Intelligence")
st.write("Upload customer data")


uploaded_file = st.file_uploader(
    "Upload data",
    type="csv"
)

if uploaded_file is None:
    st.stop()

data = pd.read_csv(uploaded_file)

rows = data.shape[0]

data["MonthlyCharges"] = pd.to_numeric(
    data["MonthlyCharges"],
    errors="coerce"
)

data["TenureMonths"] = pd.to_numeric(
    data["TenureMonths"],
    errors="coerce"
)

data["Age"] = pd.to_numeric(
    data["Age"],
    errors="coerce"
)


Churn = 0
Active = 0

i = 0

while i < rows:

    if data.loc[i, "Churn"] == "Yes":
        Churn += 1
    else:
        Active += 1

    i += 1


col5, col6, col7 = st.columns([2, 2, 2])

with col5:
    st.metric(
        label="Total Customer",
        value=rows
    )

with col6:
    st.metric(
        label="Active",
        value=Active
    )

with col7:
    st.metric(
        label="Churned",
        value=Churn
    )


df = pd.DataFrame(
    rng(0).standard_normal((20, 2)),
    columns=["Active", "Churned"]
)

st.line_chart(df)


def score(i):

    score_value = 0

    if data.loc[i, "Churn"] == "No":

        if data.loc[i, "TechSupport"] == "Yes":
            score_value += 0

        if data.loc[i, "MonthlyCharges"] >= 80:
            score_value += 2
        else:
            score_value += 1

        if data.loc[i, "Contract"] == "Month-to-month":
            score_value += 2

        if data.loc[i, "Age"] <= 50:
            score_value += 0
        if data.loc[i, "TenureMonths"] <= 40:
            score_value += 2  




    percentage = score_value / 8 * 100

    return [
        "Customer",
        data.loc[i, "CustomerID"],
        percentage,
        "%"
    ]


def start():

    results = []

    i = 0

    while i < rows:

        if data.loc[i, "Churn"] == "No":
            results.append(score(i))

        i += 1

    return results


cus = start()


customer_ids = []
percentages = []

for customer in cus:

    customer_id = customer[1]
    percentage = customer[2]

    customer_ids.append(customer_id)
    percentages.append(percentage)


data1 = pd.DataFrame({
    "Customer": customer_ids,
    "Risk": percentages
})

data1 = data1.sort_values(
    by="Risk",
    ascending=False
)


with st.container(border=True):

    st.subheader("🚨 High Risk Customers")

    st.dataframe(
        data1,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Customer": st.column_config.TextColumn(
                "Customer"
            ),
            "Risk": st.column_config.ProgressColumn(
                "Risk",
                min_value=0,
                max_value=100,
                format="%d%%"
            )
        }
    )


st.subheader("🔍 Customer Details")

for customer in cus:

    customer_id = customer[1]
    percentage = customer[2]
    value = customer_id

    result = data.eq(value)
    rows, cols = result.to_numpy().nonzero()


    with st.expander(
        f"🔴 Customer {customer_id} — {percentage:.0f}%"
    ):
        if data.loc[rows[0],"TechSupport"]== 'No':
            st.write("No Tech Support")
        if data.loc[rows[0],"Contract"]== 'Month-to-month':
            st.write("Short Contract")
        if data.loc[rows[0],"TenureMonths"]<= 40:
                st.write("Short Tenure")
        if data.loc[rows[0], "MonthlyCharges"] >= 70:
            st.write("High Charges")
