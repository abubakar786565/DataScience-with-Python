import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = [iris.target_names[i] for i in iris.target]

# Sidebar
st.sidebar.title("Iris Dataset Explorer")
page = st.sidebar.radio("Navigation", ["Dataset Overview", "Data Visualization", "Prediction Model"])

# Main content
st.title("🌼 Iris Flower Classification App")

if page == "Dataset Overview":
    st.header("Iris Dataset")
    st.write("""
    The Iris dataset contains measurements for 150 iris flowers from three different species:
    - Setosa
    - Versicolor
    - Virginica
    """)
    
    st.subheader("View Data")
    if st.checkbox("Show raw data"):
        st.dataframe(iris_df)
    
    st.subheader("Dataset Summary")
    st.write(iris_df.describe())
    
    st.subheader("Species Distribution")
    species_count = iris_df['species'].value_counts()
    st.bar_chart(species_count)

elif page == "Data Visualization":
    st.header("Data Visualization")
    
    st.subheader("Scatter Plot")
    x_axis = st.selectbox("X-axis", iris.feature_names)
    y_axis = st.selectbox("Y-axis", iris.feature_names, index=1)
    
    fig, ax = plt.subplots()
    sns.scatterplot(data=iris_df, x=x_axis, y=y_axis, 
                    hue='species', ax=ax, palette='viridis')
    st.pyplot(fig)
    
    st.subheader("Pair Plot")
    st.write("Relationships between all features:")
    pair_fig = sns.pairplot(iris_df, hue='species', palette='viridis')
    st.pyplot(pair_fig.fig)
    
    st.subheader("Feature Distributions")
    feature = st.selectbox("Select feature", iris.feature_names)
    dist_fig, ax = plt.subplots()
    sns.histplot(data=iris_df, x=feature, hue='species', 
                 kde=True, ax=ax, palette='viridis')
    st.pyplot(dist_fig)

elif page == "Prediction Model":
    st.header("Predict Iris Species")
    
    # Model training
    X = iris_df.drop('species', axis=1)
    y = iris_df['species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    st.subheader("Model Performance")
    st.write(f"Accuracy: {accuracy:.2f}")
    
    st.subheader("Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    cm_fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=iris.target_names,
                yticklabels=iris.target_names, ax=ax)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    st.pyplot(cm_fig)
    
    st.subheader("Make a Prediction")
    st.write("Enter flower measurements:")
    
    col1, col2 = st.columns(2)
    with col1:
        sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.4)
        petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 3.8)
    with col2:
        sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.4)
        petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.2)
    
    if st.button("Predict Species"):
        input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data).max()
        
        st.subheader("Prediction Result")
        st.success(f"Predicted species: **{prediction}**")
        st.info(f"Confidence: {probability:.1%}")
        
        species_emoji = {
            'setosa': '🌼',
            'versicolor': '🌺',
            'virginica': '🌸'
        }
        st.markdown(f"### {species_emoji.get(prediction.lower(), '🌷')} This is a {prediction} flower")

# Footer
st.sidebar.markdown("---")
st.sidebar.info(
    "This app uses the classic Iris dataset to demonstrate classification of iris flowers "
    "into three species based on their measurements."
)