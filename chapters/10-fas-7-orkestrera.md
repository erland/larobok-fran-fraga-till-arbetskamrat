# Kapitel 10 – Fas 7: Orkestrera

När AI har blivit bra på att genomföra en flerledad uppgift uppstår lätt nästa tanke:

> Kan vi koppla ihop flera sådana uppgifter så att hela arbetsflödet hänger samman?

Det kan handla om en förändring i ett system:

> behov → analys → implementation → test → review → leveransunderlag

eller om arkitekturarbete:

> ny styrning → påverkansanalys → modelländring → konsekvensbedömning → granskningsunderlag

eller om kvalitet:

> ny pull request → riskanalys → riktad review → testanalys → mänskligt beslut

När AI inte längre används som ett separat verktyg vid enstaka tillfällen utan blir en medvetet designad del av **hur arbetet går till**, har vi nått fas 7:

**Orkestrera.**

## Orkestrering betyder inte många agenter

Det är viktigt att börja med en avgränsning.

Ordet orkestrering används ofta i tekniska diskussioner om flera AI-agenter som samarbetar. Det är en möjlig form, men i den här boken använder vi ordet bredare.

> **Orkestrering är att designa hur människor, AI, deterministisk automation, information och verktyg tillsammans för arbetet från ett mål till ett kontrollerat resultat.**

Ett orkestrerat arbetsflöde kan alltså innehålla:

- en enda AI-agent,
- flera specialiserade agenter,
- vanliga scripts och CI-jobb,
- sökning eller retrieval,
- mänskliga beslut,
- automatiska kvalitetsgrindar,
- manuella godkännanden.

Mognaden ligger inte i hur tekniskt avancerat flödet ser ut.

Den ligger i att **arbetsfördelningen är medveten och utvärderbar**.

Anthropic skiljer i sin tekniska vägledning mellan workflows, där modeller och verktyg följer fördefinierade vägar, och agentsystem där modellen mer dynamiskt bestämmer hur uppgiften ska genomföras. Deras rekommendation är att börja med den enklaste lösningen som fungerar och bara lägga till agentisk komplexitet när den faktiskt förbättrar resultatet. [K-046]

Det är leverantörsvägledning, inte en kontrollerad effektstudie.

Men principen är viktig för vår mognadsmodell:

> **Fas 7 är inte "mer agent". Fas 7 är bättre systemdesign för AI-assisterat arbete.**

## Skillnaden mellan delegering och orkestrering

I fas 6 kunde du säga:

> Implementera storyn, kör relevanta tester och stanna före commit.

Du delegerade en avgränsad uppgift.

I fas 7 tänker du i stället på hur den typen av uppgift passar in i ett större flöde.

Exempel:

1. ett förändringsbehov registreras,
2. AI sammanställer berörd funktionalitet och öppna frågor,
3. en människa bekräftar scope,
4. AI analyserar repositoryt och föreslår förändringsplan,
5. arkitekturpåverkan kontrolleras,
6. AI implementerar i en branch,
7. tester körs deterministiskt,
8. AI analyserar diff och testresultat,
9. en människa gör slutlig review,
10. leveransunderlag genereras.

Det avgörande är inte att AI förekommer i många steg.

Det avgörande är att någon har tänkt igenom:

- vilka steg som behövs,
- vad varje steg får göra,
- vilken kontext som flyttas vidare,
- var fel ska stoppas,
- vilka beslut som är mänskliga,
- hur resultatet mäts.

Delegering frågar:

> **Hur ska AI genomföra den här uppgiften inom våra gränser?**

Orkestrering frågar:

> **Hur ska hela arbetssystemet vara utformat så att AI används där det ger värde och kontrolleras där det behövs?**

## Automatisera inte det oklara

Det finns en frestande väg till fas 7:

Ta ett befintligt manuellt flöde och automatisera varje steg.

Det kan vara helt fel angreppssätt.

Om processen innehåller:

- oklara mål,
- dubbla ansvar,
- beslut som ingen egentligen äger,
- dokument som inte hålls uppdaterade,
- tester utan tydlig koppling till risk,
- granskningssteg som bara är ritual,

så kan AI göra processen snabbare utan att göra den bättre.

I värsta fall får organisationen ett system som producerar felaktiga resultat snabbare, mer konsekvent och i större volym.

Därför bör en mogen orkestrering börja med frågan:

> **Vilket utfall behöver processen skapa, och vilka kontroller behövs för att vi ska lita på utfallet?**

Först därefter kommer frågan om vad AI kan automatisera.

