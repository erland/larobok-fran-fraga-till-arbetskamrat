# Layoutprov v1 – PDF och EPUB

Datum: 2026-09-02
Projektversion: 1.4.0

## Vald provlayout

- PDF-format: 6 × 9 tum
- Omslag: `assets/cover.png`, helsida
- Brödtext: Noto Serif
- Rubriker: Noto Sans
- Kapitel börjar på ny sida
- Innehållsförteckning: översta rubriknivån, med sidnummer i PDF
- Tabeller: diskreta radavskiljare, återkommande tabellhuvud
- Kod/preformaterad text: ram och radbrytning
- Käll-ID i manus länkar till källförteckningen
- EPUB: EPUB3, flödande layout, samma omslag och innehållsordning

## Resultat

PDF-versionen omfattar 267 fysiska sidor inklusive omslag och källförteckning. Källförteckningen börjar på fysisk sida 251. Själva boken inklusive titelblad, innehåll, huvudmanus och bilagor ryms därmed inom cirka 250 sidor, vilket ligger nära projektets ursprungliga ambitionsnivå.

Kapitel 15 börjar på fysisk sida 196 och kapitel 16 på fysisk sida 224. Kapitel 15 är längre än genomsnittet men fungerar i layout tack vare tydliga underrubriker, kortare stycken, tabeller och exempel.

## Verifiering

PDF har renderats och visuellt kontrollerats på omslag, titelblad, innehållsförteckning, normal brödtextsida, kapitelstart, kapitel 15, tabell/preformaterad text, bilagor och källförteckning. Inga klippta texter eller överlapp noterades i stickprovet.

EPUB-arkivet har integritetskontrollerats med `unzip -t` utan fel. EPUB:s slutliga typografiska finjustering bör göras efter provläsning i minst två läsmotorer/enheter.

## Kvar inför slutlayout

1. Provläs PDF/EPUB för språkliga restfel som blir synliga först i satt text.
2. Bedöm om källförteckningen ska komprimeras ytterligare eller behållas utförlig.
3. Kontrollera EPUB i faktisk läsare och särskilt breda tabeller.
4. Överväg PDF-bokmärken/outline i slutexporten.
5. Slutlig kontroll av aktuella, färskhetskänsliga leverantörskällor inför publicering.
