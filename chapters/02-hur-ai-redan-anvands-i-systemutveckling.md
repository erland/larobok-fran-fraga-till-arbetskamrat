# Kapitel 2 – Hur AI redan används i systemutveckling

De mest entusiastiska rösterna ger lätt en skev bild av AI-användningen. I vissa utvecklarforum kan det låta som om nästan all kod redan skrivs av agenter. I andra miljöer kan det verka som om professionella utvecklare knappt använder AI alls.

Mätningar från 2025–2026 visar en mer blandad verklighet: användningen är hög, men förtroendet är betydligt lägre; enklare och individuella aktiviteter ligger längre fram än systemiska aktiviteter; och agentiskt arbete är växande men fortfarande långt ifrån universellt.

Det är en bra utgångspunkt för en bok om mognad. Människor befinner sig uppenbart på olika nivåer – ibland samtidigt.

## Hög användning, lägre tillit

**Mätdata – utvecklarenkät:** Stack Overflows Developer Survey 2025 hade över 49 000 svar från 177 länder. På frågan om AI-verktyg i utvecklingsprocessen svarade 84 procent att de använde eller planerade att använda sådana verktyg. Bland professionella utvecklare uppgav 51 procent daglig användning. [K-007]

Det är en mycket hög användningsnivå.

Men samma enkät visar något minst lika viktigt. 46 procent uppgav att de aktivt **inte litade** på riktigheten i AI-verktygens resultat, medan 33 procent uppgav tillit. Endast 3 procent angav hög tillit. Erfarna utvecklare var de mest försiktiga. [K-007]

Detta skapar en intressant situation:

> Ett verktyg kan vara så användbart att det används varje dag och samtidigt så opålitligt att användaren inte vill acceptera resultatet utan kontroll.

Det är inte en paradox. Det är precis så många professionella verktyg fungerar. En statisk analys kan ge falska positiva. En extern konsult kan ha fel. En junior kollega kan bidra enormt men behöva review. Skillnaden är att generativ AI kan producera mycket material mycket snabbt, vilket gör verifieringsfrågan mer central.

## Vilka uppgifter kommer först?

Stack Overflows data visar att utvecklare är mest bekväma med AI i aktiviteter som informationssökning, lärande och vissa delar av kod- och dokumentationsarbetet. Motståndet är betydligt större för aktiviteter med större systemansvar. I 2025 års enkät svarade 76 procent att de inte planerade att använda AI för deployment och monitoring, och 69 procent sade detsamma om projektplanering. [K-007]

Detta är enkätdata om intentioner och användning, inte ett bevis för att vissa aktiviteter objektivt lämpar sig bättre. Men mönstret är logiskt.

Ju mer en aktivitet:

- påverkar produktionsmiljön,
- kräver organisatorisk koordinering,
- innehåller svårkodad domänkunskap,
- har hög konsekvens vid fel,
- eller saknar enkel automatisk verifiering,

desto svårare blir det att delegera den tryggt.

Det betyder att mognadsresan inte bara styrs av modellernas kapabilitet. Den styrs också av **verifierbarhet och risk**.

## Kodning dominerar bilden – men inte hela arbetet

Generativ AI blev tidigt starkt förknippad med kodkomplettering och kodgenerering. Det är förståeligt: programmering har tydliga artefakter, mycket träningsmaterial och många automatiska kontrollmekanismer.

Men systemutveckling består av betydligt mer än att producera kod.

Krav ska förstås och förfinas. Arkitekturbeslut ska vägas mot begränsningar. Teststrategier ska prioritera risk. Dokumentation ska hållas konsistent med implementation. Incidenter ska analyseras. Releaseunderlag ska skapas. Team behöver förstå varandras ändringar.

Forskningen om AI i dessa områden är ojämnt utvecklad, men den finns.

En systematisk litteraturöversikt om generativ AI i requirements engineering identifierade 238 artiklar och fann särskilt mycket arbete kring analys och elicitering, samtidigt som reproducerbarhet, hallucinationer och utvärderingskvalitet återkom som problem. [K-015]

En systematisk översikt om språkmodeller i software architecture hittade däremot bara 18 relevanta studier i sitt material, vilket visar att evidensbasen är betydligt mindre. [K-016]

Detta är en viktig metodprincip för resten av boken: vi kommer inte behandla ”AI för systemutveckling” som ett enhetligt forskningsfält. För vissa aktiviteter finns stora studier. För andra finns mest prototyper, små experiment eller praktisk erfarenhet.

## Testning: en naturlig men inte enkel AI-uppgift

Test är ett intressant område eftersom det både är produktions- och kontrollarbete.

AI kan generera testfall, testdata, assertions och förslag på edge cases. Samtidigt kan AI-genererade tester bli meningslösa om de bara bekräftar den implementation som AI:n själv nyss skapade.

Stora empiriska studier har börjat undersöka modellernas förmåga till unit testing mer systematiskt. En peer-reviewad studie publicerad i samband med ISSTA 2025 jämförde 37 modeller och undersökte bland annat testgenerering, assertions och test-evolution. [K-017] Annan forskning har explicit försökt skapa tidsmässigt obiaserade dataset för att minska risken att modeller redan sett samma testmaterial under träningen. [K-018]

