# Release candidate v1.0.0-rc.1

## Syfte

Första release candidate för *Från fråga till arbetskamrat*.

## Publiceringsfinish

- Copyright-/kolofonsida införd i PDF och EPUB.
- Kort författarpresentation införd som avslutande läsaravsnitt före källförteckningen.
- Baksidestext fastställd i `docs/baksidestext.md`.
- Författarpresentation för externa ytor finns i `docs/forfattarpresentation.md`.
- Metadata uppdaterad till `v1.0.0-rc.1` och svenska rättighetsuppgifter.

## RC-kontroll

Release candidate ska verifieras genom:

1. ren lokal build utan tidigare `build/` och `exports/`,
2. PDF-preflight och visuellt stickprov av omslag, titelblad, kolofon, kapitelstart, bilagor, författarpresentation och källor,
3. kontroll av EPUB-spine, navigationsindex och copyright-sida,
4. därefter build i GitHub Actions från en ren checkout och kontroll av Actions-artifact/release-assets.
