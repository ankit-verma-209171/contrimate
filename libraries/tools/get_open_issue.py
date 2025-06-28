import requests
from libraries.common.env import GITHUB_TOKEN
from libraries.models.github_issue import Issue


def get_issues_url(user_name: str, repo_name: str) -> str:
    """Get the URL for issues in a GitHub repository.
    Args:
        user_name (str): The GitHub username or organization name.
        repo_name (str): The name of the repository.
    Returns:
        str: The URL to access the issues of the specified repository.
    """
    return f"https://api.github.com/repos/{user_name}/{repo_name}/issues"


def get_open_issues(
    user_name: str, repo_name: str, page: int = 1, per_page: int = 100
) -> dict:
    """
    Retrieve open issues from a GitHub repository.
    Args:
        user_name (str): The GitHub username or organization name.
        repo_name (str): The name of the repository.
        page (int): The page number to retrieve (default is 1).
        per_page (int): The number of issues per page (default is 100).
    Returns:
        dict: A dictionary containing a list of issues and a message.
            The "issues" key maps to a list of Issue objects, and the
            "message" key maps to a string describing the status (e.g., "200 - OK" or "404 - Not Found").
    Example:
        Successful response:
        ```
        {
            "issues": [
                {
                    "html_url": "https://github.com/repos/user/repo/issues/1",
                    "number": 1,
                    "title": "Issue Title",
                    "labels": [{"name": "bug", "description": "A bug"}],
                    "state": "open",
                    "comments": 5,
                    "body": "Issue description"
                },
                ...
            ],
            "message": "200 - OK"
        }
        ```

        Failed response:
        ```
        {
            "issues": [],
            "message": "404 - Not Found"
        }
        ```
    """
    base_url = get_issues_url(user_name, repo_name)
    params = {
        "state": "open",
        "per_page": per_page,
        "page": page,
    }
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": f"Bearer {GITHUB_TOKEN}",
    }

    response = requests.get(base_url, params=params, headers=headers)
    if not response.ok:
        return {"issues": [], "message": f"{response.status_code} - {response.reason}"}

    issues_json = response.json()
    issues = [Issue(**issue).model_dump_json() for issue in issues_json]
    return {"issues": issues, "message": f"{response.status_code} - {response.reason}"}
