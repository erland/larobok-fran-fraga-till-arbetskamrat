# Kapitel 11 – Från behov och krav till lösningsidé

När en förändring börjar som en mening i en backlogg är den nästan alltid mindre tydlig än den ser ut.

> Användare ska kunna prenumerera på statusnotiser för ett ärende och välja kanal.

Det låter konkret. Men redan efter några följdfrågor blir osäkerheten synlig.

Vilka statusändringar ska ge en notis? Gäller det alla användare eller bara vissa roller? Får en användare prenumerera på ett ärende som personen kan se tillfälligt men inte längre har behörighet till senare? Ska notiser skickas om en status ändras fram och tillbaka snabbt? Vad betyder ”välja kanal” i första versionen? Hur ändrar man sitt val? Vad händer om leveransen misslyckas?

Detta är en bra plats att se varför mognadsresan inte bara handlar om kod.

En AI-assistent kan formulera ett krav på några sekunder. Den svårare uppgiften är att hjälpa teamet förstå **vilket behov som faktiskt ska lösas, vilka antaganden som fortfarande är öppna och hur man vet att lösningen senare blev rätt**.

## Kravarbete är inte textproduktion

Generativ AI passar naturligt in i requirements engineering eftersom en stor del av arbetet uttrycks i språk. Det kan därför vara frestande att tänka att den stora nyttan är att skriva user stories, krav och acceptanskriterier snabbare.

Forskningen pekar på en bredare men mer nyanserad bild.

En systematisk litteraturöversikt publicerad 2026 analyserade 238 artiklar om generativ AI i requirements engineering. Mest forskning fanns inom kravanalys och elicitering, medan kravhantering var betydligt mindre studerat. Samma översikt identifierade reproducerbarhet, hallucinationer och interpretability som återkommande problem. [K-055]

Det är alltså rimligt att säga att AI redan används och studeras för många kravaktiviteter. Det är inte rimligt att därifrån dra slutsatsen att ett välskrivet AI-genererat krav automatiskt är ett korrekt krav.

Skillnaden är central:

> **Textkvalitet kan bedömas i artefakten. Behovskvalitet kräver kunskap om verkligheten utanför artefakten.**

AI kan göra formuleringen tydligare. Den kan inte på egen hand veta att en viss stakeholder aldrig blev tillfrågad, att en verksamhetsregel saknas eller att den snygga user storyn löser fel problem.

## Samma behov på sju olika mognadsnivåer

Del II beskrev de sju faserna var för sig. Här använder vi dem som analyslinser över samma förändring.

### Fas 1: Fråga

En första användning kan vara:

> Vad bör ett bra krav på statusnotiser innehålla?

AI:n kan förklara vanliga delar: trigger, mottagare, kanal, innehåll, preferenser, felhantering och eventuellt samtycke eller andra regler.

Det är nyttigt. Framför allt kan det ge en mindre erfaren kravställare en checklista över frågor att tänka på.

Men AI:n arbetar fortfarande utan projektets verkliga kontext. Svaret är generellt.

### Fas 2: Resonera

Nästa steg är att använda AI för att bredda och utmana problemförståelsen.

> Vilka oklarheter och konflikter ser du i detta förändringsbehov? Vilka frågor bör vi ställa innan vi bestämmer lösning?

Nu blir AI:n ett bollplank.

Den kan exempelvis lyfta frågor om:

- vilka händelser som ska utlösa notiser,
- vem som får prenumerera,
- hur preferenser ska lagras,
- vad som händer när behörighet förändras,
- hur dubbla eller mycket täta händelser ska hanteras,
- hur misslyckade leveranser ska följas upp.

Det är inte svaren som är det mest värdefulla. Det är **frågerummet**.

Mognad i den här fasen innebär ofta att be AI:n hitta det som fortfarande saknas i stället för att be den fylla luckorna med antaganden.

## Fas 3: Skapa ett första kravpaket

När teamet har mer information kan AI:n skapa konkreta artefakter:

- user story,
- funktionella krav,
- acceptanskriterier,
- lista över öppna frågor,
- exempel på edge cases,
- traceability-tabell mellan behov och krav.

En peer-reviewad studie från 2026 lät två LLM:er omvandla 150 korta issue-titlar till totalt 900 krav och bedömde bland annat entydighet, verifierbarhet och singularitet. Resultaten visade att både modell och promptstrategi påverkade kvaliteten. [K-056]

Studien visar inte att AI-genererade krav alltid blir bra. Den visar något mer användbart för vår bok: **kravkvalitet kan förbättras när kriterierna görs explicita och när resultatet faktiskt bedöms mot dem**.

