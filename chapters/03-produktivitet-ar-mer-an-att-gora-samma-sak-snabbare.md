# Kapitel 3 – Produktivitet är mer än att göra samma sak snabbare

Påståendet ”AI gör utvecklare snabbare” låter som ett faktapåstående men är egentligen flera frågor hopslagna.

Snabbare på vad?

För vem?

Med vilket verktyg?

I vilken kodbas?

Mätt som vad – tid till första kodrad, slutförd issue, mergead pull request, releasad funktion eller faktisk verksamhetsnytta?

Och vad händer med kvalitet, reviewtid och omarbete?

När frågorna formuleras så blir forskningsläget mindre motsägelsefullt. Olika studier mäter helt enkelt olika delar av ett mycket stort problem.

## Tre experiment som visar tydlig positiv effekt

**Forskningsresultat – randomiserade fältexperiment:** En studie publicerad av forskare med koppling till bland annat Microsoft analyserade tre randomiserade fältexperiment vid Microsoft, Accenture och ett anonymiserat Fortune 100-företag. Totalt omfattades 4 867 utvecklare. När resultaten slogs samman ökade antalet slutförda uppgifter med 26,08 procent för utvecklare som hade tillgång till den AI-baserade kodassistenten. Mindre erfarna utvecklare hade högre användning och större produktivitetsvinster. [K-008]

Det är ett starkt resultat eftersom randomisering gör det möjligt att säga mer om kausalitet än i en vanlig enkät.

Men vad mättes?

Studien handlade om tillgång till en kodassistent som gav intelligenta kodförslag i företagsmiljöer. Resultatet säger inte att varje typ av utvecklingsuppgift blir 26 procent snabbare, att varje AI-verktyg ger samma effekt eller att en agent som får göra större förändringar autonomt skulle ge samma resultat.

Det säger att i dessa miljöer och experiment kunde AI-assistans öka den uppmätta mängden slutfört arbete.

Det är betydelsefullt – men avgränsat.

## Ett experiment där AI gjorde experter långsammare

**Forskningsresultat – randomiserat experiment:** METR studerade 16 mycket erfarna open-source-utvecklare som arbetade med 246 verkliga issues i stora och mogna repositories de själva hade bidragit till under flera år. Uppgifterna slumpades så att AI ibland var tillåten och ibland inte. När AI var tillåten användes främst Cursor Pro tillsammans med Claude 3.5/3.7 Sonnet, vilket motsvarade tidiga 2025-verktyg. [K-009]

Resultatet gick i motsatt riktning: utvecklarna tog i genomsnitt **19 procent längre tid** när de fick använda AI. [K-009]

Ännu mer intressant var skillnaden mellan upplevd och uppmätt effekt. Före experimentet trodde utvecklarna att AI skulle göra dem ungefär 24 procent snabbare. Efteråt trodde de fortfarande att AI hade gjort dem omkring 20 procent snabbare – trots att mätningen visade en försämring. [K-009]

Detta är en av de viktigaste observationerna i hela boken.

Självupplevd produktivitet är inte samma sak som faktisk genomloppstid.

AI kan kännas snabbt eftersom mycket händer: kod skrivs omedelbart, förslag kommer utan väntetid och användaren slipper vissa monotona moment. Men tiden kan flyttas till läsning, korrigering, väntan på agenten, felsökning eller bortkastade spår.

## Varför resultaten inte behöver motsäga varandra

Det vore enkelt att välja den studie som passar den berättelse man vill berätta.

Den AI-entusiastiske kan lyfta 26 procents ökning i slutförda uppgifter. Skeptikern kan lyfta 19 procents försämring för erfarna open-source-utvecklare.

En bättre slutsats är att **uppgiften och kontexten spelar stor roll**.

De tre positiva fältexperimenten omfattade företagsutvecklare som fick en kodassistent. METR:s deltagare var mycket erfarna maintainers i stora kodbaser de kände väl. De arbetade med verkliga issues där kvaliteten behövde vara tillräcklig för review och där repositoryspecifik kunskap spelade stor roll. [K-008, K-009]

