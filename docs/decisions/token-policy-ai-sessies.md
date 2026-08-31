# Ontwerpbesluit: token-policy voor AI-sessies

## Doel
Beperk toegang van AI-tools tot alleen wat nodig is voor de huidige taak en repository.

## Kernregels
- Gebruik nooit persoonlijke broad-admin tokens in een AI-sessie.
- Gebruik per sessie een apart, beperkt token.
- Scope altijd tot exact 1 repository.
- Geef alleen minimale rechten voor de taak (least privilege).
- Gebruik korte geldigheid (bij voorkeur uren, maximaal 7 dagen).
- Werk via feature branches; merge naar `main` alleen via PR en menselijke review.

## Minimale rechten per scenario
- Alleen lezen: `Metadata: Read`, `Contents: Read`.
- Codewijziging met PR: `Metadata: Read`, `Contents: Read/Write`, `Pull requests: Read/Write`.
- Beheeracties (admin/secrets/repo-settings): niet toegestaan in trainingssessies.

## Korte howto: fine-grained PAT op GitHub
1. Open GitHub en ga naar Settings -> Developer settings -> Personal access tokens -> Fine-grained tokens.
2. Kies Generate new token.
3. Selecteer bij repository access: Only select repositories.
4. Selecteer alleen de repository van deze sessie.
5. Stel een korte expiration in (bij voorkeur 1 dag, maximaal 7 dagen).
6. Zet minimale rechten:
	- Metadata: Read
	- Contents: Read (of Read and Write als je commit/push nodig hebt)
	- Pull requests: Read and Write (alleen als je PR's aanmaakt of wijzigt)
7. Genereer het token, kopieer het eenmalig en gebruik het alleen tijdelijk in de actieve shell.

## Gebruik in de sessie (tijdelijk)
- Exporteer in de huidige shell: `export GITHUB_TOKEN=...`
- Optioneel voor GitHub CLI: `export GH_TOKEN="$GITHUB_TOKEN"`
- Na de oefening direct opruimen: `unset GITHUB_TOKEN GH_TOKEN`

## Sessiestandaard
1. Maak een fine-grained token voor alleen deze repository.
2. Exporteer token tijdelijk in de actieve shell (`GITHUB_TOKEN` en optioneel `GH_TOKEN`).
3. Rond de sessie af en verwijder het token uit de omgeving.
4. Revoke of laat token verlopen direct na de oefening.

## Verboden
- Tokens in commits, markdown, issues of chattranscript plaatsen.
- Tokens opslaan in git-config of permanente shell-profielen.
- Hergebruik van hetzelfde token over meerdere repositories.

## Controlepunten voor trainer
- Is de token-scope aantoonbaar beperkt tot 1 repository?
- Is de expiry kort en bekend?
- Zijn alleen benodigde rechten toegekend?
- Is PR-review verplicht gebleven?