Detta är ett exempel på varför forskningsmetoden spelar roll. En modell kan se imponerande ut på ett benchmark och ändå ha svårare för en ny, domänspecifik kodbas.

## Från augmentation till automation

Anthropic har analyserat stora mängder interaktioner i sina egna produkter och skiljer bland annat mellan *augmentation*, där människan och AI:n arbetar tillsammans, och *automation*, där AI:n tar en större del av uppgiften. I en analys av programvaruutveckling 2025 noterade Anthropic att coding-agent-interaktioner innehöll mer automation än vanlig chattanvändning. [K-005]

Detta är leverantörens egen produktdata, inte oberoende forskning. Men den fångar ett tydligt produktmönster: när AI flyttar från chattfönster till verktyg som kan läsa repositoryn, ändra filer och köra kommandon blir **delegering** mer praktiskt genomförbar.

Samma utveckling syns i andra leverantörers produkter och i den bredare marknaden för kodningsagenter.

Det är en av orsakerna till att vår mognadsmodell skiljer på *Samarbeta*, *Ge kontext* och *Delegera*. Ett långt samtal om kod är inte samma sak som att ge AI tillgång till kodbasen, och det är inte samma sak som att låta AI genomföra ändringen.

## Agenter är synliga – men ännu inte normen

AI-agenter får oproportionerligt mycket uppmärksamhet eftersom de representerar den mest dramatiska formen av automation. Men användningsdata från utvecklare visar att de fortfarande är en minoritetsarbetsform.

I Stack Overflows 2025-enkät uppgav en majoritet att de antingen inte använde agenter eller höll sig till enklare AI-verktyg. 38 procent hade inga planer på agentanvändning. Samtidigt rapporterade de som faktiskt använde agenter ofta positiva individuella effekter: omkring 69 procent av agentanvändarna ansåg att de ökat produktiviteten. Däremot var förbättrad teamsamverkan mycket mindre vanligt rapporterad; endast 17 procent höll med om den effekten. [K-007]

Detta är självrapporterade effekter, inte objektivt uppmätt produktivitet. Men skillnaden mellan individ och team är intressant.

Ett verktyg kan göra en person snabbare utan att göra värdeflödet snabbare.

Om en utvecklare producerar fler kodändringar men review, testmiljö, releaseprocess eller kravförtydligande blir flaskhalsar, kan lokal hastighet rentav skapa mer kö och omarbete.

Detta blir centralt i kapitel 3 och återkommer när vi senare diskuterar orkestrering.

## AI-användning breddas över tid

**Mätdata – leverantörstelemetri:** OpenAI:s Signals-data från individuella ChatGPT-konton visar att användare efter sex månader skickade ungefär 50 procent fler meddelanden per dag och hade provat dubbelt så många uppgiftstyper jämfört med sin första period. Datamängden bygger på ett urval av konton skapade mellan oktober 2025 och maj 2026. [K-001]

Detta stödjer idén att människor utvecklar en större repertoar med tiden.

Men man ska vara försiktig med tolkningen. Att prova fler uppgifter betyder inte automatiskt att arbetssättet blivit bättre. En person kan bredda sin användning utan att bli bättre på verifiering eller informationshantering.

Bokens mognadsbegrepp är därför starkare än ”använder AI till fler saker”.

Vi kommer kräva tre komponenter:

- större repertoar,
- bättre situationsanpassning,
- bättre kontroll.

## Från att fråga till att göra

OpenAI har i en senare analys beskrivit en övergripande förskjutning från *asking* mot *doing* i arbetsrelaterad användning av ChatGPT. [K-002] Anthropic har på motsvarande sätt beskrivit ökande automation och längre agentiska arbetssekvenser i sin produktdata. [K-005, K-006]

Eftersom båda källorna kommer från AI-leverantörer bör de inte ensamma användas som bevis för en allmän samhällsutveckling. De har kommersiella skäl att uppmärksamma mer avancerad användning.

Men när samma riktning också syns i produktutvecklingen – fler verktygsintegrationer, kodningsagenter, dokumentåtkomst och flerledade arbetsflöden – är det rimligt att betrakta förskjutningen som verklig, även om hastigheten varierar kraftigt mellan användare och organisationer.

Detta är bakgrunden till bokens titel: **från fråga till arbetskamrat**.

## En utvecklare, en testare och en arkitekt kan vara lika mogna

Det är viktigt att inte förväxla tekniskt avancerad användning med mognad.

En utvecklare kan använda en kodningsagent som gör stora förändringar autonomt men acceptera resultatet utan ordentlig review. En testare kan använda en vanlig chatt men arbeta mycket metodiskt: ge rätt kontext, be om alternativa riskhypoteser, verifiera varje påstående mot krav och använda AI:n som en kontrollerad del av testdesignen.

Vem är mest mogen?

I bokens modell är svaret inte självklart utvecklaren.

