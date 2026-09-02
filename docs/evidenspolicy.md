# Evidens- och källpolicy

## Syfte

Boken ska göra det tydligt för läsaren **vad som är mätt eller studerat, vad som är en tjänsteleverantörs dokumenterade egenskap och vad som är bokens egen syntes**. Ett välformulerat resonemang ska aldrig presenteras som forskning bara för att det verkar rimligt.

## Fem evidenstyper

### 1. Forskningsresultat

Används för resultat från peer-reviewade studier, randomiserade experiment, systematiska litteraturöversikter eller annan tydligt beskriven vetenskaplig metod.

I manus ska texten ange vilken sorts studie det handlar om när det är relevant, exempelvis:

> I ett randomiserat fältexperiment med 4 867 utvecklare ...

Ett enskilt experiment ska inte beskrivas som ett universellt faktum. Population, uppgift, verktyg och tidsperiod ska framgå när de påverkar tolkningen.

### 2. Mätdata eller enkätdata

Används för observerad produkttelemetri, större användningsmätningar och enkäter. Här ska läsaren kunna se **vem som mätt, vilken population som ingår och om källan är en AI-leverantör**.

Exempel:

> OpenAI rapporterar, baserat på aggregerad användningsdata från individuella ChatGPT-konton, att ...

Detta är empirisk data men ska inte ges samma oberoendestatus som en extern studie.

### 3. Leverantörsuppgift

Används för tjänstespecifika egenskaper: modellträning, retention, datalagring, avtal, behörighet, data residency, connectors och liknande.

Formulera alltid på ett sätt som binder påståendet till leverantören och aktuell tjänst/plan:

> Microsoft anger för Microsoft 365 Copilot att ...

Sådana uppgifter är tidskänsliga och ska verifieras mot aktuell officiell dokumentation inför publicering.

### 4. Bokens syntes

Används för mognadsmodellen, pedagogiska kategoriseringar, slutsatser som väger samman flera källor och praktiska rekommendationer som inte direkt har testats som en helhet.

Boken ska uttryckligen säga när något är en syntes, exempelvis:

> I den här boken delar vi pedagogiskt upp denna utveckling i sju steg.

Mognadsmodellens sju steg får aldrig beskrivas som en vetenskapligt etablerad sjufasmodell.

### 5. Illustrativt exempel

Fiktiva scenarier, exempelprompter och arbetsflöden används för att förklara en princip. De är inte evidens för att arbetssättet är vanligt eller bättre.

## Källans oberoende är en separat dimension

Evidenstyp och avsändare ska hållas isär. En leverantör kan publicera en väl dokumenterad mätning eller vetenskaplig studie, men läsaren ska ändå få veta att avsändaren har ett kommersiellt intresse.

Källregistret använder därför både **Typ** och **Oberoende/leverantör**.

## Regler för manus

1. Centrala kvantitativa påståenden ska ha källa.
2. Procenttal ska normalt ange population och år i samma stycke eller närliggande text.
3. Kausala formuleringar som "AI gör utvecklare snabbare" får bara användas när studiedesignen stödjer kausalitet och ska avgränsas till den studerade situationen.
4. Självrapporterad produktivitet ska kallas självrapporterad; den får inte blandas ihop med uppmätt produktivitet.
5. Leverantörstelemetri ska namnge leverantören.
6. Produkt- och säkerhetsegenskaper ska knytas till tjänst och abonnemangs-/avtalsmodell.
7. När forskning pekar åt olika håll ska boken visa konflikten i stället för att välja det mest positiva resultatet.
8. Osäkerhet, urvalsproblem och begränsad generaliserbarhet ska nämnas när de påverkar slutsatsen.
9. Bokens egna modeller och råd ska inte ges en forskningsetikett om de endast är synteser.
10. Inför slutpublicering görs ett färskhets-pass på alla produkt-, säkerhets- och policyuppgifter.

## Visuell presentation i boken

Boken bör använda diskreta faktarutor eller inledande ord i stycken snarare än märka varje mening. Föreslagna etiketter:

- **Forskningsresultat**
- **Mätdata**
- **Leverantörsuppgift**
- **Bokens syntes**

De används när källtypen annars riskerar att missförstås. Vanliga källhänvisningar används fortfarande i löptext/slutnoter.

## Kvalitetsfråga vid varje kapitelgranskning

För varje centralt påstående ska redaktören kunna svara på:

> Vet läsaren om detta är mätt, studerat, leverantörsdokumenterat eller vår egen slutsats?
