from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    IN_REVIEW = "IN_REVIEW"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    CLOSED = "CLOSED"


@dataclass
class ChangeRequest:
    id: int
    title: str = ""
    description: str = ""
    requester: str = ""
    priority: str = "MEDIUM"
    status: Status = Status.DRAFT
