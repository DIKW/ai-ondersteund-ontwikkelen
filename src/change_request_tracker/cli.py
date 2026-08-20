from __future__ import annotations

import argparse

from .service import ChangeRequestService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="change-request-tracker")
    parser.add_argument("command", choices=["demo"], help="Uit te voeren commando")
    return parser


def run_demo() -> int:
    service = ChangeRequestService()
    created = service.create_change_request(
        title="Verbeter logging",
        description="Voeg context toe aan foutmeldingen",
        requester="team-api",
        priority="HIGH",
    )
    submitted = service.submit_change_request(created.id)

    print(f"Aangemaakt: id={created.id}, status={created.status}, priority={created.priority}")
    print(f"Ingediend: id={submitted.id}, status={submitted.status}, priority={submitted.priority}")
    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "demo":
        return run_demo()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
