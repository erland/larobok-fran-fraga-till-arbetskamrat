# Kapitel 14 – Det människan fortfarande måste vara bra på

När AI kan skriva krav, föreslå arkitektur, ändra kod och skapa tester uppstår en lockande fråga:

> Vad återstår egentligen för människan?

Det finns två enkla svar.

Det ena är att nästan ingenting förändras eftersom en människa ändå måste granska allt.

Det andra är att människans roll snart reduceras till att formulera en beställning och trycka på godkänn.

Båda missar det viktigaste.

När AI tar en större del av produktionen förändras **var den mänskliga kompetensen behövs**.

En utvecklare som tidigare använde större delen av sin tid till att skriva implementation kan i ett AI-assisterat arbetssätt lägga mer tid på att:

- förstå vilket problem som faktiskt ska lösas,
- avgöra vilka begränsningar som gäller,
- välja mellan alternativa lösningar,
- bedöma om förändringen passar systemet,
- verifiera kod och tester,
- upptäcka sådant AI:n inte har förstått,
- ta ansvar för att förändringen är rimlig att leverera.

Motsvarande förskjutning kan ske för kravanalytikern, testaren och arkitekten.

Det betyder inte att den gamla kompetensen blivit oviktig.

Tvärtom uppstår en paradox:

> **Ju mer arbete du delegerar, desto viktigare blir förmågan att bedöma det delegerade arbetet.**

## Kritiskt tänkande flyttar

AI beskrivs ofta som ett hot mot kritiskt tänkande.

Forskningsläget är mer nyanserat.

En peer-reviewad CHI-studie från 2025 undersökte 319 kunskapsarbetare och samlade in 936 konkreta exempel på hur de använde generativ AI i arbetet. Högre tillit till AI var associerad med mindre självrapporterat kritiskt tänkande, medan högre tillit till den egna kompetensen var associerad med mer. [K-066]

Detta är viktigt, men det är också viktigt att säga vad studien **inte** visar.

Den mätte inte deltagarnas hjärnor eller gjorde ett långt experiment där deras faktiska tankeförmåga följdes över tid. Resultaten bygger till stor del på hur deltagarna själva beskrev sitt arbete.

Samtidigt fann forskarna något som passar väl med den mognadsresa vi sett genom hela boken: det kritiska tänkandet tenderade att **byta plats**.

Arbetet försköts bland annat:

- från att samla information till att verifiera information,
- från att själv lösa varje delproblem till att integrera AI:s bidrag,
- från direkt produktion till att styra och övervaka uppgiften. [K-066]

Det betyder att frågan inte bara är:

> Tänker jag mindre?

En bättre fråga är:

> **Vilket tänkande har jag slutat göra – och vilket nytt tänkande kräver arbetsformen?**

Det är en avgörande skillnad.

## Från producent till bedömare

Anta att du ska skriva ett ADR för notifieringslösningen från Del III.

Utan AI kanske du själv:

1. går igenom alternativen,
2. sammanfattar konsekvenserna,
3. formulerar beslutet,
4. skriver dokumentet.

Med AI kan en stor del av det första utkastet skapas på några minuter.

Då har textproduktion blivit billigare.

Men beslutet har inte blivit gratis.

Du måste fortfarande kunna bedöma:

- om rätt alternativ jämförts,
- om någon central constraint saknas,
- om konsekvenserna är rimliga,
- om AI:n blandat samman generella best practices med förutsättningarna i just ert system,
- om beslutet är spårbart till verkliga behov.

Detta återkommer i nästan alla roller.

När produktionen automatiseras blir **bedömningsförmågan** en större del av arbetet.

En longitudinell studie av AI-kodassistenter har också beskrivit en förskjutning från direkt skapande mot mer verifierande och övervakande utvecklingsarbete, som forskarna kallar *supervisory engineering work*. [K-040]

Studien är en mixed-methods preprint och ska därför inte läsas som slutgiltigt bevis för hur utvecklaryrket kommer att utvecklas. Men riktningen är värd att ta på allvar eftersom den stämmer med flera andra observationer i boken.

## Bedömning kräver egen kompetens

