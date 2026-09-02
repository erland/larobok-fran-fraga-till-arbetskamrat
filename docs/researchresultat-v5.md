# Researchresultat v5 – Orkestrering, evals och observerbara agentflöden

## Syfte

Detta just-in-time-pass stödjer kapitel 10: **Fas 7: Orkestrera** och den sammanhållna granskningen av mognadsresan i kapitel 4–10. Fokus är flerledade agentflöden, single-agent kontra multi-agent, kontrollpunkter, observability/spårbarhet, evals samt hur man avgör om ett mer komplext AI-assisterat arbetssystem faktiskt är bättre än en enklare lösning.

Researchpasset leder till en viktig precisering:

> **Orkestrering är inte synonymt med multi-agent.**

I boken betyder orkestrering att AI blir en medvetet designad del av ett återkommande eller sammanhängande arbetssystem. Det systemet kan bestå av en agent, flera agenter, deterministisk automation, människor och andra verktyg.

## Huvudfynd

### 1. Arbetsflöden och agenter är olika former av agentiska system

Anthropic skiljer mellan **workflows**, där modeller och verktyg följer fördefinierade kodvägar, och **agents**, där modellen dynamiskt styr processen och väljer verktyg. De rekommenderar att börja med den enklaste lösningen som fungerar och bara lägga till agentisk komplexitet när den ger mätbar nytta. [K-046]

Konsekvens för boken: fas 7 ska inte presenteras som "bygg ett multi-agent-system" utan som **designa rätt kombination av determinism, AI-frihet och mänskliga kontrollpunkter**.

### 2. Orchestrator–workers är ett användbart mönster, men inte ett standardmål

Anthropic beskriver ett orchestrator–workers-mönster där en central modell delar upp en uppgift dynamiskt, delegerar deluppgifter och syntetiserar resultaten. De anger komplexa kodändringar över flera filer och sökuppgifter över flera källor som exempel där mönstret kan passa. Samma vägledning framhåller samtidigt att komplexitet har kostnad i latency, ekonomi och felsökningsbarhet. [K-046]

OpenAI:s praktiska agentguide beskriver på liknande sätt single-agent och multi-agent-orchestration samt rekommenderar att börja enkelt, bygga guardrails och lägga mänsklig intervention vid högrisksteg. [K-052]

Konsekvens för boken: **multi-agent blir ett exempel på orkestrering, inte definitionen av den**.

### 3. Fler agenter ger inte automatiskt bättre resultat

En empirisk studie av flera agentramverk över kodcentrerade mjukvaruuppgifter fann tydliga trade-offs mellan effektivitet, task success, tokenkostnad och koordinationsöverhead. Vissa orkestrerade system fick längre trajectories och fler korrigeringsförsök utan att detta automatiskt gav bäst resultat. Studien är en preprint och används därför som kompletterande evidens, inte universell effektmätning. [K-051]

En mixed-method-studie publicerad 2026 om multi-agent-ramverk för software engineering fann god täckning av grundfunktioner men brister i bland annat telemetry och ingen signifikant skillnad i ROUGE-resultat i deras gemensamma summariseringsuppgift. Författarna betonar teknikval, koordinationsregler och agentroller som praktiska utmaningar. [K-050]

Konsekvens för boken: mognad kan inte mätas i **antal agenter**. Komplexitet måste motiveras av uppgiften och verifieras mot utfall.

### 4. Agentiska system behöver utvärderas som hela förlopp, inte bara på slutsvaret

Anthropics vägledning om agent-evals betonar att agenter arbetar över flera turer, använder verktyg, ändrar state och anpassar sig efter mellanresultat. Det skapar flera möjliga felpunkter innan slutresultatet syns. De rekommenderar därför evals som fångar hela beteendet, inte bara sluttexten. [K-047]

NIST:s arbete om agentutvärderingar och transcript analysis pekar i samma riktning: längre agentbanor kräver metoder för att analysera vad som faktiskt hände under körningen, inklusive mätfel och beteenden som kan göra en benchmark missvisande. [K-049]

Konsekvens för boken: fas 7 behöver introducera skillnaden mellan **resultatobservability** och **processobservability**.

### 5. En eval är inte bara ett engångstest före lansering

Anthropic beskriver evals som ett sätt att göra fel och beteendeförändringar synliga genom en agents livscykel. [K-047]

