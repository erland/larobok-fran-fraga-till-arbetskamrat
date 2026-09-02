# Kapitel 16 – Från individuell AI-användning till AI-assisterat arbetssystem

AI-resan börjar ofta med individen.

En utvecklare upptäcker att AI kan förklara en obekant kodbas.

En testare börjar få hjälp att hitta kantfall.

En arkitekt använder AI för att jämföra alternativ.

En kravanalytiker låter AI hjälpa till att strukturera ett otydligt behov.

Efter ett tag händer något annat.

Individen har blivit bättre på att använda AI än organisationen är på att ta emot arbetssättet.

Det märks när samma person behöver:

- använda privata konton eftersom godkända verktyg saknas,
- kopiera information manuellt mellan system,
- själv bedöma vilken data som får användas,
- bygga egna evals och kvalitetskontroller,
- förklara sitt arbetssätt från början för varje kollega,
- arbeta runt processer som är utformade för en tid då AI inte fanns.

Då är nästa mognadsfråga inte längre:

> Hur blir jag bättre på AI?

Den blir:

> **Hur behöver arbetssystemet förändras för att moget AI-arbete ska bli möjligt, säkert och reproducerbart?**

Detta är bokens sista perspektivskifte.

Från individens repertoar till organisationens förmåga att absorbera den.

## Individuell produktivitet förändrar inte automatiskt systemet

Det finns experimentell evidens för att AI kan spara tid för enskilda kunskapsarbetare utan att arbetsorganisationen förändras i motsvarande grad.

Dillon med flera genomförde ett randomiserat fältexperiment över 66 företag och 7 137 kunskapsarbetare. De som faktiskt använde det integrerade AI-verktyget lade i experimentets senare del ungefär två timmar mindre per vecka på e-post och arbetade mindre utanför ordinarie arbetstid. Forskarna fann däremot inga tydliga förändringar i mängden eller sammansättningen av arbetsuppgifter som följd av individuell AI-tillgång. [K-085]

Det är ett viktigt resultat för den här boken.

Om en utvecklare kan implementera en förändring snabbare men:

- kodgranskningen har samma kapacitet som tidigare,
- testmiljön är en flaskhals,
- säkerhetsgranskning fortfarande sker manuellt i slutet,
- releaseprocessen bara körs på torsdagar,

så blir inte systemets genomloppstid automatiskt lika mycket bättre som utvecklarens lokala produktivitet.

Samma princip gäller tidigare i flödet.

En kravanalytiker kan generera fler utkast utan att besluten fattas snabbare.

En arkitekt kan analysera fler alternativ utan att organisationen blir bättre på att välja.

En testare kan skapa fler testfall utan att felupptäckande förmåga förbättras.

Mogen AI-användning på organisationsnivå handlar därför mindre om att göra varje individ maximalt effektiv och mer om att förbättra **hela värdeflödet**.

## AI kan förändra hur expertis kombineras

AI förändrar inte bara hur snabbt människor arbetar. Den kan även förändra vem som kan bidra med vad.

I ett preregistrerat fältexperiment med 791 professionella vid Procter & Gamble studerade Dell'Acqua med flera verkliga produktinnovationsuppgifter. Individer med AI nådde i den studerade uppgiften prestation i nivå med tvåpersonsteam utan AI. Dessutom minskade skillnaden mellan tekniskt och kommersiellt orienterade lösningar: deltagare med olika yrkesbakgrund producerade mer balanserade förslag när de använde AI. Forskarna fann samtidigt att mänskligt omdöme fortsatt hade ett värde i den utvärderande selektionen. [K-086]

Det betyder inte att AI ersätter team.

Men det antyder att organisationer behöver tänka om kring två frågor:

1. **Vilken expertis måste finnas i varje arbetsmoment?**
2. **Vilken expertis kan göras tillgänglig genom AI-stöd, gemensam kontext och väl utformade kontrollpunkter?**

För systemutveckling kan det innebära att en utvecklare tidigare i arbetet kan testa resonemang ur test-, säkerhets- eller arkitekturperspektiv.