Det finns en obekväm egenskap hos verifiering:

> Du behöver kunna tillräckligt mycket själv för att veta vad som är fel.

Om du inte förstår SQL blir det svårt att upptäcka en subtilt felaktig query.

Om du inte förstår transaktionsgränser blir det svårt att bedöma en föreslagen arkitektur för konsistens.

Om du inte förstår testdesign blir hundra gröna AI-genererade tester lätt ett falskt trygghetsbevis.

Om du inte förstår verksamhetsdomänen blir ett elegant kravdokument inte nödvändigtvis ett korrekt kravdokument.

AI kan hjälpa även i verifieringen.

Du kan exempelvis be en annan modell eller en separat granskning att:

- hitta motexempel,
- jämföra mot källor,
- analysera diffen mot krav,
- utmana antaganden,
- leta efter säkerhetsrisker.

Men som vi såg i kapitel 7 är AI som granskar AI inte samma sak som oberoende verifiering.

Någon behöver fortfarande kunna avgöra om granskningsmetoden själv är rimlig.

## Problemformulering blir mer värdefull

Tidigt i mognadsresan är prompten ofta frågan:

> Hur gör jag X?

Senare blir den centrala mänskliga uppgiften ofta att avgöra om **X över huvud taget är rätt problem**.

Tänk på statusnotiserna igen.

Ett omoget uppdrag skulle kunna vara:

> Implementera e-postnotiser när status ändras.

Ett moget arbete börjar tidigare:

- Vilket användarproblem försöker vi lösa?
- För vilka statusförändringar finns faktiskt ett behov?
- Vilka användare får se vilken information?
- Vad händer om notifieringen misslyckas?
- Ska notisen innehålla data eller bara hänvisa tillbaka till systemet?
- Är e-post rätt kanal?

AI kan hjälpa till att ställa dessa frågor.

Men någon måste avgöra vilka frågor som är relevanta och vilka svar som är acceptabla för organisationen.

Detta gör **problemformulering** till en central förmåga i moget AI-assisterat arbete.

Den som bara är duktig på att instruera AI att genomföra en redan formulerad lösning kan bli mycket produktiv på att lösa fel problem.

## Domänkunskap försvinner inte

Generativa modeller är starka på generell kunskap och mönster.

Arbetslivet är fullt av lokal kunskap som inte finns i modellen:

- varför en viss integration ser märklig ut,
- vilket undantag som infördes efter en incident för fem år sedan,
- vilka verksamhetsregler som aldrig blivit ordentligt dokumenterade,
- vad en viss term betyder i just organisationen,
- varför en tekniskt elegant lösning tidigare valdes bort,
- vilka kompromisser organisationen faktiskt accepterar.

Fas 5 handlade därför inte bara om att ge AI fler dokument.

Människor behöver kunna se **vad dokumenten inte säger**.

Detta är en viktig form av domänkompetens.

En AI kan ha tillgång till hela repositoryt och ändå sakna förståelse för att en viss kundgrupp använder systemet på ett sätt ingen dokumentation beskriver.

En arkitekt kan därför bli mindre viktig som producent av diagram men mer viktig som bärare och prövare av organisatorisk kontext.

En erfaren utvecklare kan skriva mindre kod men bli viktigare för att känna igen när en till synes lokal ändring bryter ett implicit systemantagande.

## Omdöme är mer än faktakontroll

Verifiering låter ibland som att det räcker att kontrollera om något är sant eller falskt.

Många professionella beslut fungerar inte så.

Arkitekturen kan ha två tekniskt korrekta alternativ där det ena passar organisationens kompetens bättre.

Ett krav kan vara logiskt korrekt men för dyrt att realisera.

En refaktorering kan förbättra kodkvaliteten men vara olämplig veckan före en kritisk release.

Ett test kan vara relevant men inte värt exekveringstiden i varje commit.

Detta kräver **omdöme**.

Omdöme innebär att väga:

- kvalitet,
- risk,
- kostnad,
- tid,
- reversibilitet,
- verksamhetsnytta,
- organisatorisk förmåga.

AI kan hjälpa till att synliggöra trade-offs.

