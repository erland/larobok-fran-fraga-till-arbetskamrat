# Kapitel 7 – Fas 4: Samarbeta

Den första stora myten många möter kring generativ AI är att resultatet avgörs av **den perfekta prompten**.

Om bara instruktionen är tillräckligt smart, detaljerad och elegant ska modellen kunna leverera rätt resultat på första försöket.

Det synsättet passar dåligt för verkligt kunskapsarbete.

När uppgiften innehåller oklarheter, lokala begränsningar, kompromisser och flera kvalitetsdimensioner finns det sällan en enda instruktion som kan bära allt.

Människor arbetar inte heller så.

Vi gör ett utkast.

Vi provar.

Vi får återkoppling.

Vi upptäcker något vi inte förstod från början.

Vi ändrar.

Vi testar igen.

När AI används på samma sätt uppstår fas 4: **Samarbeta**.

Kärnan är inte att dialogen blir längre.

Kärnan är att **resultatet utvecklas genom återkoppling**.

## Från beställning till loop

I fas 3 kunde arbetsformen se ut så här:

> Skriv en första implementation av funktionen.

AI producerar artefakten.

I fas 4 fortsätter arbetet:

> Kör testerna.

> Två testfall misslyckas. Förklara varför innan du ändrar något.

> Din hypotes förklarar det första felet men inte det andra. Kontrollera hur befintlig kod hanterar tidszoner.

> Bra. Gör minsta ändringen, kör testerna igen och visa diffen.

Detta är inte bara ”fler prompts”.

Varje steg använder **information som uppstod i föregående steg**.

Arbetet har blivit en loop.

Samma sak kan ske i kravarbete:

> Skapa första kravförslaget.

> Granska det nu ur kundtjänstens perspektiv.

> Vilka krav skulle kunna tolkas på två sätt?

> Skriv inte om allt. Föreslå bara de tre ändringar som minskar störst verksamhetsrisk.

Eller i arkitekturarbete:

> Gör ett första alternativförslag.

> Anta nu att latency är dubbelt så viktig som vi först trodde. Hur ändras rekommendationen?

> Argumentera sedan för det alternativ du nyss rankade sist.

> Vilken fakta behöver vi samla in för att avgöra frågan?

Dialogen producerar inte bara text.

Den producerar **successivt bättre förståelse och ett successivt bättre arbetsobjekt**.

## Den iterativa kärnloopen

I den här boken använder vi följande återkommande loop:

**utkast → granskning → kritik → förändring → verifiering**

Detta är bokens syntes, inte en etablerad standardmodell.

### Utkast

AI eller människa producerar en första version.

### Granskning

Resultatet jämförs mot syfte, begränsningar, källor, krav eller andra kvalitetskriterier.

### Kritik

Bristen formuleras tydligt: vad är fel, varför spelar det roll och vilken evidens finns?

### Förändring

En avgränsad förbättring görs.

### Verifiering

Vi kontrollerar om förändringen faktiskt förbättrade resultatet utan att skapa nya problem.

Därefter kan loopen börja om.

Det centrala är att **verifieringen inte hoppas över**.

Annars blir samarbetet lätt en serie omskrivningar där texten förändras men kvaliteten inte nödvändigtvis ökar.

## Iteration är inte samma sak som att be om ”bättre”

En svag fas 4-dialog kan låta så här:

> Gör den bättre.

> Bättre igen.

> Mer professionell.

> Mer detaljerad.

AI kan fortsätta förändra resultatet nästan obegränsat, men användaren har inte sagt vilken riktning som är bättre.

En starkare loop gör förbättringen observerbar:

> Utkastet blandar fakta och rekommendation. Separera dem och markera varje rekommendation som inte har explicit stöd i faktaavsnittet.

Eller:

> Tre tester verifierar samma happy path. Behåll ett och använd de två andra till att testa gränsvärdena 0 och maxvärdet.

Eller:

> Alternativanalysen nämner kostnad men inte operativ komplexitet. Lägg till operativ komplexitet som eget kriterium och bedöm alla alternativ enligt samma skala.

Det är skillnaden mellan **stiliteration** och **kvalitetsiteration**.

Fas 4 blir värdefull när återkopplingen är knuten till ett faktiskt kvalitetsproblem.

## Varför multi-turn kan hjälpa

Det finns empiriskt stöd för att flerturnsarbete och relevant kontext kan förbättra vissa typer av resultat.

I den explorativa 2026-studien av LLM-genererade unit-tester gav en sekventiell multi-turn-strategi bäst resultat av de testade promptuppläggen. [K-037] Studien är begränsad och vi ska inte översätta dess exakta siffror till andra arbetsuppgifter. Men den illustrerar en mekanism som är lätt att känna igen praktiskt:

1. ett första resultat skapas,
2. resultatet eller dess fel ger ny information,
3. nästa instruktion kan använda den informationen,
4. arbetet blir mer riktat.

