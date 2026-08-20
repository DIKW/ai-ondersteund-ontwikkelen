# Learner start (preflight)

1. Open de repository in de devcontainer.
2. Draai:
   ```bash
   bash .devcontainer/scripts/verify-environment.sh
   ```
3. Draai tests:
   ```bash
   python -m unittest discover -s tests -v
   ```
4. Controleer of Copilot CLI beschikbaar is (`copilot --help`).
5. Log zo nodig zelf interactief in via de officiële GitHub-stappen.
6. Start Copilot CLI vanuit de repository-root.
7. Lees `AGENTS.md`.

> Let op: de verificatie start geen login, download of netwerkactie.
