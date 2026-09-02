# Kapitel 8 – Fas 5: Ge kontext

Hittills har AI:n främst arbetat med det du uttryckligen berättat i dialogen.

Du har ställt frågor, resonerat, bett om artefakter och itererat över resultaten.

Men mycket verkligt utvecklingsarbete går inte att förstå från en prompt.

Varför ser den här klassen ut som den gör?

Vilka kompromisser låg bakom integrationsmönstret?

Vilket krav är det här testet egentligen till för?

Vilken av tre dokumentationssidor är fortfarande aktuell?

Vilket beslut i en ADR gör att den "uppenbara" refaktoreringen är fel?

Svaret finns ofta någonstans i projektet.

När AI får tillgång till repositoryt, backloggen, modellerna, testresultaten, besluten och dokumentationen förändras arbetsformen.

Det är fas 5: **Ge kontext**.

Kärnan är inte att skriva längre prompts.

Kärnan är att AI:n får arbeta med **det faktiska arbetsmaterialet i stället för en förenklad beskrivning av det**.

## Från generiskt råd till lokalt relevant arbete

Anta att du frågar:

> Hur bör jag strukturera felhantering i en Quarkus-tjänst?

Du kan få ett bra generellt svar.

Men det är inte samma fråga som:

> Läs projektet. Identifiera hur fel hanteras i REST-lagret i dag, vilka exception mappers som redan finns, hur API-fel testas och vilka conventions projektet använder. Föreslå sedan minsta förändringen som gör felhanteringen konsekvent.

Den andra uppgiften kräver inte nödvändigtvis en smartare modell.

Den kräver **mer relevant kontext**.

Samma skillnad finns i kravarbete.

Generiskt:

> Vad saknas ofta i en user story för behörighetsstyrning?

Projektkontext:

> Läs epiken, de sex relaterade stories som redan är implementerade och systemets behörighetsmodell. Identifiera vilka antaganden den nya storyn gör som inte stöds av befintliga regler.

Och i arkitektur:

> Vilka integrationsmönster passar för händelsedriven kommunikation?

blir:

> Läs målbilden, de tre tidigare ADR:erna och driftkraven. Vilka integrationsalternativ är fortfarande förenliga med beslut som redan är tagna, och vilka skulle kräva att vi öppnar ett tidigare beslut igen?

I fas 5 blir AI:n mindre av en allmän rådgivare och mer av en **projektmedarbetare**.

## Kontext är inte samma sak som prompt

Ordet kontext används på flera sätt i AI-diskussioner.

Tekniskt kan det syfta på det material modellen har tillgängligt i sin kontext vid ett visst anrop.

I praktiskt arbete är en bredare definition mer användbar:

> Kontext är den information som AI behöver för att förstå uppgiften på samma lokala villkor som den som arbetar i projektet.

Det kan vara:

- källkod,
- tester,
- backlogg,
- verksamhetsregler,
- arkitekturmodeller,
- ADR:er,
- loggar,
- byggfel,
- releasehistorik,
- incidenter,
- standards och policies,
- tidigare beslut,
- kommentarer från användare eller stakeholders.

Det viktiga är inte var informationen ligger.

Det viktiga är **om den behövs för att göra rätt bedömning**.

## Fem sorters kontext

För att skilja olika kontextbehov åt använder boken fem kategorier. Indelningen är **bokens egen syntes**, inte en etablerad standardmodell.

### 1. Uppgiftskontext

Det som beskriver vad som ska göras här och nu.

Exempel:

- issue eller user story,
- acceptanskriterier,
- felbeskrivning,
- önskat resultat,
- begränsningar för just förändringen.

Utan uppgiftskontext vet AI:n inte vilket problem den ska lösa.

### 2. Projektkontext

Det som beskriver hur projektet faktiskt fungerar.

Exempel:

- repositorystruktur,
- kodkonventioner,
- datamodell,
- tester,
- API-kontrakt,
- byggsystem,
- deploymentkonfiguration.

