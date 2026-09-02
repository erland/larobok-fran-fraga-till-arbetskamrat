# Kapitel 15 – När AI behöver känna till det som inte är publikt

De första gångerna någon använder generativ AI i arbetet är informationsfrågan ofta enkel.

Man frågar:

> Hur fungerar optimistic locking?

eller:

> Vilka för- och nackdelar har eventdriven arkitektur?

Inget i frågan behöver säga något om den egna organisationen.

Sedan förändras användningen.

I fas 5 började vi ge AI verklig kontext. Repositoryn, dokument, testresultat, arkitekturmodeller och tidigare beslut blev en del av arbetet. I fas 6 fick AI dessutom använda verktyg. I fas 7 kunde den bli en del av ett helt arbetsflöde.

Det är också ungefär där en ny fråga blir omöjlig att ignorera:

> **Vad händer när AI behöver känna till sådant vi inte vill göra publikt?**

Det kan handla om:

- källkod,
- intern dokumentation,
- arkitekturmodeller,
- loggar och incidentdata,
- kundinformation,
- personuppgifter,
- avtal,
- säkerhetsbrister,
- ännu inte offentliggjorda produkter,
- interna strategier och beslut.

Den enkla lösningen är att säga:

> Skicka aldrig känslig information till AI.

Det rådet minskar risk, men det tar också bort en stor del av nyttan från den mogna AI-användning som resten av boken handlar om.

Den andra ytterligheten är lika problematisk:

> Vi har ett enterpriseavtal, så allt är säkert.

Ett avtal kan förändra riskbilden kraftigt. Men det ersätter inte informationsklassning, dataminimering, behörighetsstyrning eller förståelse för hur tjänsten faktiskt fungerar.

Mogen AI-användning kräver därför ett tredje förhållningssätt:

> **Ge AI den information som behövs – men gör ett medvetet val av information, tjänst, avtalsform och informationsflöde.**

## Börja inte med frågan om träning

En vanlig första fråga är:

> Tränar leverantören sin modell på våra prompts?

Det är en viktig fråga.

Men den är bara en del av problemet.

Anta att en leverantör lovar att aldrig använda organisationens data för modellträning.

Följande kan fortfarande vara relevanta frågor:

- Sparas prompten?
- Hur länge?
- Sparas uppladdade filer?
- Kan organisationens administratörer läsa konversationerna?
- Kan leverantörens personal få åtkomst i support- eller säkerhetssituationer?
- Vilka underleverantörer behandlar informationen?
- Var behandlas den geografiskt?
- Skickas delar av prompten vidare när webbsökning används?
- Kan en connector läsa eller skriva data i ett annat system?
- Vad händer om användaren skickar feedback på svaret?

Det är därför viktigt att skilja mellan åtminstone tre saker:

1. **modellträning,**
2. **databehandling för att leverera tjänsten,**
3. **lagring och annan efterföljande behandling.**

De är inte samma sak.

### Ett konkret exempel

OpenAI anger för sina företagsprodukter och API att organisationers in- och utdata inte används för modellträning som standard. Företagsprodukter har dessutom olika möjligheter till retention controls, och för kvalificerade API-kunder finns Zero Data Retention. [K-071] [K-072]

Anthropic anger på motsvarande sätt att data från kommersiella produkter som Claude for Work och API inte används för modellträning som standard. Samtidigt anger Anthropic en standardretention på upp till 30 dagar för API-data om inget annat avtalats, medan chatprodukter kan lagra konversationer för att tillhandahålla historik. [K-073] [K-074]

Microsoft anger att prompts, svar och data som Microsoft 365 Copilot hämtar via Microsoft Graph inte används för att träna foundation models. Samma dokumentation beskriver samtidigt att prompts och svar lagras som en del av användarens Copilot activity history och hanteras inom Microsoft 365:s retention- och compliancefunktioner. [K-076] [K-077]

