# app/analysis.py
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from .utils import fetch_repos
from .config import config

llm = OpenAI(api_key=config.openai_api_key)

async def analyze_repo(repo_data):
    # Placeholder for complex GPT-based analysis
    prompt = PromptTemplate.from_template(
        "Analyze the following repo and determine complexity: {repo_data}"
    )
    return llm(prompt.format(repo_data=repo_data))

async def get_most_complex_repo(username: str):
    repos = await fetch_repos(username)
    # Assume analyze_repo returns a complexity score or summary
    complexity_results = [await analyze_repo(repo) for repo in repos]
    return max(complexity_results, key=lambda x: x['complexity_score'])
