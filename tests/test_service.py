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

    def test_submit_without_required_fields_does_not_raise(self) -> None:
        request = self.service.create_change_request(title="", description="", requester="")

        submitted = self.service.submit_change_request(request.id)

        self.assertEqual(submitted.status, Status.SUBMITTED)

    @unittest.skip("Lab 01: activeer zodra businessregel is gespecificeerd en geaccepteerd.")
    def test_submit_requires_title_description_and_requester(self) -> None:
        request = self.service.create_change_request(title="", description="", requester="")

        with self.assertRaises(ValueError):
            self.service.submit_change_request(request.id)
