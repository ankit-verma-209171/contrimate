# ContriMate AI Agent

ContriMate is an AI-powered assistant that helps developers discover, understand, and navigate open GitHub issues tailored to their tech stack, interests, and focus areas. It proactively guides users to suitable issues, summarizes discussions, and provides actionable suggestions with direct links for easy access.

## Features

- **Personalized Issue Discovery:** Find open issues in any GitHub repository based on your interests and technologies.
- **Deep Contextual Summaries:** Summarizes issue details and comments for quick understanding.
- **Direct Navigation:** Provides direct links to issues and comments for seamless exploration.
- **Proactive Guidance:** Asks clarifying questions and offers next steps to help you contribute effectively.

## Tech Stack

- Python 3.13+
- [Google ADK](https://pypi.org/project/google-adk/) (Gemini API)
- [Pydantic](https://docs.pydantic.dev/) (for data models)
- [Requests](https://docs.python-requests.org/) (for GitHub API)

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ankit-verma-209171/contrimate.git
   cd contrimate
   ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies using [uv](https://github.com/astral-sh/uv):**
   ```bash
   uv pip install -r requirements.txt
   # or, if using PEP 621/pyproject.toml
   uv pip install .
   ```
4. **Configure environment variables:**
   - Copy `.env.example` to `.env` and fill in your GitHub and Google API keys.
   - Example:
     ```env
     GITHUB_TOKEN=your_github_token
     GOOGLE_API_KEY=your_google_api_key
     ```

## Usage

Run the main agent (using ADK web):

```bash
adk web
```

## Project Structure

```
contrimate/
├── contrimate_agent/        # Main agent logic and configuration
├── libraries/               # Common utilities, models, and GitHub API tools
│   ├── common/
│   ├── models/
│   └── tools/
├── pyproject.toml
├── uv.lock
└── README.md
```

## Environment Variables

- `GITHUB_TOKEN` — GitHub personal access token (required)
- `GOOGLE_API_KEY` — Google Gemini API key (required)

## License

MIT License