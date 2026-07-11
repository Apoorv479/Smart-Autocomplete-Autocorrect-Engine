# Smart Autocomplete & Autocorrect Engine

A production-oriented Natural Language Processing (NLP) backend that provides **autocomplete**, **autocorrect**, **next-word prediction**, and **sentence autocomplete** using a combination of Trie, Peter Norvig Spell Correction, N-Gram Language Modeling, and FastAPI.

---

## Features

- Trie-based prefix autocomplete
- Frequency-based suggestion ranking
- Peter Norvig spell correction
- Bigram (N-Gram) next-word prediction
- Sentence autocomplete
- Vocabulary preprocessing
- FastAPI REST API
- Interactive Swagger UI
- Modular project architecture

---

## Project Structure

```text
autocomplete-engine/
│
├── app/
│   ├── api/
│   │   ├── autocomplete.py
│   │   ├── autocorrect.py
│   │   └── prediction.py
│   │
│   ├── autocomplete/
│   │   ├── trie.py
│   │   ├── autocomplete.py
│   │   ├── ranking.py
│   │   └── ngram.py
│   │
│   ├── autocorrect/
│   │   ├── spell_checker.py
│   │   └── edit_distance.py
│   │
│   ├── preprocessing/
│   │   └── vocabulary_builder.py
│   │
│   ├── schemas/
│   │   ├── request.py
│   │   └── response.py
│   │
│   ├── data/
│   │   └── corpus.txt
│   │
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## System Workflow

```text
                User Input
                     │
                     ▼
           Text Preprocessing
                     │
                     ▼
             Vocabulary Builder
                     │
                     ▼
                Trie Search
                     │
         ┌───────────┴───────────┐
         │                       │
         ▼                       ▼
Autocomplete              Spell Correction
         │                       │
         └───────────┬───────────┘
                     ▼
             Suggestion Ranking
                     │
                     ▼
           Next Word Prediction
                     │
                     ▼
          Sentence Autocomplete
                     │
                     ▼
                API Response
```

---

# Components

## Vocabulary Builder

The preprocessing module:

- Reads the training corpus
- Converts text to lowercase
- Tokenizes words
- Builds the vocabulary
- Calculates word frequencies

---

## Trie-Based Autocomplete

The Trie stores every unique word from the corpus.

Given a prefix, it efficiently retrieves all matching words.

Example

**Input**

```text
app
```

**Output**

```text
apple
application
apply
appliance
```

---

## Suggestion Ranking

Suggestions are ranked using:

1. Word frequency
2. Word length
3. Alphabetical order

This prioritizes common words over less frequent ones.

---

## Autocorrect

If no autocomplete suggestion exists, the engine automatically performs spell correction using Peter Norvig's algorithm.

Example

**Input**

```text
aplle
```

**Output**

```text
apple
```

The spell checker:

- Generates candidate words
- Filters valid vocabulary entries
- Selects the highest-frequency candidate

---

## Next Word Prediction

A Bigram (N-Gram) model is trained from the corpus.

It predicts the most probable next word.

Example

**Input**

```text
I love
```

**Output**

```text
programming
python
coding
```

---

## Sentence Autocomplete

Combines Trie search and N-Gram prediction to complete partially typed sentences.

Example

**Input**

```text
I love pro
```

**Output**

```text
I love programming
I love projects
I love problem solving
```

---

# Algorithms Used

- Trie (Prefix Tree)
- Peter Norvig Spell Correction
- Bigram (N-Gram) Language Model
- Frequency Dictionary
- Frequency-Based Ranking

---

# FastAPI Backend

The project exposes REST APIs.

## Endpoints

### Autocomplete

```http
POST /autocomplete
```

Request

```json
{
  "text": "app"
}
```

Response

```json
{
  "suggestions": [
    "apple",
    "application",
    "apply"
  ]
}
```

---

### Autocorrect

```http
POST /autocorrect
```

Request

```json
{
  "text": "aplle"
}
```

Response

```json
{
  "corrected_word": "apple",
  "suggestions": [
    "apple"
  ]
}
```

---

### Next Word Prediction

```http
POST /predict-next
```

Request

```json
{
  "text": "I love"
}
```

Response

```json
{
  "predictions": [
    "programming",
    "python",
    "coding"
  ]
}
```

---

### Sentence Autocomplete

```http
POST /sentence-autocomplete
```

Request

```json
{
  "text": "I love pro"
}
```

Response

```json
{
  "sentences": [
    "I love programming",
    "I love projects"
  ]
}
```

---

# Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- Trie Data Structure
- Natural Language Processing (NLP)

---

# Running the Project

Clone the repository

```bash
git clone <repository-url>
cd autocomplete-engine
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the FastAPI server

```bash
uvicorn app.main:app --reload
```

Open Swagger documentation

```text
http://127.0.0.1:8000/docs
```

---

# Future Improvements

- Trigram and higher-order N-Gram models
- Context-aware sentence prediction
- Weighted Trie with Top-K cached suggestions
- Personalized autocomplete
- Redis caching
- Fuzzy prefix matching
- Multilingual support
- Transformer/LLM-based prediction
- Docker support
- CI/CD pipeline
- Unit and integration tests
- Cloud deployment (AWS, Azure, GCP, Render, Railway)

---

# Learning Outcomes

This project demonstrates practical knowledge of:

- Data Structures
- Natural Language Processing
- Search Algorithms
- String Matching
- Language Modeling
- REST API Development
- FastAPI
- Backend Architecture

---

# License

This project is intended for educational purposes and portfolio demonstration.
