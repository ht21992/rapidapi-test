from fastapi import FastAPI

app = FastAPI()

programming_languages = [
    {"name": "Python", "year_created": 1991, "creator": "Guido van Rossum"},
    {"name": "JavaScript", "year_created": 1995, "creator": "Brendan Eich"},
    {"name": "Java", "year_created": 1995, "creator": "James Gosling"},
    {"name": "C#", "year_created": 2000, "creator": "Microsoft"},
    {"name": "Go", "year_created": 2009, "creator": "Google"},
    {"name": "Rust", "year_created": 2010, "creator": "Mozilla"},
]


@app.get("/programming-languages")
def get_programming_languages():
    return programming_languages
