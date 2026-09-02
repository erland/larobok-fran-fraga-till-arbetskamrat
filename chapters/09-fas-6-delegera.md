# Kapitel 9 – Fas 6: Delegera

Det finns ett tydligt ögonblick när AI-assisterat arbete förändrar karaktär igen.

Du slutar säga:

> Öppna filen.

> Leta efter felet.

> Föreslå en ändring.

> Skriv testet.

> Kör testet.

Och börjar i stället säga:

> Åtgärda felet. Gör minsta rimliga förändringen, kör relevanta tester och visa vad du ändrat. Stanna före commit.

Du har inte längre specificerat varje steg.

Du har specificerat **målet, gränserna och kontrollpunkten**.

Det är fas 6: **Delegera**.

## Från instruktion till mål

Delegering betyder inte att människan slutar vara ansvarig.

Det betyder att AI:n får större ansvar för **vägen från start till mål**.

Jämför två arbetssätt.

### Stegvis styrning

> Läs `OrderService.java`.

> Leta efter var leveranssätt väljs.

> Kontrollera om enumen redan innehåller `PICKUP`.

> Lägg till hanteringen.

> Skapa ett test.

> Kör testet.

Här bestämmer människan arbetsplanen.

### Målbaserad delegering

> Implementera stöd för `PICKUP` enligt storyn. Följ befintliga kodmönster, ändra inte API-kontrakt utanför storyns scope, lägg till relevanta tester och kör dem. Om befintliga krav motsäger storyn ska du stanna och visa konflikten i stället för att gissa.

Här bestämmer människan fortfarande:

- önskat resultat,
- viktiga begränsningar,
- stoppvillkor,
- kvalitetskrav.

Men AI:n får planera hur arbetet ska genomföras.

Det är mognadsskiftet.

## Delegering är redan ett observerbart användningsmönster

Detta är inte bara en framtidsvision.

Anthropic analyserade 500 000 kodrelaterade interaktioner mellan Claude.ai och den agentiska kodmiljön Claude Code under april 2025. I Claude Code klassificerades 79 procent av interaktionerna som automation, jämfört med 49 procent i det vanliga chattgränssnittet. [K-005]

Ett mer specifikt mönster, "Directive", definierades som att AI:n genomför en uppgift med minimal användarinteraktion. Det stod för 43,8 procent av Claude Code-interaktionerna och 27,5 procent av Claude.ai-interaktionerna. [K-005]

Det är leverantörens egen produktdata och ska inte generaliseras till alla utvecklare eller alla verktyg.

Men den visar något viktigt:

> När AI får verktyg och en arbetsmiljö förändras beteendet från samtal mot faktisk uppgiftsdelegering.

Samtidigt var feedback-loopar vanliga.

Delegering behöver alltså inte betyda "fire and forget".

## En mogen delegation har fyra delar

Boken använder här en fyrdelad pedagogisk modell. Det är **bokens egen syntes**.

### 1. Mål

Vad ska vara sant när arbetet är klart?

Exempel:

> API:t ska acceptera det nya leveranssättet och befintliga leveranssätt ska fortsätta fungera.

### 2. Begränsningar

Vilka gränser gäller?

Exempel:

- ändra inte databasschemat,
- använd befintligt felhanteringsmönster,
- lägg inte till nya dependencies,
- rör inte autentiseringsflödet,
- inga breaking API changes.

### 3. Handlingsutrymme

Vad får AI:n faktiskt göra?

Exempel:

- läsa hela repositoryt,
- redigera filer,
- köra tester,
- installera dependencies,
- göra nätverksanrop,
- skapa commits,
- öppna pull requests,
- skriva till produktionssystem.

Detta är inte samma sak som mål eller prompt.

Det är en **behörighetsfråga**.

### 4. Verifiering

Hur avgör vi att resultatet är acceptabelt?

Exempel:

- relevanta automatiska tester går igenom,
- diffen håller sig inom scope,
- inga nya säkerhetsvarningar,
- en människa reviewar förändringen,
- ett arkitekturbeslut verifieras mot styrande underlag.

När dessa fyra delar saknas blir delegation lätt ett experiment i hopp.

## Delegationsbudgeten

När AI får verktyg behöver vi ett sätt att tänka på hur mycket den får disponera.

Vi använder därför begreppet **delegationsbudget**. Även detta är bokens egen pedagogiska syntes.

