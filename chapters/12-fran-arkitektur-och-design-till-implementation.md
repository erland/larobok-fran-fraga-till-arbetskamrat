# Kapitel 12 – Från arkitektur och design till implementation

Kravpaketet för statusnotiser är nu tillräckligt stabilt för att teamet ska börja tala om lösning.

Det är här generativ AI lätt blir imponerande.

På några sekunder kan den föreslå:

- en notifieringstjänst,
- eventdriven arkitektur,
- databasmodell för prenumerationer,
- API-endpoints,
- retry-kö,
- mallar för e-post,
- kodstruktur.

Problemet är inte att förslagen är dåliga.

Problemet är att **nästan alla rimliga lösningsmönster kan låta bra när de beskrivs utan det befintliga systemets begränsningar**.

Arkitektur och implementation handlar därför mindre om att hitta en tekniskt möjlig idé och mer om att välja en förändring som passar systemets mål, kvalitetskrav, befintliga struktur och förmåga att förvaltas.

## Arkitektens AI-problem är inte brist på alternativ

I en traditionell diskussion kunde det ta tid att få fram tre genomarbetade alternativ.

Med generativ AI är kostnaden för att generera alternativ nära noll.

Det flyttar flaskhalsen.

Den viktiga kompetensen blir att kunna fråga:

- Vilket problem löser alternativet?
- Vilka antaganden bygger det på?
- Vilka kvalitetsattribut förbättras eller försämras?
- Vilka nya beroenden introduceras?
- Hur passar det med systemets befintliga gränser?
- Är komplexiteten motiverad av behovet?

Detta är ett område där forskningsläget fortfarande är betydligt tunnare än inom kodgenerering.

En systematisk litteraturöversikt från 2025 identifierade 18 forskningsartiklar om LLM:er i mjukvaruarkitektur. Studierna omfattade bland annat klassificering av designbeslut, mönsteridentifiering och generering av arkitektur från krav, men flera centrala områden var underutforskade, exempelvis konformitet mellan arkitektur och implementation. [K-058]

Det är därför mer rimligt att beskriva AI som **arkitekturassistent och kritikpartner** än som autonom arkitekt.

## Från lösningsidé till beslut

Anta att AI:n föreslår tre alternativ för statusnotiser:

### Alternativ A – direkt utskick i befintlig ärendetjänst

När status ändras skickar samma tjänst e-post direkt.

Fördelar:

- liten initial förändring,
- få nya komponenter,
- enkel att förstå.

Nackdelar:

- statusändringen blir kopplad till extern leverans,
- svårare retry och observability,
- framtida kanaler kan öka komplexiteten i kärntjänsten.

### Alternativ B – intern händelse + notifieringskomponent

Ärendetjänsten publicerar en intern händelse. En notifieringskomponent avgör mottagare och kanal och gör leveransförsök.

Fördelar:

- tydligare ansvar,
- leveransfel kan isoleras,
- enklare att lägga till fler kanaler.

Nackdelar:

- fler komponenter och mer drift,
- eventual consistency,
- kräver robust händelsehantering.

### Alternativ C – generell ny meddelandeplattform

Bygg en bred plattform för notifieringar som flera system kan använda.

Det kan låta strategiskt.

Det kan också vara ett klassiskt exempel på att lösa ett större problem än det som faktiskt finns.

En mogen AI-dialog skulle därför inte fråga:

> Vilket alternativ är bäst?

utan något mer i stil med:

> Jämför alternativen mot våra faktiska kvalitetskrav, befintliga komponenter, förväntad förändringstakt och driftförmåga. Markera vilka slutsatser som bygger på information i projektmaterialet och vilka som är generella antaganden.

AI:n hjälper då teamet att **göra trade-offs synliga**.

Beslutet ligger fortfarande hos människor med ansvar för konsekvenserna.

## AI är bra på att generera rational – och kan också hitta på rational

Arkitekturbeslut är mer än själva valet.

Det är ofta rationalen som gör beslutet användbart senare:

- vilket problem fanns,
- vilka alternativ övervägdes,
- vilka kriterier användes,
- varför valdes detta,
- vilka konsekvenser accepterades.

En empirisk studie från 2025 utvärderade fem LLM:er på 100 arkitekturrelaterade problem och jämförde genererad design rationale med mänskliga expertunderlag. Modellerna kunde fånga en betydande del av expertargumenten och genererade också många ytterligare argument som bedömdes som hjälpsamma. Samtidigt var precisionen låg och en mindre andel argument var potentiellt missledande. [K-059]

Det är nästan en perfekt illustration av hur AI bör användas här.

> **Bra på att bredda rationalen. Dålig grund för att okritiskt fastställa rationalen.**

