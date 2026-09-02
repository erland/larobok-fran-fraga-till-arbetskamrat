# Researchresultat v6 – Mognadsresan genom utvecklingsprocessen

## Syfte

Detta researchpass prövar om bokens sjufasmodell fortfarande är pedagogiskt och empiriskt rimlig när samma förändring följs genom behov/krav, arkitektur/design, implementation, test och leverans.

Researchen används som underlag för kapitel 11–13. Den försöker inte etablera en vetenskaplig sjufasmodell. Fokus är i stället att se om forskningen inom respektive del av systemutvecklingsprocessen stödjer eller motsäger bokens centrala tes: att värdet av generativ AI förändras när användaren går från enstaka frågor och artefakter till kontextmedvetet samarbete, delegering och orkestrerade arbetsflöden.

## Övergripande slutsats

Sjufasmodellen håller även tvärs över utvecklingsprocessen, men researchen förstärker tre begränsningar:

1. **Mognaden är uppgiftsberoende.** En person eller ett team kan arbeta på fas 6 med kodändringar men på fas 2 med verksamhetskrav. Det är inte ett misslyckande utan kan vara rationell riskanpassning.
2. **Artefaktgränserna blir mindre viktiga än spårbarheten mellan dem.** När AI arbetar över krav, arkitektur, kod och test blir det avgörande att veta vilka antaganden och beslut som förts vidare mellan stegen.
3. **Kvalitetskontroll måste följa med när produktionsförmågan växer.** Forskningen visar användbara resultat inom krav, arkitektur, kod och test, men också återkommande problem med hallucinationer, reproducerbarhet, kontext, felaktig konformitetsbedömning och mätetal som inte fångar verklig kvalitet.

Det finns alltså stöd för att använda hela utvecklingsprocessen som bokens arena, men inte för att framställa AI som lika mogen eller lika pålitlig i alla delar av den.

## Krav och behov

En systematisk litteraturöversikt av 238 artiklar om generativ AI i requirements engineering visar ett snabbt växande forskningsfält. Mest forskning fanns inom kravanalys och elicitering, medan kravhantering var betydligt mindre studerat. Översikten identifierade reproducerbarhet, hallucinationer och interpretability som återkommande utmaningar. [K-055]

Detta stödjer kapitel 11:s upplägg: AI kan vara användbar för att bredda, strukturera och formulera kravmaterial, men en välformulerad requirement är inte samma sak som ett verifierat verksamhetsbehov.

En peer-reviewad studie från 2026 genererade 900 krav från 150 korta issue-titlar och utvärderade bland annat entydighet, verifierbarhet och singularitet. Resultaten visar att promptstrategi och modell påverkar kvaliteten och att kvalitetsbedömning behöver göras explicit. [K-056]

En mycket ny tväruppgiftsstudie från augusti 2026 fann att LLM-prestanda i requirements engineering varierade tydligt mellan fem olika aktiviteter och att ingen modell konsekvent var bäst. Studien är en preprint och ska därför användas som kompletterande evidens, men den stärker bokens princip att AI-användning måste anpassas till uppgift snarare än modellvarumärke. [K-057]

### Manuskonsekvens

Kapitel 11 bör tydligt skilja mellan:

- att formulera ett krav,
- att upptäcka saknad information,
- att förstå stakeholdermål,
- att validera att kravet faktiskt uttrycker rätt behov,
- att upprätthålla spårbarhet när kravet förändras.

AI kan hjälpa i alla fem, men evidensläget och verifieringsbehovet är inte samma.

## Arkitektur och design

En systematisk litteraturöversikt från 2025 identifierade endast 18 forskningsartiklar om LLM:er i mjukvaruarkitektur. Tillämpningar omfattade bland annat klassificering av designbeslut, mönsteridentifiering och arkitekturgenerering från krav, men flera centrala områden – exempelvis arkitekturkonformitet och kopplingen mellan design och implementation – var underutforskade. [K-058]

Det innebär att kapitel 12 bör vara försiktigare med effektpåståenden än kapitel som handlar om kodgenerering. AI:s styrka kan beskrivas som att snabbt generera alternativ, explicita antaganden och första utkast till beslutsrational, snarare än att forskningen skulle visa att AI självständigt kan fatta robusta arkitekturbeslut.

En empirisk studie av generering av design rationale för 100 arkitekturrelaterade problem visar detta väl. Modellerna kunde återge en stor del av den mänskliga expertens argument och genererade dessutom många argument som bedömdes som hjälpsamma, men precisionen var låg och en mindre andel argument var potentiellt missledande. [K-059]

En systematisk kartläggning av 86 studier om LLM:er i model-driven engineering visar dessutom snabbt växande användning för modellartefakter, men pekar på brister i rapportering och reproducerbarhet samt att vanliga mätetal inte alltid passar för komplexa modellartefakter. [K-060]

### Manuskonsekvens

Kapitel 12 bör göra en tydlig skillnad mellan:

- **alternativgenerering** – AI kan bredda lösningsrymden,
- **rationaldokumentation** – AI kan hjälpa till att formulera trade-offs och ADR-utkast,
- **beslut** – människan/teamet äger värderingen av kvalitetsattribut och konsekvenser,
- **konformitet** – verifiering behöver koppla arkitekturbeslut till verklig implementation.

## Implementation och repositoryarbete

En bred survey från 2026 sammanställer 926 studier om 112 kodrelaterade uppgifter över fem faser i software engineering. Den visar att forskningen inte längre är begränsad till funktion-level code completion; LLM:er används för ett stort spektrum av aktiviteter genom livscykeln. [K-061]

