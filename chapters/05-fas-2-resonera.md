# Kapitel 5 – Fas 2: Resonera

Den stora förändringen i fas 2 sker när AI slutar vara en maskin som förväntas leverera rätt svar och börjar fungera som en **motpart i ett resonemang**.

Det låter som en liten skillnad.

I praktiken förändrar det nästan hela arbetssättet.

Frågan är inte längre bara:

> Vad är rätt?

utan:

> Hur kan jag tänka om detta?

För utvecklare, testare, kravanalytiker och arkitekter är det ofta här AI börjar bli betydligt mer användbar än en förbättrad sökruta.

## Många professionella problem har inget facit

Systemutveckling består visserligen av många faktauppgifter.

Ett API finns eller finns inte. En testsvit passerar eller misslyckas. Ett syntaxfel kan ofta ha en tydlig orsak.

Men mycket av det kvalificerade arbetet är annorlunda.

Ska den här funktionen ligga i den befintliga tjänsten eller i en ny?

Är kravet tillräckligt tydligt?

Vilken teststrategi ger bäst riskreduktion för tiden vi har?

Vilket arkitekturalternativ ger rimligast balans mellan förändringsbarhet, komplexitet och driftskostnad?

Bör vi refaktorera nu eller acceptera den tekniska skulden?

Här finns sällan ett universellt korrekt svar.

Det finns:

- mål,
- begränsningar,
- antaganden,
- risker,
- trade-offs,
- och information vi ännu saknar.

AI:s styrka blir då inte bara att känna till mycket, utan att snabbt kunna generera och strukturera flera perspektiv.

## Från ”ge mig svaret” till ”hjälp mig se problemet”

Antag att ett team överväger att införa asynkron kommunikation mellan två system.

En fas 1-fråga kan vara:

> Vilka fördelar har event-driven architecture?

En fas 2-dialog kan börja så här:

> Vi har två tjänster där beställningsflödet idag använder synkrona REST-anrop. Vi har problem med koppling och tillgänglighet men behöver samtidigt snabb återkoppling till användaren. Hjälp mig identifiera vilka beslutskriterier som är viktigast innan vi väljer mellan fortsatt synkron kommunikation, köbaserad asynkronitet och eventdriven arkitektur.

Skillnaden är central.

I det andra fallet ber du inte modellen välja åt dig. Du ber den hjälpa dig **strukturera beslutet**.

Det är ofta en bättre användning av AI.

## AI som generator av alternativ

Människor är bra på många saker men vi fastnar lätt i den första lösning som känns rimlig.

AI kan billigt producera alternativa perspektiv.

För en utvecklare:

> Ge tre olika refaktoreringsstrategier för den här komponenten. Optimera en för minimal förändring, en för testbarhet och en för långsiktig modularitet.

För en testare:

> Analysera kravet ur ett riskbaserat testperspektiv. Vilka felmoder är mest kostsamma även om de är mindre sannolika?

För en kravanalytiker:

> Vilka alternativa tolkningar kan olika intressenter göra av detta krav?

För en arkitekt:

> Ta fram tre arkitekturalternativ och gör trade-offs explicita. Undvik att rekommendera något innan du har identifierat vilken ytterligare information som skulle kunna ändra bedömningen.

I samtliga fall ökar värdet eftersom AI:n breddar sökrymden.

Men fler alternativ är inte automatiskt bättre beslut.

Det krävs fortfarande mänskligt omdöme.

## Resonemang är inte samma sak som korrekt resonemang

Språkmodeller kan producera resonemang som ser övertygande ut men bygger på felaktiga premisser.

Det gäller särskilt när modellen själv fyller i sådant som aldrig angavs.

Antag att en arkitekt frågar:

> Bör vi använda Kafka eller RabbitMQ?

AI:n kan ge ett elegant jämförelsesvar.

Men utan kontext vet den kanske inget om:

- organisationens befintliga kompetens,
- driftsplattform,
- licens- och supportkrav,
- krav på ordering,
- trafikvolym,
- återspelning,
- redan gjorda strategiska beslut.

Svaret kan därför vara välargumenterat och ändå irrelevant.

