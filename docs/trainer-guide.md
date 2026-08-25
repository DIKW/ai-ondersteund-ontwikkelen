# Trainer guide

## Volgorde en tijdsduur (indicatief)
- Dag 1
	- Lab 01 (60-75 min)
	- Lab 02 (60-75 min)
	- Lab 03 (45-60 min)
- Dag 2
	- Lab 04 (45-60 min)
	- Lab 05 (60-75 min)
	- Lab 06 (45-60 min)
	- Lab 09 optioneel, advanced (45-60 min)
- Dag 3
	- Lab 07 (45-60 min)
	- Lab 08 (60-75 min)

## Aanbevolen uitvoeringsvolgorde
- Gebruik per dag maximaal 3 kernlabs in de standaardroute.
- Gebruik Lab 09 alleen als verdiepingslab bij teams die voorlopen.
- Houd per lab een expliciet go/no-go moment op basis van bewijs.

## Vooraf te controleren artefacten
- `docs/domain.md`
- `specs/template/*`
- `docs/labs/*`
- `knowledge-lab/*` startstructuur
- Groene tests

## Niet wijzigen tijdens labs
- Trainingskaders in `AGENTS.md`
- Basisafspraken in `docs/decisions/training-repository-scope.md`
- Devcontainer-beveiligingsgrenzen

## Veilig samenwerken
- Werk per team op eigen branch of fork.
- Laat menselijke review verplicht vóór merge.

## Trainingsstates in GitHub
- Gebruik per lab een vaste feature branch voor uitwerking (bijvoorbeeld `training/lab-01`).
- Gebruik per lab twee tags voor reproduceerbare states:
	- `lab-01-start`
	- `lab-01-solution`
- Herhaal dit patroon voor volgende labs (`lab-02-start`, `lab-02-solution`, etc.).
- Gebruik start-tags als oefenstartpunt en solution-tags als referentie tijdens review.

## Fallback zonder Copilot CLI
Deelnemers schrijven spec, plan en review handmatig in Markdown.

## Dag 3 bronpakket
Plaats een klein, geanonimiseerd bronpakket handmatig in `knowledge-lab/raw/`.

## Consistency-check voor trainer
- Labnummers en benamingen in `README.md`, `docs/labs/` en `docs/cursus-outline.md` komen overeen.
- Scopegrenzen uit `docs/decisions/training-repository-scope.md` blijven leidend.
