# Domein: change-request-tracker

## Model
Een wijzigingsverzoek bevat:
- `id`
- `title`
- `description`
- `requester`
- `priority`
- `status`

## Statussen
- `DRAFT`
- `SUBMITTED`
- `IN_REVIEW`
- `APPROVED`
- `REJECTED`
- `CLOSED`

## Toegestane overgangen
- `DRAFT -> SUBMITTED`
- `SUBMITTED -> IN_REVIEW`
- `IN_REVIEW -> APPROVED`
- `IN_REVIEW -> REJECTED`
- `APPROVED -> CLOSED`
- `REJECTED -> CLOSED`

## Oefenbehoeften
1. **Dag 1 (bewuste lacune in huidige code):** bij indienen moet het verzoek volledig zijn (titel, beschrijving, aanvrager).
2. **Dag 2 (nog niet geïmplementeerde veranderwens):** na indienen mag prioriteit niet meer wijzigen; in `DRAFT` wel.

## Buiten scope
- Database
- Netwerk- of webinterface
- Externe systemen

## Open vraag
- Prioriteitswaarden zijn bewust eenvoudig gehouden; verdere standaardisatie is nog niet vastgelegd.