Budgeten består av fem delar.

### Data

Vilken information får AI:n läsa?

Ett publikt open-source-repository är något annat än en incidentdatabas med personuppgifter.

### Verktyg

Vilka funktioner får AI:n använda?

Att läsa Git-status är något annat än att kunna radera branches.

### Behörigheter

Vilka rättigheter har verktygen?

Read-only, constrained write och full write är fundamentalt olika risknivåer.

NIST använder just sådana skillnader när de beskriver verktygsåtkomst i agentsystem och skiljer bland annat på read-only, constrained write och write i betrodda respektive obetrodda miljöer. [K-043]

### Tid och kostnad

Hur länge får uppgiften pågå och vilka resurser får agenten förbruka?

Agentloopar kan annars fortsätta felsöka, göra API-anrop eller starta tester långt efter att marginalnyttan försvunnit.

### Irreversibla åtgärder

Vad får AI:n göra som är svårt att ta tillbaka?

Exempel:

- merge till main,
- publicera release,
- skicka e-post externt,
- radera data,
- ändra produktionskonfiguration,
- godkänna ekonomiska transaktioner.

En mogen delegation ger inte automatiskt samma budget till alla uppgifter.

## Läsande, förändrande, exekverande och externverkande agent

Ett användbart sätt att tänka är att agentens risk inte bara beror på hur smart den är, utan på vad den får göra.

### Läsande agent

Kan söka och analysera men inte förändra systemet.

Exempel:

> Analysera repositoryt och föreslå en fix.

### Förändrande agent

Kan redigera arbetsmaterial men förändringen är fortfarande lokal eller versionshanterad.

Exempel:

> Gör ändringen i en branch men skapa ingen commit.

### Exekverande agent

Kan köra kommandon eller arbetsflöden som påverkar miljön.

Exempel:

> Kör migrationen i testmiljön och verifiera resultatet.

### Externverkande agent

Kan åstadkomma effekter utanför den lokala arbetsytan.

Exempel:

- öppna en PR,
- skicka ett meddelande,
- publicera en release,
- ändra ett ärende,
- uppdatera en extern tjänst.

Skillnaden är central.

Samma prompt kan vara låg risk med read-only-verktyg och hög risk med produktionsbehörighet.

## Excessive Agency

OWASP använder begreppet **Excessive Agency** för situationer där ett LLM-baserat system kan utföra skadliga handlingar därför att det fått för mycket funktionalitet, för stora behörigheter eller för mycket autonomi. [K-044]

Det är en användbar säkerhetsprincip även utanför ren säkerhetsdesign.

Anta att en agent ska sammanfatta inkommande supportärenden.

För uppgiften behöver den kanske:

- läsa ärenden,
- kategorisera dem,
- skriva ett utkast till svar.

Den behöver inte nödvändigtvis:

- stänga ärenden,
- radera information,
- skicka svar direkt till kund,
- ändra användarbehörigheter.

Mogen delegation handlar därför inte bara om att formulera bättre instruktioner.

Den handlar om att **inte göra farliga handlingar möjliga från början om de inte behövs**.

Det är klassiskt least privilege översatt till AI-assisterat arbete.

## Kontrollpunkter efter risk, inte efter kalender

En vanlig idé är att människan ska godkänna "varje steg".

Det kan vara säkert men också göra agenten nästan meningslös.

En annan idé är att låta agenten göra allt och granska resultatet på slutet.

Det kan vara effektivt men för sent om agenten redan gjort något irreversibelt.

Ett bättre angreppssätt är att lägga kontrollpunkter där **riskprofilen ändras**.

Exempel:

1. AI får läsa repositoryt och analysera.
2. AI får redigera lokalt.
3. AI kör tester.
4. Människa granskar diff och testresultat.
5. AI får skapa commit och PR.
6. Merge kräver separat godkännande.

Här är de första tre stegen relativt reversibla.

Kontrollpunkten placeras före det arbete som påverkar det gemensamma repositoryt.

I ett annat system kan gränsen ligga tidigare.

Det viktiga är principen:

> **Mänsklig kontroll ska placeras före högkonsekvenshandlingar, inte bara med jämna mellanrum.**

## Människa-i-loopen är inte magi

En "Approve"-knapp kan ge intrycket att alla agentrisker försvinner så snart en människa står sist i kedjan.

Så enkelt är det inte.

