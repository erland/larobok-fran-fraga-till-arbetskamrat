# Pedagogisk canon

## Bokens röda tråd

Boken handlar om mognadsresan, inte om promptteknik och inte om en specifik AI-produkt.

## Grundfrågan i varje kapitel

Läsaren ska kunna svara på:

> Vad gör en person annorlunda på den här nivån jämfört med föregående nivå, och vilket konkret nästa steg kan jag själv prova?

## Standardstruktur för mognadskapitlen 4–10

1. Vad som förändras.
2. Hur arbetssättet ser ut i praktiken.
3. Exempel från minst tre delar av utvecklingsprocessen.
4. Vad AI är bra respektive dålig på på denna nivå.
5. Vanliga fallgropar.
6. Informations- och kontrollperspektiv där det är relevant.
7. Så tar du nästa steg.
8. När du inte bör gå vidare.
9. Kort reflektion eller övning.

## Genomgående scenario

Arbetsnamn: **Statusnotiser för ärenden**.

Ett befintligt verksamhetssystem ska låta användare prenumerera på statusnotiser för ett ärende och välja kanal. Förändringen påverkar:

- behov, verksamhetsregler, krav och acceptanskriterier,
- behörighet och användarpreferenser,
- arkitektur- och integrationsbeslut,
- API, datamodell och implementation i en befintlig kodbas,
- felhantering och observability,
- en kombination av domän-, enhets-, integrations- och acceptanstester,
- releaseunderlag och uppföljning efter leverans.

Scenariot ska hållas tekniskt neutralt och tillräckligt litet för att inte bli bokens ämne. Det används framför allt i Del III för att visa hur samma förändring följs genom hela utvecklingsprocessen och hur mognad påverkar sambanden mellan artefakterna.

## Rollvariation

Samma mognadsprincip visas med olika arbetsmaterial:

- kravanalytiker: behov, regler, backlogg och acceptanskriterier,
- utvecklare: repository, kod, tester och CI,
- testare: krav, risker, testfall, resultat och defekter,
- arkitekt: mål, constraints, modeller, beslut och systemlandskap,
- plattforms-/DevOps-roll: pipeline, konfiguration, observability och driftsättning.

## Återkommande motvikt

Boken ska återkommande påminna om att:

- välskrivna svar kan vara fel,
- högre autonomi inte automatiskt är högre kvalitet,
- AI kan öka både produktionshastighet och mängden fel/omarbete,
- mogen användning innefattar att välja bort AI eller välja en lägre nivå,
- mänskligt ansvar inte delegeras bara för att en aktivitet gör det.


## Evidens i pedagogiken

När ett kapitel introducerar ett viktigt faktapåstående ska texten göra källtypen begriplig utan att bli akademiskt tung. Skriv exempelvis "i ett randomiserat experiment", "i Stack Overflows enkät", "OpenAI:s aggregerade användningsdata visar" eller "Microsoft anger för Microsoft 365 Copilot".

Bokens egna slutsatser ska markeras med formuleringar som "i den här boken använder vi", "vi betraktar" eller "vår syntes är".

Särskilt i kapitel 2–3 och 14–16 ska motstridig evidens presenteras öppet. Boken får inte välja en positiv leverantörsstudie när oberoende forskning visar en mer blandad bild.

## Tillägg efter researchpass v5 – orkestrering

- **Orkestrering är inte synonymt med multi-agent.** Boken använder begreppet för design av ett AI-assisterat arbetssystem där människor, AI, deterministisk automation, verktyg och kontrollpunkter kombineras medvetet.
- Multi-agent är ett specialfall och ska bara rekommenderas när specialisering, parallellism eller arbetsdelning ger ett verifierbart värde som motiverar koordinationskostnaden.
- Fas 7 inför bokens **arbetsflödeskontrakt**: trigger/mål, state/kontext, roller/steg, handoffs/kontrollpunkter, observability samt evals/förbättringsloop.
- Från fas 7 ska kvalitet beskrivas på två nivåer: **körningskvalitet** (blev just detta resultat bra?) och **systemkvalitet** (är arbetsflödet fortfarande bra över tid?).
- Evals ska beskrivas som ett återkommande sätt att upptäcka kvalitetsförändring, inte som bevis för generell säkerhet eller korrekthet.

## Tillägg efter researchpass v6 – utvecklingsprocessen

- Del III använder **behov → beslut → förändring → bevis** som en vertikal spårbarhetskedja. Detta är bokens syntes, inte en etablerad forskningsmodell.
- Mognadsfaserna ska användas som analyslinser och får inte återberättas mekaniskt i varje processkapitel.
- Kravkapitlet skiljer tydligt mellan välformulerad kravtext och validerat verksamhetsbehov.
- Arkitekturkapitlet ska vara mer återhållsamt med autonomipåståenden än kodkapitlen eftersom det empiriska forskningsunderlaget är tunnare.
- Testkapitlet ska skilja mängd/coverage från felupptäckande förmåga och systemförtroende.
- Del III ska visa att spårbarheten mellan artefakter är minst lika viktig som kvaliteten i varje enskild AI-genererad artefakt.


## Sex delar i ett AI-assisterat arbetssystem

Kapitel 16 avslutar bokens progression med en organisatorisk syntes:

1. riktning,
2. miljö,
3. arbetsdesign,
4. kontroll,
5. kvalitet,
6. lärande.

Modellen är **bokens egen syntes**. Den ska inte beskrivas som ett etablerat forskningsramverk. Den används för att visa hur individuell AI-mognad behöver absorberas av ett gemensamt arbetssystem.
