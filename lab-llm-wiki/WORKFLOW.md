# Wiki-ingestworkflow

Deze workflow vult de algemene stappen uit de llm-wiki-skill aan met afspraken voor deze wiki. `SCHEMA.md` blijft leidend voor domein, paginatypen, frontmatter en tags.

## 1. Selecteer en controleer bronnen

- Bevestig dat de trainer de bron heeft goedgekeurd en dat deze geen productie- of klantgegevens bevat.
- Gebruik bestanden onder `raw/` als onveranderlijke bronnen. Bewerk, hernoem of verwijder ze niet.
- Noteer het exacte bronpad en controleer of dezelfde bron al onder `raw/`, `Clippings/` of elders is opgenomen. Verwerk een identieke kopie niet nogmaals.
- Bij herverwerking: controleer eventuele `sha256`-metadata. Behandel gewijzigde broninhoud als source drift en vraag om beoordeling.
- Voor PDF-extractie: gebruik waar beschikbaar `uv run markitdown` en schrijf extracties buiten de wiki, bijvoorbeeld naar `/tmp/`. Meld OCR-, tabel- en extractieproblemen; presenteer de extractie niet als foutloos.

## 2. Lees de bron en zoek bestaande dekking

- Lees de volledige bron of een controleerbare extractie. Scheid wat de bron beweert van interpretatie en externe verificatie.
- Doorzoek `index.md` en bestaande pagina's op onderwerpen, personen, organisaties, systemen en concepten. Werk bestaande pagina's bij waar dat duplicatie voorkomt.
- Beoordeel expliciet welke onderdelen van de bron buiten het domein in `SCHEMA.md` vallen; neem ze alleen op wanneer ze nodig zijn om een relevante relatie te begrijpen.

## 3. Doe altijd een entity-pass

Maak na de conceptuele lezing een korte inventaris van concrete entiteiten: organisaties, systemen of producten, standaarden en personen. Classificeer iedere kandidaat als `entity`, `person`, `concept` of alleen een vermelding.

- Maak een entity-pagina wanneer een concrete organisatie, systeem of product centraal staat in de bron of herhaaldelijk terugkomt en zelfstandig bruikbare kennis oplevert.
- Maak geen pagina voor iedere genoemde productnaam. Voor leveranciersmateriaal: schrijf claims toe aan de bron, noteer het commerciële belang en behandel niet-onafhankelijk gevalideerde voordelen of cijfers niet als feiten.
- Een auteursnaam alleen rechtvaardigt geen person-pagina. Maak die alleen wanneer de persoon inhoudelijk relevant is en controleerbare broninformatie over diens bijdrage beschikbaar is. Gebruik gewone tekst voor namen wanneer er geen person-pagina is; maak geen verweesde Obsidian-link.
- Onderscheid entiteiten van concepten. Een methode, lifecycle of model hoort doorgaans onder `concepts/`; een bedrijf, concreet product of systeem doorgaans onder `entities/`.
- Leg op nieuwe of bijgewerkte pagina's relaties naar relevante concepten en entiteiten met map-gespecificeerde wikilinks vast. Voeg nieuwe pagina's ook toe aan de juiste sectie in `index.md`.

## 4. Schrijf alleen gerechtvaardigde pagina's

- Houd per oefening maximaal drie nieuwe of bijgewerkte wiki-pagina's aan. Vraag eerst goedkeuring wanneer meer nodig zijn.
- Gebruik de verplichte frontmatter, toegestane tags en lowercase, hyphenated bestandsnamen uit `SCHEMA.md`.
- Behoud bronpaden en voeg verwijzingen toe bij relevante claims. Markeer confidence, onzekerheid en tegenstrijdigheden; verhoog confidence niet alleen omdat een bron is goedgekeurd voor trainingsgebruik.
- Vermijd persoonsclaims uit alleen een naamvermelding en vermijd normatieve formuleringen voor een brongebonden model of leveranciersaanbeveling.
- Houd pagina's scanbaar en doorgaans onder circa 200 regels.

## 5. Werk navigatie bij en vraag review

- Werk `index.md` eenmaal bij voor alle nieuwe pagina's.
- Voeg één append-only vermelding toe aan `log.md` met bronpaden, gewijzigde wiki-pagina's en belangrijke onzekerheden. Vermeld dat `raw/` ongewijzigd bleef.
- Controleer bronpaden, frontmattervelden, toegestane tags, interne links, indexvermelding en diff-whitespace.
- Vraag menselijke review voor bronselectie, feitelijke juistheid, confidence en tegenstrijdigheden. Leg vast wat precies is goedgekeurd; goedkeuring voor trainingsgebruik onderschrijft niet automatisch iedere claim uit de bron.
