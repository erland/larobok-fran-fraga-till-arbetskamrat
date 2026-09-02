# Mognadsmodell för AI-assisterat arbete

## Modellens syfte

Den sjufasmodell som används i boken beskriver hur AI-assisterat kunskapsarbete kan utvecklas från enstaka frågor till integrerade arbetsflöden. **Modellen är bokens pedagogiska syntes och är inte en etablerad vetenskaplig sjufasmodell.** Researchpass v1 visar att flera underliggande rörelser i modellen stöds av användningsdata och forskning, men inte att alla personer följer stegen linjärt. Se `docs/researchresultat-v1.md`.

Mognad betyder inte att AI alltid ska få större autonomi. Research från 2026 om avancerade AI-användare stärker snarare synen att mogen användning innebär att välja rätt arbetsform för uppgiften. En mogen användare kan medvetet välja ett enklare arbetssätt när risk, osäkerhet eller behov av eget tänkande kräver det.

En och samma person kan samtidigt befinna sig på olika nivåer i olika aktiviteter. En utvecklare kan exempelvis delegera implementation på hög nivå men bara använda AI som bollplank för säkerhetskritisk arkitektur.


## Tre lager i mognad efter researchpass v1

### Repertoar

Användaren behärskar fler sätt att arbeta med AI: fråga, resonera, skapa, iterera, använda verklig kontext, delegera och designa arbetsflöden.

### Situationsanpassning

Användaren kan välja rätt arbetsform utifrån uppgiftens risk, komplexitet, informationsklassning, egen kompetens och hur reversibla konsekvenserna är.

### Kontroll

Användaren kan verifiera resultat, sätta kvalitetsribba, styra behörigheter och verktyg, upptäcka när AI sannolikt ligger utanför sin kapabilitetsgräns och mäta om arbetssättet förbättrar helheten.

**Forskningsanknytning:** OpenAI:s användningsdata visar ökad bredd och djup över tid; Anthropic visar en rörelse mot mer agentiska och automatiserade arbetsformer; Microsofts 2026-data om avancerade användare betonar medvetet val mellan arbetsformer samt kvalitet och mänskligt ansvar. Detta stödjer modellens riktning men inte en strikt sjufas-sekvens. Källor: K-001, K-003, K-005, K-006.

## De sju pedagogiska mognadsstegen

### Fas 1 – Fråga

**AI används som:** interaktiv kunskapskälla.

**Typiskt beteende:** användaren ställer fristående frågor och bedömer svaret.

**Kärnförändring:** från traditionell sökning och dokumentationsläsning till dialogbaserad informationsinhämtning.

**Exempel:**

- "Vad är skillnaden mellan optimistic och pessimistic locking?"
- "Vad innebär en icke-funktionell kravtyp?"
- "Vad är contract testing?"

**För att ta nästa steg:** börja använda följdfrågor, jämförelser, motargument och alternativa perspektiv.

### Fas 2 – Resonera

**AI används som:** bollplank och rådgivare.

**Typiskt beteende:** användaren för en dialog för att förstå problem, alternativ, konsekvenser och luckor.

**Kärnförändring:** från att få svar till att tänka tillsammans.

**Exempel:**

- jämföra tre arkitekturalternativ,
- be AI identifiera svagheter i ett krav,
- resonera om möjliga orsaker till ett fel,
- be om argument både för och emot en design.

**För att ta nästa steg:** be AI skapa ett konkret arbetsresultat i stället för att bara beskriva hur det kan göras.

### Fas 3 – Skapa

**AI används som:** produktionsverktyg.

**Typiskt beteende:** AI skapar första versioner av artefakter som användaren sedan granskar och bearbetar.

**Kärnförändring:** från information till produktion.

**Exempel:**

- kod och tester,
- kravförslag och acceptanskriterier,
- ADR-utkast,
- analysunderlag,
- dokumentation och tabeller.

**För att ta nästa steg:** sluta behandla första resultatet som leveransen och börja arbeta iterativt med kritik och förbättring.

### Fas 4 – Samarbeta

**AI används som:** digital arbetskamrat.

**Typiskt beteende:** människan och AI:n itererar över samma problem eller artefakt i flera steg.

**Kärnförändring:** från beställning till samarbete.

**Typisk loop:** utkast → kritik → förändring → kontroll → ny iteration.

**Exempel:**

- stegvis refaktorering,
- kravförfining,
- testanalys,
- arkitekturreview där AI först föreslår och sedan utmanar sitt eget förslag.

**För att ta nästa steg:** ge AI tillgång till den faktiska projektkontext som behövs för att slippa arbeta på generiska antaganden.

### Fas 5 – Ge kontext

**AI används som:** projektmedarbetare.

**Typiskt beteende:** AI arbetar med verkligt arbetsmaterial: filer, repositoryn, modeller, dokument, historik, krav, beslut eller andra informationsmängder.

**Kärnförändring:** från generiskt kunnande till situationsförståelse.

**Exempel:**

- analysera hela kodbasen före en refaktorering,
- jämföra krav med befintliga testfall,
- läsa arkitekturmodeller och styrande dokument tillsammans,
- använda tidigare beslut som begränsningar.

**Nytt ansvar:** informationsklassning, dataskydd, behörighet, retention och kontroll över vilka externa tjänster som får tillgång till materialet. Researchpass v4 preciserar dessutom att mer kontext inte automatiskt är bättre: relevans, aktualitet, auktoritet och synliga luckor behöver bedömas. [K-041]

**För att ta nästa steg:** delegera ett sammanhängande mål snarare än att instruera varje enskilt delsteg.

### Fas 6 – Delegera

**AI används som:** utförare av flerledade arbetsuppgifter.

