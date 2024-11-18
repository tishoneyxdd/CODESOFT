import streamlit as st
from data import get_data
from recommendations import get_recommendations, get_fallback_recommendations

df, cosine_sim, vectorizer = get_data()

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
        custom_cosine_sim = cosine_similarity(custom_tfidf_matrix, cosine_sim)
        idx = custom_cosine_sim.argmax()
        recommendations = df.iloc[[idx]]
    else:
        recommendations = get_recommendations(selected_item, category_filter, cosine_sim, df=df)

    if not recommendations.empty:
        st.subheader(f"Recommendations based on '{selected_item}':")
        for i, row in recommendations.iterrows():
            st.write(f"**{row['Title']}**: {row['Description']}")
            st.write(f"**Category**: {row['Category']}")
            st.write("---")
    else:
        st.write("No relevant recommendations found. Try adjusting the category or the description.")
        st.subheader("Fallback Recommendations (from other categories):")
        fallback_recommendations = get_fallback_recommendations(selected_item, category_filter, cosine_sim, df)
        if not fallback_recommendations.empty:
            for i, row in fallback_recommendations.iterrows():
                st.write(f"**{row['Title']}**: {row['Description']}")
                st.write(f"**Category**: {row['Category']}")
                st.write("---")

st.markdown("---")
st.markdown(
    "🔗 Built by [Shivam Badhopulu](https://shivamworks.netlify.app/work)"
)
