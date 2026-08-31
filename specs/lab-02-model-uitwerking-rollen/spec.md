# Spec (lab 02 modeluitwerking met rollen)

## Probleem
De huidige Lab 02-modeluitwerking toont vooral het eindresultaat (diff, tests, review), maar legt nog niet expliciet vast welke input en output bij planner-, implementer- en reviewer-agent horen. Daardoor is het lastiger om in Lab 03 evidence-driven review uit te voeren op het procesniveau.

## Doel
Breid de Lab 02-uitwerking uit met expliciete rolgebaseerde input/output en leg deze wijziging vast via een aparte spec, plan en tasks, zodat cursisten het proces kunnen volgen en Lab 03 de review direct kan toetsen.

## Scope
- Gebruik als planner-startinput expliciet `docs/lab-uitwerkingen/lab-01/voorbeeld-feature-voor-lab-02.md`.
- Update `docs/lab-uitwerkingen/lab-02/model-uitwerking.md` met afzonderlijke planner/implementer/reviewer input-outputsecties.
- Update `docs/lab-uitwerkingen/lab-02/traceability.md` met een expliciete planner -> implementer -> reviewer keten.
- Update `docs/labs/lab-02-spec-to-change.md` zodat rol-artefacten onderdeel zijn van de verwachte output.
- Gebruik de map `specs/lab-02-model-uitwerking-rollen/` met `spec.md`, `plan.md`, `tasks.md`.

## Niet-doen-lijst
- Geen nieuwe productfunctionaliteit in `src/` of `tests/`.
- Geen wijziging van domeinregels in `docs/domain.md`.
- Geen uitbreiding buiten Lab 02/Lab 03 didactische keten.

## Acceptatiecriteria
- Er bestaat een expliciet planner-input artefact: `docs/lab-uitwerkingen/lab-01/voorbeeld-feature-voor-lab-02.md`.
- Lab 02 modeluitwerking bevat expliciet drie secties: planner input/output, implementer input/output, reviewer input/output.
- Traceability legt de keten planner -> implementer -> reviewer expliciet vast.
- Lab 02 werkblad noemt rol-artefacten als verwachte output.
- `specs/lab-02-model-uitwerking-rollen/` bevat `spec.md`, `plan.md`, `tasks.md`.
- Wijziging blijft documentair en laat code/testgedrag ongewijzigd.

## Open vragen
- Moet de reviewer-uitkomst in dit lab strikt op de drie reviewer-oordelen uit `.github/agents/reviewer.agent.md` blijven, of volstaat een tekstuele equivalent? Richtlijn: gebruik expliciet een van de drie oordelen.
