# Kapitel 1 – När dialogen blev ett arbetsverktyg

Generativ AI har ofta beskrivits med ord som revolution, paradigmskifte och transformation. Sådana ord blir snabbt tröttande. För den som arbetar med systemutveckling är en mer praktisk fråga bättre:

> Vad är det egentligen som blivit möjligt i vardagsarbetet som inte var lika enkelt tidigare?

Svaret är inte bara att datorn kan skriva text eller kod. Program har kunnat generera text, kod och rapporter länge. Det nya är kombinationen av **språk som gränssnitt, bred generell kunskap, situationsberoende kontext och möjlighet att använda verktyg**.

Tillsammans gör dessa egenskaper att vi kan arbeta med datorn på ett sätt som liknar samarbete mer än traditionell programstyrning.

## Från exakta kommandon till avsikt

Traditionell programvara kräver i regel att användaren uttrycker sig i den struktur som programmet förväntar sig. Ett formulär har bestämda fält. Ett API har ett kontrakt. Ett programspråk har syntax och semantik. Om instruktionen är felaktig får vi ett fel eller ett deterministiskt men oönskat resultat.

En språkmodell fungerar annorlunda. Den kan tolka en instruktion som:

> Läs dessa tre alternativ och hjälp mig förstå vilket som bäst passar ett system med höga krav på spårbarhet och låg operativ komplexitet.

Instruktionen beskriver ett mål och en bedömningssituation snarare än ett exakt program. Modellen försöker tolka vad användaren menar och producera ett användbart svar.

Detta är en viktig anledning till att generativ AI snabbt blir relevant i kunskapsarbete. Många aktiviteter i systemutveckling är svåra att beskriva som algoritmer men lätta att beskriva i vanligt språk:

- sammanfatta ett beslut,
- föreslå alternativ,
- identifiera motsägelser,
- skriva ett första utkast,
- förklara en kodbas,
- hitta tänkbara testfall,
- kritisera en arkitekturskiss,
- jämföra två lösningar,
- omformulera ett krav så att det blir testbart.

Det betyder inte att modellen förstår uppgiften på samma sätt som en människa. Men gränssnittet gör att människan kan uttrycka **avsikten** utan att först programmera varje steg.

## Vad en språkmodell gör – på rätt abstraktionsnivå

Du behöver inte kunna transformerarkitektur eller optimeringsalgoritmer för att använda generativ AI professionellt. Men några egenskaper är viktiga att förstå eftersom de påverkar hur man bör arbeta.

En modern språkmodell genererar svar stegvis utifrån mönster den lärt sig från stora mängder data och den kontext den får i den aktuella interaktionen. Den producerar alltså inte svar genom att slå upp en garanterat korrekt post i en faktadatabas.

Det har flera praktiska konsekvenser.

För det första kan modellen ge olika svar på liknande frågor. För det andra kan den formulera en felaktighet övertygande. För det tredje påverkar den tillgängliga kontexten resultatet kraftigt. För det fjärde kan ett svar vara användbart även när det inte är sant i faktamässig mening – exempelvis som idé, hypotetiskt scenario eller första utkast – medan samma beteende är farligt när uppgiften kräver ett exakt rätt svar.

Det viktiga är alltså inte att memorera hur modellen räknar sannolikheter. Det viktiga är att förstå att **språklig säkerhet inte är samma sak som faktamässig säkerhet**.

Detta är en fundamental skillnad mot verktyg där användaren är van vid att ett välformaterat resultat implicerar att beräkningen är korrekt.

## Prompten är bara början

Ordet *prompt* används ofta för den instruktion eller det material som skickas till modellen. Under den första vågen av generativ AI växte en idé fram om att avancerad användning främst handlade om att skriva mycket bra prompts.

Det finns naturligtvis skicklighet i att ge tydliga instruktioner. Ett konkret mål, relevant bakgrund, begränsningar och önskat format förbättrar ofta resultatet.

Men i professionellt arbete blir det snabbt uppenbart att prompten bara är en del av systemet.

Föreställ dig två sätt att be om hjälp med ett arkitekturbeslut.

**Variant A:**

> Är Kafka eller RabbitMQ bäst?

**Variant B:**

> Vi behöver asynkron kommunikation mellan tre befintliga tjänster. Här är lastprofilen, kravet på ordning, återläsning, operativa kompetensen i teamet och våra befintliga plattformstjänster. Jämför alternativen mot dessa begränsningar, redovisa osäkerheter och peka särskilt ut vilka antaganden som måste verifieras innan beslut.

Skillnaden är inte att variant B innehåller magiska formuleringar. Den innehåller bättre **problembeskrivning och kontext**.

