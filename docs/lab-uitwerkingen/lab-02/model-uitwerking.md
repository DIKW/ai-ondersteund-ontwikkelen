# Lab 02 modeluitwerking

## Doel van de wijziging
Vertaal de Lab 01-spec naar een kleine codewijziging die voorkomt dat onvolledige verzoeken kunnen worden ingediend.

## Scopegrens (kleine wijziging)
- Alleen submit-validatie in de service-laag aanpassen.
- Bijbehorende tests voor positief en negatief pad toevoegen of activeren.
- Geen wijziging aan prioriteitsregels of andere statusovergangen.

## Wijzigingsaanpak
1. Voeg validatie toe in `submit_change_request` voor `title`, `description` en `requester`.
2. Laat submit alleen doorgaan als alle verplichte velden gevuld zijn.
3. Laat bij ontbrekende velden een `ValueError` terugkomen met duidelijke melding.
4. Werk tests bij zodat zowel geslaagde submit als falende submit-varianten zijn afgedekt.

## Sub-agent uitvoering (input en output)

### Planner-agent
- **Input**
    - Voorbeeldfeature uit Lab 01: `docs/lab-uitwerkingen/lab-01/voorbeeld-feature-voor-lab-02.md`.
    - Lab 02-opdrachtkader uit `docs/labs/lab-02-spec-to-change.md`.
    - Domeinregel uit `docs/domain.md`: submit vereist complete velden.
    - Bestaande code in `src/change_request_tracker/service.py` en tests in `tests/test_service.py`.
- **Output**
    - Maximaal 5-stappenplan:
        1. Voeg submit-validatie toe op `title`, `description`, `requester`.
        2. Behoud bestaande statusregels; geen scope-uitbreiding.
        3. Activeer negatieve test voor ontbrekende velden.
        4. Behoud positieve submit-test.
        5. Draai `bash scripts/check.sh` en leg reviewbesluit vast.
    - Relevante bestanden: `src/change_request_tracker/service.py`, `tests/test_service.py`.
    - Aannames: whitespace-only geldt als ontbrekend veld.
    - Risico: onduidelijkheid over expliciete vastlegging van whitespace-regel.
    - Open vraag: moet de whitespace-regel bronmatig expliciet worden gemaakt?

### Implementer-agent
- **Input**
    - Goedgekeurd planner-plan.
    - Scopegrens: alleen submit-validatie + bijbehorende tests.
- **Output**
    - Diff-samenvatting:
        - `submit_change_request` valideert nu lege/whitespace verplichte velden.
        - Negatieve submit-test geactiveerd en permissieve test omgezet naar faalpad met statusbehoud op `DRAFT`.
    - Testuitvoer:
        - `bash scripts/check.sh` -> `OK`.
    - Onzekerheden:
        - Functioneel gedrag is correct, maar businessregel rond whitespace vraagt expliciete documentatie voor toekomstige reviews.

### Reviewer-agent
- **Input**
    - Spec (Lab 02), planner-output, implementer-diff en testbewijs.
- **Output**
    - Oordeel: `akkoord voor menselijke merge-review`.
    - Onderbouwing:
        - Scope is beheerst en spec-conform.
        - Positief en negatief pad zijn aantoonbaar afgedekt.
        - Restpunt: leg whitespace-regel expliciet vast als follow-up/rework om interpretatierisico te verlagen.

## Compacte git-diff (uitgevoerd)
```diff
--- a/src/change_request_tracker/service.py
+++ b/src/change_request_tracker/service.py
@@
 def submit_change_request(self, request_id: int) -> ChangeRequest:
     current = self.get(request_id)
     if current.status is not Status.DRAFT:
         raise ValueError("Alleen DRAFT kan worden ingediend.")
+    required = {
+        "title": current.title,
+        "description": current.description,
+        "requester": current.requester,
+    }
+    missing = [name for name, value in required.items() if not value.strip()]
+    if missing:
+        raise ValueError(f"Verplichte velden ontbreken: {', '.join(missing)}")
     updated = replace(current, status=Status.SUBMITTED)
     self._items[request_id] = updated
     return updated

--- a/tests/test_service.py
+++ b/tests/test_service.py
@@
-def test_submit_without_required_fields_does_not_raise(self) -> None:
-    submitted = self.service.submit_change_request(request.id)
-    self.assertEqual(submitted.status, Status.SUBMITTED)
+def test_submit_without_required_fields_raises(self) -> None:
+    with self.assertRaisesRegex(ValueError, "Verplichte velden ontbreken"):
+        self.service.submit_change_request(request.id)
+    current = self.service.get(request.id)
+    self.assertEqual(current.status, Status.DRAFT)

@@
-@unittest.skip("Lab 01: activeer zodra businessregel is gespecificeerd en geaccepteerd.")
 def test_submit_requires_title_description_and_requester(self) -> None:
```

## Testbewijs (uitgevoerd)
- Positief pad: `test_valid_request_can_be_submitted` groen.
- Negatief pad: `test_submit_requires_title_description_and_requester` groen.
- Extra regressiecheck: `test_submit_without_required_fields_raises` groen en bevestigt status blijft `DRAFT`.
- Basiscontrole: `bash scripts/check.sh` uitgevoerd met resultaat:

```text
Ran 11 tests in 2.419s

OK
```

## Reviewuitkomst
- **Bevinding:** wijziging blijft binnen scope en dekt kern van Lab 01-spec.
- **Risico:** betekenis van whitespace-only invoer moet expliciet bevestigd zijn.
- **Besluit:** accept met voorwaarde dat whitespace-regel in spec/open vraag expliciet blijft.