Tidigare researchpass har redan visat att repository-level context och retrieval är en egen svårighet. För Del III innebär det att implementationen inte bör beskrivas som en enkel översättning från krav till kod. När AI arbetar i ett existerande system måste den hitta relevanta komponenter, följa lokala konventioner och förstå vilka delar av designen som redan är realiserade. [K-041]

Empiriska studier av kodkvalitetsproblem och requirement-conformance visar samtidigt att AI både kan hjälpa till att identifiera/åtgärda problem och överkorrigera när den används som granskare. [K-039] [K-064]

### Manuskonsekvens

Kapitel 12 bör därför använda **ändringsplanen** som en central brygga mellan arkitektur och implementation:

> kravpåverkan → designbeslut → berörda komponenter → planerade kodändringar → verifiering

Det gör det möjligt att arbeta iterativt med AI utan att låtsas att design och kod är samma artefakt.

## Test, kvalitet och leverans

En systematisk litteraturöversikt från 2026 analyserade 38 peer-reviewade artiklar om LLM-baserad testgenerering. Den visar möjligheter att öka hastighet och coverage men också stora variationer i dataset, integration och utvärderingsmetoder. Översikten betonar att coverage behöver kompletteras med andra kvalitetsmått, exempelvis mutation testing och faktisk exekveringskorrekthet. [K-062]

Tidigare researchpass visade också att kontext och flerturnsarbete kan förbättra genererade tester samtidigt som hög branch coverage inte garanterar hög mutation score. [K-037]

En empirisk studie av automatiserad compliance testing för webbtillgänglighet från 2026 visar ett annat viktigt mönster: LLM:er kunde vara användbara, men hade stora problem att avgöra när vissa kriterier faktiskt var tillämpliga och författarna bedömde human-in-the-loop som den lämpliga användningsformen. [K-065]

DORA:s 2025-rapport bygger på data från nära 5 000 teknikprofessionella och beskriver AI som en förstärkare av befintliga organisatoriska förmågor. Rapporten betonar att lokala produktivitetsvinster behöver kopplas till värdeflöde, plattformar, feedback och organisatoriska grundförmågor för att ge systemeffekt. Det är leverantörsproducerad branschforskning och ska märkas som sådan, men är relevant för övergången från test till leverans och vidare till kapitel 16. [K-063]

### Manuskonsekvens

Kapitel 13 bör skilja mellan tre frågor:

1. **Har vi producerat fler tester?**
2. **Hittar testerna relevanta fel?**
3. **Ger hela leveransflödet tillräckligt förtroende för förändringen?**

AI kan påverka alla tre, men det tredje är systemfrågan och kan inte reduceras till testgenerering.

## Det genomgående scenariot

För Del III används ett gemensamt scenario i ett existerande system:

> Användare ska kunna prenumerera på statusnotiser för ett ärende och välja kanal. Lösningen ska passa befintligt system, respektera behörighet och användarpreferenser, hantera misslyckade leveranser och kunna verifieras före utrullning.

Scenariot är medvetet vardagligt. Syftet är inte att demonstrera en spektakulär AI-agent utan att visa hur samma förändring kräver olika sorters mänsklig och AI-assisterad kompetens genom utvecklingsprocessen.

### Scenariofakta som är pedagogiska, inte domänkrav

Följande antaganden är bokens exempel och ska inte uppfattas som forskningsresultat:

- Systemet har redan webbgränssnitt, backend, databas och en befintlig händelsemekanism.
- E-post finns som befintlig integrationsmöjlighet; push/SMS behandlas som tänkbara alternativ men inte nödvändigtvis i första leveransen.
- Användare kan se ärenden enligt befintlig behörighetsmodell.
- Teamet har CI, automatiserade tester och ett etablerat reviewflöde.
- Kraven är initialt ofullständiga och innehåller medvetet öppna frågor.

Det gör att mognad kan visas genom hur användaren hanterar osäkerheten, inte genom hur mycket information scenariot råkar ge från början.

## Ny pedagogisk syntes: den vertikala spårbarhetskedjan

Del III inför en ny modell som är **bokens syntes**:

> **behov → beslut → förändring → bevis**

- **Behov:** varför förändringen behövs och vilket utfall som eftersträvas.
- **Beslut:** vilka krav- och designval som gjorts och varför.
- **Förändring:** vad som faktiskt ändrats i systemet.
- **Bevis:** vilken evidens som gör att teamet kan bedöma om förändringen är korrekt och tillräckligt säker att leverera.

Mognaden i Del III visas inte genom att varje roll når fas 7. Den visas genom att dessa fyra länkar blir tydligare, mer sammanhängande och lättare att verifiera när AI används väl.

## Beslut efter researchpass v6

1. Kapitel 11–13 skrivs med samma scenario genom hela blocket.
2. Alla sju faser visas, men kapitlen ska inte återberätta kapitel 4–10. Faserna används som analyslinser.
3. Del III inför den vertikala spårbarhetskedjan **behov → beslut → förändring → bevis** som bokens syntes.
4. Kravkapitlet skiljer genererad formulering från validerat behov.
5. Arkitekturkapitlet är försiktigt med autonomi eftersom forskningsfältet är mindre och mindre empiriskt moget än kodområdet.
6. Testkapitlet behandlar coverage som ett delmått, inte som synonym till kvalitet.
7. Leverans behandlas som ett systemutfall: snabbare lokal produktion är inte tillräckligt om review, test eller deploy blir flaskhalsar.
8. Evidenstyp ska fortsatt vara synlig i brödtexten.
