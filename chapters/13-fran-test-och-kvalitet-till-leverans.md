# Kapitel 13 – Från test och kvalitet till leverans

Statusnotiserna är nu implementerade i en branch.

Builden går igenom.

Ett antal nya tester är gröna.

Är förändringen klar?

Det är en av de viktigaste frågorna i AI-assisterad systemutveckling, eftersom generativ AI gör det mycket lättare att skapa **både implementation och bevisliknande artefakter**.

En agent kan på kort tid producera:

- kod,
- enhetstester,
- integrationstester,
- testdata,
- release notes,
- en sammanfattning som säger att allt ser bra ut.

Men mängden producerat material är inte samma sak som graden av förtroende.

I det här kapitlet avslutar vi den vertikala spårbarhetskedjan:

> **behov → beslut → förändring → bevis**

## Tester är inte bevis bara för att de är gröna

Anta att AI:n genererar tjugo nya tester för notifieringsfunktionen och rapporterar 95 procent branch coverage.

Det låter tryggt.

Men coverage svarar främst på frågan:

> Vilka delar av koden exekverades av testerna?

Den svarar inte automatiskt på:

- om rätt beteende verifierades,
- om assertionerna är meningsfulla,
- om edge cases täcks,
- om testet skulle upptäcka en relevant defekt,
- om felhantering och race conditions fungerar,
- om implementationen överensstämmer med verksamhetsbehovet.

En systematisk litteraturöversikt från 2026 analyserade 38 peer-reviewade studier om LLM-baserad testgenerering. Den fann potential att öka hastighet och coverage men också stor variation i metoder, dataset och integration. Författarna lyfter flera typer av utvärderingsmått, däribland exekveringskorrekthet och mutation score, snarare än att behandla coverage som ett komplett kvalitetsmått. [K-062]

Tidigare i boken såg vi också en studie där mer relevant kontext och flerturnsarbete förbättrade genererade tester samtidigt som hög branch coverage inte motsvarade lika hög mutation score. [K-037]

Det leder till en enkel princip:

> **AI kan generera testmängd. Teamet måste fortfarande skapa testförtroende.**

## Testarbete genom mognadsresan

### Fas 1: Fråga

> Vilka testfall bör finnas för statusnotiser?

AI kan ge en bra generell checklista:

- normal leverans,
- inga prenumeranter,
- felaktig e-postadress,
- leveransfel,
- användare utan behörighet,
- dubbla händelser,
- avregistrering.

Det är användbart men generellt.

### Fas 2: Resonera

> Vilka risker är viktigast i just den här designen? Vilka fel kan ge störst konsekvens?

Nu kan AI hjälpa till med riskbaserad testdesign.

För scenariot kan den identifiera att ett allvarligare fel inte är ”e-post skickas inte” utan exempelvis:

> en användare får en notis om ett ärende som personen inte längre har behörighet att se.

Det förändrar testprioriteringen.

### Fas 3: Skapa

AI genererar konkreta testfall, testkod, fixtures eller syntetiska testdata.

Här gäller samma artefaktprincip som tidigare:

Testet måste ha ett kvalitetskriterium.

Det räcker inte att det kompilerar.

### Fas 4: Samarbeta

En människa granskar testerna och pekar på luckor:

> Du testar behörighet när prenumerationen skapas, men inte när behörigheten tas bort efteråt. Lägg till scenarier för det och för retry efter ett tillfälligt e-postfel.

AI:n reviderar testsviten.

Detta är ofta mycket effektivare än att försöka beskriva alla testfall perfekt i första prompten.

### Fas 5: Ge kontext

AI får tillgång till:

- krav och acceptanskriterier,
- ADR och ändringsplan,
- implementation,
- befintliga testmönster,
- historiska buggar,
- CI-resultat.

Nu kan den analysera **testgap mot verklig förändring** i stället för att generera generella tester.

### Fas 6: Delegera

> Analysera diffen mot kravpaket och ADR. Identifiera saknade testfall, implementera tester inom befintlig teststruktur, kör relevanta sviter och stanna om ett fel tyder på att kravet eller designen är motsägelsefull.

AI:n får ett mål och en verifieringsuppgift, men inte mandat att skriva om kravet för att få testerna gröna.

### Fas 7: Orkestrera

I ett moget flöde kan varje pull request automatiskt ge:

1. deterministisk build och statisk analys,
2. riskklassificering av förändringen,
3. val av relevanta testsviter,
4. AI-assisterad analys av krav- och designtäckning,
5. testgenerering för identifierade luckor,
6. deterministisk exekvering,
7. mänsklig review för definierade risker,
8. releasebeslut och återkoppling efter leverans.

