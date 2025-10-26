import pandas as pd
import plotly.express as px
import streamlit as st

def perform_eda(df):
    """
    Returns a summary dictionary of the dataframe.
    """
    summary = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Rows": df.duplicated().sum(),
        "Numeric Columns": len(df.select_dtypes(include="number").columns),
        "Categorical Columns": len(df.select_dtypes(exclude="number").columns)
    }
    return summary

def show_visuals(df):
    """
    Generates numeric and categorical plots for EDA.
    """
    num_cols = df.select_dtypes(include="number").columns.tolist()
    cat_cols = df.select_dtypes(exclude="number").columns.tolist()

    # ------------------- Numeric Columns ------------------- #
    if num_cols:
        st.write("### 📉 Numeric Data Distribution")
        num_col = st.selectbox("Select numeric column", num_cols)
        fig = px.histogram(df, x=num_col, nbins=30, title=f"Distribution of {num_col}")
        st.plotly_chart(fig, use_container_width=True)

        # Boxplot for outliers
        fig_box = px.box(df, y=num_col, title=f"Boxplot of {num_col}")
        st.plotly_chart(fig_box, use_container_width=True)

    # ----------------- Categorical Columns ----------------- #
    if cat_cols:
        st.write("### 🧩 Categorical Value Counts")
        cat_col = st.selectbox("Select categorical column", cat_cols)
        vc = df[cat_col].value_counts().reset_index()
        vc.columns = [cat_col, 'count']  # rename for Plotly
        vc['percent'] = round(vc['count'] / vc['count'].sum() * 100, 2)

        fig = px.bar(vc, x=cat_col, y='count', text='percent',
                     title=f"Value Counts for {cat_col}")
        fig.update_traces(texttemplate='%{text}%', textposition='outside')
        st.plotly_chart(fig, use_container_width=True)

        # Pie chart
        fig_pie = px.pie(vc, names=cat_col, values='count', title=f"Distribution of {cat_col}")
        st.plotly_chart(fig_pie, use_container_width=True)