En expert i en välkänd kodbas har redan ett stort internt index över var saker finns, vilka historiska beslut som ligger bakom en märklig konstruktion och vilken typ av lösning maintainergruppen accepterar. En generell AI-modell måste rekonstruera mycket av den kunskapen från kontext.

En mindre erfaren person kan däremot få större värde av att AI tillhandahåller mönster och exempel som experten redan kan.

Detta är en hypotes som stöds av flera studier, men den ska inte göras absolut. Effekten beror även på hur bra verktygen blir på repositoryförståelse och långvarigt agentiskt arbete.

## Forskningen förändras medan verktygen förändras

METR:s resultat är särskilt värdefullt eftersom organisationen själv betonar hur tidsbundet det är. Studien mäter tidiga 2025-verktyg. Under 2026 publicerade METR uppföljningsinformation som pekar mot bättre resultat med senare verktyg men också beskriver betydande urvalsproblem, bland annat att utvecklare kan välja bort uppgifter där de tror AI skulle hjälpa mest. Organisationen avråder därför från att läsa den senare datan som en enkel exakt produktivitetsprocent. [K-010]

Detta illustrerar ett problem som kommer följa all litteratur om generativ AI:

> En välgjord studie kan bli tekniskt daterad snabbare än forskning i många andra områden.

Vi bör därför vara mer intresserade av **mekanismer** än av enskilda procentsatser.

Exempel på mekanismer är:

- erfarenhetsskillnader,
- uppgiftens struktur,
- hur mycket lokal kontext som behövs,
- hur lätt resultatet kan verifieras,
- hur mycket tid som går åt till omarbete,
- hur väl AI:n kan använda verktyg,
- hur stora konsekvenser fel får.

De mekanismerna är mer hållbara än frågan om modellversion X gav 14, 19 eller 26 procent effekt i en viss studie.

## Den ojämna kapabilitetsfronten

En peer-reviewad studie som blivit viktig i diskussionen om generativ AI i kunskapsarbete är *Navigating the Jagged Technological Frontier*. Forskarna genomförde ett fältexperiment med 758 konsulter och lät dem lösa olika kunskapsintensiva uppgifter med eller utan AI. [K-011]

På uppgifter som låg **inom** AI:ns kapabilitetsområde arbetade deltagarna snabbare, producerade mer och nådde högre kvalitet. Men på en komplex uppgift som forskarna valt för att ligga **utanför** den aktuella modellens förmågefront var deltagare med AI 19 procent mindre benägna att producera rätt lösning än gruppen utan AI. [K-011]

Forskarna beskriver därför teknikfronten som *jagged* – ojämn.

AI kan vara imponerande på en svår uppgift och samtidigt opålitlig på en till synes närliggande uppgift.

Detta är mycket relevant för systemutveckling. En modell kan exempelvis:

- skriva en korrekt implementation av ett känt mönster,
- men missa en lokal affärsregel,
- förklara ett ramverk mycket väl,
- men föreslå ett API som inte finns i den version ni använder,
- generera många testfall,
- men missa den viktigaste domänrisken,
- analysera en arkitekturskiss övertygande,
- men inte känna till ett organisatoriskt constraint som aldrig fanns i underlaget.

Mognad handlar därför delvis om att lära sig känna igen när uppgiften sannolikt befinner sig nära en sådan ojämn gräns.

## Kvalitet är en del av produktiviteten

Om en AI-assistent halverar tiden till första kodversion men dubblerar review- och felsökningstiden har vi inte nödvändigtvis vunnit något.

Samma sak gäller i andra roller.

Ett kravdokument kan genereras på fem minuter men orsaka dagar av missförstånd om de centrala begreppen blev fel. En arkitekturanalys kan se fullständig ut men skapa falsk trygghet om ett avgörande constraint saknas. Hundra genererade tester kan öka testsvitens storlek utan att öka dess förmåga att upptäcka viktiga fel.

Därför behöver produktivitet minst ses i relation till:

- hastighet,
- kvalitet,
- omarbete,
- verifieringskostnad,
- genomloppstid,
- och värdet av resultatet.

För vissa arbetsuppgifter är tid till första utkast en bra mätpunkt. För andra är den nästan irrelevant.

