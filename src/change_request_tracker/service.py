from __future__ import annotations

from dataclasses import replace

from .models import ChangeRequest, Status


class ChangeRequestService:
    def __init__(self) -> None:
        self._next_id = 1
        self._items: dict[int, ChangeRequest] = {}

    def create_change_request(
        self,
        title: str = "",
        description: str = "",
        requester: str = "",
        priority: str = "MEDIUM",
    ) -> ChangeRequest:
        change_request = ChangeRequest(
            id=self._next_id,
            title=title,
            description=description,
            requester=requester,
            priority=priority,
        )
        self._items[change_request.id] = change_request
        self._next_id += 1
        return change_request

    def get(self, request_id: int) -> ChangeRequest:
        return self._items[request_id]

    def submit_change_request(self, request_id: int) -> ChangeRequest:
        current = self.get(request_id)
        if current.status is not Status.DRAFT:
            raise ValueError("Alleen DRAFT kan worden ingediend.")
        updated = replace(current, status=Status.SUBMITTED)
        self._items[request_id] = updated
        return updated

    def transition_status(self, request_id: int, target_status: Status) -> ChangeRequest:
        current = self.get(request_id)
        allowed = {
            Status.DRAFT: {Status.SUBMITTED},
            Status.SUBMITTED: {Status.IN_REVIEW},
            Status.IN_REVIEW: {Status.APPROVED, Status.REJECTED},
            Status.APPROVED: {Status.CLOSED},
            Status.REJECTED: {Status.CLOSED},
            Status.CLOSED: set(),
        }
        if target_status not in allowed[current.status]:
            raise ValueError(f"Overgang niet toegestaan: {current.status} -> {target_status}")
        updated = replace(current, status=target_status)
        self._items[request_id] = updated
        return updated

    def update_priority(self, request_id: int, priority: str) -> ChangeRequest:
        current = self.get(request_id)
        updated = replace(current, priority=priority)
        self._items[request_id] = updated
        return updated