Google anger för kvalificerade Workspace-erbjudanden med Gemini att organisationens innehåll inte används för att träna generativa modeller utanför organisationens domän utan tillstånd. Samtidigt varierar retention mellan olika Gemini-funktioner och kan styras av administratörer. [K-078]

Detta är **leverantörsuppgifter**.

De är relevanta för en bedömning, men de är inte oberoende forskningsresultat om hur säkra tjänsterna är.

Och de illustrerar en viktig princip:

> **"Används inte för träning" betyder inte "behandlas eller lagras inte".**

## Kontotypen kan vara lika viktig som produktnamnet

Det räcker sällan att fråga:

> Får vi använda Claude?

eller:

> Får vi använda ChatGPT?

Samma produktfamilj kan ha:

- konsumentkonto,
- individuellt betalkonto,
- team-/businesskonto,
- enterpriseavtal,
- API-användning med separata villkor.

Datahantering och administrativa kontroller kan skilja sig mellan dessa.

Anthropic gör exempelvis en uttrycklig skillnad mellan kommersiella erbjudanden och konsumentprodukter när det gäller användning av konversationer för modellförbättring. [K-073]

Det är därför ett dåligt organisationsbeslut att säga:

> "AI-tjänst X är godkänd."

Ett bättre beslut är närmare:

> "Den här produktvarianten, med den här kontotypen, under dessa avtalsvillkor och konfigurationer, får användas för dessa informationsklasser och användningsfall."

Det låter byråkratiskt.

Men skillnaden blir konkret den dag en medarbetare använder ett privat konto för att göra något som hade varit accepterat i organisationens enterprise-miljö.

## Informationen du skickar är inte bara filen

Anta att du vill få hjälp att analysera en incident.

Du tar bort loggfilens verkliga IP-adresser och användar-ID:n.

Sedan skriver du:

> Vi har upptäckt att vår internetexponerade administrationsportal för kärnsystemet X accepterar återanvända sessionscookies efter logout. Incidenten upptäcktes i går kväll. Hur bör vi utreda om den har utnyttjats?

Du har kanske sanerat bilagan.

Men själva frågan berättar:

- vilket system som berörs,
- att systemet är internetexponerat,
- vilken typ av sårbarhet som finns,
- att organisationen nyligen upptäckt den,
- att man inte vet om den exploaterats.

**Prompten är själv information.**

Detta är lätt att missa eftersom människor gärna tänker på "data" som filer, databaser och dokument.

I ett AI-system är även:

- instruktionen,
- konversationshistoriken,
- systemprompten,
- verktygsresultaten,
- metadata,
- svaret

potentiella informationsbärare.

OWASP:s vägledning om *Sensitive Information Disclosure* pekar uttryckligen på risken att användare oavsiktligt lämnar personuppgifter, affärshemligheter och annan känslig information till LLM-system. [K-079]

Det gör en särskild fråga värd att ställa innan man trycker på Enter:

> **Vad avslöjar min fråga även om jag inte bifogar någonting?**

## Promptminimering

Dataminimering är en etablerad princip i dataskydd och informationshantering.

I AI-arbete behöver den få en praktisk motsvarighet i själva dialogen.

Vi kommer här använda begreppet **promptminimering**.

Det är **bokens egen pedagogiska syntes**, inte en etablerad säkerhetsstandard.

Principen är:

> **Ge AI den minsta mängd identifierande och känslig kontext som behövs för att lösa just uppgiften.**

Det betyder inte att prompten ska bli så generell att AI:n inte längre kan hjälpa.

Det betyder att skilja på information som faktiskt påverkar lösningen och information som bara råkar finnas i verkligheten.

### Före

> Vi bygger om Tullsystem X hos Myndighet Y eftersom leverantör Z:s produkt inte klarar mer än 3 000 samtidiga sessioner. I november ska vi lansera en ännu ej offentliggjord e-tjänst för målgrupp Q. Vilka cachingstrategier bör vi överväga?

### Efter promptminimering