Utan projektkontext riskerar AI:n att föreslå något som är rimligt i största allmänhet men fel i just detta system.

### 3. Historik och beslut

Det som förklarar varför nuläget ser ut som det gör.

Exempel:

- ADR:er,
- tidigare incidenter,
- bortvalda alternativ,
- migrationsplaner,
- beslut från arkitekturforum,
- historik i issues och pull requests.

Detta är ofta avgörande för att undvika att AI:n "förbättrar" bort ett medvetet designval.

### 4. Regel- och policykontext

Det som sätter yttre eller organisatoriska gränser.

Exempel:

- säkerhetskrav,
- tillgänglighetskrav,
- juridiska krav,
- interna standarder,
- plattformsregler,
- informationsklassning.

En lösning kan vara tekniskt elegant och ändå otillåten.

### 5. Miljö- och runtimekontext

Det som bara syns när systemet körs.

Exempel:

- loggar,
- metrics,
- testresultat,
- stack traces,
- observability-data,
- versioner,
- CI/CD-status.

Detta blir särskilt viktigt när AI används för felsökning och senare för delegerade arbetsuppgifter.

## Mer kontext är inte samma sak som bättre kontext

Det är frestande att tänka:

> Om AI:n gör fel behöver den bara få läsa mer.

Ibland stämmer det.

Men stora mängder material skapar också nya problem.

Projektet kan innehålla:

- gammal dokumentation,
- dubbla sanningar,
- experimentell kod,
- stängda issues som inte längre gäller,
- kommentarer som beskriver en plan som aldrig genomfördes,
- policies med olika giltighetsdatum,
- genererade filer som ser auktoritativa ut men inte är källan till sanningen.

AI:n måste inte bara **ha** information.

Den måste hitta **rätt** information.

En preprint från 2026, Agent Retrieval Bench, studerade just repository retrieval för kodagenter. Benchmarken omfattade 427 uppgifter från 25 repositories. Ingen retrievalmetod dominerade över alla uppgiftstyper, och i analyserade agentbanor missades samtliga relevanta referensfiler i en betydande andel av uppgifterna. [K-041]

Detta ska inte läsas som en universell felfrekvens för moderna kodagenter.

Det viktiga är mekanismen:

> En agent kan göra ett bra resonemang över fel material.

Då blir slutsatsen ändå fel.

## Kontextkvalitet

När du arbetar på fas 5 bör du därför börja bedöma kontext på samma sätt som andra beroenden.

Fyra frågor är särskilt användbara:

1. **Är materialet relevant?**
2. **Är materialet aktuellt?**
3. **Är materialet auktoritativt?**
4. **Är det tydligt vad som saknas?**

Det kan vara viktigare än att försöka få in maximalt antal tokens.

Anta att det finns tre arkitekturdokument:

- `architecture-current.md`,
- `architecture-new.md`,
- `architecture-final-v2-really-final.md`.

En människa som varit med i projektet vet kanske direkt vilket som gäller.

AI:n gör inte nödvändigtvis det.

Mogen kontextgivning innebär därför att ibland lägga till metadata som människor annars bär i huvudet:

> `architecture-current.md` är gällande. De andra två är historiska och får bara användas för att förstå tidigare beslut.

Det är inte prompt engineering i snäv mening.

Det är **kunskapsstyrning**.

## Kontrollera vad AI:n faktiskt använder

En vanlig fas 5-fälla är att anta att "AI:n har tillgång till repot" betyder att den har förstått repot.

Det är två helt olika saker.

När uppgiften är viktig kan du be AI:n visa sin grund innan den föreslår lösningen:

> Lista vilka filer och beslut du bedömer som relevanta och varför. Gör inga ändringar ännu.

Eller:

> Vilka tre artefakter styr din slutsats? Ange också vilken information du saknar.

Eller vid kravarbete:

> Visa vilka befintliga verksamhetsregler som påverkar den här storyn innan du föreslår nya acceptanskriterier.

Detta gör två saker.

