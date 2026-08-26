import unittest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from change_request_tracker.models import Status
from change_request_tracker.service import ChangeRequestService


class ChangeRequestServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.service = ChangeRequestService()

    def test_can_create_new_request(self) -> None:
        request = self.service.create_change_request(
            title="Nieuwe feature",
            description="Kleine wijziging",
            requester="team-ops",
            priority="LOW",
        )

        self.assertEqual(request.id, 1)
        self.assertEqual(request.status, Status.DRAFT)

    def test_valid_request_can_be_submitted(self) -> None:
        request = self.service.create_change_request(
            title="Nieuwe feature",
            description="Kleine wijziging",
            requester="team-ops",
        )

        submitted = self.service.submit_change_request(request.id)

        self.assertEqual(submitted.status, Status.SUBMITTED)

    def test_list_open_requests_excludes_closed(self) -> None:
        request = self.service.create_change_request(
            title="Nieuwe feature",
            description="Kleine wijziging",
            requester="team-ops",
        )
        self.service.submit_change_request(request.id)
        self.service.transition_status(request.id, Status.IN_REVIEW)
        self.service.transition_status(request.id, Status.APPROVED)
        self.service.transition_status(request.id, Status.CLOSED)

        open_items = self.service.list_change_requests(include_closed=False)

        self.assertEqual(open_items, [])

    def test_service_can_start_with_existing_items(self) -> None:
        existing = [
            self.service.create_change_request(
                title="Bestaande request",
                description="Vanuit opslag",
                requester="team-core",
            )
        ]

        reloaded_service = ChangeRequestService(items=existing)
        created = reloaded_service.create_change_request(
            title="Nieuwe request",
            description="Na reload",
            requester="team-core",
        )

        self.assertEqual(created.id, 2)

    def test_submit_requires_title_description_and_requester(self) -> None:
        request = self.service.create_change_request(title="", description="", requester="")

        with self.assertRaises(ValueError):
            self.service.submit_change_request(request.id)

    def test_submit_without_title_raises_and_stays_draft(self) -> None:
        request = self.service.create_change_request(title="", description="Omschrijving", requester="team-ops")

        with self.assertRaises(ValueError):
            self.service.submit_change_request(request.id)

        self.assertEqual(self.service.get(request.id).status, Status.DRAFT)

    def test_submit_without_description_raises_and_stays_draft(self) -> None:
        request = self.service.create_change_request(title="Feature X", description="", requester="team-ops")

        with self.assertRaises(ValueError):
            self.service.submit_change_request(request.id)

        self.assertEqual(self.service.get(request.id).status, Status.DRAFT)

    def test_submit_without_requester_raises_and_stays_draft(self) -> None:
        request = self.service.create_change_request(title="Feature X", description="Omschrijving", requester="")

        with self.assertRaises(ValueError):
            self.service.submit_change_request(request.id)

        self.assertEqual(self.service.get(request.id).status, Status.DRAFT)
