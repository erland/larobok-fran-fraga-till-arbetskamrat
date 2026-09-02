# Inledning – Du kommer sannolikt inte arbeta med AI på samma sätt om ett år

Två personer kan öppna samma AI-tjänst på samma dator och ändå i praktiken använda två helt olika verktyg.

Den ena skriver en fråga i stil med:

> Hur fungerar en REST-baserad integration?

Den andra arbetar med ett konkret förändringsbehov i ett befintligt system. Hon låter AI:n läsa krav, kod, tester och tidigare arkitekturbeslut, ber den identifiera vilka delar som påverkas, låter den föreslå förändringar, granskar resonemanget, låter verktyget genomföra vissa av ändringarna och använder automatiska tester och mänsklig review som kontrollpunkter.

Båda använder generativ AI. Men arbetssätten är radikalt olika.

Den här boken handlar om vägen mellan dessa två sätt att arbeta.

## Bokens huvudtes

Generativ AI lärs sällan in som ett traditionellt verktyg. När vi lär oss ett nytt programmeringsspråk, en ny modelleringsnotation eller ett nytt testverktyg finns ofta en tydlig kunskapsmassa att ta till sig. Med generativ AI händer något annat. Det är lika mycket **vårt eget arbetssätt** som förändras som vår kunskap om verktyget.

I början använder många AI som en dialogbaserad sökmotor: man ställer en fråga och får ett svar. Efter hand upptäcker man att samma gränssnitt kan användas för att jämföra alternativ, kritisera ett resonemang, skapa ett första utkast, analysera ett dokument eller hjälpa till att felsöka kod. Nästa steg kan vara att ge AI:n verklig projektkontext: repository, backlogg, modeller, testresultat och tidigare beslut. Så småningom kan vissa arbetsuppgifter delegeras som mål snarare än som en lång serie detaljinstruktioner. I vissa miljöer blir AI till sist en del av själva arbetsflödet.

OpenAI:s aggregerade användningsdata ger stöd för att användningen faktiskt breddas med erfarenhet. I en analys av individuella ChatGPT-konton skickade användarna sex månader efter registrering omkring 50 procent fler meddelanden per dag än under sin första månad, och de hade ungefär fördubblat antalet olika typer av uppgifter de provat. Det är leverantörens egen produkttelemetri och ska inte läsas som en universell lag om AI-mognad, men den visar ett tydligt mönster: människor tenderar inte bara att använda verktyget mer; de lär sig använda det till fler saker. [K-001]

Det är denna utveckling vi ska undersöka.

## Inte en bok om ChatGPT

ChatGPT har haft stor betydelse för att göra generativ AI till ett vardagsverktyg, men denna bok är medvetet verktygsneutral. Samma grundläggande utveckling går att känna igen när människor arbetar med exempelvis Claude, Gemini, GitHub Copilot, Microsoft Copilot eller andra AI-assistenter och kodningsagenter.

Produktfunktionerna skiljer sig. Några verktyg har djup integration i en utvecklingsmiljö. Andra är bättre på dokument, multimodalitet, lång kontext eller agentiskt arbete. Dataskydd, retention och företagsavtal skiljer sig också. Sådana skillnader spelar roll och kommer att behandlas där de påverkar arbetssättet.

Men bokens huvudfråga är inte vilket verktyg som är bäst.

Frågan är:

> Hur förändras en människas sätt att arbeta när hon går från att ställa enstaka frågor till att använda AI som en medvetet designad del av sitt kunskapsarbete?

## Hela systemutvecklingsprocessen är arenan

Boken började som en idé om utvecklare och IT-arkitekter. Ganska snart blev det tydligt att mognadsresan är bredare än så.

En kravanalytiker kan börja med att fråga hur en bra user story ska formuleras och senare använda AI för att analysera ett stort verksamhetsunderlag, identifiera motsägelser och föreslå acceptanskriterier. En testare kan börja med att fråga om en testteknik och senare ge AI tillgång till krav, kod och tidigare defekter för att identifiera riskområden. En arkitekt kan börja med begreppsfrågor och senare använda AI som ett kritiskt bollplank för alternativanalys och konsekvensbedömning. En utvecklare kan gå från syntaxfrågor till att delegera en avgränsad förändring i ett repository.

