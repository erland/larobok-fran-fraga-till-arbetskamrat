# Slutgranskning v1

## Omfattning

Granskningen omfattar läsartexten (inledning, kapitel 1–16 och bilagor), källapparaten, PDF/EPUB-exporten och projektets releaseberedskap. Den är genomförd efter layoutrevision v1.7.

## Samlad bedömning

Bokens struktur, sjufasmodell och huvudtes håller. Ingen större innehållsomskrivning rekommenderas inför release candidate. Den viktigaste kvarvarande produktionsfasen är metadata/publiceringsfinish och kontroll av ett bygge från en ren GitHub-checkout.

## Genomförda korrigeringar

- Inledningen har fått ett läsarorienterat avsnitt som förklarar skillnaden mellan forskning, mätdata, leverantörsuppgifter och **Bokens syntes**.
- Två redundanta övergångsstycken i kapitel 1–2 togs bort eftersom de skapade onödigt korta kapitelslutsidor i PDF och inte tillförde nytt innehåll.
- Kapitel 15 har färskhetskontrollerats för centrala leverantörsuppgifter och EDPB:s anonymiseringsutkast. Samrådet för Guidelines 02/2026 är fortfarande öppet till 30 oktober 2026 vid kontrollen 2 september 2026.
- Terminologin i Microsoft-exemplet har förtydligats till **grundmodeller (foundation models)**.
- Projektmetadata har uppdaterats till slutgranskningsläge.

## Evidens och källor

- Alla K-ID som används i läsartexten finns i källregistret.
- Exporten tar endast med källor som faktiskt refereras i boken; researchkällor som inte används belastar alltså inte läsarens källförteckning.
- Leverantörskällor i kapitel 15 anges som leverantörsuppgifter, inte oberoende effekt- eller säkerhetsforskning.
- Motstridig produktivitetsevidens i kapitel 3 är fortsatt bevarad.
- Sjufasmodellen presenteras fortsatt som pedagogisk syntes och inte som validerad vetenskaplig mognadsskala.

## Språk och repetition

Ingen ny omfattande omskrivning rekommenderas. Återkommande rubriker som **Så tar du nästa steg** och **När du inte bör gå vidare** är avsiktlig pedagogisk struktur. Engelska yrkestermer som *review*, *evals* och *trade-offs* används där de speglar etablerat språk i målgruppen; centrala styrande begrepp är definierade i projektets terminologifil.

## Layout

PDF-preflight efter slutgranskningen gav inga strukturfel. Den nya PDF:n omfattar 265 sidor inklusive omslag och källförteckning. Sidvis kontroll identifierade en nästan tom kapitelslutsida, som nu har åtgärdats genom textstramning. Några kortare kapitelslutsidor med listor finns kvar men är typografiskt acceptabla och innehåller verkligt innehåll; de bör inte lösas genom generell komprimering av hela boken.

## Kvar före release candidate

1. Fastställ copyright-/kolofontext och eventuell ISBN-placeholder.
2. Besluta om kort baksidestext och eventuell författarpresentation ska ingå i projektet.
3. En ren lokal checkout-simulering utan `build/` och tidigare exporter har passerat. Kör därefter GitHub Action i det faktiska repositoryt och verifiera CI-miljön.
4. Gör en sista visuell kontroll av den CI-byggda PDF/EPUB-versionen.
5. Märk därefter en release candidate, exempelvis `v1.0.0-rc.1`.
