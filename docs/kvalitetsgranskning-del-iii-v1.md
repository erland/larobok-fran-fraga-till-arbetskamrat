# Kvalitetsgranskning Del III v1 – kapitel 11–13

## Syfte

Granskningen kontrollerar om sjufasmodellen fungerar genom hela utvecklingsprocessen utan att Del III blir en upprepning av kapitel 4–10, och om scenariot ger tillräcklig kontinuitet mellan krav, arkitektur, kod, test och leverans.

## Resultat

### 1. Sjufasmodellen fungerar tvärs över processen

Ingen fas behöver ändras efter processgenomgången. Det blir tydligt att samma person eller team kan befinna sig på olika faser för olika aktiviteter, vilket stärker beslutet att modellen ska beskrivas som repertoar och situationsanpassning snarare än en strikt trappa.

### 2. Del III behöver en egen sammanhållande modell

Att bara återanvända de sju faserna riskerade repetition. Den nya vertikala spårbarhetskedjan **behov → beslut → förändring → bevis** löser detta genom att visa vad som behöver hållas samman genom processen.

Kedjan är bokens syntes och ska märkas som sådan.

### 3. Scenariot fungerar bättre än det tidigare arbetsnamnet

**Statusnotiser för ärenden** ger naturliga frågor om krav, behörighet, arkitektur, integration, felhantering, test och observability utan att kräva en stor domänförklaring. Scenariot bör behållas genom Del III och kan återanvändas selektivt i kapitel 14–16.

### 4. Kravkapitlet behöver hålla isär språk och verklighet

Kapitel 11 lyckas undvika att beskriva kravarbete som dokumentgenerering. Den viktiga distinktionen är att AI kan förbättra textkvalitet men inte själv verifiera att ett stakeholderbehov är korrekt representerat.

### 5. Arkitekturkapitlet behöver fortsatt evidensförsiktighet

Forskningen inom mjukvaruarkitektur är mindre omfattande än kodforskningen. Kapitel 12 använder därför AI främst för alternativ, kritik, rationale, spårbarhet och ändringsplanering. Det bör behållas även vid senare språkgranskning.

### 6. Testkapitlet fullbordar produktivitetsargumentet

Kapitel 13 kopplar tillbaka till kapitel 3: lokal snabbhet i implementation är inte samma sak som snabbare värdeflöde. AI-genererad testmängd eller coverage behandlas inte som synonym till kvalitet.

### 7. Evidenspolicyn följs

Centrala forskningspåståenden introduceras med källtyp eller metod, exempelvis systematisk litteraturöversikt, peer-reviewad studie eller leverantörsproducerad branschforskning. Bokens egna modeller märks explicit som synteser.

## Justeringar efter granskning

- Behåll kapitel 11–13 som tre kapitel; de har olika uppgifter och bör inte slås ihop.
- Behåll sjufasmodellen oförändrad.
- Lägg den vertikala spårbarhetskedjan i pedagogisk canon.
- Använd scenariot sparsamt i Del IV så att det fungerar som återkoppling, inte repetition.
- I slutlig helhetsgranskning: kontrollera att uttrycken "rätt typ av steg på rätt plats", "produktivitetsflaskhals" och "verifiering" inte upprepas för tätt mellan kapitel 10, 12 och 13.

## Slutsats

Del III bekräftar bokens huvudtes: mognad i AI-assisterat systemutvecklingsarbete handlar inte främst om bättre promptformulering eller högre autonomi. Den syns i hur väl användaren eller teamet kan hålla samman kontext, beslut, handlingsutrymme och verifiering genom en verklig förändring.