NIST:s forskning om agent hijacking visar hur skadliga instruktioner kan ligga inbäddade i data agenten läser, exempelvis en webbsida eller ett dokument, och få agenten att driva en annan målsättning än användaren avsåg. [K-045]

Om agenten sedan själv formulerar godkännandetexten kan människan få en förenklad eller missvisande bild av vad som faktiskt kommer ske.

Det betyder inte att godkännanden är värdelösa.

Det betyder att de behöver kombineras med:

- minsta privilegium,
- tydligt strukturerade actions,
- separering mellan beslutsunderlag och exekvering,
- logging,
- verifierbara diffar,
- möjlighet att se exakt vilken handling som ska genomföras.

Människa-i-loopen är en kontroll.

Inte en ersättning för säker systemdesign.

## När agenten planerar själv

På fas 6 behöver du ofta inte veta exakt vilken plan AI:n väljer.

Men du behöver kunna bedöma om planen håller sig inom uppgiften.

Ett bra mönster är därför:

> Gör en kort plan, identifiera riskpunkter och genomför sedan uppgiften. Stanna om planen kräver en åtgärd utanför följande gränser ...

Det kan låta som ett steg tillbaka mot detaljstyrning.

Det är det inte.

Människan styr **ramen**, inte varje tangenttryckning.

Det är ungefär som att delegera en uppgift till en kollega:

> Lös detta, men om du upptäcker att databasschemat måste ändras vill jag att vi tar beslutet tillsammans först.

Den mogna delen är inte att kollegan aldrig behöver fråga.

Den mogna delen är att ni på förhand vet **vilken typ av upptäckt som ska eskaleras**.

## Längre uppgifter blir möjliga

METR har utvecklat ett mått de kallar **task-completion time horizon**. Det uppskattar hur lång en uppgift är, mätt i hur lång tid en mänsklig expert behöver, vid den punkt där en AI-agent förväntas lyckas med en given sannolikhet. Deras mätserie visar att frontieragenters förmåga att lösa längre mjukvaruuppgifter har vuxit kraftigt över tid. [K-042]

Men METR betonar en viktig sak:

"Time horizon" betyder **inte** hur länge en agent kan köras autonomt.

Det är ett mått på uppgiftens svårighet relativt mänsklig arbetstid.

Detta är en bra illustration av den precision boken behöver genomgående.

Det är rimligt att säga:

> Agenter klarar successivt mer omfattande flerledade mjukvaruuppgifter.

Det är inte rimligt att därifrån automatiskt dra slutsatsen:

> Därför bör vi låta dem arbeta obegränsat utan kontroll.

Kapabilitet och governance är två olika frågor.

## Delegering i kravarbete

Delegering är inte bara kodagenter.

En kravanalytiker kan exempelvis säga:

> Läs de 40 inkomna synpunkterna, gruppera dem efter behov, jämför med befintlig backlogg och identifiera vilka som redan täcks. Skapa inga nya krav för fall där underlaget är tvetydigt; lista dem separat för mänsklig bedömning.

AI:n behöver då:

1. läsa material,
2. klassificera,
3. jämföra,
4. bedöma matchning,
5. producera ett resultat.

Det är en flerledad uppgift.

Men människan har fortfarande definierat:

- vad som räknas som matchning,
- vad som inte får automatiseras,
- hur osäkerhet ska hanteras.

## Delegering i test

En testare kan säga:

> Analysera ändringen och befintliga tester. Identifiera vilka risker som inte täcks, skapa de två viktigaste nya testerna, kör relevanta sviter och sammanfatta om något befintligt beteende verkar ha förändrats.

Det är mer än testgenerering.

Agenten måste:

- förstå diffen,
- förstå teststrategin,
- prioritera risk,
- skapa kod,
- exekvera,
- tolka resultat.

Här blir verifieringsfrågan central.

Det är enkelt att verifiera om testsviten passerar.

Det är svårare att verifiera om agenten valde **rätt risker**.

Därför kan den mänskliga reviewn behöva fokusera mer på urvalet än på syntaxen.

## Delegering i arkitektur

En arkitekt kan delegera en analys:

> Läs de styrande kraven, nulägesmodellen och de fyra relevanta ADR:erna. Ta fram högst tre genomförbara alternativ. Bedöm dem mot samma kriterier och ange vilka fakta som fortfarande saknas. Gör ingen slutrekommendation om kriterierna ger olika vinnare beroende på viktning.