> Vi har en webbapplikation med en befintlig sessionsbegränsning i en beroende komponent. En kommande tjänst väntas kraftigt öka antalet samtidiga användare. Vilka caching- och sessionsstrategier bör vi jämföra, och vilka trade-offs bör vi analysera?

Den andra frågan kan mycket väl ge samma tekniska värde.

Men den avslöjar betydligt mindre.

Det centrala är alltså inte att alltid anonymisera allt.

Det centrala är att fråga:

> **Vilken detalj behöver modellen för att göra jobbet?**

## Maskning, pseudonymisering och anonymisering är inte samma sak

Ordet *anonymiserad* används ofta slarvigt.

En utvecklare kan säga:

> Jag anonymiserade loggen. Jag bytte användarnamn mot User-17.

Det kan vara en bra riskreducerande åtgärd.

Men det betyder inte nödvändigtvis att informationen juridiskt eller tekniskt är anonym.

EDPB:s vägledning om pseudonymisering beskriver pseudonymisering som att identifierande data ersätts så att ytterligare information krävs för att koppla materialet till en person. Samma vägledning är tydlig med att pseudonymiserade data fortfarande är personuppgifter när återkoppling till individen är möjlig. [K-081]

Det ger oss tre praktiskt olika situationer.

### Maskning

Du tar bort eller ersätter vissa identifierande fält:

```text
Anna Andersson, 1970-01-01
```

blir:

```text
Person A, [födelsedatum borttaget]
```

Det reducerar exponeringen.

Men andra uppgifter kan fortfarande göra personen identifierbar.

### Pseudonymisering

Du ersätter identiteten med ett stabilt alias:

```text
customer_7f92a1
```

och håller kopplingsnyckeln separat.

Det kan möjliggöra analys över flera poster utan att den direkta identiteten följer med.

Men uppgifterna kan fortfarande vara personuppgifter.

### Anonymisering

För verklig anonymisering måste risken att identifiera personen vara tillräckligt eliminerad med hänsyn till den information och de möjligheter som rimligen finns tillgängliga.

Det är ett betydligt högre krav än att ta bort namn.

EDPB publicerade i juli 2026 ett nytt utkast till riktlinjer om anonymisering. Vid denna boks researchdatum är det fortfarande ett **konsultationsutkast**, och ska därför inte behandlas som slutlig vägledning. [K-082]

Det viktigaste praktiska rådet är därför:

> **Kalla inte material anonymt bara för att de uppenbara identifierarna är borta.**

## När detaljer tillsammans identifierar

Anta att följande tas bort från ett supportärende:

- namn,
- e-postadress,
- personnummer.

Kvar finns:

- "enda kvinnliga databasadministratören på kontoret i Kiruna",
- exakt datum för en ovanlig incident,
- systemnamn,
- arbetspass,
- en unik kombination av behörigheter.

Varje uppgift kan verka oskyldig.

Tillsammans kan de peka ut en person.

Samma sak gäller affärsinformation.

Du kanske tar bort kundens namn men lämnar:

- bransch,
- land,
- avtalsstorlek,
- unik produktkombination,
- planerat lanseringsdatum.

För den som känner marknaden kan kunden fortfarande vara uppenbar.

Därför behöver minimering ske på **informationsnivå**, inte bara på fältnivå.

## Generalisering kan ibland vara bättre än borttagning

Det finns en praktisk balans.

Tar du bort för mycket blir analysen värdelös.

Ibland är det bättre att generalisera.

Exempel:

| Verklig uppgift | Möjlig generalisering |
|---|---|
| 4 732 819 kunder | flera miljoner kunder |
| Stockholm, 14 september kl. 02:13 | nordisk region, nattlig drift |
| Oracle 19c på tre specifika servrar | relationsdatabas i redundant kluster |
| intern systemkod TV-AML-07 | regelmotor för riskanalys |
| 17-årig pojke med exakt diagnos | minderårig person i relevant behandlingskategori |

