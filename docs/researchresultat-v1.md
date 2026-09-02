# Researchresultat v1 – mognadsresa och AI-assisterat systemutvecklingsarbete

**Researchdatum:** 2026-09-02  
**Syfte:** pröva bokens grundtes och sjufasmodell innan manusproduktion.

## Sammanfattande bedömning

Researchpasset ger **stöd för bokens övergripande tes**, men inte för att sju steg skulle vara en etablerad eller universellt linjär mognadsmodell.

Det finns empiriskt stöd för flera underliggande rörelser:

1. användare breddar och fördjupar AI-användningen över tid,
2. arbetsanvändning rör sig från informationsinhämtning mot att producera och utföra arbete,
3. specialist- och agentverktyg används mer för delegering/automation än vanliga chattgränssnitt,
4. avancerade användare arbetar mer med flerledade arbetsflöden och väljer mer medvetet mellan mänskligt och AI-baserat arbete,
5. verifiering och mänskligt omdöme blir inte mindre viktiga när användningen mognar – de byter delvis karaktär och blir mer systematiska.

Därför behålls de sju stegen som **bokens pedagogiska syntes**, men modellen justeras så att mognad definieras som en växande repertoar och bättre situationsanpassning, inte som en enkel resa mot mer autonomi.

---

# 1. Förändras användningen med erfarenhet?

## Starkt stöd: användningen breddas och fördjupas

OpenAI Signals rapporterade 2026 att användare sex månader efter registrering i genomsnitt skickade cirka 50 % fler meddelanden per dag än i början och hade fördubblat antalet distinkta uppgiftstyper de provat. Analysen byggde på ett 0,1-procentigt urval av individuella ChatGPT-konton skapade mellan oktober 2025 och maj 2026. Det är leverantörstelemetri, inte en oberoende studie, men direkt relevant för hypotesen att användarrepertoaren växer med användningstid. [K-001]

OpenAI redovisar också en skillnad mellan "asking" och "doing": i arbetsrelaterad användning dominerar i högre grad uppgifter där användaren producerar ett resultat eller utför en aktivitet. [K-002]

### Konsekvens för boken

Bokens inledning kan med gott stöd säga att **människor tenderar att både använda AI mer och prova fler typer av uppgifter över tid** – men inte att alla automatiskt följer exakt våra sju steg.

## Starkt stöd: avancerad användning är inte bara "mer AI"

Microsofts Work Trend Index 2026 beskriver en grupp "Frontier Professionals", cirka 16 % av de AI-användare som ingick i deras undersökning. De använder agenter för flerledade arbetsflöden och multi-agent-system, men skiljer sig också genom att oftare bestämma vad som bör göras av människa respektive AI. 53 % uppgav att de avsiktligt stannar upp före en uppgift för att göra den bedömningen, jämfört med 33 % bland övriga. Rapporten betonar att det som skiljer avancerade användare inte är vilket läge de alltid använder, utan att de vet vilket läge en uppgift kräver. [K-003]

### Konsekvens för boken

Detta stärker vår viktigaste korrigering:

> Mognad är förmågan att **välja rätt samarbetsform, kontext, autonomi och kontroll för uppgiften** – inte att alltid delegera mer.

---

# 2. Finns stöd för rörelsen fråga → samarbete → delegering → arbetsflöde?

## Flera datakällor pekar i samma riktning

Microsofts Work Trend Index 2025 presenterade en trestegsbild av organisatorisk AI-utveckling: människa med assistent, människa–agent-team och slutligen människostyrda men agentdrivna processer. Det är en leverantörsmodell och ska inte användas som bevis för vår exakta modell, men den visar att en liknande progression används i ett stort datamaterial med 31 000 arbetstagare, LinkedIn-data och Microsoft 365-signaler. [K-004]

Anthropics analys av 500 000 kodrelaterade interaktioner visade att Claude Code användes betydligt mer automatiserande än Claude.ai: 79 % av Claude Code-interaktionerna klassificerades som automation jämfört med 49 % på Claude.ai. "Directive"-mönster och feedbackloopar var också vanligare i kodagenten. [K-005]

I Anthropic Economic Index juni 2026 konstateras att Claude-användning på ett år förändrats från huvudsakligen chatt mellan användare och assistent till en växande andel långvariga agentiska uppgifter i Claude Code och Cowork. [K-006]

