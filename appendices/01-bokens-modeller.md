# Bilaga A – Bokens modeller i översikt

Boken använder flera pedagogiska modeller för att göra olika delar av AI-assisterat arbete lättare att se och diskutera. De är **bokens egna synteser**, om inget annat uttryckligen anges. De ska därför inte läsas som vetenskapligt etablerade standardmodeller.

Modellerna fyller olika funktioner. Några beskriver **hur arbetssättet mognar**, andra hjälper dig att **styra en konkret uppgift**, och några används för att **bedöma risk, kvalitet eller organisatoriska förutsättningar**.

## Mognadsresan: sju arbetsformer

**Fråga → Resonera → Skapa → Samarbeta → Ge kontext → Delegera → Orkestrera**

Detta är bokens huvudmodell. Den beskriver en växande repertoar av sätt att arbeta med AI. Den är inte en strikt trappa där varje uppgift ska förflyttas så långt åt höger som möjligt.

Använd modellen när du vill fråga: **Vilken arbetsform använder jag nu, och vilken annan arbetsform skulle kunna ge mer nytta utan att öka risk eller kontrollkostnad orimligt mycket?**

## Tre lager i mognad

**Repertoar – situationsanpassning – kontroll**

Repertoar handlar om hur många arbetsformer du behärskar. Situationsanpassning handlar om att välja rätt arbetsform för uppgiften. Kontroll handlar om att verifiera resultat, styra informationsåtkomst och handlingsutrymme samt bedöma om arbetssättet faktiskt förbättrar helheten.

Denna modell motverkar föreställningen att mognad är samma sak som maximal autonomi.

## Fyra roller i resonemang

**Bredda – strukturera – utmana – fokusera**

Används i fas 2 när AI fungerar som bollplank. Den hjälper till att göra resonemanget aktivt i stället för att bara be om en rekommendation.

- **Bredda:** hitta fler alternativ, perspektiv och hypoteser.
- **Strukturera:** ordna problemet, kriterierna och beroendena.
- **Utmana:** leta efter svaga antaganden, motargument och risker.
- **Fokusera:** identifiera vad som faktiskt behöver avgöras eller verifieras härnäst.

## Artefaktkontraktet

**Syfte – mottagare – begränsningar – kvalitetskriterier – verifieringssätt**

Används när AI ska skapa något konkret: kod, testfall, krav, analys, dokumentation eller annat arbetsmaterial. Modellen hjälper dig att definiera vad ”bra” betyder innan produktionen börjar.

## Samarbetskontraktet

**Vad får förändras – vilken återkoppling räknas – vad får stoppa arbetet – när är vi klara**

Används när arbetet går från en beställning till en iterativ loop mellan människa och AI. Syftet är att undvika oändliga förbättringsvarv där inget tydligt kvalitetskriterium avgör när resultatet är tillräckligt bra.

## Delegationsbudgeten

**Data – verktyg – behörigheter – tid/kostnad – irreversibla åtgärder**

Används när AI får genomföra flera steg självständigt. Delegationsbudgeten gör handlingsutrymmet konkret och hjälper till att skilja ett ambitiöst mål från obegränsade befogenheter.

## Arbetsflödeskontraktet

**Trigger och mål – state och kontext – roller och steg – handoffs och kontrollpunkter – observability – evals och förbättringsloop**

Används när AI inte längre bara hjälper till i en enskild uppgift utan byggs in i ett återkommande arbetssätt. Modellen flyttar fokus från en lyckad körning till kvaliteten i själva arbetssystemet.

## Behov → beslut → förändring → bevis

Denna kedja används i Del III för att hålla samman utvecklingsprocessen.

- **Behov:** vilket problem eller värde ska hanteras?
- **Beslut:** vilka vägval och antaganden ligger bakom lösningen?
- **Förändring:** vad har faktiskt ändrats i systemet och dess artefakter?
- **Bevis:** vad visar att förändringen fungerar och uppfyller relevanta krav?

Kedjan hjälper till att upptäcka när AI producerar mycket material men spårbarheten mellan problem, beslut, implementation och verifiering blir svag.

## Kompetensbudgeten

**Vad måste vi kunna själva – vad måste vi kunna verifiera – vad kan AI göra huvuddelen av – hur upptäcker vi kompetensförsvagning**

Används när AI förändrar vilka moment människor faktiskt övar på. Målet är inte att bevara varje manuell arbetsform, utan att medvetet avgöra vilken kompetens som fortfarande behövs för problemformulering, omdöme, kontroll och ansvar.

## Informationsbudgeten

**Behov → minsta kontext → identifiering → tjänst → flöde → konsekvens → beslut**

Används när arbetet kräver icke-publikt eller på annat sätt känsligt material. Modellen kombinerar dataminimering med **promptminimering**: även själva frågan kan avslöja mer än vad som behövs för uppgiften.

## Ett AI-assisterat arbetssystem

**Riktning – miljö – arbetsdesign – kontroll – kvalitet – lärande**

Detta är organisationsperspektivet i kapitel 16. Modellen används för att förklara varför individuell skicklighet inte räcker när AI blir en del av ett gemensamt arbetssätt.

- **Riktning:** vilket resultat ska förbättras?
- **Miljö:** vilka modeller, data, verktyg och integrationer finns tillgängliga?
- **Arbetsdesign:** hur fördelas arbete mellan människor, AI och deterministisk automation?
- **Kontroll:** vilka informationsgränser, behörigheter och ansvar gäller?
- **Kvalitet:** vilka tester, evals och kvalitetsgrindar behövs?
- **Lärande:** hur blir erfarenheter till gemensam organisatorisk kunskap?

## Använd inte alla modeller samtidigt

Modellerna är verktyg, inte en checklista som måste fyllas i för varje AI-interaktion. Välj den modell som hjälper dig att se nästa relevanta fråga.

Om du bara vill förstå ett tekniskt begrepp behöver du sannolikt ingen delegationsbudget. Om en agent däremot ska läsa ett internt repository, ändra kod, köra kommandon och skapa en pull request behöver du tänka både på kontext, delegation, verifiering och information.

Mognad visar sig inte i hur många modeller du använder. Den visar sig i att du väljer **rätt mängd styrning för rätt uppgift**.