Generaliseringen bör bevara det som påverkar problemet och ta bort det som bara identifierar sammanhanget.

Detta är inte alltid möjligt.

Om den exakta databasmotorn är orsaken till felet behöver modellen veta vilken den är.

Om den exakta åldern påverkar en juridisk regel kan "minderårig" vara för grovt.

Mogen informationsminimering kräver därför samma sorts omdöme som resten av boken.

## Syntetiska exempel kan räcka långt

För vissa uppgifter behövs inga verkliga data alls.

Du kanske vill veta om AI kan hjälpa till att klassificera supportärenden.

I stället för att börja med tusen verkliga supportärenden kan du skapa eller låta generera ett syntetiskt testmaterial som representerar:

- vanliga ärendetyper,
- gränsfall,
- felstavningar,
- olika språk,
- olika längd,
- motstridiga signaler.

Det ger inte samma bevis som ett test på verklig data.

Men det kan räcka för att avgöra om idén är värd att ta vidare.

Detta ger en enkel progression:

1. **syntetiskt material** för tidig utforskning,
2. **minimerat/pseudonymiserat material** när verkliga mönster behövs,
3. **verkligt material** först när nytta, avtal och skydd motiverar det.

Även detta är bokens praktiska rekommendation, inte en universell regel.

## Källkod är inte bara text

Utvecklare ser ibland en repository som mindre känslig än en kunddatabas.

Det kan vara fel.

Källkod kan avslöja:

- interna domänbegrepp,
- systemarkitektur,
- beroenden,
- säkerhetskontroller,
- interna adresser,
- API-kontrakt,
- sårbarheter,
- hemligheter som av misstag checkats in,
- framtida funktioner.

Det betyder inte att källkod aldrig bör användas med molnbaserad AI.

Det betyder att "ingen persondata" inte är samma sak som "ingen informationsrisk".

Organisationen behöver förstå både:

- **konfidentialitetsvärdet** i koden,
- **vilken AI-miljö** koden lämnas till.

Det är också en anledning till att repositorybaserade kodagenter bör köras med tydlig organisationspolicy och rätt kontotyp snarare än genom individuella ad hoc-beslut.

## Loggar är särskilt förrädiska

Loggar ser tekniska ut.

I praktiken innehåller de ofta:

- personuppgifter,
- tokens,
- sessions-ID:n,
- e-postadresser,
- interna URL:er,
- query-parametrar,
- kund-ID:n,
- stack traces,
- databasnycklar,
- delar av request- och response-payloads.

En utvecklare som kopierar "bara felet" till en AI-assistent kan därför skicka mycket mer information än avsett.

För loggar är en bra arbetsordning ofta:

1. identifiera vilka fält som faktiskt behövs,
2. ta bort credentials och tokens,
3. maska eller pseudonymisera identifierare,
4. reducera tidsfönstret,
5. kontrollera fritextfält,
6. först därefter skicka materialet.

Det är betydligt bättre än att klistra in tusen rader och be modellen "hitta problemet".

Det förbättrar dessutom ofta själva analysen genom att minska irrelevant brus.

## Säkerhetsproblem kan exponeras av själva felsökningsfrågan

För säkerhetsrelaterade frågor behöver promptminimering ibland gå längre.

Frågan:

> Vår publika inloggning på `admin.example.se` accepterar fortfarande JWT:n efter att användaren inaktiverats. Hur exploaterbart är detta?

innehåller nästan en liten sårbarhetsrapport.

För en första analys kanske följande räcker:

> I ett webbsystem fortsätter tidigare utfärdade JWT:er att accepteras efter att kontot inaktiverats. Vilka risker, designalternativ och verifieringssteg bör vi analysera?

Om det senare visar sig nödvändigt att analysera exakt implementation kan mer kontext tillföras i en godkänd miljö.

Det är samma princip som i resten av mognadsresan:

> **Öka kontexten när den ger verkligt värde – inte av slentrian.**

## Frågan kan avslöja ett ännu ej fattat beslut