Microsoft 2026 skiljer empiriskt och konceptuellt mellan fyra arbetsformer – asking, exploration, collaboration och delegation – och beskriver avancerade användare som personer som också designar flerledade agentarbetsflöden. [K-003]

### Konsekvens för sjufasmodellen

Forskningen motiverar **inte att slå ihop modellen till tre eller fyra steg**, eftersom vår modell har ett pedagogiskt annat syfte. Däremot ska vi vara tydliga med att:

- "Fråga", "resonera", "samarbeta" och "delegera" är arbetsformer som även kan samexistera.
- "Skapa" beskriver ett viktigt mentalt skifte från rådgivning till artefaktproduktion.
- "Ge kontext" är snarare en **mognadsdimension/tröskel** än en naturlig kronologisk fas; moderna IDE-assistenter kan ge kontext mycket tidigt.
- "Orkestrera" beskriver design av återkommande arbetsflöden och kontrollpunkter, inte maximal agentautonomi.

Vi behåller därför sju steg, men kallar dem konsekvent **pedagogiska mognadssteg** och betonar att de inte är en strikt sekvens.

---

# 3. Produktivitet: forskningen kräver en mycket nyanserad bok

## Resultaten går åt olika håll – med goda skäl

### Positiva kausala resultat i vissa utvecklarmiljöer

Tre randomiserade fältexperiment på Microsoft, Accenture och ett Fortune 100-företag, sammanlagt 4 867 utvecklare, fann 26,08 % fler slutförda uppgifter bland utvecklare som fick tillgång till en AI-kodassistent. Mindre erfarna utvecklare hade både högre adoption och större produktivitetsvinster. [K-008]

I kundsupport, alltså en annan typ av kunskapsarbete, fann en peer-reviewad studie av drygt 5 000 agenter cirka 15 % högre produktivitet i genomsnitt. Vinsten var betydligt större för mindre erfarna/lägre presterande medarbetare, medan de mest erfarna såg små vinster och i vissa kvalitetsmått små försämringar. [K-012]

### Negativt resultat för erfarna utvecklare i välkända kodbaser

METR:s randomiserade studie 2025 lät 16 erfarna open-source-utvecklare lösa 246 verkliga issues i projekt de i genomsnitt arbetat med i fem år. Med tidiga 2025-verktyg tog uppgifterna 19 % längre tid när AI var tillåtet. Utvecklarna trodde samtidigt att AI hade gjort dem cirka 20 % snabbare. [K-009]

METR:s uppföljning med senare verktyg antydde 2026 att AI sannolikt blivit mer produktivt, men studien drabbades av starka urvalseffekter eftersom utvecklare som var mycket beroende av AI inte ville delta i en design där de ibland skulle arbeta utan AI. METR bedömde därför att de inte kunde ge en tillförlitlig storleksuppskattning. [K-010]

### "Jagged frontier" är en bra förklaringsmodell

Ett peer-reviewat fältexperiment med 758 konsulter visade stora vinster på uppgifter inom den dåvarande modellens kapabilitetsgräns: högre kvalitet, fler slutförda uppgifter och mer än 25 % snabbare arbete. På en uppgift med korrekt svar utanför denna gräns blev AI-grupperna däremot i genomsnitt 19 procentenheter mindre korrekta. [K-011]

### Konsekvens för boken

Kapitel 3 ska inte fråga "hur mycket snabbare blir man?" utan lära läsaren att bedöma minst:

- uppgiftstyp,
- personens erfarenhet och domänkunskap,
- hur väl personen känner den befintliga kodbasen,
- AI-systemets faktiska kapabilitet för just uppgiften,
- kostnaden för verifiering och omarbete,
- om vinsten är lokal eller förbättrar hela flödet.

Självrapporterad och uppmätt produktivitet måste hållas isär konsekvent.

---

# 4. Verifiering och mänskligt omdöme är en kärna i mogen användning

Stack Overflows Developer Survey 2025 hade över 49 000 respondenter. 84 % använde eller planerade att använda AI i utvecklingsprocessen och 51 % av professionella utvecklare uppgav daglig användning. Samtidigt uppgav 46 % att de aktivt misstror AI-verktygens korrekthet jämfört med 33 % som litar på den. Erfarna utvecklare var mest skeptiska. [K-007]

