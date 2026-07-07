import streamlit as st
import math
from collections import Counter

# Page Configuration
st.set_page_config(page_title="AI Playground for Beginners", page_icon="🤖", layout="centered")

st.title("🤖 The Words-to-Numbers Game!")
st.write("Welcome, future AI scientist! Let's play a game to see how computers read.")

st.header("🎮 Level 1: Beat the 'Bag of Words'")
st.write("Remember: A 'Bag of Words' drops all your words into a literal bag and mixes them up. It loses all track of word order!")

# Inputs for Level 1
col1, col2 = st.columns(2)
with col1:
    sentence1 = st.text_input("Sentence 1:", "The dog chased the cat")
with col2:
    sentence2 = st.text_input("Sentence 2:", "The cat chased the dog")

if st.button("Mix them into the Bags! 🌪️"):
    bow1 = Counter(sentence1.lower().split())
    bow2 = Counter(sentence2.lower().split())
    
    st.subheader("What the computer counts:")
    st.json({"Bag 1 Counts": dict(bow1), "Bag 2 Counts": dict(bow2)})
    
    if dict(bow1) == dict(bow2):
        st.error("🚨 TRICKED! The bags match exactly! The computer thinks these two sentences mean the exact same thing because it cannot see word order!")
    else:
        st.success("Nice! You used completely different words, so the computer can tell the bags apart.")

st.markdown("---")

st.header("🪐 Level 2: The TF-IDF Superstar Detector")
st.write("Let's look at 3 short storybooks. One is about space, one is about puppies, and one is about cooking.")

docs = {
    "Book 1 (Space)": "the astronaut launched the rocket into space the the",
    "Book 2 (Pets)": "the fluffy puppy chased the happy little puppy the",
    "Book 3 (Cooking)": "the chef cooked the delicious pasta in the kitchen the"
}

for title, text in docs.items():
    st.caption(f"**{title}**: *\"{text}\"*")

target_word = st.selectbox("Pick a word to track across the books:", ["the", "puppy", "rocket", "chef"])

if st.button("Calculate Superstar Score ✨"):
    # Total documents
    N = len(docs)
    
    # Track term presence
    docs_with_term = sum(1 for text in docs.values() if target_word in text.lower().split())
    
    # Calculate IDF
    idf = math.log(N / docs_with_term) if docs_with_word > 0 else 0
    
    st.write(f"🔍 **Background Noise Score (IDF)** for *'{target_word}'*: `{round(idf, 4)}` (Lower means it is common noise across books!)")
    
    st.subheader("Final Scores per Book:")
    for title, text in docs.items():
        words = text.lower().split()
        tf = words.count(target_word)
        tfidf = tf * idf
        
        if tf > 0:
            st.info(f"🏆 **{title}** score for *'{target_word}'*: `{round(tfidf, 4)}` (Appears {tf} times)")
        else:
            st.write(f"❌ **{title}** score for *'{target_word}'*: `0.0` (Not in this book)")
            
    if target_word == "the":
        st.warning("Notice how 'the' drops to 0 everywhere? Because it's in every single book, TF-IDF completely ignores it!")
    else:
        st.success(f"See that? '{target_word}' scored super high only in the book it belonged to! TF-IDF successfully found the unique superstar word.")