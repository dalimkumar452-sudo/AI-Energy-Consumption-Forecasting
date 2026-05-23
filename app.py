import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib
import numpy as np

# Configure Streamlit page to match your screenshots
st.set_page_config(page_title="Energy AI Dashboard", layout="wide", initial_sidebar_state="expanded")

# Load Data and Model
@st.cache_data
def load_data():
    return pd.read_csv("data/energy_dataset.csv")

@st.cache_resource
def load_model():
    return joblib.load("models/rf_model.pkl")

df = load_data()
model = load_model()

# Sidebar Configuration
st.sidebar.title("⚡ Prediction Panel")
st.sidebar.markdown("---")

hour = st.sidebar.slider("⏰ Hour of Day", 0, 23, 12)
day = st.sidebar.slider("📅 Day of Week (0=Mon)", 0, 6, 2)
month = st.sidebar.slider("🌍 Month", 1, 12, 6)
day_type = st.sidebar.selectbox("🔥 Day Type", ["Weekday", "Weekend"])
is_weekend = 1 if day_type == "Weekend" else 0

if st.sidebar.button("⚡ Generate Prediction"):
    input_data = pd.DataFrame({'hour': [hour], 'day': [day], 'month': [month], 'is_weekend': [is_weekend]})
    prediction = model.predict(input_data)[0]
    
    st.sidebar.markdown("### ⚡ Predicted Energy")
    st.sidebar.info(f"**{prediction:.2f} Units**")

# Main Dashboard
st.title("⚡ AI-Powered Energy Consumption Forecasting")
st.markdown("AI-powered forecasting for smart grids & energy optimization")

st.success("🟢 System Active | Model Loaded | Data Ready")

# Layout Columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Energy Trend")
    # Show last 100 data points trend
    fig_trend = px.line(df.tail(100), x='Datetime', y='Energy', template='plotly_dark')
    st.plotly_chart(fig_trend, use_container_width=True)

with col2:
    st.subheader("📌 Dataset Preview")
    st.dataframe(df.head(10), height=300)

st.markdown("---")

# Analytics Section
col3, col4 = st.columns(2)

with col3:
    st.subheader("🌍 Monthly Energy Pattern")
    monthly_avg = df.groupby('month')['Energy'].mean().reset_index()
    fig_month = px.line(monthly_avg, x='month', y='Energy', template='plotly_dark')
    st.plotly_chart(fig_month, use_container_width=True)

with col4:
    st.subheader("⚡ Weekday vs Weekend Usage")
    weekend_avg = df.groupby('is_weekend')['Energy'].mean().reset_index()
    weekend_avg['Day Type'] = weekend_avg['is_weekend'].map({0: 'Weekday', 1: 'Weekend'})
    fig_bar = px.bar(weekend_avg, x='Day Type', y='Energy', template='plotly_dark', color_discrete_sequence=['#87CEEB'])
    st.plotly_chart(fig_bar, use_container_width=True)

# AI vs Reality Section
st.markdown("---")
st.subheader("📊 Energy Forecast Intelligence (AI vs Reality)")

# Simulating actual vs predicted on a small subset
sample_df = df.tail(100).copy()
sample_df['Predicted'] = model.predict(sample_df[['hour', 'day', 'month', 'is_weekend']])

fig_ai = go.Figure()
fig_ai.add_trace(go.Scatter(x=np.arange(100), y=sample_df['Energy'], mode='lines', name='Actual Energy', line=dict(color='#1E90FF')))
fig_ai.add_trace(go.Scatter(x=np.arange(100), y=sample_df['Predicted'], mode='lines', name='Predicted Energy', line=dict(color='#FF8C00')))
fig_ai.update_layout(template='plotly_dark', xaxis_title="Samples", yaxis_title="Energy Usage")

st.plotly_chart(fig_ai, use_container_width=True)