Men värderingen av dem behöver fortfarande förankras i människors och organisationens mål.

## Att veta när man ska misstro ett bra svar

En av språkmodellens mest förrädiska egenskaper är att kvaliteten på formuleringen och kvaliteten på innehållet kan skilja sig åt.

Ett svar kan vara:

- tydligt,
- välstrukturerat,
- övertygande,
- komplett till formen,

och ändå bygga på fel premiss.

Det gör skepticism till en professionell färdighet.

Men skepticism betyder inte att misstro allt AI gör.

Det vore lika ineffektivt som blind tillit.

Mogen skepticism handlar om att kunna fråga:

- Vad i detta svar är mest osäkert?
- Vilket antagande skulle kunna göra slutsatsen fel?
- Vilken källa eller observation kan falsifiera detta?
- Finns ett motexempel?
- Vilken del kan verifieras deterministiskt?
- Hur stor blir konsekvensen om AI:n har fel?

Det är samma situationsanpassning som går genom hela bokens mognadsmodell.

## Kompetens kan offloadas – men den kan också försvagas

Människor har alltid flyttat kognitivt arbete till verktyg.

Vi använder:

- miniräknare,
- sökmotorer,
- dokumentation,
- IDE:er,
- statiska analysverktyg,
- automatiserade tester.

Generativ AI gör denna *cognitive offloading* mer omfattande eftersom verktyget inte bara lagrar eller räknar utan kan producera hela resonemang, texter, lösningar och beslutunderlag.

Det finns därför en rimlig oro för **deskilling**.

Men här måste evidensspråket vara noggrant.

En forskningsartikel från 2024 diskuterar, med utgångspunkt i tidigare forskning om automation, risken att AI-assistans kan accelerera skill decay hos experter eller hämma färdighetsutveckling hos nybörjare. [K-068]

Det är en teoretisk perspektivartikel.

Den visar alltså inte att ”AI orsakar X procent kompetensförlust”. Den formulerar och grundar en risk som behöver undersökas empiriskt.

En senare review i *Trends in Cognitive Sciences* från 2026 sammanfattar evidens som tyder på att kognitiv offloading till AI **kan** hindra kompetensutveckling och bidra till skill decay, men betonar samtidigt att effekten beror på hur verktyget används. [K-069]

Det är en mycket mer användbar slutsats för den här boken än ett generellt förbud mot offloading.

## När snabbare lärande blir ytligare lärande

Det finns också experimentell forskning som visar att arbetsformen påverkar själva lärandet.

En studie publicerad i *PNAS Nexus* 2025 genomförde sju online- och laboratorieexperiment med totalt 10 462 deltagare. Deltagarna fick lära sig om ämnen antingen via LLM-sammanfattningar eller genom traditionell webbsökning. [K-067]

De som använde LLM-sammanfattningar utvecklade i genomsnitt ytligare kunskap och producerade senare råd som var mindre originella och bedömdes som mindre användbara av andra deltagare. [K-067]

Detta ska inte övertolkas.

Studien handlade inte om erfarna utvecklare som använder en kodagent under flera månader.

Men den visar något viktigt:

> **Att få tillgång till ett korrekt och kompakt svar är inte samma sak som att lära sig det arbete som annars krävdes för att komma fram till svaret.**

Det spelar stor roll för hur vi använder AI när syftet är kompetensutveckling.

## Två helt olika mål: leverera och lära

Anta att en junior utvecklare behöver förstå en komplex transaktionsbugg.

Om målet är:

> Lös incidenten så snabbt som möjligt.

kan det vara rimligt att låta en avancerad agent analysera repositoryt, loggar och tester och föreslå fixen.

Om målet är:

> Utvecklaren ska lära sig att själv diagnostisera den här typen av problem.

är samma arbetsform kanske dålig.

Då kan AI användas annorlunda:

> Ge mig inte lösningen. Hjälp mig stegvis att formulera hypoteser. Fråga vad jag vill kontrollera härnäst och utmana mina slutsatser.

AI blir då mer lärare eller träningspartner än utförare.

Detta leder till en central princip:

> **Optimera inte alltid samma AI-interaktion för både leveranshastighet och lärande.**