## Självrapporterad nytta är fortfarande relevant

Att självrapporterad produktivitet kan vara fel betyder inte att den är värdelös.

Stack Overflows enkät visar exempelvis att 52 procent av utvecklarna ansåg att AI-verktyg eller agenter haft en positiv effekt på deras produktivitet. Bland agentanvändare var den positiva självrapporteringen högre. [K-007]

Sådana resultat berättar något viktigt om **upplevd nytta och adoption**. Ett verktyg som människor upplever som värdelöst används sällan dagligen i stor skala.

Men självrapporten kan inte ensam besvara om organisationen levererar mer värde eller om uppgifterna faktiskt slutförs snabbare.

Boken kommer därför konsekvent skilja mellan:

- *användarna upplever att*,
- *telemetri visar att*,
- *ett experiment mätte att*.

Det är små språkliga skillnader som gör stor epistemisk skillnad.

## Var hamnar den sparade tiden?

Ett randomiserat fältexperiment över 66 företag och 7 137 arbetstagare har undersökt hur generativ AI påverkar arbetsmönster. Resultaten pekar på individuell tidsbesparing men mer begränsad förändring i hur arbetet som helhet organiseras. [K-014]

Detta hjälper oss förstå varför lokal AI-effektivitet inte automatiskt skapar organisatorisk transformation.

Om AI gör det snabbare att skriva en implementation kan den sparade tiden användas till:

- fler funktioner,
- bättre tester,
- mer refaktorering,
- mer review,
- andra arbetsuppgifter,
- eller helt enkelt absorberas av mer arbete i samma takt.

För att produktiviteten på systemnivå ska öka måste organisationen kunna omsätta den lokala vinsten.

Det är här värdeflöde blir relevant.

## Flaskhalsen flyttar sig

Antag att ett team tidigare lade ungefär lika mycket kapacitet på:

1. kravförtydligande,
2. implementation,
3. review,
4. test och verifiering,
5. release.

Om AI plötsligt dubblerar implementationskapaciteten men inget annat förändras kan kön inför review växa. Testmiljön kan bli överbelastad. Product owner kan få fler frågor. Releasefrekvensen kanske inte ändras alls.

I värsta fall producerar teamet mer förändring än det kan förstå och kontrollera.

DORA:s 2025-rapport beskriver AI-införande just som ett systemproblem och lyfter Value Stream Management som ett sätt att undvika att lokala produktivitetsvinster skapar nedströms kaos. [K-019]

Det är en viktig förskjutning i tänkandet:

> Från ”hur mycket kod kan AI skriva?” till ”hur förbättras det faktiska flödet från behov till verifierat värde?”

## Den dolda kostnaden: verifiering

Generativ AI har en speciell kostnadsprofil. Att producera ett första förslag är ofta mycket billigt. Att säkerställa att förslaget är korrekt kan vara dyrt.

Det gör att ekonomin blir annorlunda än i traditionellt kunskapsarbete.

Tidigare kunde det vara dyrt att producera fem arkitekturalternativ, därför tog man kanske fram två. Med AI kan man få tio alternativ på några minuter. Men beslutsarbetet blir inte automatiskt tio gånger bättre. Någon måste fortfarande förstå alternativen, sortera duplicerade idéer, upptäcka orealistiska antaganden och värdera konsekvenserna.

Samma sak med kod. Mer kod är inte automatiskt mer värde.

Detta kan uttryckas som en enkel modell:

**Nettonytta = sparad produktionstid − extra verifiering − omarbete − följdkostnad av fel + värde av förbättrad kvalitet/idébredd.**

Det är inte en vetenskaplig ekvation. Det är **bokens syntes**, avsedd som tankemodell.

Poängen är att produktionshastigheten bara är en term.

## När AI kan fungera som erfarenhetsaccelerator

Studien *Generative AI at Work* med 5 172 kundsupportagenter visade i den peer-reviewade versionen en genomsnittlig produktivitetsökning på 15 procent, men mycket större förbättringar för mindre erfarna och lägre presterande medarbetare. [K-012]

