from typing import List, Optional
from pydantic import BaseModel

"""
This module defines Pydantic models representing GitHub issues, labels, users, and comments.

Classes:
    Label: Represents a GitHub label with a name and optional description.
    Issue: Represents a GitHub issue, including its ID, URL, number, title, labels, state, comment count, and optional body.
    User: Represents a GitHub user with a login and ID.
    Comment: Represents a comment on a GitHub issue, including its ID, URL, body, and the user who made the comment.
"""


class Label(BaseModel):
    """
    Represents a GitHub label with a name and optional description.
    Attributes:
        name (str): The name of the label.
        description (Optional[str]): An optional description of the label.
    """

    name: str
    description: Optional[str] = None


class Issue(BaseModel):
    """
    Represents a GitHub issue.
    Attributes:
        html_url (str): The HTML URL to access the issue.
        number (int): The issue number in the repository.
        title (str): The title of the issue.
        labels (Optional[List[Label]]): A list of labels associated with the issue.
        state (str): The state of the issue (e.g., "open", "closed").
        comments (int): The number of comments on the issue.
        body (Optional[str]): The body content of the issue, if available.
    """

    html_url: str
    number: int
    title: str
    labels: Optional[List[Label]] = None
    state: str
    comments: int
    body: Optional[str] = None


class User(BaseModel):
    """
    Represents a GitHub user.
    Attributes:
        login (str): The username of the GitHub user.
        id (int): The unique identifier of the user.
    """

    login: str
    id: int


class Comment(BaseModel):
    """
    Represents a comment on a GitHub issue.
    Attributes:
        id (int): The unique identifier of the comment.
        html_url (str): The HTML URL to access the comment.
        body (str): The content of the comment.
        user (User): The user who made the comment.
    """

    id: int
    html_url: str
    body: str
    user: User
