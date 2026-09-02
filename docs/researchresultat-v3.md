# Researchresultat v3 – Skapa, samarbeta, kvalitet och review

## Syfte

Detta just-in-time-pass stödjer kapitel 6–7: **Fas 3: Skapa** och **Fas 4: Samarbeta**. Fokus är kvaliteten i AI-genererade artefakter, skillnaden mellan första utkast och leveransklart resultat, betydelsen av kontext och iteration samt AI:s roll i review.

Researchpasset förändrar inte sjufasmodellen, men preciserar två övergångar:

- Fas 3 börjar när AI:n får ansvar att producera ett konkret arbetsobjekt, inte bara resonera om det.
- Fas 4 börjar när användaren behandlar AI-output som något som ska granskas, testas, kritiseras och förbättras i en återkopplingsloop.

## Huvudfynd

### 1. AI-generering är redan spridd över flera utvecklingsaktiviteter

En peer-reviewad studie i *Information and Software Technology* baserad på en enkät med 481 programmerare kartlade användning av AI-assistenter för fem breda aktiviteter: implementering av nya funktioner, testskrivning, bug triage, refaktorering samt naturligt språk-baserade artefakter. Detta stödjer bokens val att behandla "Skapa" som en generell produktionsfas och inte som en synonym till kodgenerering. [K-035]

### 2. Första genererade artefakten kan inte likställas med korrekt eller leveransklar artefakt

En systematisk empirisk utvärdering av GitHub Copilots kodförslag visar att korrekthet varierar och att kodförslag behöver bedömas snarare än antas vara korrekta. Studien är ett argument för kvalitetssäkring, inte en universell felfrekvens för alla moderna modeller. [K-036]

En stor empirisk studie av LLM-baserad unit testing visar samtidigt att modeller kan vara användbara för testgenerering, assertions och testutveckling, men att kvaliteten varierar mellan modeller och uppgifter. Resultatet stödjer ett arbetssätt där generering följs av exekvering och kvalitetsevaluering. [K-017]

### 3. Kontext och flerturnsarbete kan förbättra resultatet

En explorativ studie från 2026 med sex moderna modeller och egenkonstruerade Python-metoder fann att mer relevant kodkontext och särskilt sekventiell multi-turn prompting gav bättre unit-testresultat än enklare engångspromptning. Den bästa strategin nådde hög branch coverage men betydligt lägre mutation score, vilket illustrerar att en enkel kvalitetsmetrik kan ge en överoptimistisk bild. Studien är begränsad till ett mindre specialkonstruerat dataset och ska användas som exempel, inte allmän effektstorlek. [K-037]

### 4. AI-assisterad review är värdefull men kontext- och riskberoende

En svensk empirisk fältstudie vid WirelessCar jämförde två LLM-assisterade code-reviewupplägg. Utvecklare föredrog ofta en AI-ledd review, särskilt för stora eller obekanta pull requests, men preferenser varierade med kodkännedom och risk. Studien identifierade också kontextbrist och false positives som praktiska problem. [K-038]

Nyare forskning om LLM:er som requirement-conformance-reviewers visar risk för systematisk överkorrigering. Detta stärker bokens princip att AI bör vara en reviewaktör, inte ensam kvalitetsgrind. [K-039]

### 5. Arbetet förskjuts från ren produktion mot styrning och verifiering

En longitudinell mixed-methods-studie från 2026 rapporterar en förskjutning från skapande mot verifieringsarbete bland professionella utvecklare och använder begreppet "supervisory engineering work" för att beskriva att styra, utvärdera och korrigera AI-output. Studien är publicerad som preprint och används därför som kompletterande, inte bärande, evidens. [K-040]

Detta ligger i linje med tidigare forskning i boken om kritiskt tänkande: AI kan minska arbetet med ren produktion men öka betydelsen av verifiering, integrering och stewardship. [K-013]

## Konsekvenser för kapitel 6 – Skapa

1. "Skapa" ska omfatta kod, tester, krav, acceptanskriterier, dokumentation, ADR:er, tabeller och analysutkast.
2. Kapitlet ska tydligt skilja mellan **genererbarhet** och **leveranskvalitet**.
3. Första utkastet ska beskrivas som ett sätt att minska startkostnaden, inte som slutprodukten.
4. Läsaren ska få en praktisk modell för att specificera:
   - syfte,
   - målgrupp/användare,
   - constraints,
   - kvalitetskriterier,
   - verifieringssätt.
5. Testbarhet/verifierbarhet ska vara en central faktor när man väljer vad AI får skapa.

## Konsekvenser för kapitel 7 – Samarbeta

1. Kärnloopen behålls: **utkast → granskning → kritik → förändring → verifiering**.
2. Kapitlet ska tona ned idén om "den perfekta prompten" och i stället betona återkopplingsloopar.
3. Review ska delas upp i olika roller: självgranskning av AI:n, mänsklig granskning, exekverbar verifiering och oberoende kontroll.
4. AI kan användas både som producent och kritiker, men samma modell ska inte betraktas som oberoende verifierare av sin egen output.
5. Kontextens kvalitet och relevans ska introduceras som brygga till kapitel 8, där "Ge kontext" behandlas på djupet.

## Evidensmässig försiktighet

- Kodstudier ska inte generaliseras direkt till krav, arkitektur eller dokument utan explicit markering att boken gör en analogi.
- Resultat för en specifik modellversion eller produkt är inte en bestående generell felfrekvens.
- Coverage, compilability och andra automatiska mått är inte ensamma liktydiga med kvalitet.
- Preprints används endast som kompletterande evidens när peer-reviewat stöd eller etablerade empiriska mönster finns i närliggande forskning.

## Slutsats

Researchpasset stärker skillnaden mellan fas 3 och 4. **Fas 3 handlar om att få AI att producera ett arbetsobjekt. Fas 4 handlar om att bygga en återkopplingsloop där arbetsobjektet förbättras och verifieras.** Mognadsökningen ligger därför mindre i längre prompts och mer i hur användaren designar samspelet mellan produktion, kritik och kontroll.