De två målen kan kräva olika grad av offloading.

## Bokens syntes: kompetensbudgeten

Vi kan nu lägga till ytterligare en modell till bokens verktygslåda.

Det här är **bokens egen syntes**, inte en etablerad forskningsmodell.

### Kompetensbudgeten

För varje viktig förmåga kan individen eller teamet ställa fyra frågor:

1. **Vad måste vi fortfarande kunna göra själva?**
2. **Vad måste vi kunna tillräckligt väl för att verifiera AI?**
3. **Vad kan vi tryggt låta AI göra huvuddelen av?**
4. **Hur märker vi om vår egen kompetens håller på att försvagas?**

Ta testning som exempel.

Ett team kan låta AI generera en stor del av testkoden.

Men teamet kanske fortfarande behöver kunna:

- identifiera kvalitetsrisker,
- välja rätt testnivå,
- bedöma assertions,
- tolka mutation testing,
- avgöra om testsviten ger relevant förtroende.

Det är en medveten kompetensbudget.

Målet är inte att bevara varje manuellt moment av nostalgiska skäl.

Målet är att inte råka automatisera bort **förmågan att kontrollera det automatiserade arbetet**.

## Kompetensbudgeten förändras med rollen

För en junior utvecklare kan det vara viktigt att fortfarande skriva vissa saker manuellt för att bygga mental modell och handlag.

För en mycket erfaren utvecklare kan det vara rationellt att offloada samma syntaxarbete men aktivt behålla förmågan att:

- designa lösningen,
- upptäcka subtila fel,
- förstå prestandakonsekvenser,
- bedöma arkitekturpassning.

För en enterprise-arkitekt kan det vara helt rimligt att AI producerar första versionen av en tabell eller modellbeskrivning.

Men arkitekten behöver fortfarande kunna:

- tolka styrningen,
- förstå verksamhetens målkonflikter,
- avgöra vilka relationer som faktiskt är meningsfulla,
- skilja verklig arkitektureffekt från en snygg visualisering.

Det finns alltså ingen universell lista över sådant människor alltid måste göra manuellt.

Det finns däremot en universell fråga:

> **Vilken mänsklig förmåga krävs för att vi ska kunna bära ansvar för resultatet?**

## Ansvar kan inte delegeras lika enkelt som arbete

En agent kan få mandat att:

- ändra filer,
- köra tester,
- skapa en pull request,
- skriva ett beslutsunderlag.

Men organisationen måste fortfarande veta vem som ansvarar för:

- kravet,
- arkitekturbeslutet,
- säkerhetsbedömningen,
- releasen,
- konsekvensen för användaren.

Det är skillnad mellan **utförandeansvar** och **ansvar för beslutets konsekvens**.

AI kan vara en aktör i arbetsflödet utan att vara organisationens ansvarsbärare.

Detta är främst en styrningsprincip i boken, inte ett forskningsresultat om en viss AI-produkt.

I praktiken betyder det att ett moget arbetsflöde behöver göra ansvar synligt:

| AI kan göra | Mänsklig/organisatorisk uppgift |
|---|---|
| analysera alternativ | fastställa vad som värderas högst |
| skapa förslag | fatta eller äga beslutet |
| utföra förändring | bestämma vilket mandat som ges |
| köra verifiering | avgöra om evidensen räcker |
| sammanfatta risk | acceptera, reducera eller eskalera risk |

Ju högre upp i mognadsresan vi kommer, desto viktigare blir denna separation.

## Människan behövs också för att förändra systemet

Ett sex månader långt randomiserat fältexperiment med omkring 6 000 kunskapsarbetare visade att generativ AI främst förändrade sådant individer kunde ändra på egen hand. Användare lade mindre tid på e-post och slutförde dokument snabbare, medan mötestid inte förändrades signifikant. [K-070]

Det är ett användbart resultat långt utanför kontorsarbete.

Många problem i systemutveckling är inte individuella produktionsproblem.

De kan bero på:

- otydligt mandat,
- beroenden mellan team,
- långsam beslutsprocess,
- miljöbrist,
- tung releaseprocess,
- svåråtkomlig data,
- motstridiga mål.