Mognad handlar inte om hur imponerande verktyget ser ut. Den handlar om kvaliteten i arbetsfördelningen.

## Erfarenhet påverkar nyttan

Flera studier utanför ren systemutveckling visar att mindre erfarna personer ibland får större produktivitetsvinster av generativ AI än experter.

Den peer-reviewade studien *Generative AI at Work* analyserade införandet av en AI-assistent hos 5 172 kundsupportmedarbetare. I den publicerade versionen ökade produktiviteten i genomsnitt med 15 procent, men vinsterna var betydligt större för mindre erfarna och lägre presterande medarbetare. De mest erfarna fick små hastighetsvinster och i vissa fall små kvalitetsförsämringar. [K-012]

Det är inte en studie av utvecklare och resultatet kan inte flyttas över direkt till kodarbete. Men det illustrerar en viktig mekanism: AI kan fungera som ett sätt att göra erfarenhetsbaserade arbetsmönster mer tillgängliga för den som ännu inte hunnit bygga upp samma repertoar själv.

I tre randomiserade experiment med utvecklare såg forskarna också större adoption och större produktivitetsvinster för mindre erfarna utvecklare. [K-008]

Detta kan vara en förklaring till varför expertanvändare ibland beskriver mindre dramatisk nytta av enkla AI-funktioner: de hade redan verktygen i huvudet.

Men expertens potentiella värde kan i stället ligga i högre steg – att använda AI för större informationsmängder, alternativanalys, automatiserad verifiering eller flerledat utförande.

## Privat experimenterande och organisatoriskt arbete är olika saker

En individ kan börja använda ett konsumentkonto på några minuter. Organisatorisk användning är mer komplex.

När AI ska arbeta med icke-publikt material uppstår frågor om:

- vilka konton och avtal som får användas,
- om materialet kan användas för modellträning,
- hur länge data lagras,
- vilka underleverantörer som behandlar den,
- vilka interna informationskällor AI:n får komma åt,
- hur actions och verktygsanrop styrs,
- hur resultat granskas och spåras.

Det betyder att individens mognad ibland springer före organisationens förmåga att stödja arbetssättet.

En utvecklare kan veta exakt hur en AI-agent skulle kunna hjälpa till i ett repository, men organisationen kanske ännu inte har en godkänd lösning för att ge agenten tillgång till källkoden. En arkitekt kan vilja analysera styrande dokument tillsammans men sakna en tjänst med rätt avtals- och informationshantering.

Detta gap är i sig en viktig del av AI-mognaden.

## DORA: AI-införande som systemproblem

DORA:s 2025-rapport om AI-assisterad mjukvaruutveckling argumenterar för att framgångsrikt AI-införande är ett **systemproblem, inte bara ett verktygsproblem**. Rapporten betonar bland annat värdeflöde och organisatoriska grundförmågor för att lokala produktivitetsvinster ska ge bättre produktresultat i stället för nedströms problem. [K-019]

DORA är en leverantörsfinansierad forskningsrapport från Google, så även här ska avsändaren vara synlig. Men perspektivet ligger nära etablerad kunskap inom mjukvaruleverans: optimering av en enskild aktivitet förbättrar inte nödvändigtvis systemets genomlopp.

Det är särskilt viktigt när AI ökar produktionskapaciteten snabbare än review-, test- eller beslutskapaciteten.

## Vad säger användningsmönstret om mognadsresan?

När vi lägger samman dessa observationer får vi inte en exakt sjufasmodell. Men vi får ett tydligt mönster:

1. **AI är redan vardagsverktyg för många utvecklare.** [K-007]
2. **Förtroendet släpar efter användningen.** [K-007]
3. **Informations- och produktionsnära uppgifter ligger längre fram än systemiskt ansvar.** [K-007]
4. **Användningen tenderar att breddas med erfarenhet.** [K-001]
5. **Produkter och användning rör sig från chatt mot agentiskt utförande.** [K-005, K-006]
6. **Individuell nytta och team-/systemnytta är inte samma sak.** [K-007, K-019]

Detta räcker för att motivera bokens huvudfråga: hur tar man sig vidare på ett sätt som ger mer nytta utan att samtidigt tappa kontroll?

## En enkel självdiagnos

Tänk på din egen AI-användning de senaste två veckorna.

Vilka av dessa påståenden stämmer?

- Jag använder AI främst för fakta- och syntaxfrågor.
- Jag ber ofta AI jämföra alternativ eller kritisera mina idéer.
- Jag låter AI skapa första utkast till konkreta arbetsartefakter.
- Jag arbetar iterativt med AI över flera rundor.
- Jag ger AI tillgång till verkliga projektfiler eller repositoryn.
- Jag delegerar flerledade uppgifter med tydliga mål och begränsningar.
- Jag har designade arbetsflöden där AI, verktyg och mänskliga kontrollpunkter samverkar.

Se inte listan som ett test där flest kryss vinner. Försök i stället identifiera **vilka arbetsformer du har tillgång till** och vilka du ännu sällan använder.

I nästa kapitel tar vi itu med den kanske viktigaste frågan av alla: blir arbetet faktiskt bättre?