Det är samma anledning till att en utvecklare ofta felsöker bättre efter ett testfel än före det.

Återkopplingen minskar osäkerheten.

## Samarbete kan vara asymmetriskt

Ordet arbetskamrat kan ge intryck av två jämbördiga aktörer.

Så behöver det inte vara.

I en bra AI-loop har människan ofta roller som AI:n inte har:

- ansvar för syftet,
- lokal verksamhetskunskap,
- förståelse för informella begränsningar,
- tillgång till människor och organisatoriska beslut,
- ansvar för konsekvenserna.

AI:n kan samtidigt ha andra styrkor:

- generera många alternativ snabbt,
- läsa stora textmängder,
- omformulera,
- hitta mönster,
- göra mekaniska transformationer,
- hålla flera perspektiv aktiva i samma dialog.

Moget samarbete betyder därför inte att människan och AI:n ”gör hälften var”.

Det betyder att arbetet fördelas efter styrkor, risk och verifierbarhet.

## Låt AI:n kritisera, men kalla det inte oberoende review

En praktisk teknik är att byta roll i samma dialog:

> Granska nu din egen lösning som om du vore en erfaren reviewer som försöker stoppa den från produktion. Lista de tre allvarligaste riskerna.

Det kan vara mycket användbart.

Modellen kan upptäcka inkonsekvenser eller alternativa tolkningar som inte syntes i första utkastet.

Men vi bör vara noggranna med språket.

Det är **självkritik**, inte oberoende verifiering.

Samma modell, samma kontext och ofta samma underliggande antaganden finns kvar.

Ny forskning om LLM:er som code reviewers illustrerar varför detta spelar roll. En peer-reviewad studie från 2026 fann systematisk överkorrigering när modeller bedömde om kod uppfyllde krav. [K-039] Slutsatsen är inte att AI-review är värdelös. Den är att en AI-reviewer också har egna felmoder.

En svensk empirisk fältstudie vid WirelessCar visar en mer nyanserad praktisk bild. Utvecklare föredrog ofta en AI-ledd review, särskilt för stora eller obekanta pull requests, men studien identifierade också problem med kontextbrist och false positives. Preferenserna varierade med hur väl utvecklaren kände koden och med risknivån. [K-038]

Det passar bokens övergripande mognadsprincip:

> Rätt arbetsform beror på uppgiften.

AI-review kan vara ett starkt extra filter.

Den behöver inte vara den enda kvalitetsgrinden.

## Fyra sorters kontroll i samarbetet

För att undvika att alla verifieringar reduceras till ”läs igenom svaret” skiljer vi i den här boken mellan fyra kontrollformer. Detta är **bokens syntes**.

### 1. Självgranskning

AI:n får kritisera eller kontrollera sitt eget resultat.

Billigt och snabbt, men inte oberoende.

### 2. Mänsklig granskning

En person bedömer resultatet mot domänkunskap, syfte och konsekvenser.

Starkt när tacit knowledge och ansvar är viktigt, men kan vara dyrt och påverkas av automation bias.

### 3. Exekverbar verifiering

Resultatet testas mot något observerbart:

- kompilerar,
- test går grönt,
- schema validerar,
- beräkning stämmer,
- query ger förväntat resultat,
- scenario kan reproduceras.

Detta är ofta den starkaste kontrollen för tekniska artefakter när den finns.

### 4. Oberoende kontroll

En annan källa eller mekanism används för att försöka falsifiera resultatet:

- originaldokument,
- separat dataset,
- en annan reviewer,
- annan modell eller verktyg,
- experiment,
- externa mätvärden.

De fyra formerna konkurrerar inte.

En stark loop kombinerar ofta flera.

## Exempel: refaktorering som samarbete

Anta att en utvecklare vill dela upp en stor serviceklass.

En enkel fas 3-instruktion kan vara:

> Refaktorera klassen till mindre komponenter.

I fas 4 kan arbetet i stället delas upp:

### Utkast

> Föreslå tre sätt att dela ansvaret. Ändra ingen kod ännu.

### Granskning

> Jämför alternativen mot testbarhet, transaktionsgränser och hur mycket publikt API som måste förändras.

### Kritik

> Alternativ 2 ser bäst ut, men du flyttar transaktionsansvaret. Kontrollera vilka metoder som i dag körs i samma transaktion.

### Förändring

> Implementera bara extraktionen av PricingPolicy. Lämna övriga ansvar kvar.

### Verifiering

> Kör relevanta tester och visa om diffen förändrade något utanför servicepaketet.

Det intressanta är att AI:n inte behöver få större frihet för att samarbetet ska bli mer moget.

Tvärtom blir varje steg ofta **mer avgränsat**.

Mognaden ligger i återkopplingsloopen och kontrollen.