Detta kommer bli allt viktigare längre fram i mognadsresan.

## Kontext är AI:ns arbetsminne

I denna bok använder vi *kontext* för den information modellen har tillgänglig när den utför uppgiften. Det kan vara:

- tidigare meddelanden i konversationen,
- text som användaren klistrar in,
- filer,
- kod från ett repository,
- dokument hämtade via en integration,
- resultat från webbsökning,
- information från verktyg modellen får använda.

En modell kan vara mycket kapabel och ändå ge ett dåligt svar om den saknar rätt kontext.

Det är lätt att misstolka detta som en modellbrist när det egentligen är ett informationsproblem. Om du ber AI bedöma en systemförändring men inte ger den de begränsningar som organisationen arbetar under, kommer modellen fylla luckorna med generella antaganden. De kan vara rimliga och ändå vara helt fel för just ditt system.

Detta är en av anledningarna till att mognadssteg 5 – **Ge kontext** – får en egen plats i boken.

## Från text till multimodalt arbetsmaterial

De första stora språkmodellerna uppfattades huvudsakligen som textverktyg. Moderna AI-assistenter kan i varierande grad arbeta med flera typer av material: text, bilder, skärmbilder, diagram, ljud, strukturerad data och kod.

För systemutveckling spelar detta större roll än det först verkar.

En testare kan visa en skärmbild på ett felaktigt gränssnitt och samtidigt bifoga loggutdrag. En arkitekt kan kombinera en modellbild med en textuell beskrivning av begränsningar. En utvecklare kan ge AI:n kod, stack trace och ett testresultat. En kravanalytiker kan arbeta med intervjutranskript och processbilder.

Detta gör AI till ett mer generellt **arbetsmaterialgränssnitt** snarare än bara ett textfält.

Men multimodalitet ändrar inte den grundläggande kontrollfrågan: modellen kan fortfarande misstolka material, missa detaljer eller dra en plausibel men fel slutsats. Ju rikare materialet blir, desto viktigare blir det att förstå vad som faktiskt låg till grund för resultatet.

## När modellen får använda verktyg

En avgörande förändring inträffar när AI:n inte bara kan svara utan också använda verktyg.

Det kan exempelvis innebära att modellen får:

- söka på webben,
- läsa filer,
- söka i en kodbas,
- köra tester,
- exekvera kod i en sandlåda,
- skapa eller ändra filer,
- använda API:er,
- arbeta med issues eller pull requests,
- hämta information från organisationens system.

Här går gränsen mellan **rådgivning och handling**.

En AI som säger ”du bör ändra denna konfiguration” är ett rådgivande system. En AI som själv ändrar konfigurationen och kör verifieringen är del av utförandet.

Den skillnaden är central för mognadssteg 6 och 7, eftersom verktygsanvändning innebär att fel inte längre bara finns i en text som människan kan ignorera. Ett felaktigt resonemang kan omsättas i en faktisk förändring.

Därför behöver handlingsutrymme alltid följas av kontrollmekanismer.

## Vad betyder agentisk AI?

Begreppet *agent* används mycket brett och inkonsekvent. I den här boken använder vi det pragmatiskt.

En agentisk AI får ett mål, kan planera eller välja flera delsteg, använda verktyg och återkoppla på resultatet av sina egna handlingar innan uppgiften är färdig.

En traditionell chatt kan se ut så här:

1. Människan frågar.
2. AI svarar.
3. Människan gör något.
4. Människan återkommer med resultatet.

Ett mer agentiskt flöde kan vara:

1. Människan beskriver målet och gränserna.
2. AI analyserar repositoryt.
3. AI ändrar kod.
4. AI kör tester.
5. AI läser testfelen.
6. AI justerar implementationen.
7. AI kör tester igen.
8. Människan granskar slutresultatet.

Det är inte nödvändigtvis bättre. Men det är en annan arbetsform.

Stack Overflows Developer Survey 2025 visar dessutom att agentanvändning ännu inte var norm för utvecklare. En majoritet uppgav att de antingen inte använde agenter eller höll sig till enklare AI-verktyg, och 38 procent sade att de inte planerade att använda agenter. [K-007] Det är en nyttig motvikt till en teknisk diskussion där det ibland låter som om full agentisk utveckling redan är standard.

## AI är både kunskapsverktyg och produktionsverktyg

Det är användbart att skilja mellan fyra sorters aktiviteter:

### Information

Du vill veta eller förstå något.

Exempel:

- Vad innebär idempotens?
- Vilka risker finns med denna autentiseringsmodell?
- Hur fungerar property-based testing?

