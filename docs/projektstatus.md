# Projektstatus

## Status v1.8 – Slutgranskning v1

- Hela läsartexten har genomgått en ny slutgranskning efter layoutrevisionen.
- Inledningen förklarar nu explicit hur forskning, mätdata, leverantörsuppgifter och bokens egna synteser skiljs åt.
- Kapitel 15:s färskhetskänsliga källor har kontrollerats den 2 september 2026; EDPB Guidelines 02/2026 är fortfarande ett konsultationsutkast med öppet samråd till 30 oktober 2026.
- Onödigt korta kapitelslutsidor i PDF har minskats genom att ta bort två redundanta övergångsstycken i kapitel 1–2.
- Se `docs/slutgranskning-v1.md` för samlad bedömning och återstående release-steg.
- Ren lokal checkout-simulering utan tidigare build/export har verifierat att exportskriptet kan bygga PDF och EPUB från projektkällorna.

## Version

1.8.0 – slutgranskning v1, evidensförtydligande och riktade layoutkorrigeringar.

## Status v1.5 – Kapitelrubriker och GitHub Actions

- Numrerade kapitelrubriker visas vid export på två horisontellt centrerade rader: **Kapitel N** och därefter kapitelnamnet.
- Canonical Markdown behåller rubriken i en rad; ett Pandoc Lua-filter gör endast presentationsändringen vid PDF/EPUB-export.
- Innehållsförteckningen behåller kapitelnummer och kapitelnamn på en läsbar rad.
- `.github/workflows/build-book.yml` kan köras manuellt med `workflow_dispatch`.
- Samma workflow körs automatiskt när en GitHub Release publiceras och laddar då även upp PDF/EPUB som release-assets.
- Lokal och CI-baserad export använder samma `scripts/export-book.sh`.

## Version

1.5.0 – två-radiga kapitelrubriker och automatiserad GitHub Actions-build.

## Status v1.3 – Omslag fastställt

- Det av användaren godkända omslaget har lagts in som `assets/cover.png`.
- Titel, undertitel och författare på omslaget matchar projektmetadata.
- Tidigare preliminär illustrationsplan har uppdaterats så det fastställda motivet är styrande.
- `docs/export-metadata.yaml` pekar på omslagsfilen.
- EPUB-exporten använder `assets/cover.png` via Pandocs `--epub-cover-image`.
- Nästa steg: första riktiga EPUB/PDF-layoutprov och layoutbaserad kvalitetsgranskning.

## Version

1.3.0 – fastställt omslag integrerat i projekt och exportstruktur.

## Status v1.2 – Språkpass och läsarverktyg klara

- Huvudmanuset, inledning + kapitel 1–16, har språk- och repetitionsredigerats i ett första sammanhållet pass.
- Engelska `constraints` har ersatts med **begränsningar** där begreppet inte behöver stå på engelska.
- Repetitiva meningsstarter och introduktioner av bokens egna synteser har stramats utan att evidensnyanser ändrats.
- **Bilaga A – Bokens modeller i översikt** samlar de pedagogiska synteserna och visar när de är användbara.
- **Bilaga B – Självvärdering: vilket är ditt nästa steg?** låter läsaren bedöma repertoar, situationsanpassning och kontroll utan poängsättning.
- Exportskriptet inkluderar nu båda bilagorna.
- Nästa steg: omslagsarbete och första riktiga EPUB/PDF-layoutprov; därefter layoutbaserad redigering och beslut om slutnotformat.

## Version

1.2.0 – språk-/repetitionspass v1 samt modeller- och självvärderingsbilagor.

## Status v1.1 – Huvudmanus komplett och helhetsgranskat