I fas 2 blir en central färdighet att skilja mellan **argumentets form** och **premissernas kvalitet**.

Fråga därför:

> Vilka antaganden gör du i den här bedömningen?

Det är en av de mest kraftfulla följdfrågorna i AI-assisterat arbete.

## Kritiskt tänkande försvinner inte – det flyttar

En vanlig oro är att AI gör människor passiva.

Det finns skäl att ta frågan på allvar, men forskning ger en mer nyanserad bild.

**Forskningsresultat – kritiskt tänkande i kunskapsarbete:** En CHI 2025-studie med 319 kunskapsarbetare samlade 936 verkliga exempel på generativ AI i arbetsuppgifter. Högre tilltro till AI var associerad med mindre upplevd kritisk ansträngning, medan högre tilltro till den egna kompetensen var associerad med mer kritiskt tänkande. Forskarna såg samtidigt att kritiskt tänkande förändrade form: från produktion av innehåll mot verifiering av information, integrering av svar och styrning av uppgiften. [K-013]

Detta passar väl med bokens mognadsmodell.

Mogen AI-användning innebär inte att människan tänker mindre.

Den kan innebära att människan behöver tänka **på en högre styrnivå**.

I stället för att formulera varje stycke själv behöver användaren avgöra:

- om premisserna är rimliga,
- om viktiga perspektiv saknas,
- om underlaget stödjer slutsatsen,
- om svaret passar den verkliga kontexten,
- och vilken del som måste verifieras externt.

Det är en annan kognitiv arbetsfördelning.

## Överdriven tillit är en egen risk

Ett övertygande AI-svar påverkar människor även när rådet är inkonsekvent eller felaktigt.

**Forskningsresultat – påverkan av AI-råd:** Experiment i Scientific Reports har visat att ChatGPT-råd kan påverka mänskliga beslut även när råden varierar mellan körningar. En annan serie experiment inom personalurval visade att felaktiga AI-råd kunde försämra mänskliga beslut och att förklaringar av rådet inte i sig eliminerade problemet. [K-033, K-034]

Dessa studier handlar inte om systemutveckling och resultaten ska därför inte generaliseras rakt av till kod eller arkitektur.

Men mekanismen är relevant:

> En förklaring kan göra ett råd mer begripligt utan att göra det mer korrekt.

Det är lätt att blanda ihop transparens med sanning.

Ett välstrukturerat resonemang ska därför bedömas mot underlaget, inte mot hur intelligent det låter.

## Använd AI för att argumentera emot sig själv

Ett enkelt sätt att förbättra resonemanget är att separera olika roller i dialogen.

Först:

> Föreslå den lösning du anser är mest rimlig utifrån underlaget.

Sedan:

> Agera nu som en skeptisk reviewer. Vilka svagheter, dolda antaganden och missade konsekvenser finns i förslaget?

Och därefter:

> Revidera rekommendationen med hänsyn till kritiken. Markera vilka frågor som fortfarande inte går att avgöra från underlaget.

Detta garanterar inte korrekthet. Modellen kan reproducera samma blinda fläck i flera roller.

Men arbetsformen gör två saker:

1. den motverkar att första svaret får oproportionerligt stor auktoritet,
2. den gör antaganden och osäkerheter mer synliga för människan.

Det är ofta tillräckligt för att förbättra kvaliteten på den mänskliga bedömningen.

## Be om beslutskriterier före rekommendationen

Ett återkommande misstag är att fråga efter rekommendationen för tidigt.

> Vilken databas ska vi välja?

> Vilken autentiseringslösning är bäst?

> Ska vi bygga eller köpa?

En bättre ordning är:

1. Vilka kriterier bör styra beslutet?
2. Vilka kriterier är viktigast i vår kontext?
3. Vilken information saknas?
4. Hur presterar alternativen mot kriterierna?
5. Vilken rekommendation följer – och hur känslig är den för antagandena?

Den ordningen är inte specifik för AI. Det är god beslutsmetodik.

AI gör den bara billigare att genomföra konsekvent.

## Resonera med explicita perspektiv