Ett praktiskt arbetssätt är därför:

1. AI tar fram första lista över trade-offs.
2. Arkitekt/team markerar vilka som faktiskt är relevanta.
3. AI formulerar ett ADR-utkast utifrån validerade argument.
4. Teamet granskar att beslut, motiv och konsekvenser stämmer.
5. ADR:n kopplas till den planerade förändringen.

Det är samarbete snarare än textgenerering.

## Kontexten gör arkitekturarbetet verkligt

Om AI bara känner kraven kan den föreslå en elegant grönfältsarkitektur.

Om den också får:

- systemmodell,
- repositorystruktur,
- befintliga integrationsmönster,
- tidigare ADR:er,
- driftkrav,
- observability-standard,
- data- och säkerhetsprinciper,

kan den göra en annan typ av analys:

> Vilken är minsta förändring som uppfyller behovet och samtidigt följer befintliga arkitekturprinciper?

Det är ofta en bättre fråga än:

> Hur skulle du designa detta från början?

Repository-level arbete är i sig svårt. Tidigare research i boken visade att kodagenter kan misslyckas redan med att hitta rätt kontext i ett repository och att ingen retrievalstrategi är bäst för alla uppgiftstyper. [K-041]

Det innebär att AI:s arkitekturförståelse behöver verifieras precis som dess kod.

En agent som läser fel delar av systemet kan skapa ett mycket välformulerat designförslag för en arkitektur som systemet inte har.

## Ändringsplanen som brygga

Här inför vi en central arbetsartefakt för kapitlet: **ändringsplanen**.

Den är inte en forskningsstandard utan **bokens syntes** för att binda ihop arkitektur och implementation.

En ändringsplan beskriver:

> kravpåverkan → designbeslut → berörda komponenter → planerade kodändringar → verifiering

För vårt scenario skulle en förenklad plan kunna se ut så här:

| Beslut | Berörd del | Förändring | Verifiering |
|---|---|---|---|
| E-post i första versionen | notifieringskomponent | återanvänd befintlig e-postintegration | integrationstest |
| Aktiv prenumeration per ärende | API + databas | ny preference-resurs/tabell | API- och persistensprov |
| Bara definierade statusövergångar | ärendedomän | publicera händelse efter godkänd övergång | domän-/integrationstest |
| Aktuell behörighet ska gälla | notifieringslogik | kontroll före leverans | behörighetstest |
| Leveransfel får inte blockera status | async leverans | retry/loggning, separerad transaktion | fault-injection/integrationstest |

Tabellen är inte designen i sig.

Den gör sambanden granskningsbara.

## Mognadsfaserna i design och implementation

### Fråga

> Vilka arkitekturmönster passar notifieringar?

Bra för lärande. Svagt för beslut.

### Resonera

> Vilka trade-offs finns mellan direkt utskick och asynkron notifiering i vårt fall?

Nu används AI för analys.

### Skapa

> Skapa ett ADR-utkast och en ändringsplan.

Nu produceras konkreta artefakter.

### Samarbeta

> Jag väljer alternativ B men vill undvika en generell plattform. Uppdatera ADR:n och utmana beslutet ur drift-, säkerhets- och förvaltningsperspektiv.

Nu utvecklas lösningen iterativt.

### Ge kontext

> Här är befintliga ADR:er, repositoryt, eventspecifikationen och driftkraven. Kontrollera om vårt förslag bryter mot etablerade beslut eller återuppfinner befintlig funktionalitet.

Nu arbetar AI:n med systemets verklighet.

### Delegera

> Implementera ändringsplanens första tre kodsteg i en branch. Följ befintliga konventioner, ändra inte publika API:er utöver planen, kör tester och stanna om designen visar sig kräva ett nytt arkitekturbeslut.

Detta är inte längre kodcompletion. Det är ett avgränsat förändringsuppdrag.

### Orkestrera

I ett återkommande flöde kan ett godkänt kravpaket och ADR trigga:

1. retrieval av relevant kod och dokumentation,
2. genererad ändringsplan,
3. mänsklig kontroll av scope,
4. delegerad implementation,
5. deterministisk build/test,
6. AI-analys av diff mot krav och ADR,
7. mänsklig review.

Här blir den vertikala spårbarhetskedjan konkret:

> **behov → beslut → förändring → bevis**

## När AI börjar ändra kod förändras ansvaret

Kod är annorlunda än ett analysutkast eftersom den kan exekveras.

Det gör två typer av kontroll viktiga.

### Kontroll före ändringen

Har AI:n förstått:

- rätt mål,
- rätt komponenter,
- rätt begränsningar,
- vilka filer den får ändra,
- vilka handlingar den inte får göra?

