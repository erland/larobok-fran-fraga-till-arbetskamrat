# Kapitelplan

## Övergripande progression

Boken går från faktabas och problemformulering, via den sjufasiga mognadsresan, till hur samma resa yttrar sig genom systemutvecklingsprocessen och slutligen till ansvar, informationshantering och organisatoriska arbetssätt.

Målsatt totalomfattning är cirka 210–225 sidor exklusive register och källförteckning.

## Inledning – Du kommer sannolikt inte arbeta med AI på samma sätt om ett år

**Målomfång:** 8 sidor.

**Syfte:** etablera bokens huvudtes: två personer kan använda samma AI-tjänst men i praktiken ha helt olika arbetssätt. Introducera mognadsresan och förklara hur boken ska användas.

**Läsaren ska förstå:**

- att boken handlar om utveckling av arbetssätt, inte om en viss produkt,
- att mognad inte innebär maximal AI-användning,
- att det är normalt att vara på olika nivåer för olika uppgifter,
- hur läsaren kan använda boken för att identifiera sitt nästa steg.

**Scenario:** samma enkla förändringsbehov visas kort i en nybörjarvariant och en mogen variant.

## Del I – Ett nytt sätt att arbeta

### Kapitel 1 – När dialogen blev ett arbetsverktyg

**Målomfång:** 12 sidor.

**Syfte:** förklara vad som är nytt med moderna generativa AI-assistenter ur en kunskapsarbetares perspektiv utan att göra en lång AI-historik.

**Huvudbegrepp:** generativ AI, språkmodell, kontext, prompt, verktygsanvändning, multimodalitet, agentiska funktioner.

**Viktig avgränsning:** läsaren behöver förstå möjligheter och begränsningar, inte modellarkitektur på forskarnivå.

**Reflektionsfråga:** vilka delar av mitt arbete består främst av information, artefakter, beslut respektive handlingar?

### Kapitel 2 – Hur AI redan används i systemutveckling

**Målomfång:** 14 sidor.

**Syfte:** etablera empirisk bas för hur utvecklare och närliggande roller använder AI i dag.

**Innehåll:** användningsgrad, vanliga aktiviteter, skillnader mellan kodning och andra arbetsuppgifter, förtroende, skillnaden mellan privat experimenterande och organisatoriskt införande.

**Researchläge v1:** grundunderlag finns från Stack Overflow 2025, OpenAI Signals, Anthropic Economic Index och Microsoft Work Trend Index. Leverantörsdata ska namnges som sådan och vägas mot oberoende källor.

### Kapitel 3 – Produktivitet är mer än att göra samma sak snabbare

**Målomfång:** 14 sidor.

**Syfte:** nyansera föreställningen att AI-användning automatiskt ger produktivitetsvinster.

**Innehåll:** faktisk kontra upplevd produktivitet, kvalitet, omarbete, uppgiftsberoende effekter, erfarenhet, kodbasens betydelse och lokal optimering kontra genomloppstid.

**Bärande princip:** rätt fråga är inte om AI är produktivt generellt, utan för vilken uppgift, person, kontext och kontrollmodell. Kapitel 3 ska aktivt jämföra positiva fältexperiment med METR:s negativa 2025-resultat och "jagged frontier"-forskningen.

## Del II – Mognadsresan

### Kapitel 4 – Fas 1: Fråga

**Målomfång:** 11 sidor.

**Syfte:** beskriva den naturliga startpunkten och visa både nyttan och begränsningen i att använda AI som dialogbaserad sök- och kunskapskälla.

**Exempel:** syntax, begrepp, API-frågor, testteknik, arkitekturmönster och kravbegrepp.

**Nästa steg:** träna på följdfrågor, motargument och jämförelser.

### Kapitel 5 – Fas 2: Resonera

**Målomfång:** 11 sidor.

**Syfte:** visa hur AI blir mer värdefull när den används för att tänka igenom problem i stället för bara ge svar.

**Exempel:** designalternativ, felsökningshypoteser, kravluckor, teststrategier och arkitekturtradeoffs.

**Fallgrop:** att acceptera välformulerade resonemang utan faktakontroll.

### Kapitel 6 – Fas 3: Skapa

**Målomfång:** 11 sidor.

**Syfte:** beskriva skiftet från rådgivning till produktion av konkreta artefakter.

**Exempel:** kod, tester, krav, acceptanskriterier, dokumentation, ADR:er, tabeller och analysutkast.

**Fallgrop:** att behandla första AI-genererade versionen som färdig leverans.

### Kapitel 7 – Fas 4: Samarbeta

**Målomfång:** 11 sidor.

**Syfte:** göra det iterativa arbetssättet tydligt och avdramatisera jakten på den perfekta prompten.

**Kärnloop:** utkast → granskning → kritik → förändring → verifiering.

**Exempel:** refaktorering, kravförfining, testreview och arkitekturkritik.

### Kapitel 8 – Fas 5: Ge kontext

**Målomfång:** 12 sidor.

**Syfte:** visa varför tillgång till verkligt arbetsmaterial förändrar kvaliteten och användningssättet fundamentalt.

**Exempel:** repository, backlogg, dokumentation, modeller, styrande dokument, testresultat och historiska beslut.

**Informationsperspektiv:** här introduceras den första större fördjupningen om icke-publikt material, databehandling, kontotyper och informationsklassning.

### Kapitel 9 – Fas 6: Delegera

**Målomfång:** 12 sidor.

**Syfte:** beskriva skiftet från stegvisa instruktioner till målbaserad delegering av flerledade uppgifter.