En annan teknik är att be modellen analysera samma problem från flera professionella perspektiv.

För ett nytt API:

- utvecklarperspektiv,
- driftperspektiv,
- säkerhetsperspektiv,
- testperspektiv,
- konsumentperspektiv.

För ett krav:

- verksamhetsnytta,
- användbarhet,
- dataskydd,
- testbarhet,
- arkitekturell påverkan.

Det betyder inte att modellen ersätter personer med dessa roller.

En säkerhetsarkitekt har domänkunskap, ansvar och lokal kontext som modellen kan sakna.

Men perspektivväxlingen fungerar som en **checklista-generator**. Den hjälper dig upptäcka vilka frågor som borde tas vidare till rätt människa eller källa.

## Använd AI för att hitta vad du inte vet

Ett av de mest värdefulla resonemangsmönstren är att fråga efter informationsluckor.

> Vilka fem frågor behöver besvaras innan vi kan fatta ett robust beslut?

eller:

> Vilken information skulle, om den visade sig vara annorlunda än vi antar, kunna ändra rekommendationen mest?

Detta flyttar fokus från svar till **informationsvärde**.

För arkitekturarbete är det särskilt kraftfullt.

I stället för att lägga en timme på att diskutera ett elegant alternativ kan teamet upptäcka att beslutet egentligen beror på en enda oklar sak – exempelvis om data måste kunna återspelas, om systemet måste fungera offline eller om ett visst avtal tillåter vald driftform.

AI används då för att prioritera vad människan ska undersöka härnäst.

## Resonera över osäkerhet

Många AI-svar låter mer precisa än underlaget motiverar.

Det kan motverkas genom att explicit efterfråga osäkerhet.

Exempel:

> Rangordna inte bara alternativen. Ange vilka antaganden som bär slutsatsen och beskriv ett scenario där det lägre rankade alternativet skulle bli bättre.

eller:

> Vilka delar av ditt resonemang bygger direkt på information jag gav, och vilka delar är generella antaganden?

Detta är en viktig övergång från fas 1.

I fas 1 verifierar vi främst **fakta**.

I fas 2 behöver vi även verifiera **resonemangets struktur**.

## Resonemang med kod

För en utvecklare kan fas 2 se ut så här:

I stället för:

> Hur fixar jag den här metoden?

fråga:

> Här är metoden, de relevanta testerna och felet. Identifiera tre möjliga orsaker. Rangordna dem efter sannolikhet, ange vilken observation som stödjer varje hypotes och föreslå det minsta testet jag kan göra för att falsifiera den mest sannolika hypotesen.

Detta förvandlar AI:n från kodgenerator till felsökningspartner.

Det är ofta bättre eftersom människan behåller förståelsen för vad som händer.

Samma mönster fungerar i incidentanalys:

> Separera observerade fakta från hypoteser. Vilken ytterligare telemetri skulle mest effektivt skilja hypoteserna åt?

Det är ett moget resonemangssätt även innan AI får tillgång till systemen själv.

## Resonemang med krav

Antag detta krav:

> Systemet ska snabbt visa kundens aktuella saldo.

AI kan direkt skriva om det till något mer precist.

Men i fas 2 är det bättre att först fråga:

> Vilka tvetydigheter finns i formuleringen? Vilka stakeholderfrågor behöver besvaras innan vi kan göra kravet testbart? Vilka icke-funktionella krav kan gömma sig bakom ordet ”snabbt”?

Nu används AI för kravanalys snarare än textproduktion.

Det kommer göra fas 3 – Skapa – mycket bättre, eftersom det som senare genereras bygger på ett mer genomtänkt problem.

## Resonemang med test

En testare kan använda AI för att bredda riskbilden:

> Vi inför möjlighet att ändra leveransadress efter lagd beställning. Vilka felmoder bör vi prioritera om vi utgår från ekonomisk skada, integritetsrisk, kundpåverkan och sannolikhet?

Därefter:

> Vilka av dessa risker fångas sannolikt inte av vanliga happy-path-tester?

AI:n har då inte fått skapa testfallen ännu.

Den hjälper till att formulera vad kvalitet betyder.