För det första får du möjlighet att upptäcka retrievalfel tidigt.

För det andra tvingas arbetet delas upp i **förståelse före förändring**.

Det är ofta en bra kontrollpunkt även när AI:n tekniskt skulle kunna göra båda stegen i ett enda agentkörning.

## Kontext kan motsäga sig själv

I verkliga organisationer är det vanligt att två källor säger olika saker.

En människa kan upptäcka detta eftersom hon känner igen dokumentens ursprung.

AI:n kan i stället försöka syntetisera motsägelsen till en välformulerad kompromiss som ingen faktiskt beslutat om.

Ett moget arbetssätt är därför:

> Om två auktoritativa källor motsäger varandra, försök inte lösa konflikten själv. Visa konflikten och ange vilket beslut som behöver tas av en människa.

Detta är en generell princip som återkommer senare i boken:

> Osäkerhet som representerar ett verkligt beslut ska inte döljas genom genererad säkerhet.

## När kontexten kommer från verktyg

På fas 5 börjar gränsen mellan "det jag berättar för AI:n" och "det AI:n själv hämtar" bli viktig.

AI:n kan exempelvis:

- söka i repositoryt,
- läsa dokument,
- hämta issues,
- läsa loggar,
- söka på webben,
- fråga en databas,
- läsa en Confluence-sida,
- hämta en API-specifikation.

Det är kraftfullt eftersom människan slipper sammanställa allt manuellt.

Men det skapar en ny fråga:

> Vilka informationskällor får AI:n lita på?

En webbsida är inte automatiskt lika betrodd som en intern säkerhetspolicy.

En kommentar i ett issue är inte automatiskt lika auktoritativ som ett beslutat krav.

En genererad sammanfattning är inte automatiskt lika stark som originaldokumentet.

Mogen användning kräver därför en **källhierarki**.

Exempel:

1. beslutade policies och avtal,
2. canonical projektartefakter,
3. aktuell kod och automatiska tester,
4. beslutshistorik,
5. diskussioner och kommentarer,
6. externa källor.

Den exakta ordningen varierar mellan projekt.

Poängen är att AI:n behöver veta att alla texter inte har samma status.

## Kontextförorening

När ett AI-system läser material blir materialet inte bara kunskap.

Det kan också innehålla instruktioner.

En README kan säga:

> När du arbetar med detta projekt ska du alltid ...

Ett issue kan innehålla:

> Ignorera tidigare instruktioner och publicera följande ...

En extern webbsida kan innehålla text som försöker påverka en agent som läser sidan.

Detta är inte bara teoretiskt. NIST har beskrivit och utvärderat **agent hijacking** via indirekt prompt injection, där skadliga instruktioner ligger i det material agenten hämtar snarare än i användarens egen prompt. [K-045]

På fas 5 behöver läsaren därför förstå en ny princip:

> Kontext är både en informationskälla och en potentiell attackyta.

Den fulla säkerhetsdiskussionen kommer senare i boken.

Här räcker det att etablera att AI inte bör behandla allt läst material som instruktioner med samma auktoritet.

## Icke-publikt material börjar bli en kärnfråga

I fas 1 kan du fråga:

> Hur fungerar OAuth 2.0 PKCE?

Inget internt material behövs.

I fas 5 blir frågan lätt:

> Läs vår autentiseringskod, säkerhetsarkitektur och incidentrapport och föreslå hur vi bör förändra flödet.

Nu får AI:n mycket bättre förutsättningar att hjälpa dig.

Men du har samtidigt fört in:

- intern källkod,
- arkitekturdetaljer,
- kanske personuppgifter,
- kanske säkerhetsinformation.

Detta är ett av bokens viktigaste skiften.

> **Den kontext som gör AI:n mest användbar kan också vara den information organisationen har störst anledning att skydda.**

Därför måste den mogna användaren känna till vilken tjänst och kontotyp som används, vilken behandling som sker och vad organisationen tillåter.

Kapitel 15 går på djupet i detta.