**Exempel:** analysera–ändra–testa, kravanalys över flera artefakter, testluckor och arkitekturgranskning.

**Viktig princip:** större handlingsutrymme kräver tydligare constraints, verktygsgränser och verifiering.

### Kapitel 10 – Fas 7: Orkestrera

**Målomfång:** 12 sidor.

**Syfte:** visa hur AI blir en designad del av arbetsflödet snarare än ett separat verktyg som användaren öppnar vid behov. Orkestrering definieras som systemdesign för människor, AI och deterministisk automation – inte som ett krav på multi-agent.

**Exempel:** sammanhängande kedjor från behov till verifierad förändring, återkommande granskningar och agentiska arbetsflöden.

**Fallgrop:** automatisera ett dåligt eller otydligt arbetsflöde och därmed förstärka dess svagheter. Kapitlet skiljer också mellan körningskvalitet och systemkvalitet och introducerar arbetsflödeskontrakt, observability och evals.

## Del III – Mognadsresan genom systemutvecklingsprocessen

### Kapitel 11 – Från behov och krav till lösningsidé

**Målomfång:** 14 sidor.

**Syfte:** visa samma mognadsresa i tidiga utvecklingsfaser.

**Innehåll:** behovsanalys, krav, user stories, acceptanskriterier, domänförståelse, stakeholderperspektiv och spårbarhet.

**Genomgående scenario:** ett förändringsbehov introduceras och bearbetas från fas 1 till högre nivåer.

### Kapitel 12 – Från arkitektur och design till implementation

**Målomfång:** 15 sidor.

**Syfte:** koppla samman arkitektens och utvecklarens arbete och visa hur AI kan röra sig mellan modell, designbeslut och kod utan att ansvar försvinner.

**Innehåll:** alternativanalys, ADR, kodbasförståelse, refaktorering, implementation, teknisk skuld och konsistens mellan dokumentation och implementation.

### Kapitel 13 – Från test och kvalitet till leverans

**Målomfång:** 14 sidor.

**Syfte:** visa att mognad inte slutar när koden är skapad.

**Innehåll:** testdesign, testautomatisering, felanalys, kvalitetsrisk, CI/CD, releaseunderlag, observationer efter leverans och återkopplingsloopar.

**Viktig poäng:** AI kan både skapa fel snabbare och hjälpa oss hitta dem; kvalitetssäkringen måste därför utvecklas tillsammans med produktionsförmågan.

## Del IV – Moget AI-assisterat arbete

### Kapitel 14 – Det människan fortfarande måste vara bra på

**Målomfång:** 14 sidor.

**Syfte:** beskriva vilka mänskliga förmågor som blir viktigare när AI tar större del av produktionen.

**Innehåll:** problemformulering, domänförståelse, omdöme, skepticism, beslut, kvalitet, ansvar och förmågan att verifiera resultat.

**Bärande paradox:** ju mer som delegeras, desto viktigare blir förmågan att bedöma det delegerade arbetet.

### Kapitel 15 – När AI behöver känna till det som inte är publikt

**Målomfång:** 17 sidor.

**Syfte:** ge en praktisk beslutsmodell för användning av molnbaserad AI med intern eller känslig information utan att göra kapitlet till juridisk specialrådgivning.

**Innehåll:** informationsklassning, privatkonto kontra företags-/enterpriseavtal, träning kontra annan databehandling, lagring och retention, administrativ åtkomst, personuppgifter, företagshemligheter, källkod, säkerhetskänsligt material, anonymisering/pseudonymisering/maskning, prompten som informationsbärare, promptminimering, connectors, webbsökning och tredjepartsverktyg.

**Bärande frågor:**

1. Vilken information vill jag använda?
2. Vilken tjänst, kontotyp och avtalsmodell används?
3. Hur behandlas informationen och vilka kan få tillgång?
4. Vilka externa verktyg eller integrationer kan föra data vidare?
5. Är den återstående risken acceptabel för uppgiften?

### Kapitel 16 – Från individuell AI-användning till AI-assisterat arbetssystem

**Målomfång:** 15 sidor.

**Syfte:** knyta ihop boken och flytta perspektivet från individens mognad till hur team och organisationer kan skapa hållbara arbetssätt.

**Innehåll:** gemensamma verktyg, governance, kompetens, kvalitetsgrindar, behörighet, spårbarhet, återkommande arbetsflöden, mätning och kontinuerlig förbättring.

**Slutmodell:** den mogna användaren frågar inte bara "kan AI göra detta?" utan väljer medvetet vad människan ska förstå och besluta, vad AI ska undersöka och skapa, vad AI får genomföra och hur resultatet ska verifieras.

## Progressionskontroll

- Mognadsmodellen introduceras före detaljkapitlen och återanvänds konsekvent.
- Produktivitet och begränsningar behandlas innan hög autonomi introduceras.
- Icke-publikt material introduceras redan i fas 5 och fördjupas i kapitel 15.
- Krav, arkitektur, utveckling och test förekommer som exempel genom hela Del II, så Del III blir syntes snarare än fyra separata handböcker.
- Fas 7 presenteras inte som slutmålet för varje uppgift.
- Varje mognadskapitel ska avslutas med "Så tar du nästa steg" och "När du inte bör gå vidare".


## Evidenskrav genom hela manusproduktionen

Kapitelplanen ska läsas tillsammans med `docs/evidenspolicy.md`. Centrala sakpåståenden ska kunna spåras till `docs/kallregister.md`. Mognadsmodellen presenteras som bokens syntes även när enskilda delar av den stöds av data. Produkt- och policyuppgifter i kapitel 15–16 ska alltid färskhetskontrolleras inför slutpublicering.