Agenten får då göra mycket av analysarbetet.

Men två typer av ansvar ligger kvar hos människan:

- vilket problem som faktiskt ska lösas,
- vilket alternativ organisationen accepterar.

Det är viktigt att inte kalla ett AI-genererat beslutsunderlag för ett beslut.

Delegering av analys är inte delegation av ansvar.

## När delegering misslyckas genom målfel

En agent kan göra exakt det du bad om och ändå skapa ett dåligt resultat.

Exempel:

> Få alla tester att gå igenom.

Agenten kan då i princip ändra testet så att det inte längre verifierar beteendet.

Målet var mätbart men fel specificerat.

Ett bättre mål är:

> Åtgärda implementationen så att det beteende som testet beskriver uppfylls. Ändra inte testets assertion utan att först visa varför kravet eller testet är fel.

Detta illustrerar ett centralt mognadsskifte:

> Ju mer du delegerar vägen, desto viktigare blir kvaliteten i målet.

Det påminner om klassisk management, outsourcing och API-design.

Ett dåligt kontrakt blir inte bättre för att utföraren är snabb.

## När delegering misslyckas genom lokal optimering

Anta att agentens mål är:

> Minimera lint-varningar i projektet.

Det kan lyckas genom stora kosmetiska förändringar som gör en viktig pull request nästan omöjlig att reviewa.

Lokalt mål: bättre.

Helhetsresultat: sämre.

Därför behöver delegation ofta kvalitetskriterier från **hela värdeflödet**:

- liten och reviewbar diff,
- inga orelaterade ändringar,
- bibehållen spårbarhet,
- rimlig testtid,
- inga nya driftberoenden.

Detta blir ännu viktigare i nästa fas, när flera delegerade steg kopplas ihop till ett arbetsflöde.

## Avancerade användare delegerar selektivt

Microsofts Work Trend Index 2026 beskriver fyra arbetsformer: asking, exploration, collaboration och delegation. Rapporten betonar att deras mest avancerade användargrupp inte definieras av att alltid delegera. De väljer arbetsform efter uppgift och uppger oftare att de stannar upp före arbetet för att avgöra vad AI respektive människa bör göra. [K-003]

Det är leverantörsproducerad survey- och telemetrydata, men den passar väl med bokens mognadsdefinition.

Fas 6 är därför inte:

> Nu ska du sluta göra saker själv.

Den är:

> Nu kan du delegera flerledade uppgifter när mål, risk och verifiering gör det rimligt.

## Ett praktiskt delegationskontrakt

Innan du ger en agent en större uppgift kan du formulera fem saker:

**Mål**  
Vad ska uppnås?

**Scope**  
Vad ingår och vad ingår inte?

**Delegationsbudget**  
Vilka data, verktyg, behörigheter och resurser får användas?

**Eskalering**  
Vilka fynd ska stoppa arbetet och lämnas tillbaka till människan?

**Verifiering**  
Hur bedöms resultatet innan det får påverka nästa miljö eller aktör?

Det behöver inte vara en lång prompt.

Ofta räcker några tydliga meningar.

Det viktiga är att du tänker igenom kontraktet.

## Så tar du nästa steg

Nästa fas börjar när delegering inte längre är en enstaka aktivitet.

I stället designar du ett återkommande flöde där flera aktiviteter kopplas ihop:

> behov → analys → implementation → test → review → leveransunderlag

eller:

> ändrat regelverk → analys av påverkan → modelländring → dokumentation → granskningsunderlag

Då har AI blivit mer än en agent du delegerar en uppgift till.

Den har blivit en del av **hur arbetet är organiserat**.

Det är fas 7: Orkestrera.

## När du inte bör gå vidare

Delegera inte en uppgift bara för att den innehåller flera steg.

Stanna på tidigare nivå när:

- målet fortfarande är oklart,
- ett centralt beslut inte är fattat,
- det saknas verifierbara kvalitetskriterier,
- agenten skulle behöva onödigt breda behörigheter,
- fel är svåra att upptäcka men lätta att sprida,
- konsekvenserna är irreversibla eller samhällskritiska,
- informationshanteringen inte är godkänd,
- du själv saknar tillräcklig kompetens för att bedöma resultatet.

Mogen delegering betyder inte största möjliga handlingsutrymme.

Den betyder **minsta handlingsutrymme som räcker för att nå målet på ett kontrollerbart sätt**.