## Fyra sorters steg i ett moget flöde

Ett praktiskt sätt att designa ett AI-assisterat arbetsflöde är att inte behandla alla steg likadant.

För att hålla isär olika arbetsflöden skiljer boken mellan fyra typer. Indelningen är **bokens egen syntes**.

### Deterministiska steg

Utfallet bör följa tydliga regler och behöver inte kreativt resonemang.

Exempel:

- kompilera kod,
- köra formattering,
- exekvera definierade tester,
- kontrollera schema,
- verifiera att obligatoriska filer finns.

Det är ofta bättre att låta vanlig programvara göra detta än att be en språkmodell improvisera.

### AI-bedömda steg

Här behövs tolkning, sammanvägning eller arbete med ostrukturerat material.

Exempel:

- identifiera möjliga kravkonflikter,
- sammanfatta en större diff,
- föreslå riskområden för review,
- jämföra arkitekturalternativ.

AI ger ett underlag, men behöver inte få handlingsrätt.

### Delegerade agentsteg

Här får AI både resonera och agera inom delegationsbudgeten från föregående kapitel.

Exempel:

- göra en avgränsad kodändring och köra tester,
- uppdatera flera sammanhängande dokument,
- analysera en modell och skapa ett ändringsförslag.

### Mänskliga beslutspunkter

Vissa steg bör vara mänskliga därför att de innehåller ansvar, värdering eller konsekvenser som inte kan reduceras till en automatisk kontroll.

Exempel:

- acceptera ett arkitekturtrade-off,
- besluta att känslig information får behandlas på ett visst sätt,
- godkänna en breaking change,
- välja mellan motstridiga verksamhetsmål,
- göra slutligt produktionsgodkännande i ett högriskflöde.

Ett moget arbetsflöde använder alltså inte AI överallt.

Det använder **rätt typ av steg på rätt plats**.

## Arbetsflödeskontraktet

När orkestreringen blir återkommande räcker det inte längre att varje enskild delegation är bra formulerad.

Vi behöver kunna beskriva själva systemet.

Som stöd använder boken därför ett **arbetsflödeskontrakt**. Det är en egen pedagogisk modell med sex delar.

### 1. Trigger och mål

Vad startar flödet, och vilket utfall ska det skapa?

Exempel:

> En godkänd story flyttas till "Ready for implementation". Flödet ska resultera i ett granskningsbart ändringsförslag med tester och dokumenterad påverkan – inte automatiskt i produktionssättning.

Det skiljer aktivitet från utfall.

### 2. State och kontext

Vilken information behöver följa med mellan stegen?

- story och acceptanskriterier,
- repositoryversion,
- tidigare beslut,
- testresultat,
- identifierade risker,
- vad en människa redan har godkänt.

Om state är otydligt kan varje nytt AI-steg börja om från en annan verklighetsbild.

### 3. Roller och steg

Vilka delar är deterministiska, AI-bedömda, delegerade eller mänskliga?

Här avgörs också om en enda agent räcker eller om specialisering faktiskt behövs.

### 4. Handoffs och kontrollpunkter

När får resultat gå vidare?

Exempel:

- kravkonflikt → människa,
- testfel → tillbaka till implementation,
- säkerhetskritisk fil ändrad → obligatorisk specialistreview,
- oklar informationsklassning → stopp.

En kontrollpunkt är värdefull när den stoppar ett meningsfullt riskförlopp, inte bara för att "human in the loop" låter tryggt.

### 5. Observability

Kan vi förstå vad som hände?

Ett agentiskt arbetsflöde kan göra hundratals små beslut före slutresultatet. Om vi bara sparar den sista texten blir felsökning och ansvar svårt.

Vi behöver, i den grad uppgiften motiverar det, kunna se exempelvis:

- vilket mål som användes,
- vilken kontext agenten läste,
- vilka verktyg som anropades,
- vilka filer eller objekt som ändrades,
- vilka handoffs som gjordes,
- vilka kontroller som passerades,
- vilken modell- och instruktionsversion som användes.

NIST:s arbete med transcript analysis för agentutvärderingar illustrerar varför detta blir viktigare när agentbanor blir längre: man behöver kunna analysera själva förloppet, inte bara slutresultatet. [K-049]

### 6. Evals och förbättringsloop

Hur vet vi att flödet fortsätter fungera?

Det räcker inte att det fungerade i demonstrationen.

Modeller uppdateras. Instruktioner ändras. Verktyg får nya versioner. Repositoryt växer. Processer förändras.