- Inledning + kapitel 1–16 finns som första manusutkast.
- Researchpass v9 om organisatorisk AI-beredskap, governance, plattformar, evals och lärande arbetssystem är dokumenterat i `docs/researchresultat-v9.md`.
- Kapitel 16 inför bokens egen sexdelade syntes för ett AI-assisterat arbetssystem: **riktning, miljö, arbetsdesign, kontroll, kvalitet och lärande**.
- Första sammanhållna kvalitetsgranskningen av hela manus finns i `docs/kvalitetsgranskning-hela-manus-v1.md`.
- Källregistret omfattar K-001–K-090.
- Huvudmanuset ligger runt 40 000 ord; slutligt sidomfång ska avgöras efter faktisk layout, inte genom utfyllnad.
- Nästa steg: språk-/repetitionsredigering, självvärderingsverktyg, omslag och första export.

## Version

1.1.0 – huvudmanus komplett, researchpass v9 och första helhetsgranskning.

## Låsta beslut

- Titel: **Från fråga till arbetskamrat**.
- Undertitel: *Från enkla frågor till moget AI-assisterat arbete*.
- Författare: Erland Lindmark.
- Språk: svenska.
- Omfattning: cirka 180–250 sidor, målnivå runt 210–225.
- Struktur: inledning + 16 kapitel.
- Fokus: mognadsresan i AI-assisterat arbete genom systemutveckling och IT-arkitektur.
- Boken ska vara verktygsneutral.
- Hela systemutvecklingsprocessen kan användas som arena: behov/krav, arkitektur/design, utveckling, test/kvalitet och leverans.
- Icke-publikt material och molnbaserad AI ska behandlas som en viktig del av mogen användning.
- Omslagsbild ska tas fram.
- Inre illustrationer avgörs senare.

## Arbetsmodell v0.2

1. Fråga.
2. Resonera.
3. Skapa.
4. Samarbeta.
5. Ge kontext.
6. Delegera.
7. Orkestrera.

Modellen är låst efter researchpass v1 som bokens pedagogiska syntes, men kan finjusteras om senare kapitelresearch motiverar det.

## Researchpass v1 – beslut

- Sjufasmodellen behålls som pedagogisk syntes.
- Modellen ska inte beskrivas som vetenskapligt etablerad eller strikt linjär.
- Mognad definieras genom **repertoar, situationsanpassning och kontroll**.
- "Ge kontext" behålls men beskrivs tydligare som en viktig mognadsdimension/tröskel, eftersom verktyg kan ge kontext tidigt.
- Produktivitetskapitlet ska visa motstridig evidens och hålla uppmätta respektive självrapporterade effekter isär.
- Evidenstyp och källans oberoende ska vara synliga för läsaren.
- Leverantörsspecifika säkerhets-/dataskyddsuppgifter färskhetskontrolleras nära publicering.

## Nästa steg

1. Språk- och repetitionsredigera hela manus utan att fylla ut det artificiellt.
2. Skapa ett kort självvärderingsverktyg/bilaga kopplat till repertoar, situationsanpassning och kontroll.
3. Bestäm slutligt källnotformat och skapa omslag.
4. Gör första EPUB/PDF-exporten och bedöm faktiskt sidomfång och typografi.
5. Färskhetskontrollera kapitel 15–16 nära publicering.

## Öppna frågor

- Ska boken använda ordet "mognadsnivå" eller främst "fas/steg" för att undvika värderande ton?
- Behöver modellen ett självvärderingsverktyg i slutet av inledningen eller som bilaga?
- Ska källhänvisningar ligga som fotnoter/slutnoter eller parentetiskt i löptext i slutlig bokdesign?

## 2026-09-02 – Manusdel 7 v0.9

- Researchpass v7 om mänskliga förmågor, kritiskt tänkande, lärandedjup och skill decay är genomfört.
- Kapitel 14, **Det människan fortfarande måste vara bra på**, är skrivet som fullständigt första manusutkast.
- Källregistret är utökat med K-066–K-070.
- Boken undviker den förenklade tesen att AI generellt orsakar deskilling och skiljer experimentell evidens från teoretiska riskargument.
- Boken inför den egna syntesen **kompetensbudgeten**: vad människor måste kunna själva, vad de måste kunna verifiera, vad AI kan göra huvuddelen av och hur kompetensförsvagning upptäcks.
- Nästa steg: research och manus för kapitel 15, **När AI behöver känna till det som inte är publikt**.