Det kan också innebära att en arkitekt snabbare kan komma nära koden och verifiera om ett designantagande verkligen stämmer.

Men det finns en avgörande skillnad mellan att **få tillgång till ett perspektiv** och att **äga kompetensen eller ansvaret** för området.

AI kan hjälpa en utvecklare att ställa bättre säkerhetsfrågor.

Det gör inte automatiskt utvecklaren till säkerhetsexpert.

## När individen springer snabbare än organisationen

Microsofts Work Trend Index 2026 beskriver en intressant organisatorisk obalans. I deras globala survey klassificerades endast 19 procent av AI-användarna i en grupp där både individuell AI-förmåga och organisatorisk beredskap var höga. Ytterligare 10 procent hade hög individuell förmåga men låg organisatorisk beredskap – ett läge rapporten kallar *blocked agency*. [K-087]

Detta är leverantörsproducerad surveydata, inte ett kausalt forskningsresultat.

Men mönstret är lätt att känna igen organisatoriskt.

En medarbetare kan vara redo att:

- ge AI projektkontext,
- delegera flerledade uppgifter,
- arbeta med agentiska verktyg,
- skapa återkommande AI-assisterade flöden,

samtidigt som organisationen fortfarande bara har en regel som säger:

> Använd AI med försiktighet.

Det är för lite styrning för moget arbete.

Men motsatsen är också möjlig.

Organisationen kan investera i en avancerad enterpriseplattform, centrala modeller och agentinfrastruktur medan användarna fortfarande främst frågar AI om syntax.

Därför bör vi inte prata om en enda organisatorisk mognadsnivå som om alla delar utvecklades samtidigt.

Precis som individen kan organisationen vara ojämnt mogen.

## Sex delar i ett AI-assisterat arbetssystem

För att knyta ihop boken använder vi här en sista modell.

Den är **bokens egen syntes**, inte ett etablerat forskningsramverk.

Ett AI-assisterat arbetssystem behöver sex saker som förstärker varandra:

1. **Riktning** – var AI ska skapa värde och var den inte ska användas.
2. **Miljö** – godkända tjänster, modeller, data, verktyg och integrationer.
3. **Arbetsdesign** – hur människor, AI och automation samarbetar i konkreta flöden.
4. **Kontroll** – behörigheter, informationsstyrning, ansvar och spårbarhet.
5. **Kvalitet** – testning, evals, kvalitetsgrindar och uppföljning.
6. **Lärande** – hur erfarenheter fångas, delas och förbättrar nästa iteration.

Ingen av delarna är särskilt revolutionerande ensam.

Det viktiga är att de fungerar tillsammans.

### 1. Riktning: vad försöker vi förbättra?

En organisation kan köpa AI-verktyg utan att veta vilket problem de ska lösa.

Då blir användning lätt ett mål i sig.

Det kan leda till mätetal som:

- antal aktiva AI-användare,
- antal prompts,
- mängd genererad kod,
- antal skapade agenter.

Sådana mått kan beskriva adoption.

De säger mycket mindre om värde.

En bättre startfråga är:

> Vilket resultat vill vi förbättra?

För ett utvecklingsteam kan det vara:

- kortare ledtid från behov till verifierad förändring,
- färre defekter,
- snabbare förståelse av äldre kod,
- bättre testtäckning av riskfyllda flöden,
- snabbare onboarding,
- bättre spårbarhet mellan beslut och implementation.

Riktning innebär också att säga var AI **inte** är rätt verktyg.

En mogen AI-strategi behöver kunna innehålla meningen:

> Detta arbetsmoment ska fortsatt kräva ett mänskligt beslut.

### 2. Miljö: gör det godkända arbetssättet lätt

Kapitel 15 visade varför kontotyp, avtal, databehandling och connectors spelar roll.

På organisationsnivå uppstår därför en praktisk princip:

> **Det säkra standardspåret bör vara enklare än improvisation.**

Om en utvecklare behöver ett AI-stöd för att analysera intern kod bör organisationen helst inte kräva att personen själv:

- väljer leverantör,
- granskar avtalsvillkor,
- skapar API-nycklar,
- bedömer informationsklass,
- konfigurerar loggning,
- bygger åtkomstkontroll.

Det är typiska kandidater för gemensam plattformskapacitet.

DORA:s 2025-rapport beskriver AI-införande i mjukvaruutveckling som ett systemsproblem och lyfter bland annat interna plattformar, dataekosystem och ett tydligt kommunicerat AI-ställningstagande som centrala organisatoriska förmågor. Rapporten bygger på nära 5 000 teknikprofessionella och är leverantörsproducerad branschforskning, inte ett randomiserat experiment. [K-088]

För en utvecklingsorganisation kan en gemensam AI-miljö exempelvis ge:

- godkända modeller,
- centralt hanterade identiteter,
- åtkomst till rätt repositories och dokument,
- standardiserade connectors,
- gemensamma säkerhetsinställningar,
- loggning och kostnadsuppföljning,
- fördefinierade verktygsbehörigheter.

Det minskar inte bara risk.

Det minskar också friktion.

## Governance som möjliggör – inte bara förbjuder

Governance får ibland en dålig start i AI-sammanhang.

Den blir en lista över sådant användaren inte får göra.

Det behövs gränser.

Men governance som bara består av förbud skapar ett tomrum mellan ambition och praktik.

En utvecklare får kanske veta:

> Lägg inte känslig information i publika AI-tjänster.

Men får inget svar på:

> Vilken miljö ska jag använda när jag faktiskt behöver analysera intern kod?

NIST:s AI Risk Management Framework och dess GenAI-profil behandlar AI-risk som en livscykel- och organisationsfråga: governance behöver kopplas till hur AI kartläggs, mäts och hanteras genom användningen, inte ligga som en separat policy vid sidan av. [K-089]

För den här bokens målgrupp kan bra governance därför vara mycket konkret:

- vilka AI-miljöer är godkända för vilken informationsklass,
- vilka verktyg får läsa respektive skriva,
- när krävs mänskligt godkännande,
- vilka arbetsflöden behöver evals,
- hur rapporteras AI-relaterade incidenter,
- vem ansvarar för ett AI-assisterat resultat,
- hur granskas nya modeller eller agenter innan bred användning.

Det centrala är att reglerna går att omsätta i arbete.

## Arbetsdesign: flytta fokus från verktyget till flödet

När organisationen blir mer mogen bör diskussionen gradvis flytta sig från:

> Vilken AI-produkt använder vi?

mot:

> Hur ser arbetsflödet ut?

Tänk på förändringsscenariot från Del III.

Ett omoget organisatoriskt införande kan se ut så här:

1. Kravanalytikern använder AI privat för ett första utkast.
2. Arkitekten använder en annan AI för alternativanalys.
3. Utvecklaren använder en kodagent.
4. Testaren genererar testfall i ett fjärde verktyg.
5. Ingen av aktiviteterna delar kontext, kvalitetskriterier eller spårbarhet.

Alla använder AI.

Men organisationen har inget AI-assisterat arbetssystem.

Ett mer moget flöde kan i stället definiera:

- vilka artefakter som är auktoritativ kontext,
- vilka beslut AI får föreslå men inte fatta,
- när ett verktyg får ändra repositoryt,
- vilka tester som måste passera,
- vilken evidens som ska följa en förändring,
- var mänskliga handoffs sker,
- hur resultat och fel fångas för förbättring.

Detta är precis det perspektiv som kapitel 10 kallade orkestrering.

På organisationsnivå blir orkestrering mindre en fråga om en enskild avancerad användare och mer en fråga om **gemensam arbetsdesign**.

## Kontroll: ge AI minsta nödvändiga handlingsutrymme

När AI går från fråga och resonemang till verktygsanvändning förändras styrningen.

Det räcker inte längre att styra vilken information AI får se.

Organisationen behöver även styra vad AI får göra.

