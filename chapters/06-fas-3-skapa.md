# Kapitel 6 – Fas 3: Skapa

Det finns ett tydligt ögonblick i många människors AI-användning när arbetssättet förändras.

Fram till dess har AI:n främst svarat, förklarat och resonerat.

Sedan kommer en annan typ av instruktion:

> Skriv ett första utkast.

> Generera testerna.

> Skapa en ADR.

> Ta fram acceptanskriterierna.

> Föreslå implementationen.

> Gör tabellen åt mig.

AI:n producerar nu inte bara information om arbetet. Den producerar **ett arbetsobjekt** som kan bli en del av det faktiska resultatet.

Det är fas 3: **Skapa**.

Övergången kan kännas mindre dramatisk än den egentligen är. Att be om en förklaring och att be om en fil med produktionskod kan göras i samma chattfönster. Men ansvarsmässigt är det två olika situationer.

Ett svar kan vara fel utan att något annat händer.

En artefakt kan bli kopierad till en backlogg, checkas in i ett repository, skickas till en beslutsgrupp, byggas in i en release eller ligga till grund för ett avtal.

När AI börjar skapa sådant som andra människor eller system kommer att använda måste vi börja tänka på **leveranskvalitet**, inte bara på om svaret verkar hjälpsamt.

## Från tom sida till första version

En av de starkaste praktiska egenskaperna hos generativ AI är att den kan minska kostnaden för att komma igång.

En tom sida kräver att du själv väljer struktur, språk, detaljnivå och startpunkt. En tom testklass kräver att du bestämmer vilka fall som är viktiga. Ett nytt ADR-dokument kräver att du formulerar problemet, alternativen och konsekvenserna.

AI kan snabbt skapa ett första objekt som går att reagera på.

Det är ofta lättare att säga:

> Det här är för tekniskt. Flytta fokus från komponenterna till beslutet och konsekvenserna.

än att själv skriva hela dokumentet från början.

På samma sätt kan det vara lättare att granska tio föreslagna testfall än att börja med ett blankt papper och försöka minnas alla relevanta scenarier.

Det är en verklig produktivitetsmekanism, men den måste förstås rätt.

AI:n tar inte automatiskt bort arbetet. Den kan flytta arbetet från **initial produktion** till **urval, granskning och förbättring**.

Forskning om AI-assistenter i praktisk mjukvaruutveckling stödjer att användningen redan sträcker sig långt utanför enbart kodkomplettering. En peer-reviewad enkätstudie med 481 programmerare undersökte användning inom bland annat nya funktioner, tester, bug triage, refaktorering och naturligt språk-baserade artefakter. [K-035]

Det är viktigt för den här boken. Fas 3 är inte ”börja låta AI skriva kod”.

Den är:

> Börja låta AI producera konkreta artefakter som ingår i ditt arbete.

## Artefakten förändrar relationen

I fas 1 kunde du fråga:

> Vad är en ADR?

I fas 2:

> Vilka beslutskriterier bör vi använda när vi jämför köhantering med direkt synkron kommunikation?

I fas 3:

> Skriv ett första ADR-utkast för beslutet. Ta med kontext, tre alternativ, beslutskriterier, konsekvenser och öppna frågor. Markera sådant som saknar stöd i underlaget som antaganden.

Det sista svaret har en annan status.

Det är inte längre bara input till ditt tänkande. Det kan bli ett dokument som någon annan läser som en representation av beslutet.

Samma skillnad finns i andra roller.

En kravanalytiker går från:

> Vad är skillnaden mellan ett krav och ett acceptanskriterium?

via:

> Vilka oklarheter finns i det här behovet?

 till:

> Skriv ett första kravpaket med user story, affärsregler, acceptanskriterier och öppna frågor.

En testare går från:

> Hur fungerar boundary-value analysis?

via:

> Vilka riskområden finns i den här funktionen?

 till:

> Generera testfall för de riskområdena och strukturera dem så att de kan importeras i vårt testhanteringsverktyg.

En utvecklare går från:

> Hur använder man retries med exponential backoff?

via:

> Vilka trade-offs finns mellan retry i klienten och i integrationslagret?

 till:

