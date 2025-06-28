import requests
from libraries.common.env import GITHUB_TOKEN
from libraries.models.github_issue import Comment


def get_issue_comments_url(user_name: str, repo_name: str, issue_number: int) -> str:
    """Get the URL for comments on a specific issue in a GitHub repository.
    Args:
        user_name (str): The GitHub username or organization name.
        repo_name (str): The name of the repository.
        issue_number (int): The number of the issue to get comments for.
    Returns:
        str: The URL to access the comments of the specified issue.
    """
    return f"https://api.github.com/repos/{user_name}/{repo_name}/issues/{issue_number}/comments"


def get_issue_comments(
    user_name: str,
    repo_name: str,
    issue_number: int,
    page: int = 1,
    per_page: int = 100,
) -> dict:
    """
    Retrieve comments from a specific issue in a GitHub repository.
    Args:
        user_name (str): The GitHub username or organization name.
        repo_name (str): The name of the repository.
        issue_number (int): The number of the issue to get comments for.
        page (int): The page number to retrieve (default is 1).
        per_page (int): The number of comments per page (default is 100).
    Returns:
        dict: A dictionary containing a list of comments and a message.
        The "comments" key maps to a list of Comment objects, and the
        "message" key maps to a string describing the status (e.g., "200 - OK" or "404 - Not Found").
    Example:
        Successful response:
        ```
        {
            "comments": [
                {
                    "id": 123456789,
                    "html_url": "https://github.com/repos/user/repo/issues/comments/1",
                    "body": "This is a comment on the issue.",
                    "user": {
                        "login": "username",
                        "id": 987654321
                    }
                }
            ],
            "message": "200 - OK"
        }
        ```
        Failed response:
        ```
        {
            "comments": [],
            "message": "404 - Not Found"
        }
        ```
    """
    base_url = get_issue_comments_url(user_name, repo_name, issue_number)
    params = {
        "page": page,
        "per_page": per_page,
    }
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": f"Bearer {GITHUB_TOKEN}",
    }

    response = requests.get(base_url, params=params, headers=headers)

    if not response.ok:
        return {
            "comments": [],
            "message": f"{response.status_code} - {response.reason}",
        }

    comments_data = response.json()
    comments = [Comment(**comment) for comment in comments_data]
    return {
        "comments": comments,
        "message": f"{response.status_code} - {response.reason}",
    }
