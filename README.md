# News Article Summarizer and Sentiment Analysis

## Project Overview

The News Article Summarizer and Sentiment Analysis System is a Python-based Natural Language Processing (NLP) application that extracts news articles from a given URL, generates a concise summary, and analyzes the sentiment of the summarized content.

The application helps users quickly understand lengthy news articles without reading the entire text and determines whether the article sentiment is Positive, Negative, or Neutral.

---

## Features

- Extracts news articles directly from URLs
- Removes unnecessary webpage content and extracts the main article text
- Generates concise summaries using NLP techniques
- Performs sentiment analysis on summarized content
- Classifies sentiment as Positive, Negative, or Neutral
- Simple command-line interface

---

## Technologies Used

- Python
- Newspaper3k
- Hugging Face Transformers
- BART (Bidirectional and Auto-Regressive Transformers)
- Natural Language Processing (NLP)
- NLTK

---

## Project Structure

```
news_summerizer/
│
├── app.py
├── summerizer.py
├── sentiment.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Working Flow

1. User enters a news article URL.
2. Newspaper3k downloads and extracts the article content.
3. The extracted article text is passed to the summarization module.
4. The BART model generates a concise summary of the article.
5. Sentiment analysis is performed on the generated summary.
6. The application displays the summary and sentiment result.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd news_summerizer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python app.py
```

Enter a valid news article URL when prompted.

Example:

```text
Enter News URL:
https://example-news-article.com
```

---

## Sample Output

```text
========== SUMMARY ==========

India launched a new communication satellite to improve
internet connectivity in rural areas.

========== SENTIMENT ==========

Label : POSITIVE
Confidence : 0.98
```

---

## Applications

- News summarization
- Media monitoring
- Content analysis
- Sentiment tracking
- NLP-based text processing

---


