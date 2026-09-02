# Researchresultat v8 – Icke-publikt material, databehandling och informationsminimering

## Syfte

Researchpasset stödjer kapitel 15, **När AI behöver känna till det som inte är publikt**. Fokus är att skilja mellan leverantörsspecifika dataskyddslöften och mer generella principer för informationsrisk.

## Huvudslutsats

Frågan "kan vi använda denna AI-tjänst med intern information?" kan inte besvaras enbart genom att kontrollera om leverantören tränar modeller på kunddata. Minst följande behöver skiljas åt:

1. vilken information användaren lämnar,
2. vad själva prompten avslöjar,
3. om data används för modellträning,
4. hur länge prompts, svar och filer lagras,
5. vilka personer och administrativa funktioner som kan få tillgång,
6. var data behandlas och vilka underbiträden/tredjeparter som används,
7. om webbsökning, connectors, plugins eller andra verktyg kan föra information vidare,
8. vilka rättigheter och kontroller som följer av den specifika kontotypen och avtalsmodellen.

Detta är en syntes av källorna och ska inte framställas som en formell standard.

## Leverantörsuppgifter måste knytas till produkt och avtalsform

### OpenAI

OpenAI anger för ChatGPT Business, Enterprise, Edu och API att organisationens in- och utdata inte används för modellträning som standard. Enterprise-erbjudanden har även retention controls. För kvalificerade API-kunder finns Zero Data Retention, där OpenAI enligt sin uppgift inte behåller prompts och svar efter behandlingen. [K-071] [K-072]

Dessa uppgifter ska beskrivas som **leverantörsuppgifter**, inte oberoende forskning.

### Anthropic

Anthropic anger att in- och utdata från kommersiella produkter, exempelvis Claude for Work och API, inte används för modellträning som standard. Standardretention för API anges till högst 30 dagar om inget annat avtalats, medan produkter som sparar konversationer behåller dem för produktfunktionen. Enterprise-kunder kan ha egna retention controls och vissa API-kunder kan få zero-data-retention-avtal. [K-073] [K-074] [K-075]

### Microsoft

Microsoft anger att prompts, svar och data som nås via Microsoft Graph i Microsoft 365 Copilot inte används för träning av foundation models. Samtidigt lagras användarinteraktioner, inklusive prompt och svar, som Copilot activity history och omfattas av organisationens retention- och compliancefunktioner. [K-076] [K-077]

Detta är pedagogiskt viktigt: **"används inte för träning" betyder inte "lagras inte"**.

### Google

Google anger för kvalificerade Workspace-erbjudanden med Gemini att prompts, Workspace-innehåll och svar inte används för att träna generativa modeller utanför organisationens domän utan tillstånd. Samma Privacy Hub visar samtidigt att retention varierar mellan produktvarianter och administratörsinställningar. [K-078]

## Anonymisering och pseudonymisering

EDPB:s riktlinjer om pseudonymisering tydliggör att pseudonymiserade data fortfarande är personuppgifter när de kan kopplas tillbaka till en individ med kompletterande information. Pseudonymisering reducerar risk men innebär alltså inte automatiskt att GDPR inte längre är relevant. [K-081]

EDPB publicerade i juli 2026 ett utkast till riktlinjer om anonymisering. Eftersom dokumentet fortfarande är ute på offentlig konsultation vid researchdatumet ska det uttryckligen beskrivas som **utkast**, inte slutlig vägledning. [K-082]

För boken innebär detta att termen "anonymisering" ska användas försiktigt. Att ersätta namn med "Person A" är normalt pseudonymisering eller maskning, inte nödvändigtvis anonymisering.

## Prompten är själv data

OWASP:s vägledning om Sensitive Information Disclosure betonar risken att användaren oavsiktligt lämnar känslig information till ett LLM-system. [K-079]

Bokens viktiga syntes är därför:

> **Det är inte bara bilagan, kodfilen eller databasutdraget som kan vara känsligt. Frågan kan vara känslig i sig.**

Exempel:

- "Hur åtgärdar vi CVE-X i vår internetexponerade betalningsgateway AcmePay?"
- "Skriv ett kommunikationsutkast om den ännu ej offentliggjorda nedläggningen av produkt X."
- "Analysera varför användaren med personnummer ... nekades ersättning."
- "Vilka angreppsvägar finns mot vår adminportal på ...?"

Även om dokumenten anonymiserats kan själva formuleringen avslöja organisation, system, incident, affärsbeslut, sårbarhet eller personkontext.

## Promptminimering som komplement till dataminimering

Boken inför **promptminimering** som pedagogiskt begrepp och egen syntes:

> Ge AI:n den minsta mängd identifierande och känslig kontext som behövs för att lösa just uppgiften.

Detta betyder inte att kontext ska tas bort tills svaret blir oanvändbart. Principen är snarare att skilja mellan:

- kontext som påverkar lösningen,
- kontext som bara gör exemplet mer verklighetstroget,
- identifierande detaljer som inte behövs alls.

Exempel: för att resonera om felhantering i ett API behövs ofta felmönster, kontrakt och constraints, men inte kundens namn, produktens marknadsnamn eller verkliga personuppgifter.

## Verktyg och connectors förändrar informationsflödet

När en AI-tjänst får webbsöka, använda connectors eller anropa verktyg räcker det inte att granska modellleverantörens grundläggande dataskyddsvillkor. Prompt injection kan påverka hur modellen behandlar information från externa källor och i agentsystem leda till oönskade verktygsanrop eller informationsspridning. [K-080]

Kapitlet ska därför återkoppla till **delegationsbudgeten** från kapitel 9: databehörighet och verktygsbehörighet behöver bedömas tillsammans.

## Rekommenderad boksynthes: informationsbudgeten

Kapitel 15 kan införa en enkel beslutsmodell som bokens egen syntes:

1. **Behov** – vilken uppgift försöker vi lösa?
2. **Minsta kontext** – vilken information behöver AI faktiskt?
3. **Identifiering** – vilka detaljer kan tas bort, generaliseras, maskas eller pseudonymiseras?
4. **Tjänst** – vilken produkt, kontotyp och avtalsmodell används?
5. **Flöde** – vart kan informationen gå via lagring, webbsökning, connectors, verktyg och administrativ åtkomst?
6. **Konsekvens** – vad händer om informationen exponeras eller används fel?
7. **Beslut** – använd, minimera ytterligare, välj annan miljö eller avstå.

Modellen ska inte beskrivas som juridisk klassningsmodell eller informationssäkerhetsstandard.

## Evidenshantering i manus

- Leverantörernas egna privacy-/security-sidor märks som leverantörsuppgifter.
- OWASP märks som expertbaserad öppen säkerhetsvägledning, inte experimentell forskning.
- EDPB-källor används för dataskyddsbegrepp; anonymiseringsriktlinjen från 2026 är vid researchdatumet ett konsultationsutkast.
- Bokens "informationsbudget" och "promptminimering" är pedagogiska synteser.

## Konsekvenser för kapitel 15

Kapitelplanen bör kompletteras med:

- anonymisering, pseudonymisering och maskning,
- prompten som informationsbärare,
- promptminimering,
- skillnaden mellan "inte träning" och "ingen lagring",
- feedbackfunktioner och andra undantag där data kan behandlas annorlunda,
- risken att connectors och externa verktyg skapar nya informationsflöden.
