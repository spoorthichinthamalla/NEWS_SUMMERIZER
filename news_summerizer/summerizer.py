from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def generate_summary(text):
    result = summarizer(
        text[:1024],
        max_length=600,
        min_length=120,
        do_sample=False
    )
    return result[0]["summary_text"]