## 2026-09-02 – Manusdel 1 v0.3

- Inledningen är skriven som fullständigt första manusutkast.
- Kapitel 1–3 är skrivna och käll-ID:n från `docs/kallregister.md` används direkt i manus.
- Evidenspolicyn tillämpas språkligt: texten skiljer uttryckligen mellan forskningsresultat, enkät-/mätdata, leverantörstelemetri och bokens syntes.
- Kapitel 3 använder motstridiga produktivitetsresultat som bärande pedagogik i stället för att välja en enkel positiv eller negativ berättelse.
- Nästa steg: just-in-time-research om hallucinationer/faktaverifiering och därefter kapitel 4–5 (Fråga och Resonera), alternativt hela blocket 4–7 om kvaliteten håller.


## 2026-09-02 – Manusdel 2 v0.4

- Just-in-time-research om hallucinationer, källverifiering, retrieval och kritiskt tänkande är genomfört och dokumenterat i `docs/researchresultat-v2.md`.
- Kapitel 4, **Fas 1: Fråga**, är skrivet som fullständigt första manusutkast.
- Kapitel 5, **Fas 2: Resonera**, är skrivet som fullständigt första manusutkast.
- Källregistret har utökats med K-028–K-034.
- Mognadsmodellens sju steg behålls. Gränsen mellan fas 1 och 2 har preciserats: fas 1 handlar primärt om information/förklaring och faktaverifiering; fas 2 om problemstruktur, premisser, trade-offs och relevans.
- Boken inför en egen fyrdelad syntes för resonemangsarbete: **bredda, strukturera, utmana, fokusera**. Den märks uttryckligen som bokens syntes.
- Nästa steg: research och manus för kapitel 6–7, **Skapa** och **Samarbeta**, med fokus på kvaliteten i AI-genererade artefakter, iteration, review och varför den första genererade versionen sällan bör betraktas som leveransklar.


## 2026-09-02 – Manusdel 3 v0.5

- Just-in-time-research om AI-genererade artefakter, kvalitet, iteration och review är genomfört och dokumenterat i `docs/researchresultat-v3.md`.
- Kapitel 6, **Fas 3: Skapa**, är skrivet som fullständigt första manusutkast.
- Kapitel 7, **Fas 4: Samarbeta**, är skrivet som fullständigt första manusutkast.
- Källregistret har utökats med K-035–K-040.
- Fasgränsen har preciserats: fas 3 börjar när AI producerar ett konkret arbetsobjekt; fas 4 när resultatet ingår i en återkopplingsloop med granskning, kritik, förändring och verifiering.
- Boken inför två egna synteser: **artefaktkontraktet** (syfte, mottagare, begränsningar, kvalitetskriterier, verifieringssätt) och **samarbetskontraktet** (vad får förändras, vilken återkoppling räknas, vad stoppar arbetet, när är vi klara).
- Nästa steg: research och manus för kapitel 8–9, **Ge kontext** och **Delegera**.


## 2026-09-02 – Manusdel 4 v0.6

- Just-in-time-research om repository-/dokumentkontext, retrieval, delegation, agentverktyg, människa-i-loopen och agentrisk är genomfört och dokumenterat i `docs/researchresultat-v4.md`.
- Kapitel 8, **Fas 5: Ge kontext**, är skrivet som fullständigt första manusutkast.
- Kapitel 9, **Fas 6: Delegera**, är skrivet som fullständigt första manusutkast.
- Källregistret har utökats med K-041–K-045.
- Fas 5 har preciserats: mognad handlar inte om maximal kontext utan om relevant, aktuell och auktoritativ kontext samt synliga informationsluckor.
- Fas 6 har preciserats: delegation definieras genom mål, constraints, handlingsutrymme och verifiering. Boken inför den egna syntesen **delegationsbudget** för data, verktyg, behörigheter, tid/kostnad och irreversibla åtgärder.
- Agenters handlingsutrymme behandlas som en konkret behörighetsfråga, och human-in-the-loop beskrivs som en kontroll bland flera snarare än en fullständig säkerhetsgaranti.
- Nästa steg: research och manus för kapitel 10, **Orkestrera**, följt av helhetsgranskning av hela Del II.