En AI-assistent kan göra en individ snabbare utan att dessa hinder försvinner.

Den mänskliga förmågan att **förändra arbetssystemet** blir därför central när AI-mognaden ökar.

Det är också bron till kapitel 16.

## Fem mänskliga kärnförmågor

Om vi sammanfattar kapitlet blir fem förmågor särskilt viktiga.

### 1. Problemformulering

Att förstå vilket problem som är värt att lösa och vilka begränsningar som faktiskt gäller.

### 2. Domänförståelse

Att känna igen kontext, undantag, historik och implicita regler som inte finns i modellens generella kunskap.

### 3. Omdöme

Att väga alternativ, risk, kostnad och konsekvens när det inte finns ett objektivt facit.

### 4. Verifieringsförmåga

Att kunna avgöra om AI:s resultat är korrekt, relevant och tillräckligt bra för uppgiften.

### 5. Ansvar och systemförmåga

Att bestämma mandat, bära beslut och förändra arbetsflödet när problemet inte kan lösas genom bättre prompting.

Ingen av dessa förmågor innebär att människan måste göra allt själv.

Tvärtom blir de viktiga **just för att hon inte längre behöver göra allt själv**.

## Vad bör du fortsätta öva på?

Ett praktiskt sätt att använda kapitlet är att välja tre arbetsuppgifter där AI redan gör mycket av jobbet.

För varje uppgift, skriv ned:

- vad AI gör,
- vad du själv fortfarande behöver förstå,
- hur du verifierar resultatet,
- vilken kompetens du skulle förlora om du aldrig gjorde eller analyserade uppgiften själv,
- om den kompetensen faktiskt behöver bevaras.

Den sista punkten är viktig.

All deskilling är inte dålig.

De flesta utvecklare behöver inte kunna handoptimera maskinkod bara för att tidigare generationer gjorde det.

När verktyg förändras förändras också vad det är rationellt att kunna.

Målet är därför inte **kompetensbevarande till varje pris**.

Målet är **medveten kompetensförskjutning**.

## Så tar du nästa steg

Om du redan använder AI för stora delar av ditt arbete, prova följande under en vecka:

1. Identifiera en uppgift där du ofta accepterar AI:s första rimliga svar.
2. Formulera i förväg vilka kriterier du själv använder för att bedöma kvaliteten.
3. Be AI:n generera ett resultat.
4. Granska det utan att först be AI:n själv förklara varför det är bra.
5. Notera vilka delar du hade svårt att bedöma.
6. Bestäm om det är en kompetens du behöver stärka, en kontroll du behöver automatisera eller ett område där du bör minska AI:ns mandat.

Det är ett praktiskt sätt att kartlägga din egen kompetensbudget.

## När du inte bör gå vidare

Gå inte mot mer delegering eller orkestrering enbart därför att verktyget kan göra mer.

Stanna eller minska AI:ns handlingsutrymme när:

- du inte kan formulera vad ett bra resultat innebär,
- ingen i teamet kan verifiera den centrala delen av arbetet,
- uppgiften används för att bygga en kompetens som AI:n annars skulle ersätta,
- konsekvensen av ett fel är hög och kontrollen är svag,
- ansvarsfördelningen blir oklar.

Mognad innebär ibland att låta AI göra mer.

I andra situationer innebär mognad att medvetet låta människan göra mer.

Det avgörande är att skillnaden är ett **val**, inte en bieffekt av verktygets bekvämlighet.

## Nästa fråga: vilken information får arbetskamraten se?

Hittills har kapitlet handlat om kompetens och ansvar.

Men när AI blir en verklig arbetskamrat uppstår nästa fråga nästan automatiskt:

> Om AI behöver repositoryt, kravdokumenten, incidenthistoriken, kundinformationen och arkitekturmodellerna för att göra ett bra jobb – får vi verkligen ge den allt detta?

Det är inte en fråga som kan besvaras med ett generellt ”ja” eller ”nej”.

Det beror på informationen, tjänsten, avtalet, inställningarna, integrationerna och den risk organisationen accepterar.

Det är ämnet för nästa kapitel.