Forskarna fann också stöd för att AI hjälpte nya medarbetare att snabbare nå arbetsmönster som liknade mer erfarna kollegors.

Även om detta inte är systemutveckling är principen intressant.

En junior utvecklare kan få omedelbar tillgång till exempel på etablerade mönster. En ny testare kan få hjälp att tänka bredare kring gränsfall. En ny arkitekt kan få en lista över vanliga tradeoffs som annars hade tagit längre tid att bygga upp.

Men samma mekanism kan också standardisera dåliga mönster om AI:ns råd är fel eller kontextlöst.

Erfarenhetsacceleration utan verifiering kan bli **felaccelerering**.

## Kritisk förmåga blir en produktivitetsfaktor

CHI-studien om kritiskt tänkande med 319 kunskapsarbetare fann att högre tilltro till AI var förknippad med mindre kritisk ansträngning, medan arbetet med AI ofta flyttade kritiskt tänkande mot verifiering, integration och övervakning. [K-013]

Det antyder en viktig sak för mognadsresan:

Den person som är bra på AI-assisterat arbete är inte nödvändigtvis den som accepterar flest förslag eller lyckas automatisera flest steg. Det kan vara den som snabbt kan avgöra:

- vad som behöver kontrolleras,
- vad som kan accepteras med låg risk,
- var modellen sannolikt saknar kontext,
- när en uppgift bör delas upp,
- och när det är snabbare att göra arbetet själv.

Med andra ord blir **omdöme en produktivitetsförmåga**.

## Fem nivåer av produktivitetsmätning

För att undvika att vi pratar förbi varandra kommer boken använda fem nivåer när vi diskuterar effekt:

### 1. Moment

Blev en enskild aktivitet snabbare?

Exempel: tid att skriva ett unit test.

### 2. Uppgift

Blev hela arbetsuppgiften klar snabbare med accepterad kvalitet?

Exempel: tid från att issue påbörjas till reviewbar förändring.

### 3. Teamflöde

Ökade genomloppet genom teamets gemensamma process?

Exempel: tid från utvecklingsstart till merge.

### 4. Leveransflöde

Kom värdet snabbare och säkrare till användaren?

Exempel: lead time från beslutat behov till produktion.

### 5. Verksamhetsvärde

Gav förändringen bättre resultat för användare eller organisation?

AI kan ge en stor förbättring på nivå 1 och ingen förbättring alls på nivå 5.

Det är inte ett argument mot AI. Det är ett argument för att mäta på rätt nivå.

## En praktisk produktivitetsövning

Välj en återkommande arbetsuppgift där du redan använder AI. Gör inte en stor studie. Gör ett litet eget experiment.

Under några uppgifter, anteckna:

- total arbetstid,
- ungefärlig tid aktivt med AI,
- tid för review och korrigering,
- antal större omtag,
- vad som hade varit svårt utan AI,
- och om slutkvaliteten blev bättre, sämre eller ungefär densamma.

Jämför sedan med liknande arbete utan AI när det är möjligt.

Syftet är inte att få en publicerbar procentsats. Syftet är att kalibrera din intuition.

METR:s studie visar varför det behövs: vi kan känna oss snabbare utan att vara det. [K-009]

## Bokens produktivitetsprincip

Vi kan nu formulera en princip som kommer följa resten av boken:

> AI-produktivitet är en egenskap hos kombinationen människa, uppgift, kontext, verktyg och kontrollmodell – inte en konstant egenskap hos AI-verktyget.

Det är **bokens syntes**, men den är förenlig med det varierande empiriska underlaget vi sett i detta kapitel.

När vi senare går genom de sju mognadsstegen kommer vi därför inte fråga enbart ”kan AI göra mer?”.

Vi kommer också fråga:

- Blir den totala uppgiften bättre?
- Blir fel billigare eller dyrare att upptäcka?
- Flyttar vi bara flaskhalsen?
- Har människan tillräcklig kompetens för att verifiera resultatet?
- Är en mer autonom arbetsform faktiskt motiverad?

Med den grunden på plats kan vi börja själva mognadsresan.

Nästa kapitel börjar där många börjar: med en fråga.
