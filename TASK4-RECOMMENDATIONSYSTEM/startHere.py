import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

data = {
    "Title": [
        "Introduction to AI",
        "Deep Learning Basics",
        "Advanced AI Techniques",
        "Natural Language Processing",
        "AI in Healthcare",
        "AI in Robotics",
        "Machine Learning in Finance",
        "AI for Social Good",
        "Reinforcement Learning",
        "AI in Business",
        "Popular Action Games",
        "RPG Games You Must Play",
        "Best Horror Movies 2024",
        "Top Action Movies",
        "AI in Movies",
        "Machine Learning in Video Games"
    ],
    "Description": [
        "An overview of artificial intelligence concepts and applications.",
        "Basics of neural networks and deep learning techniques.",
        "Cutting-edge techniques in artificial intelligence.",
        "Understanding how machines process human language.",
        "Applications of AI in medical diagnostics and healthcare.",
        "Exploring robotics and AI to improve automation and efficiency.",
        "The use of machine learning algorithms in financial markets.",
        "How AI is being applied to solve societal issues.",
        "Fundamentals and techniques of reinforcement learning.",
        "AI's impact on business strategies and operations.",
        "The best action games you can play right now, filled with excitement and adventure.",
        "Top RPG games for immersive gameplay and storytelling.",
        "The scariest horror movies released in 2024.",
        "A list of the best action-packed movies to watch.",
        "AI-driven plotlines in popular movies and their impact.",
        "Exploring how machine learning is transforming video game development."
    ],
    "Category": [
        "AI", "AI", "AI", "NLP", "Healthcare", "Robotics", "Finance", "Social Good", "AI", "Business",
        "Games", "Games", "Movies", "Movies", "Movies", "Games"
    ]
}

assert len(data["Title"]) == len(data["Description"]) == len(data["Category"]), "The lists must have the same length!"

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 3))  
tfidf_matrix = vectorizer.fit_transform(df["Description"])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_recommendations(title, category_filter=None, cosine_sim=cosine_sim, min_similarity=0.05):
    # Find the index of the given title
    idx = df[df["Title"] == title].index[0]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    st.write(f"Similarity scores for '{title}':")
    for i, score in sim_scores[:10]:  
        st.write(f"Title: {df.iloc[i]['Title']}, Similarity: {score}")
    
    sim_scores = sim_scores[1:6]  # Adjust to return top 5 recommendations
    
    item_indices = [i[0] for i in sim_scores if i[1] >= min_similarity]
    
    if item_indices:
        recommendations = df.iloc[item_indices]
        if category_filter and category_filter != "All":
            recommendations = recommendations[recommendations["Category"] == category_filter]
        return recommendations
    else:
        return pd.DataFrame()

# Streamlit UI
st.title("AI and Entertainment Recommendation System")
st.write("Explore related topics in the world of AI, Movies, and Games!")

category_filter = st.sidebar.selectbox("Select a Category", ["All"] + df["Category"].unique().tolist())

if category_filter == "All":
    selected_item = st.selectbox("Select a topic:", df["Title"])
else:
    filtered_df = df[df["Category"] == category_filter]
    selected_item = st.selectbox("Select a topic:", filtered_df["Title"])

st.sidebar.header("Or Enter a Custom Description")
custom_input = st.sidebar.text_area("Describe your topic of interest:")

if st.button("Get Recommendations"):
    if custom_input.strip():
        custom_tfidf_matrix = vectorizer.transform([custom_input])
        custom_cosine_sim = cosine_similarity(custom_tfidf_matrix, tfidf_matrix)
        idx = custom_cosine_sim.argmax()
        recommendations = df.iloc[[idx]]
    else:
        recommendations = get_recommendations(selected_item, category_filter)

    if not recommendations.empty:
        st.subheader(f"Recommendations based on '{selected_item}':")
        for i, row in recommendations.iterrows():
            st.write(f"**{row['Title']}**: {row['Description']}")
            st.write(f"**Category**: {row['Category']}")
            st.write("---")
    else:
        st.write("No relevant recommendations found. Try adjusting the category or the description.")
        st.subheader("Fallback Recommendations (from other categories):")
        fallback_recommendations = get_recommendations(selected_item, category_filter="All")
        if not fallback_recommendations.empty:
            for i, row in fallback_recommendations.iterrows():
                st.write(f"**{row['Title']}**: {row['Description']}")
                st.write(f"**Category**: {row['Category']}")
                st.write("---")

st.markdown("---")
st.markdown(
    "🔗 Built by [Shivam Badhopulu](https://shivamworks.netlify.app/work)"
)