### Kontroll efter ändringen

Har förändringen:

- byggt,
- klarat tester,
- följt lokala konventioner,
- behållit spårbarhet till beslutet,
- introducerat oväntade beroenden,
- ändrat något utanför scope?

En bred akademisk survey från 2026 sammanställde 926 studier över 112 kodrelaterade software-engineering-uppgifter. [K-061] Det visar hur omfattande forskningsfältet har blivit, men den stora mängden uppgifter är i sig ett argument för försiktighet: ”AI för kod” är inte en enda förmåga.

Att skriva en fristående funktion, förstå en stor kodbas, refaktorera tvärs över moduler och genomföra en arkitekturellt korrekt förändring är olika problem.

## Granskning är inte en automatisk motvikt

När AI kan skapa kod snabbt är det naturligt att låta AI granska den också.

Det kan vara nyttigt, men det ska inte blandas ihop med oberoende verifiering.

En peer-reviewad studie från 2026 fann systematisk överkorrigering när LLM:er bedömde om implementationer uppfyllde krav. [K-039]

En annan empirisk studie visar att LLM:er kan hjälpa till att adressera problem som identifierats av statisk analys, men även där behöver resultaten bedömas i sitt sammanhang. [K-064]

Det mogna mönstret är därför:

- deterministiska verktyg för sådant som kan avgöras deterministiskt,
- AI för bredare tolkning och förändringsarbete,
- mänsklig review där ansvar, risk och helhetsförståelse kräver det.

Vi återkommer till samma princip från kapitel 10: rätt typ av steg på rätt plats.

## Arkitekturmodeller och annan strukturerad design

Generativ AI används också allt mer för modellartefakter.

En systematisk mapping från 2026 analyserade 86 studier om LLM:er i model-driven engineering. Modellartefakter var vanliga outputobjekt, men studien pekade samtidigt på brister i reproducerbar rapportering och att traditionella mått som accuracy eller F1 inte alltid fångar kvaliteten i komplexa modeller. [K-060]

Detta är relevant för arkitekter.

En modell kan vara:

- syntaktiskt giltig,
- visuellt rimlig,
- full av korrekt namngivna element,

och ändå vara konceptuellt fel.

Därför bör AI-genererade modeller granskas mot:

- metamodell,
- källor,
- relationernas semantik,
- etablerade arkitekturbeslut,
- det verkliga systemet.

Det är samma logik som för kod, men verifieringsverktygen ser annorlunda ut.

## När ska AI få fortsätta själv?

Ett användbart stoppvillkor i delegerad implementation är:

> **Om arbetet kräver ett nytt beslut med större konsekvens än uppgiften uttryckligen delegerade, stanna.**

Exempel:

AI:n upptäcker att befintlig eventmekanism inte kan garantera det beteende som ändringsplanen förutsätter.

Den kan:

- beskriva problemet,
- ta fram alternativ,
- visa vilka filer och tester som påverkas.

Den bör inte automatiskt:

- införa en ny message broker,
- ändra transaktionsmodell,
- skapa en ny gemensam plattform,

bara för att ”få uppgiften klar”.

Det är här mognad och kontroll möts.

## Från förändring till bevis

När kapitel 12 slutar finns implementationen kanske redan som branch eller pull request.

Men den vertikala kedjan är fortfarande ofullständig:

> behov → beslut → förändring → **?**

Vi behöver bevis för att förändringen fungerar och att den är rimlig att leverera.

Det är nästa kapitels ämne.

AI:s förmåga att producera kod snabbt gör inte test och kvalitet mindre viktiga.

Den gör dem till en ännu tydligare begränsande faktor.

## Så tar du nästa steg

För ett verkligt förändringsärende kan du prova följande:

1. ge AI det godkända kravpaketet och relevanta arkitekturartefakter,
2. be om flera lösningsalternativ med explicita trade-offs,
3. validera argumenten innan AI skriver ADR:n,
4. skapa en ändringsplan som binder beslut till komponenter och verifiering,
5. låt AI arbeta med verklig repositorykontext,
6. delegera bara inom tydliga arkitektur- och kodgränser,
7. definiera stoppvillkor för nya eller större designbeslut.

## När du inte bör gå vidare

Öka inte autonomin när:

- arkitekturkontexten är ofullständig,
- AI:n inte kan lokalisera relevant kod pålitligt,
- designbeslut saknar ägare,
- lösningen rör säkerhets- eller dataflöden som teamet inte förstår,
- en ”liten kodändring” i praktiken kräver ny systemarkitektur,
- teamet saknar tester eller andra sätt att verifiera ändringen.

AI kan göra implementationen billigare.

Det gör inte fel arkitektur billig.