## 2026-09-02 – Manusdel 6 v0.8

- Researchpass v6 om requirements engineering, mjukvaruarkitektur, implementation, test och leverans är genomfört.
- Kapitel 11, **Från behov och krav till lösningsidé**, är skrivet.
- Kapitel 12, **Från arkitektur och design till implementation**, är skrivet.
- Kapitel 13, **Från test och kvalitet till leverans**, är skrivet.
- Genomgående scenario är låst till **Statusnotiser för ärenden**.
- Del III inför den egna syntesen **behov → beslut → förändring → bevis**.
- Källregistret är utökat med K-055–K-065.
- Del III har kvalitetsgranskats och sjufasmodellen behålls oförändrad.
- Nästa steg: Del IV, med start i kapitel 14 om mänskliga förmågor, omdöme och ansvar.


## 2026-09-02 – Manusdel 8 v1.0

- Researchpass v8 om icke-publikt material och databehandling är genomfört.
- Kapitel 15, **När AI behöver känna till det som inte är publikt**, är skrivet som fullständigt första manusutkast.
- Källregistret är utökat med K-071–K-084.
- Kapitlet skiljer mellan modellträning, retention och annan databehandling och märker leverantörsuppgifter som sådana.
- Anonymisering, pseudonymisering och maskning behandlas separat; EDPB:s anonymiseringsriktlinje 02/2026 anges uttryckligen vara konsultationsutkast.
- Kapitlet inför **promptminimering**: själva frågan betraktas som en informationsbärare och minimeras tillsammans med bilagor och andra kontextkällor.
- Kapitlet inför **informationsbudgeten**: behov → minsta kontext → identifiering → tjänst → flöde → konsekvens → beslut.
- Nästa steg: kapitel 16 och därefter helhetsgranskning.


## Layoutprov v1

Första PDF- och EPUB-exporten är genomförd och verifierad. PDF använder 6 × 9 tum och omfattar 267 fysiska sidor inklusive omslag och källförteckning; huvudbok inklusive bilagor ryms till cirka sida 250. Se `docs/layoutprov-v1.md`.


## 2026-09-02 – Layoutrevision v1.7

- Checklistor i Bilaga B har justerats så checkbox och text ligger på samma rad i PDF och EPUB.
- Inledning och bilagor använder nu samma visuella två-radsprincip som kapitelstarter: typetikett på första raden och rubriknamn centrerat under.
- Innehållsförteckningen behåller de fullständiga rubrikerna kompakt på en rad.
- Exporten har byggts om lokalt och PDF-layouten har verifierats på inledningen, Bilaga B och checklistan.
- GitHub Actions från v1.5 använder fortsatt samma exportskript och får därmed automatiskt de nya layoutreglerna.


## EPUB-layout v1.7

- EPUB:s navigationsindex behålls men ligger inte längre i läsordningen som en vanlig innehållsförteckningssida.
- Navigationsindexet visar skiljetecknet `–` mellan Kapitel/Bilaga/Inledning och rubriknamnet.
- EPUB:s titelsida centrerar titel, undertitel och författare i linje med PDF-versionens grundkomposition.

## Release candidate 1 – 2026-09-02

Projektet är nu satt till `v1.0.0-rc.1`.

Publiceringsfinishen omfattar:

- separat copyright-/kolofonsida i PDF och EPUB,
- baksidestext i `docs/baksidestext.md`,
- kort författarpresentation i boken och en extern version i `docs/forfattarpresentation.md`,
- svenska rättighetsuppgifter och RC-metadata,
- fortsatt stöd för manuell GitHub Actions-build och automatisk build vid publicerad release.

RC:n ska verifieras från ren checkout och därefter i GitHub Actions innan `v1.0.0`.
