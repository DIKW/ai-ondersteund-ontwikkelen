from __future__ import annotations

from collections.abc import Iterable
from dataclasses import replace

from .models import ChangeRequest, Status


class ChangeRequestService:
    def __init__(self, items: Iterable[ChangeRequest] | None = None) -> None:
        self._items: dict[int, ChangeRequest] = {}
        if items is not None:
            for item in items:
                self._items[item.id] = item
        self._next_id = max(self._items, default=0) + 1

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

    def list_change_requests(self, include_closed: bool = True) -> list[ChangeRequest]:
        items = sorted(self._items.values(), key=lambda request: request.id)
        if include_closed:
            return items
        return [request for request in items if request.status is not Status.CLOSED]

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