Det som skiljer rollerna är främst **arbetsmaterialet, kvalitetskriterierna och konsekvenserna av fel**. Den underliggande mognadsresan är påfallande likartad.

Därför använder boken systemutvecklingsprocessen som gemensam arena: behov och krav, arkitektur och design, implementation, test, leverans och återkoppling.

## Sju steg – men ingen vetenskaplig sjugradig skala

I den här boken delar vi pedagogiskt upp utvecklingen i sju arbetsformer:

1. **Fråga** – AI används som interaktiv kunskapskälla.
2. **Resonera** – AI används som bollplank för alternativ, hypoteser och konsekvenser.
3. **Skapa** – AI producerar konkreta artefakter som kod, tester, krav eller dokumentation.
4. **Samarbeta** – arbetet blir iterativt: utkast, kritik, förändring och verifiering.
5. **Ge kontext** – AI får tillgång till det verkliga arbetsmaterialet och kan resonera i projektets sammanhang.
6. **Delegera** – användaren beskriver ett mål och låter AI genomföra flera steg inom tydliga gränser.
7. **Orkestrera** – AI blir en designad del av ett större arbetsflöde med människor, verktyg och kontrollpunkter.

Det är viktigt att vara exakt med vad denna modell är och inte är.

**Bokens syntes:** De sju stegen är inte en vetenskapligt etablerad mognadsskala. De är en pedagogisk syntes av observerade användningsmönster, forskning om människa–AI-samarbete och utvecklingen från chattbaserad assistans mot agentiska arbetsflöden. Forskningen ger stöd för flera delar av riktningen, men inte för att alla människor går igenom exakt sju faser i denna ordning.

Dessutom kommer du sannolikt att befinna dig på olika steg samtidigt. Du kanske delegerar implementation av en väl avgränsad testförbättring men använder AI enbart för resonemang när du arbetar med ett säkerhetskritiskt arkitekturbeslut.

Det är inte inkonsekvent. Det är ofta ett tecken på mognad.

## Mognad betyder inte maximal autonomi

Det är frestande att beskriva AI-mognad som en rak linje där varje steg innebär att människan gör mindre och AI:n gör mer. Den bilden är missvisande.

En erfaren användare kan mycket väl välja att inte delegera en viss uppgift, även om verktyget tekniskt skulle kunna utföra den. Skälet kan vara att problemet är oklart, konsekvensen av ett fel är stor, informationen är känslig, domänkunskapen är svår att uttrycka eller verifieringskostnaden är högre än vinsten.

Mogen AI-användning handlar därför om tre saker:

**Repertoar.** Du har fler arbetsformer att välja mellan. Du kan fråga, resonera, skapa, samarbeta, ge kontext, delegera och orkestrera när det passar.

**Situationsanpassning.** Du väljer arbetsform utifrån uppgiften i stället för att alltid använda den mest avancerade funktionen.

**Kontroll.** Du förstår vad som behöver verifieras, vilka befogenheter AI:n bör få, vilket material den får se och vilka kvalitetskriterier som måste vara uppfyllda.

Detta är en av bokens viktigaste poänger: nästa steg är inte alltid ”mer AI”. Nästa steg kan lika gärna vara att bli bättre på att avgöra **när AI ska användas, hur och med vilken kontroll**.

## Ett förändringsbehov, två arbetssätt

Vi kommer genom boken återkomma till ett enkelt scenario. Ett befintligt affärssystem behöver stöd för ett nytt leveransalternativ. Förändringen påverkar verksamhetsregler, API, domänmodell, integrationer, tester, dokumentation och releaseunderlag.

En relativt ny AI-användare kan arbeta ungefär så här:

1. Fråga hur ett leveransalternativ bör modelleras.
2. Be om ett kodexempel.
3. Kopiera och anpassa koden manuellt.
4. Fråga varför ett test misslyckas.
5. Skriva dokumentationen själv.

Det kan vara mycket värdefullt. AI har hjälpt till vid flera punkter.