Det är en viktig skillnad.

## Resonemang med arkitektur

Arkitekturarbete innehåller ofta konkurrerande kvalitetsattribut.

Ett system kan optimeras för:

- låg kostnad,
- hög tillgänglighet,
- enkel förvaltning,
- självständiga team,
- kort time-to-market,
- stark styrning,
- låg teknisk komplexitet.

Alla kan sällan maximeras samtidigt.

En bra fas 2-fråga är därför:

> Vilka trade-offs verkar vi göra med den här lösningen? Vilka av dem är explicita beslut och vilka verkar bara ha uppstått implicit?

Det senare är särskilt viktigt.

AI kan hjälpa till att göra **osynliga beslut synliga**.

## När resonemang blir pseudoanalys

Det finns en risk i andra riktningen.

Eftersom AI kan producera argument, tabeller, risklistor och alternativ på sekunder kan analysen bli större utan att bli bättre.

Tio alternativ är inte bättre än tre om sju är irrelevanta.

En riskmatris med 40 rader är inte bättre än fem välgrundade risker.

En arkitekturjämförelse med 17 kriterier är inte bättre om ingen vet vilka fyra som faktiskt styr beslutet.

Mogen fas 2-användning handlar därför även om **kompression**.

Fråga:

> Vilka tre faktorer är mest beslutspåverkande?

> Vilka två antaganden är mest osäkra?

> Vilken invändning skulle vara starkast mot din egen rekommendation?

AI:s förmåga att producera mer måste kombineras med människans förmåga att välja vad som betyder något.

## Bokens syntes: fyra roller för AI i resonemang

Boken använder fyra återkommande resonemangsroller som pedagogiskt stöd. De är **bokens egen syntes**, inte en etablerad vetenskaplig fyrfältsmodell.

### Bredda

Generera fler perspektiv, alternativ och risker än du själv spontant ser.

### Strukturera

Ordna problemet i kriterier, antaganden, beroenden och beslutspunkter.

### Utmana

Argumentera emot, sök motexempel och identifiera svaga premisser.

### Fokusera

Reducera analysen till de frågor och faktorer som faktiskt styr nästa beslut.

En bra fas 2-dialog växlar ofta mellan alla fyra.

## Vad människan ansvarar för

AI kan föreslå ett beslutskriterium.

Människan måste avgöra om kriteriet spelar roll i organisationen.

AI kan identifiera en möjlig risk.

Människan måste avgöra om risken är verklig och hur allvarlig den är.

AI kan jämföra arkitekturalternativ.

Människan måste säkerställa att underlaget, begränsningar och konsekvenser är rätt representerade.

Det är därför fas 2 inte handlar om att ”låta AI tänka åt dig”.

Den handlar om att använda AI för att **göra ditt eget tänkande mer explicit, bredare och lättare att granska**.

## Så tar du nästa steg

Nästa steg är att låta AI skapa ett faktiskt arbetsresultat.

Men gör inte övergången för tidigt.

Innan du säger:

> Skriv ADR:en.

prova först:

> Vilka beslutskriterier och trade-offs måste ADR:en göra explicita?

Innan du säger:

> Generera testerna.

prova:

> Vilka kvalitetsrisker är viktigast och vilka testnivåer lämpar sig för dem?

Innan du säger:

> Implementera förändringen.

prova:

> Vilka alternativa implementationer finns, vad påverkar de och vilken information saknas innan vi väljer?

När resonemanget är tillräckligt stabilt kan AI:n börja skapa artefakten.

Det är fas 3.

## När du inte bör gå vidare

Gå inte vidare till produktion bara för att AI:n har levererat en elegant analys.

Stanna och verifiera när:

- beslutsunderlaget innehåller osäkra fakta,
- konsekvenserna är stora,
- viktiga stakeholders inte är representerade,
- modellen saknar lokal kontext,
- rätt beslut beror på information som ännu inte finns.

Ibland är nästa steg inte att be AI göra mer.

Det är att fråga en människa, öppna dokumentationen, köra ett experiment eller samla in data.

Det är också mogen AI-användning.
