# Lab 03 traceability

## Bronketen
- Startstate: `lab-02-solution`
- Bronspec: `docs/lab-uitwerkingen/lab-02/model-uitwerking.md`
- Code/diff: submit-validatie in `src/change_request_tracker/service.py`
- Testbewijs: geslaagde testset uit Lab 02 (`Ran 11 tests ... OK`)
- Reviewkader: `docs/labs/lab-03-evidence-driven-review.md`

## Herleiding per bevinding

### Blokkerend
- **Spec-link:** Open punt rond betekenis van whitespace-only invoer (niet expliciet als bronregel geformuleerd).
- **Code-link:** Implementatie behandelt whitespace als ontbrekend veld (`strip()`-logica).
- **Test-link:** Negatieve tests tonen afwijzing op lege invoer; intentie is impliciet aanwezig.
- **Conclusie:** documentair besluit nodig om interpretatieverschil te voorkomen.

### Belangrijk
- **Spec-link:** Lab 02-scope = submit-validatie.
- **Diff-link:** Alleen submitpad en gerelateerde tests zijn geraakt.
- **Test-link:** Positief en negatief submitpad afgedekt.
- **Conclusie:** scopebeheersing is correct, maar expliciete reviewnotitie is nodig.

### Suggestie
- **Spec-link:** Uitlegbaarheid en reviewconsistentie in Lab 03-rubric.
- **Code-link:** Foutmelding bevat veldnamen, maar communicatie over volgorde/consistentie kan beter.
- **Test-link:** Geen functionele impact; verbeterkans voor feedbackkwaliteit.
- **Conclusie:** niet blokkerend, wel nuttig voor onderhoudbaarheid van review-output.

## Eindkoppeling
Het reviewbesluit `REWORK (documentair)` volgt direct uit de blokkerende traceability-gap en vereist geen aanvullende productcode.