Därför behöver mogna arbetsflöden någon form av återkommande utvärdering.

Anthropic beskriver agent-evals som särskilt viktiga eftersom agenten arbetar över flera steg, använder verktyg och förändrar state. Fel kan alltså uppstå på flera ställen innan slutresultatet syns. [K-047]

NIST:s utkast om automatiserad benchmarkutvärdering betonar på motsvarande sätt validitet, transparens och reproducerbarhet i evalueringar av språkmodeller och agentiska system. [K-048]

Det innebär inte att varje internt AI-flöde behöver ett forskningslaboratorium.

Men vi behöver ett svar på frågan:

> **Vad skulle få oss att upptäcka att arbetsflödet blivit sämre?**

## Två nivåer av kvalitet

När du arbetar i fas 1–6 granskar du framför allt resultatet av en aktuell AI-användning.

I fas 7 behöver du granska på två nivåer.

### Körningskvalitet

Blev den här konkreta körningen bra?

- var analysen korrekt?
- höll ändringen scope?
- gick testerna igenom?
- följdes kontrollpunkterna?
- blev slutresultatet användbart?

### Systemkvalitet

Är arbetsflödet fortfarande bra som system?

- leder det till färre eller fler fel över tid?
- skapar det onödigt mycket reviewarbete?
- har människor börjat klicka igenom godkännanden rutinmässigt?
- kostar koordineringen mer än den sparar?
- finns steg som borde vara deterministiska i stället för AI-baserade?
- har modellen eller verktyget förändrats så att gamla evals inte längre räcker?

Det är här orkestrering skiljer sig från en samling smarta prompts.

Du förvaltar inte bara output.

Du förvaltar **ett arbetssystem**.

## När flera agenter faktiskt kan vara motiverade

Multi-agent är attraktivt eftersom det liknar hur människor organiserar specialistarbete.

En agent analyserar krav.

En annan arkitektur.

En tredje kod.

En fjärde granskar.

Det kan fungera.

Anthropic beskriver exempelvis ett orchestrator–workers-mönster där en central modell dynamiskt delar upp en komplex uppgift och låter andra modeller arbeta med delarna. [K-046]

Men fler agenter innebär också:

- fler handoffs,
- mer kontext som kan tappas,
- större token- och kostnadsåtgång,
- fler felkällor,
- mer logging,
- svårare felsökning.

Den växande forskningen om multi-agent-system i software engineering pekar just på sådana trade-offs. En empirisk jämförelse av agentramverk fann bland annat skillnader i task success, tokenkostnad, trajectory-längd och koordinationsöverhead. [K-051]

En annan mixed-method-studie från 2026 fann att flera ramverk täckte grundläggande multi-agent-funktioner väl men att mer avancerad telemetry fortfarande saknades i delar av ekosystemet. I deras gemensamma summariseringsuppgift gav multi-agent-uppläggen inte någon signifikant skillnad i det använda ROUGE-måttet. [K-050]

Det betyder inte att multi-agent är dåligt.

Det betyder att **antalet agenter inte är ett mognadsmått**.

Använd flera när specialisering, parallellism eller tydlig arbetsdelning ger ett verifierbart värde.

Inte för att arkitekturen ser avancerad ut på en bild.

## Ett exempel genom hela utvecklingsprocessen

Anta att ett team ska införa ett nytt leveranssätt i en befintlig e-handelstjänst.

Ett orkestrerat flöde skulle kunna se ut så här.

### Behov och krav

AI sammanställer storyn mot befintliga verksamhetsregler och markerar konflikter.

En människa beslutar om scope där reglerna är otydliga.

### Arkitektur

AI jämför förändringen mot relevanta ADR:er och identifierar om ett tidigare designbeslut påverkas.

Om arkitekturprinciperna motsäger föreslagen lösning stoppas flödet för arkitektbeslut.

### Implementation

En coding agent får den godkända storyn, repositorykontext och tydlig delegationsbudget.

Den gör ändringen i en branch.

### Test

Vanliga tester körs deterministiskt.

AI analyserar dessutom om acceptanskriterier och diff antyder testluckor.

### Review

AI sammanfattar riskområden och vad den faktiskt förändrat.

En människa reviewar diffen, med extra kontroll där flödet markerat hög risk.

### Leveransunderlag

Dokumentation och releaseunderlag uppdateras från det faktiska resultatet, inte från den ursprungliga planen.

Poängen är inte att detta specifika flöde är rätt för alla team.

Poängen är att varje övergång har **ett syfte, ett ansvar och ett sätt att stoppa fel**.

