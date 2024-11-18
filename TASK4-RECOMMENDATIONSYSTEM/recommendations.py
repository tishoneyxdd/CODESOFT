import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

def get_recommendations(title, category_filter=None, cosine_sim=None, min_similarity=0.05, df=None):
    idx = df[df["Title"] == title].index[0]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    st.write(f"Similarity scores for '{title}':")
    for i, score in sim_scores[:10]:  
        st.write(f"Title: {df.iloc[i]['Title']}, Similarity: {score}")
    
    sim_scores = sim_scores[1:6]  
    
    item_indices = [i[0] for i in sim_scores if i[1] >= min_similarity]
    
    if item_indices:
        recommendations = df.iloc[item_indices]
        if category_filter and category_filter != "All":
            recommendations = recommendations[recommendations["Category"] == category_filter]
        return recommendations
    else:
        return pd.DataFrame()

def get_fallback_recommendations(selected_item, category_filter, cosine_sim, df):
    return get_recommendations(selected_item, category_filter="All", cosine_sim=cosine_sim, df=df)