En CHI 2025-studie med 319 kunskapsarbetare och 936 konkreta arbetsexempel fann att högre tilltro till AI hängde samman med mindre kritiskt tänkande, medan högre tilltro till den egna förmågan hängde samman med mer kritiskt tänkande. Studien beskriver också en förskjutning från informationsinhämtning till verifiering, från problemlösning till integration av AI-svar och från direkt utförande till "task stewardship". [K-013]

Microsofts 2026-undersökning pekar i samma riktning: avancerade användare betonade kvalitetskontroll och kritiskt tänkande och såg AI-resultat som startpunkt snarare än slutprodukt. [K-003]

### Konsekvens för boken

Kapitel 14 bör inte formuleras defensivt som "vad människan har kvar". Det handlar snarare om **hur människans arbete förändras**:

- från att producera allt själv till att formulera mål och kvalitetsribba,
- från att själv samla all information till att verifiera och integrera,
- från att utföra varje steg till att styra, utvärdera och ta ansvar för helheten.

---

# 5. Systemutvecklingsprocessen är bredare än kod – men evidensläget varierar

## Krav

En systematisk litteraturöversikt publicerad 2025/2026 omfattade 238 artiklar om generativ AI i requirements engineering. Forskningen var mest koncentrerad till analys och elicitering, medan management var betydligt mindre studerat. Återkommande problem var reproducerbarhet, hallucinationer och tolkningsbarhet. [K-015]

**Bokkonsekvens:** AI i kravarbete är tillräckligt etablerat som forskningsfält för att ingå, men boken ska inte låtsas att alla delar av kravprocessen har lika stark evidens.

## Arkitektur

En systematisk litteraturöversikt 2025 identifierade 18 studier om LLM:er i software architecture, bland annat klassificering av designbeslut, identifiering av mönster och generering av arkitektur från krav. Författarna konstaterar samtidigt att flera områden, exempelvis konformitetskontroll och cloud-native-arkitektur, är underutforskade. [K-016]

**Bokkonsekvens:** arkitekturexempel bör vara praktiska och väl avgränsade. Generella påståenden om kvalitetsvinster ska undvikas.

## Test

Forskningen om LLM-baserad testgenerering är omfattande och växande. En stor ACM-studie 2025 jämförde 37 modeller på tre unit-testing-uppgifter och fann lovande resultat, men också tydliga skillnader mellan uppgifter och metoder. [K-017] En ASE-studie 2025 använde ett dataset skapat efter modellernas träningsgränser och fann att LLM-genererade testorakel i genomsnitt nådde ungefär samma mutationspoäng som mänskligt skapade orakel i just den studien, men med tydliga begränsningar för komplexa orakel. [K-018]

**Bokkonsekvens:** test bör vara en fullvärdig del av exemplen, inte bara något AI-genererad kod "körs igenom" efteråt.

---

# 6. Organisation och orkestrering: lokal hastighet räcker inte

DORA:s 2025-rapport om AI-assisterad mjukvaruutveckling behandlar AI-införande som ett **systemproblem snarare än ett verktygsproblem**. Rapporten lyfter bland annat Value Stream Management och organisatoriska grundförmågor för att få lokala produktivitetsvinster att ge produktresultat i stället för nedströms kaos. [K-019]

Microsofts 2026-data visar att avancerade användare oftare arbetar i miljöer där AI-kvalitetsstandarder, mänskliga överlämningar och agentarbetsflöden dokumenteras och görs repeterbara. Rapporten framhåller också behovet av utvärderingsinfrastruktur när agentexekvering skalas upp. [K-003]

### Konsekvens för fas 7

"Orkestrera" bör definieras ännu tydligare som:

> att designa ett socio-tekniskt arbetsflöde med AI, människor, verktyg, behörigheter, kontrollpunkter, mätning och återkoppling.

Det är **inte** synonymt med "låt agenten göra allt".

---

# 7. Icke-publikt material: träning är bara en del av riskbilden

Researchen bekräftar att olika tjänster och planer har väsentligt olika databehandling. Därför ska boken undvika generella påståenden som "AI-tjänster tränar på det du skickar" eller "företags-AI sparar inget".

Exempel från aktuell dokumentation:

- OpenAI anger att data från ChatGPT Business/Enterprise/Edu och API inte används för modellträning som standard; API har separata retentionkontroller och vissa kvalificerade kunder kan använda Zero Data Retention. [K-020, K-027]
- Anthropic anger att data i kommersiella Claude for Work/API-tjänster inte används för att träna generativa modeller; retention skiljer mellan API och sparade konversationstjänster och Enterprise har konfigurerbara retentionperioder. [K-021]
- Google Workspace anger att Workspace-innehåll inte human-granskas eller används för generativ modellträning utanför kundens domän utan tillstånd. [K-022]
- Microsoft anger att prompts, svar och Graph-data i Microsoft 365 Copilot inte används för träning av foundation-modeller; interaktioner lagras samtidigt i Copilot-aktivitetshistorik och omfattas av Microsoft 365:s retention/compliance. Web-grounding kan generera sökfrågor som skickas till Bing. [K-023]
- GitHub skiljer mellan individuella Copilot-planer och Business/Enterprise. Business/Enterprise-data används inte för modellträning; individuella planer kan från 2026 använda interaktionsdata för träning om användaren inte väljer bort detta. Olika underliggande modellleverantörer har dessutom olika ZDR-/retentionsvillkor. [K-024]
- Vertex AI anger en avtalsmässig träningsrestriktion utan kundens tillstånd/instruktion. [K-025]
- AWS anger för Amazon Bedrock att grundmodellsleverantörer normalt inte får åtkomst till kundens prompts/completions, men aktuella retentionregler kan skilja mellan modeller och säkerhetslägen. [K-026]

### Konsekvens för kapitel 15

Kapitlets beslutsmodell ska skilja minst mellan:

1. **träning/förbättring av modeller**,  
2. **retention och loggning**,  
3. **support-/säkerhetsgranskning och administrativ åtkomst**,  
4. **data residency och underleverantörer**,  
5. **behörigheter till interna källor**,  
6. **connectors, webbsökning och externa verktygsanrop**,  
7. **vilket avtal och vilken kontotyp som faktiskt gäller**.

Alla produktspecifika uppgifter måste färskhetskontrolleras inför publicering.

---

# 8. Beslut om mognadsmodellen efter research

## Behåll

1. Fråga  
2. Resonera  
3. Skapa  
4. Samarbeta  
5. Ge kontext  
6. Delegera  
7. Orkestrera

## Justera modellens definition

Mognad ska framöver beskrivas med tre lager:

### A. Repertoar

Vilka arbetsformer kan användaren faktiskt använda: fråga, resonera, skapa, iterera, arbeta med verklig kontext, delegera och designa arbetsflöden?

### B. Situationsanpassning

Kan användaren välja **rätt nivå för rätt uppgift** utifrån risk, osäkerhet, kompetens, informationsklassning och reversibilitet?

### C. Kontroll

Kan användaren verifiera resultat, styra åtkomst och befogenheter, upptäcka när AI ligger utanför sin kapabilitetsgräns och mäta om arbetssättet ger bättre helhetsresultat?

Detta gör modellen mindre hierarkisk och bättre förenlig med det empiriska underlaget.

## Formulering som bör användas i boken

> De sju stegen i den här boken är inte en vetenskapligt etablerad mognadsskala. De är en pedagogisk syntes av observerade användningsmönster, forskning om människa–AI-samarbete och utvecklingen från chattbaserad assistans mot agentiska arbetsflöden. Du kan befinna dig på olika steg samtidigt, och mogen användning innebär framför allt att kunna välja rätt arbetssätt för uppgiften.

---

# 9. Researchfrågor som återstår inför respektive kapitel

Researchpass v1 räcker för att börja skriva inledning och kapitel 1–3. Följande kompletteringar bör göras just-in-time under manusarbetet:

- konkret forskning om hallucinationer/faktaverifiering för kapitel 1 och 5,
- ytterligare empiriska studier om kodbas-/repository-kontext för kapitel 8,
- coding-agent benchmark kontra verkligt arbete för kapitel 9–10,
- säkerhet för agentiska verktyg, prompt injection och tool-use för kapitel 15–16,
- aktuell EU-reglering och svensk vägledning endast där den behövs för informationshanteringskapitlet,
- färskhetskontroll av alla leverantörers dataskyddsvillkor nära publicering.

Research ska alltså fortsätta under skrivandet, men **bokens grundstruktur behöver inte göras om efter detta pass**.
