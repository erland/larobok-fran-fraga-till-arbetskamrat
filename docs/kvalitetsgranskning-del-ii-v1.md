# Kvalitetsgranskning Del II v1 – Kapitel 4–10

## Syfte

Granskningen bedömer om de sju mognadskapitlen tillsammans bildar en tydlig, icke-repetitiv och evidensmässigt korrekt progression. Fokus ligger på fasgränser, terminologi, rollbredd, säkerhetsprogression och risken att modellen misstolkas som en strikt autonomitrappa.

## Samlad bedömning

Del II håller som helhet. De sju kapitlen beskriver distinkta förändringar i arbetssättet och bygger successivt vidare på varandra:

1. Fråga – från egen informationsinhämtning till dialogbaserat svar.
2. Resonera – från svar till problemutforskning.
3. Skapa – från råd till konkret artefakt.
4. Samarbeta – från engångsleverans till återkopplingsloop.
5. Ge kontext – från generisk dialog till verkligt arbetsmaterial.
6. Delegera – från detaljstyrning till målbaserad flerledad uppgift.
7. Orkestrera – från enskild delegation till designat AI-assisterat arbetssystem.

Ingen fas behöver tas bort. Den viktigaste preciseringen efter researchpass v5 är att **fas 7 inte får likställas med multi-agent eller maximal autonomi**.

## Styrkor

### Tydliga fasgränser

Varje kapitel har ett mentalt skifte som går att förklara i en mening. Det minskar risken att modellen blir en lista av verktygsfunktioner.

### Repertoar snarare än nivåjakt

"När du inte bör gå vidare" fungerar väl och återkommer konsekvent. Detta är centralt för att mognad ska betyda situationsanpassning snarare än maximal AI-användning.

### Evidenspolicyn syns i texten

Kapitel 4–10 skiljer normalt mellan studier, enkäter/telemetri, teknisk vägledning och bokens egna synteser. Exakta procentsatser används bara när metod och källa kan förklaras.

### Utvecklingsprocessen finns genom hela delen

Exempel från krav, arkitektur, kod och test återkommer, vilket gör att Del III kan bli en syntes av modellen snarare än separata rollhandböcker.

## Identifierade risker och åtgärder

### 1. "Ge kontext" kan misstolkas som strikt kronologiskt steg

**Risk:** Moderna verktyg kan få repository- eller organisationskontext redan vid användarens första interaktion.

**Åtgärd:** Behåll fas 5 men beskriv den fortsatt som en mognadströskel: användaren börjar medvetet kurera, värdera och styra verklig arbetskontext. `docs/mognadsmodell.md` ska fortsatt markera evidensläget som medel för den kronologiska placeringen.

### 2. "Orkestrera" kan misstolkas som multi-agent

**Risk:** Termen används ofta tekniskt för agent-till-agent-samordning.

**Åtgärd:** Kapitel 10 definierar orkestrering som design av människor + AI + deterministisk automation + kontrollpunkter. Multi-agent behandlas som specialfall. Mognadsmodell och kapitelplan uppdateras med samma formulering.

### 3. Autonomi kan fortfarande uppfattas som riktningen genom hela trappan

**Risk:** Fas 5–7 innebär ofta rikare åtkomst och större handlingsutrymme.

**Åtgärd:** Kapitel 10 avslutar Del II med en explicit repertoarbild där samma mogna användare väljer fas 1, 2, 4, 5, 6 eller 7 beroende på uppgift. Detta ska återanvändas i Del IV.

### 4. Verifiering behöver skala från output till system

**Risk:** De tidigare kapitlen fokuserar huvudsakligen på att verifiera enskilda svar/artefakter.

**Åtgärd:** Kapitel 10 inför två nivåer: **körningskvalitet** och **systemkvalitet**. Detta förbereder kapitel 14 och 16.

### 5. Säkerhet får inte bli ett separat sent tillägg

**Bedömning:** Progressionen fungerar. Kapitel 4 introducerar faktaverifiering, kapitel 5 kognitiv påverkan, kapitel 8 informationsklassning/prompt injection, kapitel 9 behörighet/excessive agency och kapitel 10 kontrollpunkter/observability. Kapitel 15 kan därför fördjupa snarare än introducera området från noll.

## Repetitionskontroll

- Kapitel 4 och 5: tydlig skillnad mellan faktafråga och problemresonemang.
- Kapitel 6 och 7: tydlig skillnad mellan skapad artefakt och iterativ förbättring.
- Kapitel 8 och 9: tydlig skillnad mellan tillgång till arbetsmaterial och handlingsrätt.
- Kapitel 9 och 10: efter v5 tydlig skillnad mellan delegerad uppgift och designat system av uppgifter.

Vissa kärnprinciper återkommer avsiktligt – verifiering, minsta nödvändiga handlingsutrymme och situationsanpassning – och fungerar som bokens röda tråd snarare än onödig repetition.

## Evidensluckor att bevaka senare

1. Longitudinell forskning som följer individer genom en faktisk mognadsresa är fortfarande begränsad. Sjufasmodellen ska därför fortsatt beskrivas som pedagogisk syntes.
2. Multi-agent-forskningen i software engineering är ung och innehåller många preprints/små eller artificiella uppgifter.
3. Produkttelemetri från leverantörer ger starka signaler om användningsmönster men ska inte generaliseras till hela arbetsmarknaden.
4. Kapitlen om organisation och informationshantering behöver färskhetskontroll nära publicering eftersom produkter, avtal och agentfunktioner ändras snabbt.

## Beslut

Del II kan betraktas som strukturellt stabil efter kapitel 10. Ingen omnumrering eller ändring av sjufasmodellen rekommenderas.

Nästa manussteg bör vara Del III, kapitel 11–13, där samma modell prövas genom ett sammanhängande utvecklingsscenario från behov/krav via arkitektur/implementation till test/leverans.
