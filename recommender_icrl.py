import os
from dotenv import load_dotenv

load_dotenv()
my_api_key = os.getenv("HUGGINGFACE_API_KEY")

from huggingface_hub import InferenceClient

user_context = {
    "favorite_genre": "Sci-Fi",
    "watched_movies": ["Inception", "Interstellar"]
}

def generate_recommendation(user_context):
    input_prompt = f"User likes {user_context['favorite_genre']} movies and has watched {', '.join(user_context['watched_movies'])}. Recommend a movie. Give only the movie name."
    
    recommendation = ''

    for message in client.chat_completion(
        model="microsoft/Phi-3-mini-4k-instruct",
        messages=[{"role": "user", "content": input_prompt}],
        max_tokens=10,
        stream=True,
    ):
        recommendation += message.choices[0].delta.content
    
    return recommendation.strip()


def reward_function(recommended_item, user_feedback):
    if user_feedback == "liked":
        return 1  # Positive reward
    elif user_feedback == "disliked":
        return -1  # Negative reward
    else:
        return 0  # Neutral
    

def update_context(user_context, recommendation, feedback):
    if feedback == "liked":
        user_context["watched_movies"].append(recommendation)
    return user_context


import random

def explorative_recommendation(user_context):
    if random.random() < 0.2:  # Exploration with a 20% chance
        # Explore a different genre or type of recommendation
        input_prompt = "Recommend a random movie. Give only the movie name."
        
        recommendation = ''

        for message in client.chat_completion(
            model="microsoft/Phi-3-mini-4k-instruct",
            messages=[{"role": "user", "content": input_prompt}],
            max_tokens=10,
            stream=True,
        ):
            recommendation += message.choices[0].delta.content


        return recommendation
    else:
        return generate_recommendation(user_context)  # Exploit known preferences
    

for _ in range(10):  # Simulate 10 recommendation iterations
    recommendation = explorative_recommendation(user_context)
    print(f"Recommendation: {recommendation}")
    
    # Simulate feedback (In a real system, this would come from the user)
    user_feedback = random.choice(["liked", "disliked", "neutral"])
    print(f"User feedback: {user_feedback}")

    # Update user context
    user_context = update_context(user_context, recommendation, user_feedback)