Mognaden är inte att AI kör fler tester.

Mognaden är att **kvalitetssystemet är designat för den högre förändringstakten**.

## När AI ska avgöra om något är testbart

En intressant svårighet uppstår när AI inte bara genererar tester utan också avgör **vilka regler som är tillämpliga**.

En peer-reviewad studie från 2026 undersökte LLM:er för automatiserad compliance testing av webbtillgänglighet över 39 kriterier. Modellerna hade betydande problem med att avgöra när vissa kriterier faktiskt var tillämpliga och forskarna bedömde human-in-the-loop som lämplig användningsform. [K-065]

Detta är relevant långt utanför tillgänglighet.

I testarbete finns två separata frågor:

1. Kan AI genomföra kontrollen korrekt?
2. Vet AI **när kontrollen ska användas och hur resultatet ska tolkas?**

Den andra frågan glöms lätt bort.

Ett testverktyg kan vara utmärkt på att kontrollera en invariant men ändå användas på fel systemtillstånd, fel version eller fel krav.

## Bevis ska kopplas till beslut

Det genomgående scenariot hade flera explicita beslut.

Låt oss koppla dem till bevis:

| Beslut | Exempel på bevis |
|---|---|
| Bara definierade statusövergångar skickar notis | domäntester + integrationstest |
| Aktuell behörighet ska gälla | scenarier där behörighet tas bort efter prenumeration |
| Leveransfel får inte blockera statusändring | fault-injection/integrationstest |
| E-post är första kanal | API- och UI-test för kanalval; inga oimplementerade kanaler exponeras |
| Prenumeration är per ärende | persistens- och behörighetstest över flera ärenden |

Nu blir testningen mer än en separat aktivitet efter kodning.

Den blir sista länken i spårbarheten.

Detta är också ett bra område för AI, eftersom modeller är bra på att jämföra flera text- och kodartefakter och identifiera möjliga luckor.

Men själva kontrollen bör så långt möjligt göras med **exekverbara och observerbara mekanismer**.

## AI kan skapa fel snabbare – och hitta dem snabbare

Det är lätt att beskriva generativ AI som antingen produktionsverktyg eller kvalitetsverktyg.

I verkligheten är den båda.

Samma kapabilitet som gör det möjligt att skapa en stor kodförändring snabbt kan användas för att:

- analysera diffen,
- skapa testidéer,
- hitta inkonsistens mot krav,
- föreslå regressionsområden,
- sammanfatta fel,
- prioritera review.

Men det finns en asymmetri.

Om AI producerar tio gånger mer förändring och bara dubbelt så mycket effektiv verifiering kan kvalitetssystemet ändå bli överbelastat.

Det är därför produktivitet inte kan mätas bara där koden skapas.

## Lokal hastighet kontra värdeflöde

DORA:s 2025-rapport bygger på data från nära 5 000 teknikprofessionella och beskriver AI som en förstärkare av befintliga organisatoriska förmågor. Rapporten betonar bland annat value stream management, plattformar och grundförmågor för att lokala AI-vinster ska ge bättre produktutfall. [K-063]

Detta är leverantörsproducerad branschforskning, inte ett oberoende randomiserat experiment. Men observationen passar väl med den bredare evidens som boken redan diskuterat:

> **Om implementation blir snabbare men review, test, säkerhetsbedömning eller release blir flaskhalsen har systemet inte nödvändigtvis blivit snabbare.**

I värsta fall skapas en växande kö av nästan färdiga förändringar.

Moget AI-arbete behöver därför mäta hela flödet.

## Vad ska en AI-assisterad kvalitetsgrind göra?

En dålig kvalitetsgrind säger:

> AI har granskat koden: godkänd.

En bättre grind bryter upp frågan.

### Deterministiskt

- bygger koden?
- går obligatoriska tester?
- passerar definierade statiska regler?
- är migrationsfiler syntaktiskt giltiga?

### AI-assisterat

- verkar diffen omfatta något utanför scope?
- finns det en möjlig lucka mellan krav och test?
- har ett ADR-påverkat område ändrats utan dokumentationsuppdatering?
- vilka delar av diffen är mest riskvärda för mänsklig review?

### Mänskligt

- är trade-offen acceptabel?
- är återstående risk rimlig?
- är den observerade evidensen tillräcklig för denna typ av förändring?
- ska den levereras nu?

Detta är återigen orkestrering: olika former av kontroll gör det de är bäst lämpade för.

## Releaseunderlaget kan genereras – beslutet måste fortfarande ägas

AI kan med fördel skapa ett första releaseunderlag:

- vad som ändrats,
- vilka krav som berörs,
- vilka tester som körts,
- kända begränsningar,
- migrationssteg,
- rollbackinformation,
- observability som bör följas efter release.

Om informationen hämtas direkt från pull request, CI, testresultat och beslut kan detta vara betydligt bättre än ett manuellt dokument som skrivs i efterhand.

Men underlaget bör skilja mellan:

- **observerat faktum** – test X kördes och passerade,
- **AI-bedömning** – diffen verkar ha låg påverkan på modul Y,
- **mänskligt beslut** – återstående risk accepteras för release.

Det är evidenspolicyn från början av boken tillämpad på själva utvecklingsprocessen.

## Efter leverans fortsätter beviskedjan

Ett moget kvalitetssystem slutar inte vid deploy.

För statusnotiser kan teamet följa:

- leveransfel,
- retry-frekvens,
- latens från statusändring till notis,
- antal avregistreringar,
- supportärenden,
- felaktiga eller dubbla notiser.

AI kan hjälpa till att sammanfatta och korrelera observationer.

Men även här behöver den få rätt kontext och rätt fråga.

> Sammanfatta alla loggar

är sämre än:

> Jämför de första 24 timmarna efter release med våra definierade risker. Identifiera avvikelser som kan indikera brott mot acceptanskriterier eller antaganden i ADR:n. Ange vilken telemetry varje slutsats bygger på.

Det är skillnaden mellan information och evidens.

## När flödet lär sig

På fas 7 kan återkopplingen efter release påverka nästa förändring.

Exempel:

1. AI ser att många leveransfel kommer från tillfälliga timeoutfel.
2. Den kopplar detta till det tidigare designbeslutet om retry.
3. Den visar att nuvarande retry-policy inte möter den observerade profilen.
4. Teamet beslutar om en förändring.
5. Nya tester och observability-kriterier skapas.

Arbetsflödet blir då inte bara automatiserat.

Det blir **lärande**.

Det är en viktig skillnad mellan ett script och ett moget AI-assisterat arbetssystem.

## Del III:s viktigaste slutsats

Vi började med ett enda, ganska vardagligt behov:

> användaren vill få statusnotiser.

Genom tre kapitel har vi sett att den mogna AI-användningen inte främst består av en serie smarta prompts.

Den består av att hålla ihop:

> **behov → beslut → förändring → bevis**

På låg mognadsnivå hjälper AI till lokalt:

- formulera ett krav,
- föreslå ett mönster,
- skriva kod,
- generera ett test.

På högre mognadsnivå hjälper AI till att **bevara sambanden mellan aktiviteterna**:

- varför gör vi detta,
- vilket beslut togs,
- vad ändrades,
- hur vet vi att förändringen blev rätt?

Det är där utvecklingsprocessen börjar förändras på riktigt.

## Men människans roll försvinner inte

Tvärtom blir vissa frågor tydligare:

- Vem avgör vilket behov som är viktigast?
- Vem accepterar ett arkitekturtrade-off?
- Vem bedömer att evidensen räcker?
- Vem tar ansvar när ett beslut får konsekvenser?

När AI kan producera fler förslag, mer kod och fler tester blir dessa frågor inte mindre viktiga.

De blir mer koncentrerade.

Det leder direkt till Del IV.

Nästa kapitel handlar därför inte om ännu en teknisk AI-funktion.

Det handlar om **vad människan fortfarande måste vara bra på när allt mer av produktionen kan delas med AI**.

## Så tar du nästa steg

För en verklig förändring i ditt team:

1. börja med de godkända behovs- och designbesluten,
2. definiera vilket bevis som behövs för varje viktigt beslut,
3. låt AI analysera luckor mellan krav, kod och test,
4. använd deterministiska verktyg för kontroller som kan göras deterministiskt,
5. använd AI för riskanalys, testidéer och sammanhang,
6. håll releasebeslut och större riskacceptans tydligt ägda,
7. följ upp efter leverans och mata observationerna tillbaka till nästa förändring.

## När du inte bör gå vidare

Öka inte automatiseringen av kvalitet och leverans när:

- testsviten ger dåligt förtroende redan utan AI,
- teamet förlitar sig på coverage som huvudsakligt kvalitetsbevis,
- krav och designbeslut inte är spårbara,
- AI-granskning används som enda review,
- releaseprocessen saknar tydligt ansvar,
- observability är för svag för att upptäcka fel efter leverans.

Det mest mogna AI-arbetssättet är inte det som producerar snabbast.

Det är det som kan **förklara varför en förändring är värd att göra, varför den ser ut som den gör och varför vi har tillräckligt förtroende för att släppa den**.