Delegationsbudgeten från kapitel 9 blir därför ett organisatoriskt designverktyg.

För en agent i ett utvecklingsflöde kan organisationen exempelvis bestämma att den får:

- läsa hela repositoryt,
- skapa en lokal branch,
- ändra kod och tester,
- köra en begränsad testsvit,

men inte:

- merga till huvudbranch,
- ändra produktionshemligheter,
- skapa externa resurser,
- skriva direkt i produktionsdatabasen.

Det är inte misstro mot AI.

Det är samma princip som används för annan automation:

> **minsta nödvändiga privilegium och tydliga ansvarspunkter.**

## Kvalitet: från manuell granskning till eval-infrastruktur

När AI används sporadiskt kan kvalitetssäkring vara individuell.

Användaren läser svaret.

Utvecklaren kör testerna.

Arkitekten granskar alternativet.

När användningen blir återkommande och agentisk räcker det inte alltid.

Organisationen behöver kunna fråga:

> Fungerar det här arbetssättet fortfarande tillräckligt bra efter att modellen, prompten, verktyget eller kontexten har förändrats?

NIST:s AI Resource Center lyfter testing, evaluation, verification and validation – TEVV – som centrala aktiviteter för att operationalisera AI-riskhantering. [K-090]

För utvecklingsarbete kan eval-infrastruktur vara mycket jordnära.

Exempel:

- ett urval historiska issues med kända bra lösningar,
- testfall för vanliga arkitekturbedömningar,
- exempel där agenten förväntas avstå,
- säkerhetstest för otillåtna verktygsanrop,
- regressionstest när modell eller systemprompt byts,
- mätning av falska positiva fynd i AI-review.

Kapitlet om orkestrering skilde mellan **körningskvalitet** och **systemkvalitet**.

På organisationsnivå blir skillnaden central.

En lyckad körning visar att en uppgift gick bra.

Systemkvalitet handlar om huruvida arbetssättet fortsätter vara bra över tid och över många uppgifter.

## Mät resultat – inte AI-aktivitet

AI gör det lätt att skapa nya aktivitetsmått.

Men många av dem kan bli missvisande.

Mer genererad kod kan betyda:

- högre produktivitet,
- mer omarbete,
- mer teknisk skuld,
- eller bara att kod blev billigare att producera.

Fler AI-genererade testfall kan betyda bättre kvalitet.

Eller fler redundanta tester.

Fler prompts kan betyda hög adoption.

Eller att verktyget kräver fler försök för samma resultat.

Mogna organisationer behöver därför mäta närmare utfallet.

Exempelvis:

- ledtid från behov till verifierad leverans,
- defekter och incidenter,
- omarbete efter review,
- testernas felupptäckande förmåga,
- verifieringskostnad,
- kvalitet i beslutsunderlag,
- användar- eller verksamhetsutfall,
- hur snabbt nya medarbetare blir produktiva.

AI-aktivitet kan fortfarande vara diagnostisk data.

Men den bör sällan vara slutmålet.

## Lärande: gör erfarenhet till gemensam förmåga

En av de största skillnaderna mellan individuell och organisatorisk mognad är vad som händer efter en lyckad AI-interaktion.

Hos individen kan resultatet bli:

> Bra, det fungerade.

I ett lärande system blir nästa fråga:

> Vad var det som fungerade, och hur gör vi det reproducerbart för fler?

Det kan handla om att fånga:

- bra arbetsmönster,
- fungerande prompts eller instruktioner,
- evalfall,
- kvalitetsstandarder,
- vanliga failure modes,
- vilka uppgifter som inte bör delegeras,
- vilka kontextkällor som gav störst värde.

Microsofts Work Trend Index 2026 rapporterar att deras mer avancerade AI-användare oftare beskriver gemensamma kvalitetsstandarder, delning av AI-lärdomar och dokumenterade agentflöden. Det är surveydata från en leverantör, men mönstret stödjer idén att individuell experimentering behöver övergå i gemensamt lärande när arbetssättet skalar. [K-087]

Detta lärande bör inte bara spridas genom kurser.