NIST:s utkast om automatiserade benchmark-evalueringar betonar validitet, transparens och reproducerbarhet som centrala egenskaper hos utvärdering av språkmodeller och agentsystem. [K-048]

NIST:s TEVV-Athlon-utkast från augusti 2026 placerar Test, Evaluation, Verification and Validation i ett bredare livscykelperspektiv för verkliga AI-system, inklusive agentiska system. [K-053]

Konsekvens för boken: ett moget arbetsflöde behöver ett **återkommande sätt att veta om det fortfarande fungerar när modeller, prompts, verktyg, data eller processer förändras**.

### 6. Spårbarhet och observability blir en ny kvalitetsinfrastruktur

NIST:s projekt om evaluation probes beskriver behovet av mätpunkter och traceability inne i agentiska ekosystem, särskilt där faktagrundning och output traceability är viktiga. [K-054]

OpenAI:s och Anthropics tekniska vägledning lyfter tracing/evals respektive transparens och agentbanor som centrala delar av produktionsmässigt agentarbete. Dessa är leverantörsuppgifter och ska inte framställas som oberoende bevis, men visar en tydlig konvergens i praktisk systemdesign. [K-047] [K-052]

Konsekvens för boken: observability ska beskrivas som förmågan att efteråt kunna förstå exempelvis:

- vilket mål flödet arbetade mot,
- vilken kontext som användes,
- vilka verktyg som anropades,
- vilka beslut/handoffs som gjordes,
- vilka kontroller som passerades,
- vilken version av modell/instruktioner som användes,
- vad som faktiskt ändrades.

### 7. Orkestrering förändrar människans kontrollpunkt

I fas 6 granskar människan huvudsakligen en delegerad uppgift. I fas 7 måste människan också kunna granska **själva systemet som producerar uppgifterna**.

Detta stöds indirekt av forskningen om agentiska systems eval- och koordinationsproblem samt av den bredare förskjutningen mot supervisory engineering work som identifierats i tidigare researchpass. [K-040] [K-047] [K-050]

Konsekvens för boken: fas 7 ska ha två verifieringsnivåer:

1. **Är den här körningen acceptabel?**
2. **Är arbetsflödet fortfarande designat på ett bra sätt?**

## Konsekvenser för kapitel 10 – Orkestrera

1. Definiera fasgränsen som **design av ett AI-assisterat arbetssystem**, inte multi-agent.
2. Skilj mellan:
   - deterministiska steg,
   - AI-bedömda steg,
   - delegerade agentuppgifter,
   - mänskliga beslut/kontrollpunkter.
3. Inför **arbetsflödeskontraktet** som bokens egen syntes:
   - trigger och mål,
   - state och kontext,
   - roller/steg,
   - handoffs och kontrollpunkter,
   - observability,
   - evals och förbättringsloop.
4. Introducera **två nivåer av kvalitet**:
   - körningskvalitet,
   - systemkvalitet över tid.
5. Visa att återkommande processer ofta lämpar sig bättre för tydliga workflows än fri agentautonomi.
6. Multi-agent ska behandlas som ett specialfall där specialisering/parallelism kan motivera koordinationskostnaden.
7. Kapitlet ska avsluta mognadsresan med att fas 7 är en **repertoarförmåga**, inte ett slutmål för varje uppgift.

## Evidensmässig försiktighet

- Anthropic och OpenAI har djup praktisk erfarenhet av egna agentplattformar men är kommersiella leverantörer. Deras arkitekturmönster används som teknisk vägledning, inte som oberoende effektbevis.
- Forskningen om multi-agent-system i software engineering är fortfarande ung. Preprints och små uppgifter ska användas för att visa trade-offs och forskningsläge, inte för exakta generella effektpåståenden.
- Evals kan öka synligheten och jämförbarheten men bevisar inte att ett system är säkert eller korrekt i alla situationer.
- Observability gör fel lättare att förstå; den förhindrar inte i sig fel.

## Slutsats

Researchpasset stärker fas 7 men gör den mindre teknikromantisk. **Orkestrering handlar inte om att maximera antalet agenter eller graden av autonomi. Det handlar om att designa ett arbetsflöde där rätt delar är deterministiska, rätt delar använder AI, rätt beslut stannar hos människor och kvaliteten går att observera och utvärdera över tid.**
