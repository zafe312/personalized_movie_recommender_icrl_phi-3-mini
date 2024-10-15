# Personalized Recommender System with Explorative In-Context Reinforcement Learning

This project implements a personalized recommender system using explorative In-Context Reinforcement Learning (ICRL) techniques. The recommender is built using a free Large Language Model (LLM) API (Hugging Face’s 
Phi-3-mini-4k-instruct), which dynamically generates recommendations based on user preferences and feedback.

## Features
- **Personalized Recommendations**: Generates movie recommendations based on user preferences.
- **Exploration vs. Exploitation**: Occasionally explores new recommendations outside the user’s existing preferences to discover new items.
- **Contextual Learning**: Continuously updates user profiles based on interactions, learning over time.

## Getting Started

### 1. Clone the Repository
### 2. Set Up a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install the Dependencies

```bash
pip install -r requirements.txt

### Set Up the API Key
You’ll need an API key to access the Hugging Face API.

Sign up or log in to Hugging Face. Go to Settings -> Access Tokens and create a new token. Copy the token.
Create a .env file in the root directory of the project:

```bash
touch .env

Add the following line to the .env file, replacing your_huggingface_api_key_here with your actual API key:

```bash
HUGGINGFACE_API_KEY=your_huggingface_api_key_here

### Run the Application
python recommender_icrl.py

