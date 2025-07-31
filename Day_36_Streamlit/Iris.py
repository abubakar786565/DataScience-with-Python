# 🌼 Iris Classification Streamlit App

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# 🌟 Page Setup
st.set_page_config(page_title="Iris Classifier", layout="wide")
st.title("🌸 Iris Flower Classification App")

# 📥 Load Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = [iris.target_names[i] for i in iris.target]

# 🎛️ Sidebar Navigation
st.sidebar.title("🌿 Navigation")
page = st.sidebar.radio("Go to", ["1. Dataset Overview", "2. Data Visualization", "3. Prediction Model"])

# =============================
# 📄 1. Dataset Overview
# =============================
if page == "1. Dataset Overview":
    st.header("📊 Iris Dataset Overview")

    st.markdown("""
    This classic dataset contains measurements of 150 iris flowers from 3 species:
    - **Setosa** 🌼
    - **Versicolor** 🌺
    - **Virginica** 🌸
    """)

    if st.checkbox("📂 Show raw data"):
        st.dataframe(iris_df)

    st.subheader("📈 Dataset Summary")
    st.dataframe(iris_df.describe())

    st.subheader("🧮 Species Distribution")
    st.bar_chart(iris_df['species'].value_counts())

# =============================
# 📊 2. Data Visualization
# =============================
elif page == "2. Data Visualization":
    st.header("📊 Visual Explorations")

    st.subheader("🔍 Scatter Plot")
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("X-axis", iris.feature_names, index=0)
    with col2:
        y_axis = st.selectbox("Y-axis", iris.feature_names, index=1)

    fig1, ax1 = plt.subplots()
    sns.scatterplot(data=iris_df, x=x_axis, y=y_axis, hue='species', palette='viridis', ax=ax1)
    st.pyplot(fig1)

    st.subheader("🧩 Pair Plot (All features)")
    pairplot = sns.pairplot(iris_df, hue='species', palette='viridis')
    st.pyplot(pairplot.fig)

    st.subheader("📊 Feature Distribution")
    selected_feature = st.selectbox("Select feature for histogram", iris.feature_names)
    fig2, ax2 = plt.subplots()
    sns.histplot(data=iris_df, x=selected_feature, hue='species', kde=True, palette='viridis', ax=ax2)
    st.pyplot(fig2)

# =============================
# 🤖 3. Prediction Model
# =============================
elif page == "3. Prediction Model":
    st.header("🤖 Iris Species Predictor")

    # Split data
    X = iris_df.drop('species', axis=1)
    y = iris_df['species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Model Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    st.subheader("✅ Model Accuracy")
    st.metric("Accuracy", f"{accuracy:.2%}")

    st.subheader("📉 Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    fig3, ax3 = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap="YlGnBu",
                xticklabels=iris.target_names,
                yticklabels=iris.target_names, ax=ax3)
    ax3.set_xlabel("Predicted")
    ax3.set_ylabel("Actual")
    st.pyplot(fig3)

    st.subheader("🔮 Make a Prediction")

    # Collect user input
    col1, col2 = st.columns(2)
    with col1:
        sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.4)
        petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 3.8)
    with col2:
        sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.4)
        petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.2)

    if st.button("🌟 Predict"):
        input_df = pd.DataFrame([{
            'sepal length (cm)': sepal_length,
            'sepal width (cm)': sepal_width,
            'petal length (cm)': petal_length,
            'petal width (cm)': petal_width
        }])

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df).max()

        emoji = {
            'setosa': '🌼',
            'versicolor': '🌺',
            'virginica': '🌸'
        }

        st.success(f"Predicted Species: **{prediction.capitalize()}** {emoji.get(prediction, '🌷')}")
        st.info(f"Confidence: {probability:.1%}")

# 📝 Footer
st.sidebar.markdown("---")
st.sidebar.caption("Made with ❤️ by Abubakar Suleheri | Powered by Streamlit")