Det passar direkt med artefaktkontraktet från kapitel 6.

Ett kravpaket kan exempelvis få följande kvalitetskriterier:

- varje krav uttrycker en sak,
- språket ska vara verifierbart,
- antaganden ska markeras som antaganden,
- öppna verksamhetsfrågor får inte döljas genom påhittade detaljer,
- acceptanskriterier ska kunna kopplas till senare test.

AI:n blir då inte bara en skrivmaskin. Den får ett definierat kvalitetsmål.

## Fas 4: Samarbeta om det som fortfarande är oklart

I praktiskt kravarbete förändras förståelsen när materialet granskas.

En stakeholder säger att bara e-post behövs i första leveransen. En annan påpekar att vissa statusändringar är administrativa och inte ska notifieras. Säkerhetsansvarig frågar hur prenumerationer påverkas när användarens behörighet tas bort.

Det mogna AI-arbetet består då inte i att generera ett nytt dokument från noll, utan i att använda AI för att hålla ihop förändringen:

> Uppdatera kravpaketet med dessa tre beslut. Markera vilka tidigare antaganden som nu är stängda, vilka frågor som återstår och vilka acceptanskriterier som påverkas.

Här blir samarbetsloopen synlig:

> underlag → kritik → ändring → kontroll

En viktig mänsklig uppgift är fortfarande att avgöra **vilken återkoppling som är auktoritativ**. AI:n kan inte själv bestämma att en utvecklares tolkning väger tyngre än produktägarens verksamhetsbeslut eller att ett gammalt mötesprotokoll ska övertrumfa en ny policy.

## Fas 5: Ge verklig kontext

Det stora skiftet kommer när AI:n får arbeta med faktiska artefakter:

- befintlig backlogg,
- processbeskrivning,
- behörighetsmodell,
- API-dokumentation,
- tidigare beslut,
- nuvarande datamodell,
- befintliga notifieringsfunktioner.

Nu kan frågan bli:

> Läs det befintliga materialet och analysera hur förändringsbehovet passar in. Identifiera konflikter, återanvändbara mekanismer och saknad information. Skapa inget slutligt krav där källmaterialet är motsägelsefullt.

Detta är mycket mer värdefullt än att bara göra prompten längre.

Samtidigt introduceras ett nytt problem: om materialet är gammalt eller motsägelsefullt kan AI:n bli **mer övertygande men inte mer korrekt**.

Därför behöver teamet veta vad som är:

- källa,
- antagande,
- beslut,
- tolkning.

Det är också här den första länken i Del III:s nya modell blir viktig.

## Den vertikala spårbarhetskedjan

I den här delen av boken använder vi följande modell. Den är **bokens syntes**, inte en etablerad forskningsmodell:

> **behov → beslut → förändring → bevis**

I kravfasen arbetar vi främst med de två första leden.

### Behov

Varför gör vi förändringen?

I scenariot kan det vara:

> Användare missar viktiga förändringar i ärenden därför att de måste gå in i systemet för att se om status ändrats.

Det är något annat än lösningen ”skicka e-post”.

### Beslut

Vilka val gör vi för att omsätta behovet till en konkret förändring?

Exempel:

- första versionen stöder e-post,
- användaren prenumererar aktivt per ärende,
- bara definierade statusövergångar ger notis,
- prenumerationen ska respektera aktuell behörighet,
- leveransfel ska loggas men får inte blockera själva statusändringen.

När dessa beslut är explicita kan senare arkitektur-, kod- och testarbete kopplas tillbaka till dem.

AI kan hjälpa till att **underhålla kedjan**. Den kan inte ta ansvar för att besluten är rätt.

## Fas 6: Delegera en kravanalys

När kontexten och kvalitetskriterierna är tydliga kan större delar delegeras.

En uppgift kan formuleras ungefär så här:

> Analysera det godkända förändringsbehovet mot backlogg, behörighetsregler och befintlig notifieringsfunktion. Leverera ett kravpaket med: mål, scope, explicita antaganden, öppna frågor, funktionella krav, kvalitetskrav, acceptanskriterier och spårbarhet till källorna. Markera konflikter i underlaget i stället för att själv lösa dem.

Skillnaden mot fas 3 är viktig.

I fas 3 bad vi AI skapa en artefakt.

I fas 6 delegerar vi ett **analysarbete över flera artefakter**, med tydliga gränser för vad AI får avgöra.

Det gör delegationsbudgeten relevant även i kravarbete.

AI:n kan exempelvis få:

- läsa projektets kravmaterial,
- skapa ett förslag,
- föreslå ändringar i backlogg,