### Artefakt

Du vill få något skapat.

Exempel:

- skriv ett test,
- skapa en ADR,
- formulera acceptanskriterier,
- gör ett utkast till migreringsplan.

### Beslut

Du vill värdera alternativ och välja riktning.

Exempel:

- vilket arkitekturalternativ passar bäst,
- vilken risk bör prioriteras,
- ska vi refaktorera nu eller acceptera skulden?

### Handling

Du vill att något faktiskt genomförs.

Exempel:

- ändra implementationen,
- kör testerna,
- uppdatera dokumentationen,
- skapa en pull request.

Mognadsresan innebär delvis att AI-användningen rör sig mellan dessa kategorier. Men ansvarsfördelningen är olika. Att få ett informationsförslag är en sak. Att låta AI fatta ett beslut eller genomföra en irreversibel handling är något helt annat.

## Varför fel känns annorlunda med generativ AI

Ett kompileringsfel är irriterande men tydligt. Ett AI-fel kan vara farligare just för att det är svårt att upptäcka.

Stack Overflows enkät 2025 fångar denna erfarenhet väl. Den vanligaste frustrationen var AI-lösningar som var ”nästan rätt” – 66 procent av de svarande uppgav detta – och 45 procent angav att felsökning av AI-genererad kod kunde vara mer tidskrävande. [K-007]

Detta är inte samma sak som ett mätresultat av faktisk kodkvalitet. Det är enkätdata om utvecklares upplevelse. Men fenomenet är viktigt: en lösning som är uppenbart fel är lättare att avvisa än en lösning som ser professionell ut, fungerar i enkla fall och innehåller ett subtilt problem.

En mogen arbetsform behöver därför göra fel **synliga och billiga att upptäcka**.

För kod betyder det bland annat tester, statisk analys, review och små förändringsmängder. För krav kan det betyda spårbarhet mot källmaterial och stakeholdergranskning. För arkitektur kan det betyda explicita begränsningar, alternativanalys och beslut som kan ifrågasättas. För faktapåståenden betyder det källkontroll.

## Kritiskt tänkande flyttar snarare än försvinner

En peer-reviewad CHI-studie 2025 undersökte 319 kunskapsarbetare som använde generativ AI minst varje vecka och samlade in 936 konkreta arbetsexempel. Studien bygger på självrapporter, inte objektiva mätningar av tankeförmåga, så slutsatserna ska tolkas därefter. Deltagarna beskrev bland annat hur kritiskt tänkande flyttades från att själv samla information och utföra uppgiften mot att verifiera information, integrera AI-svar och övervaka uppgiftens kvalitet. Högre tilltro till AI:s förmåga var samtidigt kopplad till mindre upplevd kritisk ansträngning. [K-013]

Detta är en bättre mental modell än påståendet att ”AI gör att människor slutar tänka”.

När AI gör en större del av produktionen kan människans kognitiva arbete förskjutas mot **stewardship**: att definiera mål, kontrollera antaganden, verifiera resultat och förstå konsekvenser.

Men förskjutningen sker inte automatiskt. Om användaren bara accepterar välformulerade svar har inget moget samarbete uppstått.

## Ett nytt slags verktyg kräver ett nytt slags verktygsvana

När en såg blir vassare behöver snickaren inte omförhandla arbetsfördelningen mellan människa och verktyg. När en kompilator blir snabbare påverkas utvecklingsprocessen, men kompilatorn börjar inte själv välja vilket problem den ska lösa.

Generativ AI är annorlunda eftersom gränsen mellan instruktion och utförande är mjukare.

Du kan be den:

> Förklara detta.

eller:

> Föreslå ett alternativ.

eller:

> Skriv ett första utkast.

eller:

> Granska mitt utkast.

eller:

> Här är hela projektet – föreslå vad som behöver ändras.

eller:

> Genomför förändringen och verifiera den.

Det är samma grundteknik men helt olika arbetsfördelning.

Därför blir den viktigaste AI-kompetensen inte att känna till alla funktioner. Det blir att kunna **designa interaktionen mellan människa, modell, kontext och verktyg**.

## Reflektion: vad består ditt arbete av?

Titta på några uppgifter du gjorde den senaste veckan och dela dem i fyra kategorier:

- information,
- artefakter,
- beslut,
- handlingar.

För varje uppgift, fråga sedan:

1. Vilken del skulle en AI-assistent kunna hjälpa till med redan i dag?
2. Vilken kontext skulle den behöva?
3. Vad skulle vara dyrast att få fel?
4. Hur skulle du verifiera resultatet?


