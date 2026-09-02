# Kapitel 4 – Fas 1: Fråga

För många börjar AI-användningen på samma sätt: med en fråga.

Vad betyder ett begrepp? Hur fungerar ett ramverk? Vad gör den här raden kod? Vilken skillnad är det mellan två arkitekturmönster? Hur skriver man ett reguljärt uttryck som fångar ett visst format?

Det är en naturlig startpunkt. Dialoggränssnittet gör kunskap tillgänglig utan att användaren först behöver formulera rätt sökord, välja rätt dokumentation eller redan känna till begreppen som används i ämnet.

Men det finns en viktig skillnad mellan att **fråga en AI-modell** och att **slå upp ett faktum**.

Det är den skillnaden som gör den första fasen både kraftfull och förrädisk.

## Den första mentala modellen

I fas 1 används AI ungefär som en interaktiv kunskapskälla.

Typiska frågor är:

- Vad är dependency injection?
- Hur fungerar OAuth 2.0?
- Vad är skillnaden mellan en capability och en process?
- Hur fungerar property-based testing?
- Varför får jag det här kompileringsfelet?
- Hur borde en REST-resurs struktureras i Quarkus?
- Vad är för- och nackdelarna med event sourcing?

Det nya jämfört med traditionell informationssökning är inte bara att svaret kommer snabbt. Det är att användaren kan fortsätta dialogen.

Om första svaret är för avancerat kan man be om en enklare förklaring. Om ett ord är oklart kan man fråga om just det. Om man vill ha ett exempel i Java i stället för TypeScript går det att byta riktning utan att börja om.

Det gör fas 1 mycket användbar för **orientering och lärande**.

Men den första mentala modellen blir ofta för enkel:

> Jag ställer en fråga och AI:n hämtar svaret.

Så fungerar inte en språkmodell i grunden.

## Ett språkverktyg som kan mycket – men inte är en databas

Stora språkmodeller tränas på stora mängder text och lär sig statistiska mönster i språk och innehåll. De kan därför ofta producera mycket träffsäkra förklaringar, sammanfattningar och exempel.

Men de genererar svar, de hämtar inte nödvändigtvis ett verifierat faktum från en auktoritativ databas.

Det är därför ett svar kan vara:

- välformulerat,
- pedagogiskt,
- tekniskt plausibelt,
- och ändå fel.

**Forskningsresultat – modellfaktualitet:** En Nature-studie från 2024 undersökte hur större och mer instruktionsföljande språkmodeller beter sig över uppgifter med olika svårighetsgrad. Forskarna fann att mer kapabla modeller ofta svarar oftare i stället för att avstå, men att det samtidigt kan uppstå en zon där svaren låter rimliga trots att de är fel och där mänskliga granskare har svårt att upptäcka misstagen. [K-028]

Det är en viktig egenskap att förstå redan i fas 1.

Flyt är inte samma sak som sanning.

## Hallucination är ett vardagsord för ett verkligt problem

Begreppet *hallucination* används när en språkmodell genererar något som verkar rimligt men inte stämmer med verkligheten eller det givna underlaget.

Det kan vara:

- ett felaktigt API-anrop,
- en flagga som inte finns,
- en påhittad lagregel,
- en felaktig versionsuppgift,
- en påhittad forskningsartikel,
- en felaktig koppling mellan två verkliga fakta.

**Forskningsresultat – mekanismer bakom hallucinationer:** OpenAI och forskare vid Georgia Tech analyserade 2025 varför språkmodeller fortsätter att hallucinerar. Deras slutsats är bland annat att tränings- och utvärderingsmetoder ofta belönar en modell för att gissa när den är osäker, eftersom ett försök ibland ger poäng medan ett avstående aldrig gör det i traditionella precisionstest. [K-029]

Källan kommer från en modellleverantör och ska därför inte läsas som neutral marknadsoberoende forskning. Men analysen är tekniskt relevant och publicerad som forskningsarbete.

En praktisk konsekvens är viktigare än den exakta orsaken:

> En mogen användare bör föredra ett tydligt ”jag vet inte” framför ett övertygande fel.

Det betyder också att man aktivt kan be modellen att markera osäkerhet, skilja fakta från antaganden och säga när källunderlag saknas.

Det eliminerar inte fel, men förbättrar arbetsformen.