## Exempel: kravförfining som samarbete

Ett första kravförslag säger:

> Kunden ska kunna ändra leveransdatum före leverans.

AI:n kan först få skapa acceptanskriterier.

Sedan börjar fas 4-arbetet:

> Läs kriterierna som en utvecklare som vill implementera minsta möjliga beteende. Var kan ordalydelsen utnyttjas på ett sätt verksamheten inte avsåg?

AI:n kanske identifierar att ”före leverans” är otydligt.

Då kan människan tillföra verksamhetskunskap:

> Ändring ska vara möjlig fram till att plockning har påbörjats, inte fram till fysisk leverans.

Nästa iteration:

> Uppdatera bara de kriterier som påverkas av den nya regeln. Lägg till ett negativt scenario för påbörjad plockning.

Sedan verifierar en verksamhetsrepresentant att regeln faktiskt är korrekt.

AI:n har producerat mycket av texten.

Men kvaliteten uppstod genom **samspelet mellan textproduktion, kritik och lokal kunskap**.

## Exempel: arkitekturkritik utan skenprecision

En arkitekt kan använda AI som kritiker:

> Här är tre lösningsalternativ och våra kvalitetsattribut. Identifiera vilket kriterium som mest sannolikt förändrar rangordningen om vårt antagande visar sig vara fel.

AI:n svarar kanske att trafikvolymen är avgörande.

I stället för att be om ännu en mer detaljerad analys kan nästa steg vara:

> Bra. Vilken mätning i vår nuvarande miljö skulle bäst minska osäkerheten?

Nu leder AI-dialogen till ett **experiment i verkligheten**.

Detta är en viktig gräns för fas 4.

Samarbete med AI ska inte bli ett slutet resonemangssystem där varje osäkerhet besvaras med mer genererad text.

Ibland är det bästa AI-rådet att gå och mäta något.

## När människan börjar arbeta som reviewer

När AI producerar mer förändras människans arbetsmix.

Det finns forskning som pekar i den riktningen.

En longitudinell mixed-methods-studie från 2026 av professionella utvecklare rapporterade att arbetet försköts från skapande mot verifieringsaktiviteter. Författarna använder begreppet **supervisory engineering work** för att beskriva arbete med att styra, utvärdera och korrigera AI-output. [K-040]

Studien är en preprint och ska inte ensam bära en generell slutsats. Men den ligger nära den peer-reviewade forskning om kritiskt tänkande vi använde tidigare, där AI-användare beskriver en förskjutning mot bland annat verifiering och stewardship. [K-013]

Detta är en av bokens viktigaste hypoteser om yrkesrollen:

> När produktion blir billigare blir förmågan att specificera, välja, kontrollera och korrigera relativt viktigare.

Det gäller inte bara utvecklare.

En kravanalytiker kan gå från att skriva varje formulering till att bedöma om AI-genererade krav representerar verksamhetens intention.

En arkitekt kan gå från att manuellt skriva varje vy till att verifiera modellens konsistens och de beslut som visualiseringen förmedlar.

En testare kan gå från att producera varje testfall till att bedöma riskcoverage, oracle-kvalitet och vilka scenarier som fortfarande saknas.

## Reviewkostnaden kan äta upp vinsten

Det finns en annan sida av detta.

Om AI producerar tio gånger mer material kan människan inte rimligen läsa tio gånger mer material lika noggrant.

Detta skapar en ny flaskhals.

Produktion kan bli billig.

**Uppmärksamhet förblir dyr.**

Därför behöver fas 4 också handla om att minska mängden som kräver mänsklig detaljgranskning.

Exempel:

- automatiska tester tar hand om vissa kodfel,
- schema-validering tar hand om strukturfel,
- statisk analys tar hand om vissa säkerhets- och kvalitetsproblem,
- källspårning gör faktakontroll snabbare,
- diffbaserad review visar bara förändringen,
- AI kan först sortera och prioritera sina egna fynd innan människan granskar dem.

Målet är inte att eliminera mänsklig kontroll.

Målet är att använda människans uppmärksamhet där den har högst värde.

## Undvik recensionskarusellen

En vanlig anti-pattern är att låta flera AI-roller recensera varandra i det oändliga:

1. författare-AI skriver,
2. reviewer-AI kritiserar,
3. författare-AI skriver om,
4. säkerhets-AI kritiserar,
5. kvalitets-AI skriver om,
6. arkitekt-AI kritiserar igen.

Det ser sofistikerat ut.

Men utan extern signal kan systemet bara cirkulera mellan olika formuleringar och antaganden.

Fråga därför regelbundet:

> Vilken ny information har tillkommit sedan förra iterationen?

Om svaret är ”ingen” bör du fundera på om nästa steg verkligen är ännu en AI-iteration.

Det kanske är:

- ett test,
- en mätning,
- ett samtal med en stakeholder,
- en titt i källkoden,
- en kontroll i produktionsdata,
- ett beslut.

Detta är en viktig del av situationsanpassning.

## Kontext börjar bli den stora begränsningen

I början av fas 4 märker många att själva promptformuleringen inte längre är det största problemet.

Problemet är att AI:n **inte vet det som teamet vet**.

Den vet inte:

- varför en konstig kodstruktur finns kvar,
- vilka tidigare incidenter som förändrade designen,
- vilka kunder som är beroende av ett gammalt beteende,
- vilka regulatoriska krav som styr en viss kontroll,
- vilka kompromisser som redan beslutats,
- vilka testdata som faktiskt motsvarar verkligheten.

Det går att fortsätta fylla på detta manuellt i dialogen.

Men någonstans uppstår en ny insikt:

> Det vore bättre om AI:n kunde arbeta med det faktiska repositoryt, dokumentationen, modellerna, backloggen och historiken.

Där börjar nästa fas.

## Bokens syntes: samarbetskontraktet

I fas 3 introducerade vi artefaktkontraktet.

I fas 4 lägger vi till ett **samarbetskontrakt**. Även detta är bokens egen modell.

För en återkommande AI-loop bör fyra saker vara tydliga:

### Vad får förändras?

Hela dokumentet? En funktion? Bara testkod? Ett arkitekturalternativ?

### Vilken återkoppling räknas?

Testresultat, stakeholder-kommentarer, källor, kvalitetskriterier, runtime-mätvärden?

### Vem eller vad får stoppa arbetet?

Ett rött test? En mänsklig reviewer? Ett compliance-krav? Ett budgettak?

### När är vi klara?

Inte när AI:n säger ”klart”, utan när definierade exit-kriterier är uppfyllda.

Den här typen av regler blir ännu viktigare när vi senare går från samarbete till delegering och orkestrering.

## Den perfekta prompten ersätts av ett bra system

Den kanske viktigaste lärdomen i fas 4 är att kvalitet inte behöver bäras av en enda instruktion.

Ett robust arbetssätt kan kompensera för att första prompten är ofullständig.

Du kan:

- skapa ett utkast,
- testa det,
- observera resultatet,
- lägga till saknad kontext,
- begränsa förändringen,
- köra om kontrollen.

Det liknar hur bra systemutveckling fungerar i övrigt.

Vi försöker inte skriva all kod perfekt innan första kompileringen.

Vi försöker inte förstå alla krav innan första prototypen.

Vi bygger återkopplingsloopar.

AI blir mest användbar när den placeras **inne i dessa loopar**, inte när den förväntas ersätta dem.

## Vad människan ansvarar för

I fas 4 blir människans roll tydligare som styrande deltagare.

Människan ansvarar för att:

- avgöra vilket problem iterationen ska lösa,
- välja relevant återkoppling,
- stoppa irrelevanta eller riskabla spår,
- tillföra lokal kontext,
- avgöra när extern verifiering krävs,
- besluta när resultatet är tillräckligt bra.

AI kan vara både producent och kritiker.

Människan äger fortfarande **kvalitetsdefinitionen och konsekvensen**.

## Så tar du nästa steg

Nästa steg är inte att skriva längre prompts.

Det är att låta AI:n arbeta med **mer av den verkliga kontext som redan finns i arbetet**.

I stället för att kopiera en klass i taget:

> Här är repositoryt. Börja med att kartlägga berörda moduler, tester och dokument innan du föreslår någon förändring.

I stället för att sammanfatta verksamhetsregler manuellt:

> Här är kravdokumenten, processbeskrivningen och beslutshistoriken. Identifiera först motstridiga regler och öppna frågor.

I stället för att beskriva arkitekturen från minnet:

> Här är modellerna och ADR:erna. Bygg en nulägesbild och visa vilka delar av din slutsats som kommer från vilket underlag.

När AI får direkt tillgång till arbetsmaterialet förändras både möjligheten och riskbilden.

Det är fas 5: **Ge kontext**.

## När du inte bör gå vidare

Stanna i fas 4 när:

- du kan ge den nödvändiga kontexten manuellt utan stor kostnad,
- arbetsobjektet är litet,
- den iterativa loopen redan ger tillräcklig kvalitet,
- bredare åtkomst till repositoryn, dokument eller system skulle skapa onödig informationsrisk.

Gå inte vidare till större kontext bara för att verktyget erbjuder en connector.

Och gå inte vidare till delegering bara för att samarbetet fungerar.

Den mogna användaren vet att ett välavgränsat samarbete ofta är bättre än en mer autonom agent.

Fas 4 är därför inte ett övergångssteg som snabbt ska passeras.

För många kvalificerade arbetsuppgifter är **människa och AI i en tydlig återkopplingsloop** en mycket stark slutlig arbetsform.
