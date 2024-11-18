import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "Title": [
        "Introduction to AI", "Deep Learning Basics", "Advanced AI Techniques", "Natural Language Processing", 
        "AI in Healthcare", "AI in Robotics", "Machine Learning in Finance", "AI for Social Good", 
        "Reinforcement Learning", "AI in Business", "Popular Action Games", "RPG Games You Must Play", 
        "Best Horror Movies 2024", "Top Action Movies", "AI in Movies", "Machine Learning in Video Games"
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

def get_data():
    return df, cosine_sim, vectorizer
