import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="AI Text Generation",
    page_icon="🤖"
)

st.title("🤖 AI Text Generation")
st.write("Enter a sentence and let AI complete it for you!")

prompt = st.text_area(
    "Enter your sentence",
    placeholder="Example: Artificial intelligence is changing the world...",
    height=150
)

max_tokens = st.slider(
    "Maximum new words/tokens",
    min_value=20,
    max_value=200,
    value=100,
    step=10
)

if st.button("🚀 Generate Text"):

    if prompt.strip():

        with st.spinner("Loading AI model and generating text..."):

            generator = pipeline(
                "text-generation",
                model="gpt2"
            )

            result = generator(
                prompt,
                max_new_tokens=max_tokens,
                do_sample=True,
                temperature=0.7,
                top_p=0.9
            )

        generated_text = result[0]["generated_text"]

        st.subheader("✨ Generated Text")
        st.write(generated_text)

    else:
        st.warning("⚠️ Please enter a sentence first.")