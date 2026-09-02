# Researchresultat v4 – Kontext, delegation, verktyg och människa-i-loopen

## Syfte

Detta just-in-time-pass stödjer kapitel 8–9: **Fas 5: Ge kontext** och **Fas 6: Delegera**. Fokus är repository- och dokumentkontext, hur agenter hittar relevant information, flerledade uppgifter, verktygsanvändning, människa-i-loopen och hur riskbilden förändras när AI får både mer information och större handlingsutrymme.

Researchpasset behåller sjufasmodellen, men preciserar två saker:

- Kontext är inte värdefull bara för att den är stor. **Relevant, tillförlitlig och avgränsad kontext** är det som minskar behovet av generiska antaganden.
- Delegering är inte synonymt med autonomi. **Mogen delegering kombinerar mål, constraints, verktygsgränser, kontrollpunkter och verifiering.**

## Huvudfynd

### 1. Kontextinhämtning är en egen svår del av agentiskt kodarbete

Agent Retrieval Bench från 2026 bygger 427 retrievaluppgifter från 25 repositories och visar att det inte finns en enda retrievalmetod som dominerar över alla typer av repositoryfrågor. Loggade agentbanor missade dessutom samtliga relevanta "gold files" i 27–35 procent av exemplen. Studien är en preprint och ska inte användas som universell felfrekvens, men den stödjer en viktig mekanism: ett agentiskt system kan misslyckas redan innan kodgenereringen börjar, genom att välja fel kontext. [K-041]

Konsekvens för boken: fas 5 ska inte beskrivas som "ge AI allt" utan som att **göra rätt arbetskontext tillgänglig och kontrollera vad AI faktiskt bygger sitt resonemang på**.

### 2. Specialistagenter används betydligt mer för automation/delegering än chattgränssnitt

Anthropics analys av 500 000 kodrelaterade interaktioner fann att 79 procent av Claude Code-interaktionerna klassificerades som automation, jämfört med 49 procent på Claude.ai. "Directive"-mönstret – komplett uppgiftsdelegering med minimal interaktion – var 43,8 procent i Claude Code mot 27,5 procent i Claude.ai. Samtidigt var feedback-loopar vanliga, vilket visar att delegering och mänsklig återkoppling kan samexistera. [K-005]

Konsekvens för boken: fas 6 kan beskrivas som ett tydligt observerbart arbetssätt, men inte som "människan försvinner ur loopen".

### 3. Mer avancerade användare väljer arbetsform, de maximerar inte autonomi

Microsofts Work Trend Index 2026 skiljer mellan asking, exploration, collaboration och delegation. De mest avancerade användarna använder agenter för multi-step workflows och pausar oftare för att avgöra vad som bör göras av människa respektive AI. 53 procent uppgav detta jämfört med 33 procent bland övriga användare. Rapporten är leverantörsproducerad och bygger bland annat på självrapporterad surveydata, men mönstret stödjer bokens definition av mognad som situationsanpassning. [K-003]

### 4. Agenternas förmåga att slutföra längre uppgifter ökar, men "tidshorisont" är inte samma sak som säker autonom drifttid

METR mäter den uppgiftslängd – uttryckt som hur lång tid mänskliga experter behöver – där en agent förväntas lyckas med en viss sannolikhet. METR betonar uttryckligen att detta inte är samma sak som hur länge en agent kan eller bör köras autonomt. Mätserien visar att frontiermodellers förmåga att slutföra längre mjukvaruuppgifter har ökat kraftigt över tid. [K-042]

Konsekvens för boken: kapitel 9 kan använda detta som belägg för att flerledade uppgifter blir praktiskt relevanta, men ska undvika formuleringar som "agenter kan arbeta självständigt i X timmar".

### 5. Verktygsbehörighet är en central del av agentrisken

NIST beskriver agentverktyg längs dimensioner som read-only, constrained write och write samt trusted kontra untrusted environments. Detta gör det möjligt att resonera om handlingsutrymme som något mer konkret än "autonomi". [K-043]