**Typiskt beteende:** användaren beskriver mål, begränsningar och kvalitetskrav; AI planerar och genomför flera delsteg med verktyg och återkopplar resultat.

**Kärnförändring:** från att styra varje aktivitet till att styra mål och verifiering.

**Exempel:**

- analysera ett fel, ändra kod, köra tester och sammanfatta förändringen,
- analysera en backlogg och föreslå konsekventa kravförändringar,
- granska ett system mot arkitekturprinciper och föreslå korrigeringar,
- identifiera testluckor och implementera relevanta automatiserade tester.

**Nytt ansvar:** tydliga befogenheter, avgränsningar, verktygsåtkomst, reversibilitet och verifiering av faktiska ändringar. Researchpass v4 inför bokens begrepp **delegationsbudget** för data, verktyg, behörigheter, tid/kostnad och irreversibla åtgärder. [K-043] [K-044]

**För att ta nästa steg:** designa stabila arbetsflöden där AI återkommande används på rätt nivå i flera aktiviteter.

### Fas 7 – Orkestrera

**AI används som:** en integrerad del av arbetssystemet.

**Typiskt beteende:** människan designar ett arbetsflöde där AI, deterministisk automation och mänskliga beslut används på medvetet valda platser. Orkestrering kräver inte flera agenter; multi-agent är ett möjligt specialfall när specialisering eller parallellism motiverar koordinationskostnaden. [K-046] [K-050] [K-051]

**Kärnförändring:** från enskilda AI-uppgifter till AI-assisterade arbetsflöden.

**Exempel:**

- behov → analys → implementation → test → dokumentation → review,
- återkommande arkitekturgranskning med kända modeller och styrande dokument,
- AI-assisterad triage, förändringsanalys och kvalitetssäkring med mänskliga beslutspunkter.

**Nytt ansvar:** governance, spårbarhet, ansvarsfördelning, kvalitet, säkerhet och kontinuerlig utvärdering av både enskilda körningar och om arbetsflödet som system fortfarande ger bättre resultat. Researchpass v5 inför bokens begrepp **arbetsflödeskontrakt** för trigger/mål, state/kontext, roller/steg, handoffs/kontrollpunkter, observability och evals. [K-047] [K-048] [K-049]

## Sex dimensioner som förändras genom resan

### Uppgiftens omfattning

Från en fråga eller mikroaktivitet till ett mål som omfattar flera arbetssteg.

### Kontextens rikedom

Från allmän kunskap till faktisk projekt-, organisations- och domänkontext.

### Samarbetsformen

Från enstaka svar till återkommande iterationer och gemensam problemlösning.

### AI:ns handlingsutrymme

Från rekommendationer till verktygsanvändning och faktiska förändringar.

### Människans styrning

Från detaljinstruktioner till mål, begränsningar, kvalitetskriterier och kontrollpunkter.

### Kravet på verifiering och governance

Från rimlighetskontroll av ett svar till systematisk validering, informationsstyrning, behörighetskontroll och ansvarsfördelning.

## Viktiga principer

### Mognad är inte samma sak som maximal autonomi

Det mogna valet kan vara att stanna på fas 2 i en riskfylld situation och använda fas 6 i en väl avgränsad, reversibel arbetsuppgift.

### Mognadsresan är inte strikt linjär

Personer kan hoppa mellan nivåerna, backa medvetet och vara på olika nivåer i olika delar av sitt arbete.

### Nästa steg kräver ofta ett mentalt skifte

- Fas 1 → 2: från svar till resonemang.
- Fas 2 → 3: från råd till artefakt.
- Fas 3 → 4: från första utkast till iteration.
- Fas 4 → 5: från generisk dialog till verklig kontext.
- Fas 5 → 6: från deluppgifter till målbaserad delegering.
- Fas 6 → 7: från enskild delegering till designade arbetsflöden.

### Informationsrisken växer inte exakt med mognadsnivån

Den påverkas av vilken information, vilket verktyg, vilka avtal, vilka integrationer och vilka behörigheter som används. Däremot ökar behovet av medveten informationsstyrning normalt när AI får rikare kontext och fler verktyg.

## Evidensbedömning per steg

| Steg | Evidensläge | Kommentar |
|---|---|---|
| 1 Fråga | Starkt för arbetsformen | Asking/informationsinhämtning syns tydligt i OpenAI- och Microsoft-data. |
| 2 Resonera | Starkt för arbetsformen | Exploration/collaboration och forskning om AI som tankepartner stödjer detta som distinkt arbetssätt. |
| 3 Skapa | Starkt för skiftet till produktion | OpenAI:s doing-kategori och bred användning för artefaktproduktion stödjer skiftet. |
| 4 Samarbeta | Starkt för arbetsformen | Anthropic skiljer task iteration/feedback loop från directive automation; Microsoft skiljer collaboration från delegation. |
| 5 Ge kontext | Medel – viktig mekanism, svagare som kronologiskt steg | Kontext är central för situationsanpassat arbete, men moderna verktyg kan ge repository-/organisationskontext tidigt. Ska presenteras som tröskel/dimension snarare än universell tidsordning. |
| 6 Delegera | Starkt för arbetsformen | Agent-/kodagentdata visar mer directive/automation och flerledade uppgifter. |
| 7 Orkestrera | Växande stöd | Multi-step workflows, agent-evals och systemperspektiv ger stöd för arbetsformen. Multi-agent-forskningen är fortfarande ung; fasen definieras därför som designat AI-assisterat arbetssystem, inte som många agenter. [K-046] [K-047] [K-050] |

Källor och metodnoter finns i `docs/kallregister.md` samt researchresultat v1–v5.