> Implementera en första version enligt det här interfacet och skriv tester för timeout, transient fel och permanent fel.

Det är alltså inte typen av artefakt som definierar fasen.

Det är att AI:n producerar **något som kan leva vidare efter dialogen**.

## Genererbarhet är inte samma sak som leveranskvalitet

När AI kan skapa en artefakt på några sekunder uppstår en lätt mental fälla:

> Om den kunde skapa den så snabbt måste den väl också vara nästan färdig?

Nej.

Det finns ingen sådan koppling.

En artefakt kan vara lätt att generera men dyr att verifiera.

AI-genererad kod kan kompilera och ändå ha fel beteende.

Ett test kan köra grönt och ändå testa fel sak.

Ett krav kan vara välformulerat och ändå bygga på en felaktig verksamhetsregel.

En ADR kan se professionell ut och ändå jämföra alternativ på irrelevanta kriterier.

En tabell kan vara perfekt formaterad men innehålla två påhittade värden.

Det är därför fas 3 kräver att vi skiljer mellan två frågor:

1. **Kan AI skapa artefakten?**
2. **Hur vet vi att artefakten är tillräckligt bra för sitt syfte?**

Den första frågan blir snabbt enklare när modellerna blir bättre.

Den andra försvinner inte.

En peer-reviewad studie som systematiskt analyserade GitHub Copilots kodförslag fann varierande korrekthet och illustrerar varför genererade kodförslag måste bedömas snarare än antas vara korrekta. [K-036] Resultatet ska inte läsas som en universell felfrekvens för alla framtida modeller. Produkt, modellversion, uppgift och kontext spelar roll. Men själva kontrollprincipen består.

På testområdet finns samma mönster. En stor empirisk studie av LLM-baserad unit testing visar att modeller kan vara användbara för testgenerering, assertions och testutveckling, men att resultatet varierar mellan modeller och uppgifter. [K-017]

Möjligheten att generera många tester betyder alltså inte automatiskt att man har en bra testsvit.

## Definiera kvalitet innan du beställer produktionen

En av de enklaste förbättringarna i fas 3 är att sluta beskriva enbart **vad** som ska skapas och också beskriva **vad bra betyder**.

Jämför:

> Skriv tester för den här klassen.

med:

> Skriv en första uppsättning unit-tester för den här klassen. Prioritera beteenden som kan ge felaktiga debiteringar. Täck normala fall, gränsvärden och felvägar. Undvik tester som bara verifierar implementationens interna struktur. Testerna ska vara läsbara och varje testnamn ska uttrycka det observerbara beteendet.

Den andra instruktionen är längre, men den viktiga skillnaden är inte längden.

Den uttrycker **kvalitetskriterier**.

Samma princip gäller ett arkitekturdokument:

> Skriv en arkitekturbeskrivning.

är mycket mindre styrande än:

> Skriv ett första arkitekturutkast för beslutsfattare och utvecklingsteam. Beskriv drivkrafter, systemgräns, viktigaste kvalitetsattribut, tre centrala beslut och öppna risker. Undvik komponentdetaljer som inte påverkar besluten. Markera antaganden tydligt.

Och ett krav:

> Skriv user stories.

är svagare än:

> Skapa ett första kravförslag från behovsbeskrivningen. Varje story ska uttrycka ett användarvärde, ha observerbara acceptanskriterier och separera kända verksamhetsregler från antaganden som måste verifieras med verksamheten.

## Fem saker att specificera

För att göra detta konkret använder boken en femdelad pedagogisk modell när AI ska skapa ett arbetsobjekt. Modellen är **bokens egen syntes**, inte en etablerad forskningsmodell.

### Syfte

Varför ska artefakten finnas?

Ett dokument för beslut skiljer sig från dokumentation för framtida utvecklare. Ett test för regressionsskydd skiljer sig från ett explorativt test. En prototyp skiljer sig från produktionskod.

### Mottagare eller användare

Vem ska använda resultatet?

Det styr språk, struktur, detaljnivå och vilka förklaringar som krävs.

### Begränsningar

Vilka begränsningar måste respekteras?

Exempel:

- befintligt API får inte ändras,
- endast bibliotek som redan finns i projektet får användas,
- beslutet måste följa en viss princip,
- dokumentet får vara högst två sidor,
- personuppgifter får inte förekomma,
- lösningen måste fungera utan internetåtkomst.

### Kvalitetskriterier

Vad ska vara sant för att resultatet ska betraktas som bra?

Exempel:

- alla krav ska vara verifierbara,
- testfallen ska täcka riskerna snarare än interna implementationdetaljer,
- ADR:n ska redovisa ett verkligt alternativ som valts bort,
- koden ska följa projektets befintliga mönster,
- slutsatser ska kunna spåras till underlaget.

### Verifieringssätt

Hur ska vi avgöra om resultatet håller?

Det kan vara:

- kompilering,
- automatiska tester,
- statisk analys,
- schema-validering,
- jämförelse mot källa,
- mänsklig review,
- demonstration mot acceptanskriterier,
- ett experiment i testmiljö.

Den sista punkten är ofta den viktigaste.

Om du inte kan beskriva hur artefakten ska verifieras är det ett tecken på att du kanske ännu inte är redo att delegera produktionen.

## Skapa sådant som är lätt att kontrollera

AI:s styrka i fas 3 blir särskilt stor när resultatet är **billigt att verifiera**.

Kod är intressant just därför att delar av kvaliteten kan kontrolleras maskinellt.

Koden kan kompileras.

Tester kan köras.

Linting och statisk analys kan hitta vissa fel.

Kontrakt kan valideras.

Det betyder inte att kod är riskfri. Men det finns ofta tydliga återkopplingsmekanismer.

Samma princip kan byggas in i andra artefakter.

Ett kravpaket kan få en checklista:

- finns aktör?
- finns observerbart utfall?
- finns källa till verksamhetsregel?
- finns identifierade öppna frågor?

Ett arkitekturbeslut kan valideras mot en mall:

- kontext,
- alternativ,
- beslut,
- konsekvenser,
- status,
- ägare.

En informationsmodell kan kontrolleras mot ett schema.

En tabell kan jämföras programmässigt mot källdata.

Mogen AI-användning innebär därför ofta att man inte bara förbättrar instruktionen till AI:n. Man **designar arbetsobjektet och arbetsflödet så att kvalitet går att kontrollera**.

## Coverage är inte kvalitet

Testgenerering ger ett bra exempel på varför detta spelar roll.

En peer-reviewad explorativ studie från 2026 jämförde sex moderna modeller på tolv specialkonstruerade Python-metoder. Mer relevant kontext förbättrade resultatet, och en sekventiell multi-turn-strategi gav bäst resultat i studien. Den nådde som mest 96,3 procent branch coverage men bara 57 procent genomsnittlig mutation score. [K-037]

Studien är liten och ska inte användas för att dra generella slutsatser om alla modeller. Men kontrasten mellan två kvalitetsmått är pedagogiskt viktig.

En testsvit kan se imponerande ut enligt ett mått och ändå missa många fel som mutation testing avslöjar.

Det leder till en generell princip:

> Välj inte ett kvalitetsmått bara för att det är enkelt att mäta.

Det gäller även utanför test.

Antal genererade krav är inte kravkvalitet.

Antal identifierade risker är inte riskanalysens kvalitet.

Antal kodrader är inte leveransvärde.

Ett långt arkitekturdokument är inte nödvändigtvis en bättre arkitekturbeskrivning.

AI gör det billigt att producera **mer**. Därför måste vi bli bättre på att definiera **vad som är värdefullt**.

## Var försiktig med snygga första utkast

Generativ AI är mycket bra på yta.

Struktur, rubriker, sammanhängande språk och professionell ton kan göra att ett resultat ser mer färdigt ut än det är.

Detta är särskilt riskabelt i artefakter där felen inte ger ett omedelbart tekniskt fel.

En trasig kodrad kan ge ett rött test.

Ett felaktigt antagande i ett beslutsunderlag kan överleva i månader.

Därför bör du i fas 3 aktivt separera två bedömningar:

### Presentationskvalitet

Är artefakten tydlig, välstrukturerad och begriplig?

### Sak- och funktionskvalitet