## Orkestrering behöver observability, inte bara dashboards

Ordet observability kan låta som ännu ett tekniskt lager.

Men grundfrågan är enkel:

> Om resultatet blir fel, kan vi förstå varför?

För ett traditionellt script kan det räcka med loggar och exit codes.

För ett agentiskt flöde kan orsaken ligga i att:

- fel dokument hämtades,
- en gammal instruktion vägde tyngre än en ny,
- agenten valde fel verktyg,
- en subagent missförstod handoffen,
- en människa godkände ett otillräckligt underlag,
- en modelluppdatering ändrade beteendet.

NIST arbetar 2026 med så kallade evaluation probes och traceability i agentiska system, särskilt för situationer där faktagrundning och spårbarhet är kritiska. [K-054]

Det är ett pågående forsknings- och standardiseringsområde, inte en färdig universallösning.

Men riktningen är viktig:

När AI går från en dialog till ett arbetssystem behöver vi kunna observera **hur resultatet kom till**.

## Evals är arbetsflödets tester

Liknelsen ska inte dras för långt, men den är användbar.

Utvecklare skulle sällan vilja förvalta ett komplext system utan tester.

På samma sätt är det riskabelt att förvalta ett viktigt agentiskt arbetsflöde utan återkommande exempel som visar om det fortfarande beter sig acceptabelt.

Ett evalset kan exempelvis innehålla:

- normala uppgifter,
- tvetydiga uppgifter,
- saknad kontext,
- motstridiga instruktioner,
- verktygsfel,
- högriskfall där agenten ska eskalera,
- historiska incidenter som inte får återkomma.

Bra evals behöver inte alltid ge ett enda numeriskt betyg.

För vissa delar kan svaret vara deterministiskt:

- skrev agenten till förbjuden miljö?
- kördes obligatoriska tester?
- eskalerades säkerhetskritisk ändring?

För andra behövs mänsklig eller modellstödd kvalitetsbedömning.

Det centrala är att kvaliteten blir **något vi aktivt mäter**, inte bara något vi hoppas på.

## Fas 7 är inte slutmålet för varje uppgift

Efter sju kapitel kan modellen lätt uppfattas som en trappa där den mogna användaren alltid ska stå högst upp.

Det är inte bokens budskap.

I morgon kan samma erfarna person använda:

- fas 1 för en syntaxfråga,
- fas 2 för ett arkitekturresonemang,
- fas 4 för att iterera en viktig text,
- fas 5 för att analysera ett känsligt projekt i en godkänd miljö,
- fas 6 för en reversibel kodförändring,
- fas 7 för ett välförstått återkommande arbetsflöde.

Mognaden ligger i repertoaren och valet.

Inte i att alltid välja den mest autonoma formen.

## Så tar du nästa steg

Om du redan delegerar uppgifter till AI behöver nästa experiment inte vara ett stort agentprojekt.

Välj ett **återkommande flöde med tydligt resultat** och kartlägg det först utan teknik.

Svara på sex frågor:

1. Vad triggar flödet och vad ska det åstadkomma?
2. Vilken state och kontext måste följa med?
3. Vilka steg bör vara deterministiska, AI-assisterade, delegerade respektive mänskliga?
4. Var ska handoffs och stoppunkter ligga?
5. Vad behöver loggas för att vi ska förstå fel?
6. Hur ska vi märka att kvaliteten försämras över tid?

Automatisera sedan **en liten del** där nyttan är tydlig och reversibiliteten hög.

Mät vad som händer innan du bygger vidare.

Det är ett betydligt mognare steg än att börja med fem agenter och hoppas att de organiserar sig själva.

## När du inte bör gå vidare

Stanna i fas 6 eller tidigare när:

- arbetsflödet är sällsynt eller snabbt förändras,
- målet och ansvarsfördelningen fortfarande är oklara,
- varje ärende kräver unika mänskliga beslut,
- processens största problem inte är genomförandet utan prioritering eller styrning,
- evals saknas för ett högriskflöde,
- observability är så svag att fel inte går att förstå,
- koordinationskostnaden överstiger nyttan,
- AI skulle automatisera en process som först borde förenklas eller tas bort.

Orkestrering är alltså inte slutpunkten där människan lämnar arbetet.

Det är punkten där människans uppgift förändras från att bara **göra och granska enskilda aktiviteter** till att också **designa, begränsa och förbättra det system där aktiviteterna utförs**.

Det är vad moget AI-assisterat arbete börjar likna.
