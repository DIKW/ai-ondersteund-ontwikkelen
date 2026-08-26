# Plan (lab 02 modeluitwerking met rollen)

## Maximaal 5 stappen
1. Valideer de planner-startinput uit Lab 01 (`docs/lab-uitwerkingen/lab-01/voorbeeld-feature-voor-lab-02.md`) en identificeer ontbrekende rolinput/output onderdelen.
2. Voeg planner/implementer/reviewer input-outputsecties toe in de modeluitwerking.
3. Werk traceability bij met expliciete planner -> implementer -> reviewer keten.
4. Werk het Lab 02-werkblad bij zodat sub-agent artefacten als verwachte output zijn opgenomen.
5. Leg deze rolgerichte uitwerking vast in de specset en valideer dat de wijziging documentair en scope-beperkt is.

## Relevante bestanden
- docs/lab-uitwerkingen/lab-01/voorbeeld-feature-voor-lab-02.md
- docs/lab-uitwerkingen/lab-02/model-uitwerking.md
- docs/lab-uitwerkingen/lab-02/traceability.md
- docs/labs/lab-02-spec-to-change.md
- .github/agents/planner.agent.md
- .github/agents/implementer.agent.md
- .github/agents/reviewer.agent.md

## Risico's
- De modeluitwerking wordt te uitgebreid en verliest de kern van Lab 02.
- Agent-output wordt niet consistent met de in `.github/agents/` vastgelegde verwachtingen.
- De rolbeschrijving blijft te algemeen zonder verifieerbare koppeling naar bestaand bewijs.

## Verificatie
- Handmatige check op acceptatiecriteria uit `specs/lab-02-model-uitwerking-rollen/spec.md`.
- Controle dat alleen documentatiebestanden gewijzigd zijn.
- Controle dat reviewer-output exact een toegestaan oordeel gebruikt.