## Faktafrågor har olika risk

Alla frågor är inte lika känsliga för fel.

Om du frågar:

> Vad är skillnaden mellan en stack och en queue?

är kunskapen stabil, välrepresenterad och enkel att verifiera.

Om du frågar:

> Vilken parameter introducerades i version 3.7.2 av det här relativt smala biblioteket?

är situationen en annan.

Samma sak gäller:

- ny lagstiftning,
- nyligen ändrade molntjänstvillkor,
- säkerhetsbulletiner,
- specifika produktversioner,
- organisationsintern information,
- ovanliga forskningsresultat.

Ju mer **aktuellt, smalt, exakt eller konsekvenskänsligt** ett faktapåstående är, desto mindre bör man förlita sig på modellens interna kunskap ensam.

Då behövs källor.

## Skillnaden mellan att fråga modellen och att fråga med källor

Moderna AI-tjänster kan ofta använda webbsökning, dokument, repositoryn eller andra källor som stöd för svaret.

Det förändrar situationen betydligt.

Om modellen får relevanta källor kan den arbeta med konkret underlag i stället för att enbart förlita sig på det som finns representerat i modellens parametrar.

Det är en av de första broarna mot fas 5 – **Ge kontext** – även om användaren fortfarande befinner sig i ett enkelt frågebeteende.

Men inte heller källstödd AI ska behandlas som ofelbar.

**Forskningsresultat – retrieval och källstöd:** En Nature Communications-studie från 2025 analyserade hur väl språkmodeller stödjer medicinska påståenden med relevanta referenser. Forskarna fann att retrieval-augmented generation förbättrade vissa delar, men att retrieval i sig inte löste problemet. Modellen kunde fortfarande ge påståenden som inte faktiskt stöddes av de angivna källorna. [K-030]

Detta ger oss två separata verifieringsfrågor:

1. Finns källan verkligen?
2. Stödjer källan faktiskt påståendet?

De blandas ofta ihop.

En länk under ett svar är inte automatiskt evidens för texten ovanför länken.

## Den särskilda faran med referenser

Källhänvisningar känns trygga. De signalerar akademisk noggrannhet.

Just därför är fabricerade referenser ett bra exempel på varför AI-svar måste verifieras.

**Forskningsresultat – fabricerade referenser:** En studie i Scientific Reports analyserade 636 referenser som genererades av GPT-3.5 och GPT-4 i litteraturöversikter. I materialet var 55 procent av GPT-3.5-referenserna och 18 procent av GPT-4-referenserna fabricerade. Även bland verkliga referenser förekom betydande metadatafel. [K-031]

Studien gjordes 2023 och säger därför inte hur moderna 2026-modeller presterar. Den är däremot ett tydligt empiriskt exempel på mekanismen: en språkmodell kan skapa en referens som ser fullständigt realistisk ut.

Nyare studier visar att problemet inte är historiskt eliminerat. En studie från 2025 av GPT-4o i litteraturöversikter fann fortfarande både fabricerade referenser och många fel i verkliga referenser, särskilt inom mer specialiserade ämnen. [K-032]

Lärdomen är inte ”använd aldrig AI för research”.

Lärdomen är:

> Be AI hjälpa dig hitta och förstå källor – men verifiera källorna i den faktiska källan.

## Tre bra användningsfall i fas 1

Fas 1 är särskilt stark för tre typer av arbete.

### 1. Orientering

När du ännu inte vet vilka ord du borde söka efter.

Du kan fråga:

> Jag behöver förstå hur tjänster kan kommunicera asynkront utan att kopplas hårt till varandra. Vilka centrala begrepp och mönster bör jag läsa om?

AI:n kan då hjälpa dig bygga ett första begreppslandskap.

Det är ofta mer värdefullt än ett direkt svar eftersom det förbättrar dina kommande frågor.

### 2. Förklaring

När du redan har ett begrepp men inte förstår det.

Du kan be om:

- enklare språk,
- analogi,
- konkret kodexempel,
- kontrast mot ett närliggande begrepp,
- exempel på när tekniken inte passar.

Detta är en av dialogformens stora styrkor.

### 3. Lokal felsökning

När du har ett begränsat problem och kan ge tillräckligt med kontext.

Till exempel:

> Den här Java-metoden kompilerar inte. Här är felmeddelandet och de 25 relevanta raderna. Vad är den mest sannolika orsaken?

Det är fortfarande en fråga, men en betydligt bättre fråga än ”varför fungerar inte min kod?”.

## Den första mognadsförflyttningen: från svar till frågekvalitet

Nybörjaren bedömer ofta AI-användning efter hur bra svaret blev.

Den mer mogna fas 1-användaren börjar även bedöma **frågan**.

Har modellen tillräcklig information?

Är begreppen entydiga?

Är frågan tidskänslig?

Är det en faktauppgift eller ett resonemang?

Finns det en auktoritativ källa som borde användas?

Är konsekvensen av ett fel liten eller stor?

Det är ett litet skifte, men viktigt.

Du går från:

> Kan AI svara på detta?

mot:

> Under vilka förutsättningar kan jag lita tillräckligt på svaret för just den här uppgiften?

Det är början på mognadsresan.

## En enkel riskmodell för frågor

Ett praktiskt sätt att bedöma en AI-fråga är att väga tre faktorer:

**Osäkerhet** – Hur sannolikt är det att modellen saknar eller blandar ihop information?

**Verifierbarhet** – Hur lätt är det för dig att kontrollera svaret?

**Konsekvens** – Vad händer om svaret är fel?

Ett syntaxexempel i en sandlåda har låg konsekvens och hög verifierbarhet.

Ett råd om hur personuppgifter får behandlas i en produktionslösning har högre konsekvens och kräver mycket starkare verifiering.

Mognad innebär inte att sluta fråga AI om svåra saker.

Det innebär att ändra arbetsformen när riskprofilen ändras.

## Fråga efter osäkerhet, inte bara svar

En användbar vana är att be AI:n skilja mellan vad den vet från underlaget och vad den antar.

Till exempel:

> Besvara frågan utifrån källorna jag gett dig. Markera tydligt sådant som är en slutsats snarare än explicit stöd i källan. Om underlaget inte räcker, säg det.

Eller:

> Ge mig de tre mest sannolika förklaringarna. Ange vad som talar för och emot varje alternativ och vilken ytterligare information som bäst skulle skilja dem åt.

Detta är redan början på nästa fas.

Frågan används inte längre bara för att få ett svar.

Den används för att strukturera tänkandet.

## När fas 1 räcker

Mognad beskrivs ibland som om alla uppgifter borde flyttas mot agenter och automation.

Så är det inte.

Fas 1 är ofta den bästa arbetsformen när:

- frågan är liten,
- kontexten är begränsad,
- du vill orientera dig,
- resultatet är lätt att verifiera,
- det inte finns något faktiskt arbetsobjekt som AI behöver förändra.

Att starta ett agentiskt arbetsflöde för att få en förklaring av ett begrepp är inte moget. Det är bara mer komplicerat.

## Så tar du nästa steg

Nästa mognadssteg börjar när du slutar fråga efter **ett svar** och i stället använder AI:n för att undersöka **ett problem**.

Pröva därför att förändra några vardagsfrågor.

I stället för:

> Vilket alternativ är bäst?

fråga:

> Vilka tre rimliga alternativ finns? Vilka antaganden gör varje alternativ bra eller dåligt? Vilken information saknas för att kunna välja?

I stället för:

> Är den här arkitekturen bra?

fråga:

> Vilka kvalitetsattribut verkar arkitekturen optimera? Vilka trade-offs skapar det och vilka risker borde jag undersöka innan jag accepterar designen?

Du har då börjat använda AI som **resonemangspartner**.

## När du inte bör gå vidare

Gå inte mot en mer avancerad arbetsform bara för att verktyget kan.

Stanna i fas 1 när problemet är litet och informationsbehovet är det centrala.

Gå inte heller vidare genom att ge mer kontext eller större handlingsutrymme om materialet är känsligt och du ännu inte vet om tjänsten är godkänd för informationen. Den frågan återkommer i fas 5 och behandlas på djupet senare i boken.

Den första fasen är alltså inte något vi lämnar bakom oss.

Den blir en del av repertoaren.

Den mogna användaren ställer fortfarande enkla frågor varje dag – men vet bättre **vad ett AI-svar är, vad det inte är och när det behöver verifieras**.