Det kan byggas in i själva miljön:

- mallar,
- standardagenter,
- policies,
- testsviter,
- exempel,
- plattformstjänster,
- gemensam dokumentation.

Då behöver nästa användare inte återupptäcka allt från början.

## Organisationen behöver två slags kompetens

Kapitel 14 introducerade kompetensbudgeten.

På organisationsnivå behöver vi lägga till en distinktion.

Organisationen behöver både:

### Kompetens att utföra arbetet

Det handlar om domän, utveckling, test, arkitektur, säkerhet och verksamhet.

### Kompetens att designa AI-assisterat arbete

Det handlar om att kunna:

- välja rätt arbetsform,
- designa kontext,
- sätta kvalitetskriterier,
- avgöra vad som får delegeras,
- bygga evals,
- förstå verktygs- och informationsflöden,
- tolka resultat och failure modes.

Den andra kompetensen ersätter inte den första.

Den gör att den första kan användas på ett nytt sätt.

Om organisationen bara utbildar människor i prompts riskerar den att missa båda.

## En praktisk väg från experiment till arbetssystem

Det kan vara lockande att börja med en stor central AI-strategi.

För många utvecklingsorganisationer är en bättre väg mer iterativ.

### 1. Välj ett verkligt värdeflöde

Inte ”vi ska införa AI”.

Välj exempelvis:

> Vi vill minska tiden från ett välförstått mindre förändringsbehov till en verifierad pull request.

### 2. Kartlägg var AI faktiskt kan bidra

Använd mognadsmodellens repertoar:

- fråga,
- resonera,
- skapa,
- samarbeta,
- ge kontext,
- delegera,
- orkestrera.

Alla steg behöver inte nå samma fas.

### 3. Definiera informations- och delegationsbudget

Vilken data får läsas?

Vilka verktyg får användas?

Vad får ändras?

Vad kräver godkännande?

### 4. Sätt kvalitetsribban före automatiseringen

Bestäm:

- vilka tester som måste passera,
- vilken review som krävs,
- vilken evidens som ska sparas,
- vilka fall agenten ska eskalera.

### 5. Mät hela flödet

Följ både lokal effekt och systemeffekt.

Om implementation går snabbare men reviewkö växer har ni hittat nästa systemproblem.

### 6. Gör det fungerande mönstret gemensamt

Bygg in det i plattform, mallar, policies och dokumentation.

### 7. Fortsätt ompröva arbetsfördelningen

Modellerna förändras.

Verktygen förändras.

Organisationens kompetens förändras.

Det som var olämpligt att delegera för ett år sedan kan vara rimligt i dag.

Och något som ser automatiserbart ut kan fortfarande vara bättre som mänskligt beslut.

## Bokens slutmodell

Vi började med en enkel fråga.

> Kan AI hjälpa mig med detta?

Sedan växte repertoaren.

Vi lärde oss att resonera, skapa, samarbeta, ge kontext, delegera och orkestrera.

Men bokens slutpunkt är inte:

> AI gör allt.

Den är en annan fråga:

> **Hur fördelar vi arbetet så att människa, AI och automation tillsammans ger ett bättre resultat än någon av dem hade gjort ensam?**

Den mogna användaren – och den mogna organisationen – tänker därför i fyra återkommande frågor:

1. **Vad måste människan förstå, värdera och besluta?**
2. **Vad kan AI undersöka, skapa eller genomföra?**
3. **Vilken information och vilket handlingsutrymme behöver AI för just det?**
4. **Hur vet vi att resultatet och arbetssystemet fortfarande håller tillräcklig kvalitet?**

Det är ett annat sätt att arbeta än att skriva en bra prompt.

Det är också ett annat sätt att tänka på AI än som ett separat verktyg.

AI blir en del av arbetsdesignen.

Och där någonstans har resan gått hela vägen från fråga till arbetskamrat.

Bilagorna samlar bokens pedagogiska modeller och ger en självvärdering för att omsätta resonemanget i ett konkret nästa experiment.