En mer erfaren användare kan i stället börja med att ge AI:n relevant kontext: kravet, berörda delar av kodbasen, testsviten och tidigare arkitekturbeslut. Hon ber AI:n analysera påverkan och föreslå en plan, granskar planen, korrigerar antaganden och låter därefter verktyget genomföra en avgränsad del av förändringen. Automatiska tester körs. AI:n får analysera felen, men ändringar som påverkar externa kontrakt eller centrala domänregler måste passera en mänsklig kontrollpunkt. När implementationen är klar används samma kontext för att uppdatera dokumentation och releaseunderlag.

Skillnaden ligger inte främst i hur avancerad den första prompten är.

Skillnaden ligger i **hur arbetet har delats upp mellan människa, AI och andra verktyg**.

## Produktivitet är inte självklar

Den här boken utgår inte från att AI automatiskt gör arbetet snabbare eller bättre.

Forskningen är mer intressant än så.

I tre randomiserade fältexperiment med sammanlagt 4 867 utvecklare ökade antalet slutförda uppgifter med omkring 26 procent när utvecklarna fick tillgång till en AI-baserad kodassistent. Mindre erfarna utvecklare hade högre användning och större produktivitetsvinster. [K-008]

I ett annat randomiserat experiment studerade METR 16 mycket erfarna open-source-utvecklare som arbetade i stora repositories de kände väl. Med tidiga 2025-verktyg tog de i genomsnitt 19 procent längre tid när AI var tillåten. Det särskilt intressanta var att utvecklarna både före och efter experimentet trodde att AI hade gjort dem snabbare. [K-009]

Båda resultaten kan vara riktiga.

De studerar olika människor, olika verktyg och olika typer av arbete. Det är just därför frågan ”gör AI utvecklare snabbare?” är för grov för att vara särskilt användbar.

Vi kommer i stället återkomma till fyra frågor:

- För **vilken uppgift** används AI?
- Av **vilken person** och med vilken erfarenhet?
- Med **vilken kontext och vilket verktyg**?
- Till vilken **verifierings- och omarbetningskostnad**?

## När AI behöver se det som inte är publikt

De första stegen i mognadsresan kan ofta utföras med allmänt material. Men nyttan ökar kraftigt när AI får arbeta med verklig kontext: källkod, interna modeller, incidenter, avtal, backloggar, krav, personuppgifter eller strategiska dokument.

Då förändras frågan.

Det räcker inte att fråga om ”AI är säker”. Man måste veta vilken information som används, vilken tjänst och kontotyp som gäller, hur leverantören behandlar informationen, vilka integrationer som kan föra den vidare och vilka organisatoriska regler som gäller.

Vi behandlar detta först när rik kontext introduceras och mer systematiskt senare i boken. En mogen användare behöver kunna göra denna bedömning, inte bara kunna skriva bättre instruktioner.

## Hur du kan läsa boken

Boken är tänkt att fungera på två sätt.

Du kan läsa den från början till slut och följa utvecklingen från enkel AI-användning till mogna arbetsflöden. Det ger den tydligaste bilden av varför varje steg uppstår.

Men du kan också använda den diagnostiskt. När du känner igen ditt nuvarande arbetssätt kan du fokusera på kapitlet om nästa steg och prova en liten förändring i ett verkligt arbete.

För varje mognadssteg kommer vi därför att fråga:

- Vad förändras jämfört med föregående steg?
- Vad blir möjligt som tidigare var svårt?
- Vilka nya risker uppstår?
- Vad behöver människan fortfarande förstå och kontrollera?
- Vad är ett rimligt nästa experiment?
- När bör du medvetet **inte** gå vidare?

Målet är inte att du efter sista sidan ska använda maximal AI i varje arbetsuppgift.

Målet är att du ska ha en större repertoar, bättre omdöme och en tydligare bild av hur du vill dela arbetet mellan dig själv och AI.

I slutet av boken finns också en översikt över de pedagogiska modellerna och en självvärdering som hjälper dig välja ett konkret nästa experiment utan att reducera mognad till ett poängtal.

Det är resan från fråga till arbetskamrat.
