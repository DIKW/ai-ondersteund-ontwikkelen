from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from .models import ChangeRequest, Status
from .service import ChangeRequestService


DEFAULT_DB_PATH = Path(".issues.json")
DEFAULT_DEMO_DB_PATH = Path(".demo-issues.json")


def _load_service(db_path: Path) -> ChangeRequestService:
    if not db_path.exists():
        return ChangeRequestService()

    raw_items = json.loads(db_path.read_text(encoding="utf-8"))
    items = [
        ChangeRequest(
            id=item["id"],
            title=item.get("title", ""),
            description=item.get("description", ""),
            requester=item.get("requester", ""),
            priority=item.get("priority", "MEDIUM"),
            status=Status(item.get("status", Status.DRAFT.value)),
        )
        for item in raw_items
    ]
    return ChangeRequestService(items=items)


def _save_service(service: ChangeRequestService, db_path: Path) -> None:
    items = []
    for request in service.list_change_requests(include_closed=True):
        item = asdict(request)
        item["status"] = request.status.value
        items.append(item)

    db_path.parent.mkdir(parents=True, exist_ok=True)
    db_path.write_text(json.dumps(items, indent=2), encoding="utf-8")


def _resolve_db_path(db_arg: str) -> Path:
    return Path(db_arg).expanduser().resolve()


def _print_request(request: ChangeRequest) -> None:
    print(
        f"id={request.id} status={request.status.value} priority={request.priority} "
        f"requester={request.requester} title={request.title}"
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="change-request-tracker")
    parser.add_argument(
        "--db",
        default=str(DEFAULT_DB_PATH),
        help="Pad naar JSON-opslagbestand (default: .change_request_tracker.json)",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    demo_parser = subparsers.add_parser("demo", help="Draait een korte demo")
    demo_parser.add_argument(
        "--demo-db",
        default=str(DEFAULT_DEMO_DB_PATH),
        help="Pad naar demo JSON-opslagbestand (default: .demo-issues.json)",
    )

    create_parser = subparsers.add_parser("create", help="Maak een nieuw issue aan")
    create_parser.add_argument("--title", required=True, help="Titel van het issue")
    create_parser.add_argument("--description", required=True, help="Beschrijving")
    create_parser.add_argument("--requester", required=True, help="Aanvrager")
    create_parser.add_argument("--priority", default="MEDIUM", help="Prioriteit")

    list_parser = subparsers.add_parser("list", help="Toon issues")
    list_parser.add_argument("--all", action="store_true", help="Toon ook gesloten issues")

    show_parser = subparsers.add_parser("show", help="Toon details van een issue")
    show_parser.add_argument("id", type=int, help="Issue-id")

    submit_parser = subparsers.add_parser("submit", help="Dien een DRAFT issue in")
    submit_parser.add_argument("id", type=int, help="Issue-id")

    transition_parser = subparsers.add_parser("transition", help="Zet issue naar een andere status")
    transition_parser.add_argument("id", type=int, help="Issue-id")
    transition_parser.add_argument("status", choices=[status.value for status in Status], help="Doelstatus")

    close_parser = subparsers.add_parser("close", help="Sluit een issue")
    close_parser.add_argument("id", type=int, help="Issue-id")

    return parser


def run_demo(demo_db_path: Path) -> int:
    service = ChangeRequestService()
    created = service.create_change_request(
        title="Verbeter logging",
        description="Voeg context toe aan foutmeldingen",
        requester="team-api",
        priority="HIGH",
    )
    follow_up = service.create_change_request(
        title="Verbeter rapportage",
        description="Maak weekoverzicht per team",
        requester="team-data",
        priority="MEDIUM",
    )
    submitted = service.submit_change_request(created.id)
    in_review = service.transition_status(created.id, Status.IN_REVIEW)
    approved = service.transition_status(created.id, Status.APPROVED)
    closed = service.transition_status(created.id, Status.CLOSED)
    reprioritized = service.update_priority(follow_up.id, "LOW")

    open_items = service.list_change_requests(include_closed=False)
    all_items = service.list_change_requests(include_closed=True)

    print(f"Aangemaakt: id={created.id}, status={created.status.value}, priority={created.priority}")
    print(f"Ingediend: id={submitted.id}, status={submitted.status.value}, priority={submitted.priority}")
    print(f"In review: id={in_review.id}, status={in_review.status.value}")
    print(f"Goedgekeurd: id={approved.id}, status={approved.status.value}")
    print(f"Gesloten: id={closed.id}, status={closed.status.value}")
    print(
        "Prioriteit aangepast: "
        f"id={reprioritized.id}, status={reprioritized.status.value}, priority={reprioritized.priority}"
    )
    _save_service(service, demo_db_path)

    reloaded = _load_service(demo_db_path)
    reloaded_open_items = reloaded.list_change_requests(include_closed=False)
    reloaded_all_items = reloaded.list_change_requests(include_closed=True)

    print(f"Open issues (zonder CLOSED): {[request.id for request in open_items]}")
    print(f"Alle issues: {[request.id for request in all_items]}")
    print(f"Demo database opgeslagen: {demo_db_path}")
    print(f"Herladen open issues: {[request.id for request in reloaded_open_items]}")
    print(f"Herladen alle issues: {[request.id for request in reloaded_all_items]}")
    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    db_path = _resolve_db_path(args.db)

    try:
        if args.command == "demo":
            demo_db_path = _resolve_db_path(args.demo_db)
            return run_demo(demo_db_path)

        service = _load_service(db_path)

        if args.command == "create":
            created = service.create_change_request(
                title=args.title,
                description=args.description,
                requester=args.requester,
                priority=args.priority,
            )
            _save_service(service, db_path)
            print(f"Issue aangemaakt met id={created.id}")
            _print_request(created)
            return 0

        if args.command == "list":
            items = service.list_change_requests(include_closed=args.all)
            if not items:
                print("Geen issues gevonden.")
                return 0
            for request in items:
                _print_request(request)
            return 0

        if args.command == "show":
            request = service.get(args.id)
            _print_request(request)
            print(f"description={request.description}")
            return 0

        if args.command == "submit":
            updated = service.submit_change_request(args.id)
            _save_service(service, db_path)
            print(f"Issue {updated.id} ingediend: status={updated.status.value}")
            return 0

        if args.command == "transition":
            target_status = Status(args.status)
            updated = service.transition_status(args.id, target_status)
            _save_service(service, db_path)
            print(f"Issue {updated.id} bijgewerkt: status={updated.status.value}")
            return 0

        if args.command == "close":
            updated = service.transition_status(args.id, Status.CLOSED)
            _save_service(service, db_path)
            print(f"Issue {updated.id} gesloten")
            return 0

        parser.print_help()
        return 1
    except (KeyError, ValueError, json.JSONDecodeError) as error:
        print(f"Fout: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