Är innehållet korrekt, relevant, fullständigt nog och användbart för sitt syfte?

AI kan ofta ge hög presentationskvalitet mycket snabbt.

Det får inte bli en genväg förbi den andra bedömningen.

## Första utkastet är en arbetsform

”Första utkast” kan låta som en nedvärdering.

Det är snarare en arbetsstrategi.

När startkostnaden sjunker kan vi arbeta mer experimentellt.

I stället för att investera två timmar i ett enda arkitekturalternativ kan vi be AI:n skapa tre skisser och sedan analysera dem.

I stället för att formulera alla acceptanskriterier perfekt direkt kan vi skapa ett brett utkast och därefter eliminera redundans, otestbara formuleringar och antaganden.

I stället för att skriva en stor implementation direkt kan vi generera en liten spike för att testa ett API eller en teknisk hypotes.

Den mogna användaren utnyttjar alltså inte bara AI för att **göra samma leverans snabbare**.

AI används för att göra det billigare att skapa alternativ, prototyper och mellanprodukter som förbättrar beslutet.

Det är en viktig brygga mellan fas 2 och 3.

Resonemanget skapar alternativen.

Produktionen gör alternativen konkreta nog att utvärdera.

## AI kan skapa både problemet och kontrollen

Det finns en frestande arbetsform:

1. be AI skriva koden,
2. be samma AI skriva testerna,
3. se att testerna går grönt,
4. anta att lösningen är korrekt.

Problemet är att produktion och kontroll då kan dela samma blinda fläckar.

Om AI missförstår kravet på ett visst sätt kan både implementation och test uttrycka samma missförstånd.

Det betyder inte att AI inte ska skriva tester till AI-genererad kod.

Det betyder att verifieringen behöver innehålla **någon form av oberoende signal**.

Exempel:

- krav eller acceptanskriterier formulerade separat,
- testdata från verkliga fall,
- property-based tests,
- mutation testing,
- statisk analys,
- en mänsklig review,
- en annan modell eller annan instruktion med kritikerroll,
- observation i körande system.

Oberoende betyder inte att människan måste skriva allt för hand.

Det betyder att kontrollen inte bara ska återupprepa samma antaganden som produktionen.

## Exempel: från behov till kravpaket

Anta att verksamheten säger:

> Kunden ska kunna välja ett senare leveransdatum för en order som ännu inte har skickats.

En fas 1-användare kanske frågar vad ett bra acceptanskriterium är.

En fas 2-användare analyserar oklarheter:

- Hur sent får kunden ändra?
- Kan datumet flyttas bakåt och framåt?
- Vad händer med lagerreservation?
- Gäller det alla leveranssätt?
- Finns regulatoriska eller avtalsmässiga begränsningar?

I fas 3 kan AI:n sedan få skapa ett arbetsobjekt:

> Skapa ett första kravpaket baserat på behovet och de verifierade svaren nedan. Ta med user story, affärsregler, acceptanskriterier, negativa scenarier och öppna frågor. Markera allt som fortfarande är antagande.

Det viktiga är att artefakten skapas **efter** att de centrala osäkerheterna har synliggjorts.

AI:n får inte magiskt fylla luckorna och sedan låta dem se ut som fakta.

## Exempel: från testidé till exekverbart test

En testare och utvecklare har identifierat en risk:

> Ett datumbyte får inte skapa dubbla lagerreservationer.

I fas 2 kan AI hjälpa till att resonera om felmoder.

I fas 3 kan den få skapa testet:

> Skriv ett integrationstest som först skapar en order med lagerreservation, flyttar leveransdatum två gånger och verifierar att totalt reserverat antal aldrig överskrider orderkvantiteten. Använd projektets befintliga test-fixtures och undvik mocks av lagersaldot.

Här har användaren gjort något viktigt.

Kvalitetsrisken kommer från människans/domänens förståelse.

AI får producera den exekverbara kontrollen.

Det är ofta en stark kombination.

## När AI skapar dokument och analys

Kod och tester har exekverbara verifieringsmekanismer. Dokument kräver andra kontroller.

När AI skapar en analys bör du därför be den göra sin **evidensstruktur synlig**.

Till exempel:

> För varje slutsats: ange vilket underlag den bygger på. Skilj mellan explicit källa, härledd slutsats och antagande. Om två källor motsäger varandra ska motsättningen stå kvar i utkastet.

När AI skapar ett beslutsunderlag:

> Separera fakta, bedömning och rekommendation. Rekommendationen får inte introducera nya fakta som inte finns i faktaavsnittet.

När AI skapar en arkitekturöversikt:

> Beskriv endast komponenter som finns i underlaget. Föreslagna nya komponenter ska ligga i ett separat avsnitt och märkas som förslag.

Det är i praktiken samma princip som automatiska tester i kod: gör resultatets relation till verkligheten mer kontrollerbar.

## Mognad i fas 3 handlar inte om större leveranser

En vanlig missuppfattning är att en mogen fas 3-användare ber AI skapa större och större saker.

Det är inte nödvändigtvis sant.

Mognad kan lika gärna betyda att **göra artefakten mindre**.

I stället för:

> Bygg hela funktionen.

kan en erfaren användare säga:

> Skapa bara databas-migreringen och repository-förändringen. Ändra inte API eller domänlogik ännu. Kör migrations- och repository-testerna och stanna där.

Det är fortfarande fas 3.

Skillnaden är att användaren har bättre kontroll över arbetsobjektets gräns.

Ett litet, verifierbart steg kan vara mognare än ett imponerande helhetsuppdrag.

## Bokens syntes: artefaktkontraktet

För att sammanfatta fas 3 använder vi begreppet **artefaktkontrakt**. Det är bokens syntes.

Innan AI producerar något som ska leva vidare bör fem frågor vara tillräckligt tydliga:

1. **Varför finns artefakten?**
2. **Vem eller vad ska använda den?**
3. **Vilka begränsningar måste den följa?**
4. **Vad betyder god kvalitet?**
5. **Hur verifierar vi resultatet?**

Du behöver inte skriva ett formellt kontrakt varje gång.

Men om flera av frågorna är oklara bör du inte bli förvånad om AI fyller tomrummet med rimliga men felaktiga antaganden.

## Vad människan ansvarar för

I fas 3 kan AI stå för en stor del av den mekaniska produktionen.

Människans ansvar flyttas mot:

- syfte,
- avgränsning,
- begränsningar,
- kvalitetskriterier,
- verifiering,
- beslut om vad som faktiskt ska användas.

Detta är början på den rollförskjutning vi återkommer till senare i boken.

Att AI skriver mer betyder inte att människan blir mindre viktig.

Det förändrar **vilket arbete som är viktigast att människan gör**.

## Så tar du nästa steg

Nästa fas börjar när du slutar se AI-output som ett levererat resultat och börjar behandla den som en del av en **återkopplingsloop**.

Pröva därför att inte nöja dig med:

> Skriv ADR:n.

Fortsätt med:

> Granska nu utkastet som en skeptisk seniorarkitekt. Vilka beslutskriterier saknas? Vilka konsekvenser är underbyggda respektive antagna? Föreslå inte en ny version ännu.

Eller efter kodgenerering:

> Kör testerna, analysera felen och föreslå minsta förändring som löser dem. Ändra inget innan du har förklarat hypotesen.

Eller efter kravgenerering:

> Försök hitta fem sätt som en utvecklare skulle kunna implementera kraven korrekt enligt ordalydelsen men ändå ge ett resultat som verksamheten sannolikt inte vill ha.

Nu används AI inte bara som producent.

Den blir en deltagare i förbättringsarbetet.

Det är fas 4: **Samarbeta**.

## När du inte bör gå vidare

Stanna i fas 3 när:

- uppgiften är liten,
- artefakten är enkel att verifiera,
- första versionen håller efter en normal mänsklig kontroll,
- mer dialog skulle kosta mer än den tillför.

Gå inte vidare till långa iterativa loopar bara för att AI:n kan fortsätta prata.

Men lämna inte heller första utkastet som leverans bara för att det ser färdigt ut.

Den centrala frågan i fas 3 är inte:

> Kan AI skapa detta?

utan:

> **Har vi ett sätt att avgöra om det som skapats faktiskt är bra nog att använda?**