Teknisk information är inte den enda risken.

Tänk på följande prompt:

> Hjälp mig skriva ett migrationsmeddelande eftersom vi tänker säga upp leverantör X nästa kvartal och flytta alla kunder till produkt Y innan fusionen offentliggörs.

Ingen personuppgift finns där.

Men prompten kan innehålla:

- strategiskt beslut,
- leverantörsförhandling,
- kundpåverkan,
- tidsplan,
- potentiellt marknadspåverkande information.

Detta illustrerar varför informationsklassning måste vara bredare än GDPR.

För en organisation kan icke-publikt material också vara:

- säkerhetsskyddsvärt,
- sekretessbelagt,
- exportkontrollerat,
- avtalsmässigt konfidentiellt,
- en företagshemlighet,
- insiderinformation,
- strategiskt känsligt.

Den här boken försöker inte ge juridisk rådgivning för varje sådan kategori.

Men den mogna användaren behöver känna igen att de finns.

## Connectors förändrar frågan från "vad skickar jag?" till "vad kan AI nå?"

När AI endast tar emot text som du själv klistrar in är informationsflödet relativt synligt.

Med connectors blir det annorlunda.

AI:n kan kanske läsa:

- e-post,
- dokument,
- ärendehantering,
- källkod,
- databaser,
- kalender,
- chattar.

Då är den centrala frågan inte längre bara:

> Vad har jag skickat?

utan:

> **Vad har AI-systemet möjlighet att hämta?**

Detta återkopplar direkt till delegationsbudgeten från kapitel 9.

Databehörighet och verktygsbehörighet behöver ses tillsammans.

En agent som kan läsa hela dokumentarkivet och skicka e-post har en helt annan riskprofil än en modell som bara får analysera ett anonymiserat textstycke.

## Extern kontext kan försöka lura agenten

Connectors och webbsökning skapar dessutom en annan typ av risk.

Materialet AI:n läser kan innehålla instruktioner.

OWASP beskriver *prompt injection* som en risk där innehåll påverkar modellens beteende på ett sätt användaren eller systemägaren inte avsett. Det kan även ske indirekt genom dokument, webbsidor eller andra datakällor som agenten läser. [K-080]

Tänk dig ett automatiserat arbetsflöde som:

1. läser ett inkommande supportärende,
2. hämtar kundinformation,
3. analyserar problemet,
4. skriver ett svar.

Om ett inkommande ärende innehåller text som försöker instruera agenten att ignorera sina regler eller hämta annan kundinformation får vi ett problem som inte fanns när AI bara var en passiv frågelåda.

Det är ytterligare ett skäl till att fas 6 och 7 kräver mer än goda prompts.

De kräver systemdesign.

## Informationsbudgeten

I kapitel 9 använde vi **delegationsbudgeten** för att resonera om hur mycket handlingsutrymme AI ska få.

Här behöver vi en motsvarande modell för information.

Vi kallar den **informationsbudgeten**.

Det är **bokens egen syntes**, inte en etablerad standard eller juridisk klassningsmodell.

Den består av sju frågor.

### 1. Behov – vad försöker vi åstadkomma?

Börja med arbetsuppgiften.

> Behöver AI:n hitta ett syntaxfel, förstå ett domänproblem eller analysera en faktisk incident?

Ju mer exakt behovet är, desto lättare blir det att avgöra vilken information som faktiskt krävs.

### 2. Minsta kontext – vad måste AI veta?

Identifiera:

- fakta som påverkar lösningen,
- begränsningar,
- relevanta exempel,
- nödvändiga relationer.

Allt annat är kandidat för borttagning eller generalisering.

### 3. Identifiering – vad kan maskas, pseudonymiseras eller generaliseras?

Kontrollera både:

- dokument och filer,
- promptens formulering.

Fråga också om flera indirekta uppgifter tillsammans återidentifierar person, kund, system eller händelse.

### 4. Tjänst – var ska materialet behandlas?

Kontrollera:

- produktvariant,
- kontotyp,
- avtalsmodell,
- aktuella privacy-/securityvillkor,
- retention,
- administrativa kontroller.

Lita inte på hur produkten fungerade för ett år sedan.

Leverantörsvillkor förändras.

### 5. Flöde – vart kan informationen ta vägen?

Titta bortom modellen:

- historik,
- loggar,
- feedback,
- webbsökning,
- connectors,
- plugins,
- API-gateways,
- observability,
- underleverantörer,
- output till andra system.

### 6. Konsekvens – vad händer om vi har fel?

Fråga:

> Vad är konsekvensen om denna information exponeras för fel mottagare?

och:

> Vad är konsekvensen om AI:n använder den på fel sätt?

Riskerna kan vara olika.

### 7. Beslut – använd, minimera, byt miljö eller avstå

Resultatet behöver inte vara ja eller nej.

Det kan bli:

- använd materialet som det är i godkänd enterprise-miljö,
- maska vissa fält först,
- använd syntetiskt data,
- använd en intern modellmiljö,
- kör analysen lokalt,
- avstå från AI för just detta steg.

Det sista alternativet är också ett tecken på mognad.

## Fyra nivåer av praktisk hantering

Informationsbudgeten kan leda till fyra typiska arbetssätt.

### Nivå A – Publikt eller ofarligt abstraherat material

Exempel:

- öppen dokumentation,
- publikt repository,
- syntetiska exempel,
- generiska arkitekturfrågor.

Här är informationsrisken ofta låg.

### Nivå B – Internt men reducerat material

Exempel:

- intern kod där secrets och identifierande information tagits bort,
- pseudonymiserade loggar,
- generaliserade arkitekturproblem,
- interna dokument med känsliga bilagor borttagna.

Här kan promptminimering ge stor effekt.

### Nivå C – Verkligt känsligt material i kontrollerad AI-miljö

Exempel:

- full intern repository,
- produktionsnära loggar,
- juridiska dokument,
- personuppgifter som faktiskt behövs för uppgiften.

Här blir organisationens godkända tjänst, avtal, retention, access controls och juridiska bedömning centrala.

### Nivå D – Material som inte bör lämna den godkända säkerhetsdomänen

För vissa uppgifter kan slutsatsen vara att en extern molntjänst inte är rätt miljö alls.

Då kan alternativen vara:

- lokal behandling,
- isolerad intern miljö,
- särskilt upphandlad/konfigurerad tjänst,
- ingen AI-behandling.

Det finns ingen generell lista som passar alla organisationer.

Informationsklassning och regelverk skiljer sig.

## "Enterprise" flyttar ansvar – det tar inte bort det

Företagsavtal ger ofta sådant som privatkonton saknar:

- administrativ kontroll,
- SSO,
- central användarhantering,
- retention controls,
- audit,
- avtalsmässiga dataskyddsåtaganden,
- möjlighet till särskilda region- eller datakontroller.

Det är viktiga egenskaper.

Men ett enterpriseavtal hindrar inte automatiskt en användare från att:

- be AI hämta mer information än uppgiften kräver,
- klistra in en hemlighet,
- skapa en prompt som avslöjar ett känsligt beslut,
- dela ett genererat svar till fel mottagare,
- ge en agent för stora behörigheter.

Mognad kräver därför både **bra plattform** och **bra arbetssätt**.

Det ena ersätter inte det andra.

## Organisationens administratörer kan vara en del av åtkomstmodellen

Många användare tänker på en AI-chatt som en privat dialog mellan dem och modellen.

I en organisationsmiljö är det inte alltid en bra mental modell.

Beroende på tjänst och konfiguration kan organisationen ha funktioner för:

- retention,
- audit,
- eDiscovery,
- compliance,
- export,
- administrativ hantering.

Microsoft beskriver exempelvis att Copilot-interaktioner kan omfattas av organisationens retention- och compliancefunktioner. [K-077]

