# AI-ondersteund ontwikkelen (trainingsrepository)

Deze repository is een oefenomgeving voor een driedaagse in-company training over AI-ondersteunde softwareontwikkeling.

## Doel

De training richt zich op werkwijze, bewijs en verantwoordelijkheid met een kleine Python-app (`change-request-tracker`) als oefendomein.

## Snelle start (devcontainer)

1. Open deze repository in de devcontainer.
2. Voer uit:
   ```bash
   bash .devcontainer/scripts/verify-environment.sh
   ```

## Testcommando

```bash
python -m unittest discover -s tests -v
```

## Demo-commando

```bash
bash scripts/run-demo.sh
```

## CLI-gebruik

Gebruik de app direct via Python met een lokaal JSON-opslagbestand.

Issue aanmaken:

```bash
PYTHONPATH=src python -m change_request_tracker.cli --db .issues.json create \
   --title "Bug in export" \
   --description "CSV export mist kolommen" \
   --requester "team-data" \
   --priority HIGH
```

Open issues tonen:

```bash
PYTHONPATH=src python -m change_request_tracker.cli --db .issues.json list
```

Alle issues (inclusief gesloten) tonen:

```bash
PYTHONPATH=src python -m change_request_tracker.cli --db .issues.json list --all
```

## Veilige werkafspraken

- Gebruik alleen trainingsdata; geen productiegebruik.
- Voeg geen secrets, tokens of credentials toe.
- Werk klein en bewijsbaar; voer `bash scripts/check.sh` uit voor afronding.

## Overzicht labs

1. Lab 01: analyse naar spec
2. Lab 02: spec naar beperkte wijziging
3. Lab 03: ontwerp de loop
4. Lab 04: voer de loop uit

Zie `docs/labs/` voor werkbladen.

## LLMWiki-voorbereiding

De startstructuur voor dag 3 staat in `knowledge-lab/`.

## Waarschuwing

Deze repository bevat uitsluitend trainingsinhoud en ondersteunt geen productiegebruik.
