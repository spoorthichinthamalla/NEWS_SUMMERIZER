from newspaper import Article
from summerizer import generate_summary
from sentiment import analyze_sentiment

url = input("Enter News URL: ")

article = Article(url)

article.download()
article.parse()

text = article.text

print("\nArticle Downloaded Successfully!\n")

summary = generate_summary(text)

print("\n========== SUMMARY ==========\n")
print(summary)

sentiment = analyze_sentiment(summary)

print("\n========== SENTIMENT ==========\n")
print("Label :", sentiment["label"])
print("Confidence :", sentiment["score"])