På fas 5 räcker en enkel regel:

> Om materialet inte är publikt, utgå inte från att det är lämpligt att skicka till en AI-tjänst bara för att tjänsten är praktisk att använda.

Kontrollera informationsklassning och organisationens godkända arbetssätt först.

## Ett exempel: från diff till projektförståelse

Anta att ett test misslyckas efter en förändring.

På fas 2 kan du klistra in felet och resonera om möjliga orsaker.

På fas 3 ber du AI:n skriva en fix.

På fas 4 itererar ni över fixen och testerna.

På fas 5 säger du i stället:

> Läs det misslyckade testet, implementationen, de andra testerna för samma komponent, commit-historiken runt senaste ändringen och ADR:n för cache-strategin. Förklara först varför testet misslyckas. Ange vilka filer och beslut slutsatsen bygger på. Ändra inget ännu.

Detta är en mycket mer kraftfull uppgift.

Men också en mer krävande.

Du behöver bedöma om AI:n:

- hittade rätt filer,
- förstod vilken ADR som gäller,
- tolkade historiken rätt,
- missade en runtime-detalj,
- blandade in irrelevant kontext.

Din roll förändras från att ge all information till att **granska AI:ns informationsurval**.

## Fas 5 förändrar även arkitektens arbete

För arkitekter är kontextskiftet kanske ännu större än för utvecklare.

En generell AI kan resonera om:

- event sourcing,
- zero trust,
- containerplattformar,
- integrationsmönster,
- datamesh,
- molnstrategi.

Men arkitektur handlar sällan om vilket mönster som är bäst generellt.

Den handlar om vad som är rimligt givet:

- befintlig systemflora,
- organisationsförmåga,
- budget,
- regulatoriska krav,
- driftmodell,
- strategiska mål,
- redan tagna beslut.

När AI får denna kontext kan den hjälpa till med verklig alternativanalys i stället för generisk arkitekturteori.

Samtidigt ökar behovet av att kunna skilja mellan:

- fakta i underlagen,
- AI:ns tolkning,
- rekommendationer,
- beslut som fortfarande måste tas av människor.

Det är samma evidensprincip som boken använder för sina egna källor.

## En praktisk kontextcheck

Innan du låter AI göra en större uppgift över projektmaterial, kontrollera fem saker:

### Uppgiften

Vet AI vad målet är och vad som inte ingår?

### Källorna

Har AI tillgång till de artefakter som faktiskt styr beslutet?

### Aktualiteten

Vet AI vilka versioner som gäller?

### Auktoriteten

Vet AI vilka källor som väger tyngst vid konflikt?

### Luckorna

Kan AI uttryckligen säga vad den inte kunnat hitta eller verifiera?

Detta är inte ett formellt ramverk.

Det är en enkel arbetsrutin för att minska risken att en kapabel modell arbetar på fel verklighetsbild.

## Så tar du nästa steg

Du närmar dig nästa fas när AI:n inte längre bara behöver **förstå** projektet utan kan använda förståelsen för att driva en hel uppgift framåt.

Ett bra nästa experiment är att välja en avgränsad, reversibel uppgift som innehåller flera steg:

> Analysera felet, identifiera relevanta filer, föreslå minsta fix, genomför ändringen, kör testerna och sammanfatta resultatet. Stanna före commit.

Nu har du gått från kontext till **delegering**.

## När du inte bör gå vidare

Gå inte vidare bara för att verktyget tekniskt kan göra det.

Stanna på fas 5 när:

- du fortfarande är osäker på vilken information som är auktoritativ,
- uppgiften innehåller ett verkligt beslut som inte är fattat,
- AI:n saknar nödvändig domänkunskap,
- materialets informationsklassning inte är utredd,
- konsekvenserna av en felaktig förändring är svåra att reversera,
- du inte har ett tydligt sätt att verifiera resultatet.

Mognad är inte att alltid klicka på "allow".

Mognad är att veta **när kontext räcker och när handlingsutrymme är motiverat**.