OWASP:s vägledning om Excessive Agency identifierar tre grundorsaker till skadliga agenthandlingar: för mycket funktionalitet, för stora behörigheter och för mycket autonomi. Rekommenderade åtgärder inkluderar minsta privilegium, begränsade verktyg och mänskligt godkännande för högpåverkande åtgärder. [K-044]

Konsekvens för boken: fas 6 ska introducera **delegationsbudgeten** – ett eget pedagogiskt begrepp för vilka verktyg, data, behörigheter, kostnader, tidsramar och irreversibla åtgärder agenten får disponera.

### 6. Människa-i-loopen är viktig men inte en magisk säkerhetsbarriär

NIST:s arbete om agent hijacking visar att indirekt prompt injection kan få en agent att följa instruktioner som ligger inbäddade i material agenten läser. Detta är särskilt relevant när agenten kombinerar webbläsning, dokumentläsning och verktyg med skrivbehörighet. [K-045]

OWASP:s senare säkerhetsvägledning betonar också att human-in-the-loop behöver kombineras med least privilege, validering, isolering och logging. Ett godkännandefönster som i sig bygger på manipulerad kontext kan ge falsk trygghet. [K-044]

Konsekvens för boken: "kräv godkännande" ska beskrivas som en kontroll bland flera, inte som tillräckligt skydd i sig.

## Konsekvenser för kapitel 8 – Ge kontext

1. Kontext ska delas upp i:
   - uppgiftskontext,
   - projektkontext,
   - historik/beslut,
   - regel-/policykontext,
   - miljö-/runtimekontext.
2. Kapitlet ska skilja mellan **mer kontext** och **bättre kontext**.
3. Läsaren ska lära sig kontrollera:
   - vad AI faktiskt har läst,
   - vad som saknas,
   - vilka källor/artefakter som styr slutsatsen,
   - om materialet är aktuellt och auktoritativt.
4. Kontextförorening ska introduceras: gammal dokumentation, motstridiga instruktioner, irrelevant data och attackerande innehåll kan försämra resultatet.
5. Informationsklassning introduceras här som första tröskel, medan kapitel 15 gör full fördjupning.

## Konsekvenser för kapitel 9 – Delegera

1. Fasgränsen sätts vid **målbaserad flerledad uppgift** snarare än antalet prompts.
2. Delegering ska beskrivas med fyra komponenter:
   - mål,
   - constraints,
   - handlingsutrymme,
   - verifiering.
3. Boken inför **delegationsbudgeten** som egen syntes:
   - data,
   - verktyg,
   - behörigheter,
   - tid/kostnad,
   - irreversibla åtgärder.
4. Kontrollpunkter ska placeras efter risk och reversibilitet, inte efter ett godtyckligt antal steg.
5. Läsaren ska skilja mellan:
   - läsande agent,
   - förändrande agent,
   - exekverande agent,
   - publicerande/externverkande agent.
6. Högre autonomi ska aldrig presenteras som självändamål.

## Evidensmässig försiktighet

- Produkttelemetri från Anthropic och Microsoft visar hur deras användare arbetar, inte hur alla AI-användare arbetar.
- Agent Retrieval Bench är en preprint från 2026 och används som stöd för mekanismen att retrieval är svårt, inte som universell felfrekvens.
- METR:s time horizon mäter uppgiftssvårighet i relation till mänsklig arbetstid, inte säker eller faktisk autonom körtid.
- Säkerhetsvägledning från NIST och OWASP är normativ/teknisk vägledning, inte effektstudier av en viss kontroll.

## Slutsats

Researchpasset stärker övergången mellan fas 5 och 6. **Fas 5 handlar om att göra verklig, relevant arbetskontext tillgänglig och spårbar. Fas 6 handlar om att låta AI använda denna kontext för att driva en flerledad uppgift mot ett mål inom tydliga gränser.**

Det centrala mognadsskiftet är därför inte "mer data" följt av "mer autonomi", utan **bättre kontext följt av bättre designad delegation**.