men inte:

- ändra godkända verksamhetsregler,
- markera en fråga som beslutad utan källa,
- publicera krav som godkända.

Mognaden ligger lika mycket i vad vi förbjuder som i vad vi tillåter.

## Fas 7: Orkestrera kravflödet

På den sista nivån kan delar av kravhanteringen bli ett återkommande arbetssystem.

Exempel:

1. ett nytt förändringsbehov registreras,
2. AI samlar relevanta befintliga artefakter,
3. den identifierar frågor och möjliga konflikter,
4. en människa prioriterar vilka frågor som måste lösas,
5. svar och beslut förs tillbaka till kravpaketet,
6. AI uppdaterar spårbarhet och föreslår acceptanskriterier,
7. en människa godkänner scope,
8. det godkända paketet blir input till arkitektur och implementation.

Det är inte samma sak som att låta en agent ”göra kraven”.

Det är att designa **hur människor och AI tillsammans tar ett otydligt behov till ett beslutat och spårbart underlag**.

## En mogen användare ber inte AI gissa

Ett tydligt mognadstecken i kravarbete är hur man hanterar osäkerhet.

Den omogna impulsen är:

> Fyll i det som saknas så att dokumentet blir komplett.

Den mogna instruktionen är oftare:

> Separera det vi vet från det vi antar. Gör luckorna synliga. Föreslå frågor som behöver besvaras innan vi går vidare.

Det är mindre spektakulärt men betydligt mer värdefullt.

En mycket ny tväruppgiftsstudie från 2026 fann också att LLM-prestanda inom requirements engineering varierade tydligt mellan olika aktiviteter och att ingen modell konsekvent var bäst. Studien är en preprint och ska därför inte behandlas som slutlig evidens, men resultatet passar med den bredare bilden i boken: **rätt arbetssätt är uppgiftsberoende**. [K-057]

Det finns ingen anledning att pressa varje aktivitet till samma autonominivå.

## När kravet ser färdigt ut för tidigt

Generativ AI kan skapa ett professionellt dokument långt innan teamet har en professionell förståelse av problemet.

Det är en ny sorts risk.

Tidigare kunde ett tunt underlag se tunt ut. Nu kan samma osäkerhet döljas bakom:

- tydliga rubriker,
- konsekvent terminologi,
- välskrivna acceptanskriterier,
- snygga tabeller.

Därför bör teamet fråga:

- Vilka delar av detta kommer från verifierad källa?
- Vilka är AI-genererade förslag?
- Vilka antaganden är fortfarande öppna?
- Vilka stakeholders har faktiskt validerat behovet?
- Vilka beslut ska senare kunna spåras till test och implementation?

Detta är ett bra exempel på bokens återkommande tema:

> **När produktionskostnaden sjunker ökar värdet av omdöme och verifiering.**

## Från krav till lösningsidé

När kapitel 11 slutar har vi inte en färdig teknisk lösning.

Vi har något mer användbart:

- ett tydligare behov,
- beslutat scope,
- synliga antaganden,
- öppna frågor som faktiskt är öppna,
- verifierbara acceptanskriterier,
- spårbarhet till källor och beslut.

Det är den kontext som arkitektur- och designarbetet behöver.

I nästa kapitel följer vi samma förändring vidare och ser vad som händer när AI får hjälpa till att översätta behov och beslut till **arkitekturalternativ, tekniska trade-offs och verkliga kodändringar**.

## Så tar du nästa steg

Om du redan använder AI för krav och analys, prova att flytta fokus från dokumentproduktion till spårbar problemförståelse:

1. välj ett verkligt förändringsbehov,
2. ge AI relevanta källor i stället för bara en sammanfattning,
3. be den skilja fakta, beslut, antaganden och frågor,
4. definiera kvalitetskriterier för kravartefakterna,
5. be den hålla spårbarhet mellan behov, beslut och acceptanskriterier,
6. låt en människa godkänna det som faktiskt kräver verksamhetsbeslut.

## När du inte bör gå vidare

Gå inte mot större delegering bara för att AI:n skriver bra krav.

Stanna på en mer styrd nivå när:

- stakeholderbilden är oklar,
- verksamhetsregler motsäger varandra,
- källmaterialet inte är auktoritativt,
- beslut saknar tydlig ägare,
- konsekvensen av ett felaktigt krav är stor,
- teamet ännu inte kan verifiera spårbarheten från behov till acceptanskriterier.

Mognad är inte att låta AI skriva mer.

Mognad är att **veta vad som behöver bli sant innan nästa steg får börja**.