Anthropic beskriver att Primary Owners i Claude for Work hanterar organisationens konto och kan begära dataexporter som kan innehålla användardata. [K-083]

Det kan vara precis vad organisationen behöver för styrning och regelefterlevnad.

Men det betyder också att en användare inte bör utgå från att en företags-AI är en personlig privat anteckningsbok.

## Feedbackknappen kan vara ett eget informationsflöde

En detalj som ofta förbises är feedback.

En tjänst kan ha starka standardvillkor för kunddata men behandla material annorlunda när användaren aktivt skickar feedback eller en buggrapport.

Anthropic anger exempelvis att material som användaren uttryckligen skickar som feedback kan lagras längre och användas för modellutveckling. [K-073]

OpenAI:s företagsåtaganden bygger på att träning inte sker på företagsdata som standard, med möjlighet till uttryckligt opt-in för vissa användningsfall. [K-071]

Den praktiska principen är enkel:

> **Skicka inte feedback på en känslig konversation innan du vet vad feedbackfunktionen innebär för databehandlingen.**

Det är en liten detalj.

Men mogna arbetssätt består ofta av just sådana detaljer.

## Separera analysen från identifieringen

En användbar teknik är att dela upp arbetet.

Anta att du behöver analysera fem kundincidenter.

I stället för att låta AI:n se full kundidentitet kan du lokalt skapa:

```text
Incident A
Incident B
Incident C
Incident D
Incident E
```

AI:n analyserar:

- mönster,
- sannolik rotorsak,
- gemensamma tekniska signaler,
- rekommenderade åtgärder.

Den lokala processen mappar sedan tillbaka resultatet till verkliga kunder.

Detta är ett exempel på **separation av analys och identitet**.

Det fungerar inte för alla uppgifter.

Men när det fungerar minskar det mängden identifierande data AI:n behöver se utan att analysvärdet försvinner.

## Tänk på svaret också

Informationsflödet går åt två håll.

Du kan vara mycket noggrann med vad som skickas in och sedan få ett svar som sammanställer information på ett känsligare sätt än originalmaterialet.

Exempel:

AI:n läser hundra interna tickets där varje ticket bara innehåller en liten del av bilden.

Svaret blir:

> De tre återkommande säkerhetsbristerna finns i system A, B och C. System B har dessutom saknat patchning sedan februari och ägs av team D.

AI:n har inte skapat nya fakta.

Men den har **aggregerat** dem till en mer känslig informationsprodukt.

Därför behöver även output:

- klassificeras,
- lagras rätt,
- delas med rätt mottagare.

Ett AI-svar är inte ofarligt bara för att varje enskild källa var tillåten att läsa.

## När molnfrågan blir en arkitekturfråga

På individnivå ser problemet ut som:

> Får jag klistra in detta?

På organisationsnivå är frågan större:

> **Hur ska vår AI-arkitektur göra rätt användning enkel och fel användning svårare?**

Det kan innebära:

- central identitet,
- godkända modeller,
- informationsklassning,
- DLP,
- connectorstyrning,
- behörigheter,
- logging,
- retention,
- separata miljöer för olika informationsklasser,
- lokala eller privata modeller för vissa användningsfall.

Microsofts Purview-dokumentation illustrerar exempelvis hur organisationer kan kombinera Copilot med sensitivity labels, DLP, retention, audit och eDiscovery. [K-084]

Det är inte ett bevis för att just Microsofts lösning är rätt.

Det visar däremot hur AI-användning på högre mognadsnivå blir en fråga om **informationsarkitektur och styrning**, inte bara användarutbildning.

Det leder direkt till bokens sista kapitel.

## Ett praktiskt exempel: felsökning av en produktionsincident

Anta att ett team har ett intermittent fel i notifieringstjänsten från Del III.

De vill använda AI för rotorsaksanalys.

### Omoget arbetssätt

En utvecklare exporterar:

- hela loggfilen,
- full konfiguration,
- ett produktionsdatabasdump,
- interna URL:er,
- kunduppgifter.

