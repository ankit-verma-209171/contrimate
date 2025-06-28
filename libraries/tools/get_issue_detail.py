import requests
from libraries.common.env import GITHUB_TOKEN
from libraries.models.github_issue import Issue


def get_issue_detail_url(user_name: str, repo_name: str, issue_number: int) -> str:
    """Get the URL for a specific issue in a GitHub repository.
    Args:
        user_name (str): The GitHub username or organization name.
        repo_name (str): The name of the repository.
        issue_number (int): The number of the issue to get details for.
    Returns:
        str: The URL to access the details of the specified issue.
    """
    return f"https://api.github.com/repos/{user_name}/{repo_name}/issues/{issue_number}"


def get_issue_detail(user_name: str, repo_name: str, issue_number: int) -> dict:
    """
    Retrieve details from a specific issue in a GitHub repository.
    Args:
        user_name (str): The GitHub username or organization name.
        repo_name (str): The name of the repository.
        issue_number (int): The number of the issue to get details for.
    Returns:
        dict: A dictionary containing the issue details and a message.
        The "issue" key maps to an Issue object, and the
        "message" key maps to a string describing the status (e.g., "200 - OK" or "404 - Not Found").
    Example:
        Successful response:
        ```
        {
            "issue": {
                "html_url": "https://github.com/repos/user/repo/issues/1",
                "number": 1,
                "title": "Issue Title",
                "labels": [{"name": "bug", "description": "A bug"}],
                "state": "open",
                "comments": 5,
                "body": "Issue description"
            },
            "message": "200 - OK"
        }
        ```

        Failed response:
        ```
        {
            "issue": null,
            "message": "404 - Not Found"
        }
        ```
    """
    base_url = get_issue_detail_url(user_name, repo_name, issue_number)
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": f"Bearer {GITHUB_TOKEN}",
    }

    response = requests.get(base_url, headers=headers)

    if not response.ok:
        return {"issue": None, "message": f"{response.status_code} - {response.reason}"}

    issue_data = response.json()
    issue = Issue(**issue_data)
    return {"issue": issue, "message": f"{response.status_code} - {response.reason}"}
