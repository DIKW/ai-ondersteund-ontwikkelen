# Review: Prioriteit vastzetten na indienen

## Reviewbesluit
`akkoord voor menselijke merge-review`

## Spec-conformiteit
De wijziging in `src/change_request_tracker/service.py` voldoet aan de feature uit `specs/lab-05-priority-lock-feature/spec.md`: in `DRAFT` is prioriteitswijziging toegestaan; in `SUBMITTED` en later is deze geblokkeerd. De scope blijft beperkt tot deze businessregel.

## Bewijsdekking
De tests in `tests/test_service.py` dekken zowel het positieve pad (`DRAFT` mag wijzigen) als het negatieve pad (`SUBMITTED` mag niet wijzigen) af. Er is expliciet bewijs dat de status intact blijft bij een mislukte wijziging.

## Risico's
Laag risico. De wijziging is klein, traceerbaar en binnen de domeinregel. Er is geen extra scope of statusflow-verwijding toegevoegd buiten de gevraagde feature.

## Openstaande vragen
Er is nog geen standaardisatie van prioriteitswaarden toegevoegd; dat is expliciet buiten scope gebleven, wat consistent is met `docs/domain.md`.

## Besluit en reden
Akkoord voor menselijke merge-review, omdat de feature voldoet aan de domeinregel, de tests zijn toegevoegd en de projectcheck succesvol is uitgevoerd. De verificatie is recent uitgevoerd met `bash scripts/check.sh`, met resultaat: `Ran 16 tests in 2.463s` en `OK`.

## Handoff naar gatekeeper
- Samenvatting bevindingen (ernst): Laag risico; wijziging is gecontroleerd, klein en goed gedocumenteerd.
- Spec-conformiteit: Voldoet aan de feature in de spec.
- Bewijsdekking: Positief en negatief pad zijn getest en bewijs is aanwezig.
- Besluitadvies: accept
- Voorwaarden voor vervolg: Geen extra scope; verdere standaardisatie van prioriteitswaarden moet apart worden vastgelegd.