Sedan laddas allt upp till ett privat AI-konto med prompten:

> Varför fungerar det inte?

Problemet är inte bara att informationen är omfattande.

Arbetssättet saknar kontroll över:

- behov,
- dataminimering,
- tjänst,
- kontotyp,
- informationsflöde,
- verifiering.

### Mognare arbetssätt

Teamet börjar med hypotesen:

> Felet tycks uppstå mellan statusändring och publicering till meddelandekön.

De tar fram:

- relevant kod för publiceringssteget,
- några få representativa stack traces,
- pseudonymiserade correlation IDs,
- relevant konfiguration utan secrets,
- kontraktet för meddelandet.

Prompten beskriver systemet generellt och nämner inte kunder eller interna värden som inte påverkar analysen.

Materialet behandlas i organisationens godkända AI-miljö.

AI:n får i första steget bara analysera.

Om mer kontext behövs läggs den till medvetet.

Skillnaden mellan de två arbetssätten är större än skillnaden mellan två språkmodeller.

Det är just den sortens mognad den här boken handlar om.

## En checklista före känslig AI-användning

Innan icke-publikt material används kan följande frågor fungera som en snabb kontroll:

1. **Behövs informationen?** Kan uppgiften lösas med mindre eller syntetisk kontext?
2. **Vad avslöjar prompten?** Även utan bilagor.
3. **Är materialet verkligen anonymt?** Eller bara maskat/pseudonymiserat?
4. **Vilket konto använder jag?** Privat, individuellt, business, enterprise eller API?
5. **Används materialet för träning?** Under just denna avtalsmodell?
6. **Hur lagras det?** Prompts, svar, filer, feedback och loggar.
7. **Vem kan få åtkomst?** Leverantör, organisationens administratörer och underleverantörer.
8. **Vilka verktyg är aktiva?** Webbsökning, connectors, plugins och agentverktyg.
9. **Vilken konsekvens får exponering?** För person, organisation, säkerhet eller affär.
10. **Finns en bättre miljö?** Intern, lokal eller särskilt kontrollerad behandling.

Checklistan ersätter inte organisationens juridiska eller säkerhetsmässiga bedömning.

Den hjälper användaren att upptäcka när en sådan bedömning behövs.

## Mogen användning kan innebära att säga nej

Genom stora delar av boken har mognadsresan gett AI större roll.

Det skulle därför vara lätt att tro att den mest mogna användaren alltid hittar ett sätt att använda AI.

Så är det inte.

En mogen användare kan komma fram till:

> Jag kan anonymisera detta tillräckligt och använda vår godkända tjänst.

eller:

> Jag behöver full kontext, så detta ska köras i vår interna miljö.

eller:

> Nyttan är för liten i förhållande till informationsrisken. Jag gör just detta steg utan AI.

Det är samma princip som vi sett kring autonomi.

Mognad betyder inte **mer AI överallt**.

Mognad betyder **bättre beslut om var och hur AI ska användas**.

## Från individens beslut till organisationens system

Det här kapitlet började med frågan:

> Vad händer när AI behöver känna till det som inte är publikt?

På individnivå kan svaret sammanfattas som:

- minimera onödig information,
- se prompten som data,
- skilj maskning, pseudonymisering och anonymisering,
- förstå tjänst och avtalsform,
- kartlägg hela informationsflödet,
- ge inte verktyg större åtkomst än de behöver,
- bedöm konsekvensen om något går fel.

Men det finns en gräns för hur mycket varje utvecklare, testare eller arkitekt rimligen ska behöva utreda på egen hand.

Om hundra medarbetare var och en måste läsa leverantörsvillkor, bedöma retention och avgöra vilka connectors som är säkra har organisationen skapat ett dåligt arbetssystem.

Det är därför nästa steg inte är ännu en personlig checklista.

Det är att flytta mognaden från individen till organisationen.

Det är ämnet för nästa och sista kapitel.
