# Från fråga till arbetskamrat

**Undertitel:** Från enkla frågor till moget AI-assisterat arbete  
**Författare:** Erland Lindmark  
**Språk:** Svenska  
**Status:** Projekt v1.5 – kapitelrubriker reviderade; GitHub Actions för PDF/EPUB tillagda

Detta projekt innehåller planering, researchunderlag och manus för faktaboken *Från fråga till arbetskamrat*.
Boken beskriver hur personer som arbetar med systemutveckling och IT-arkitektur successivt utvecklar sitt sätt att arbeta med generativ AI: från enkla frågor till kontextmedvetet samarbete, delegering och AI-assisterade arbetsflöden.

## Nuvarande fas

Researchpass v1–v9 är genomförda och inledningen samt kapitel 1–16 är skrivna som första manusutkast. Hela den sjufasiga mognadsresan finns i manus, och Del III prövar modellen genom ett sammanhängande scenario från behov och krav till arkitektur, implementation, test och leverans.

Mognadsmodellen behandlas fortsatt som bokens pedagogiska syntes. Repertoar, situationsanpassning och kontroll är viktigare än maximal autonomi. Researchpass v5 preciserar dessutom att orkestrering betyder design av ett AI-assisterat arbetssystem och **inte** automatiskt multi-agent.

## Viktiga dokument

- `docs/bokspecifikation.md` – bokens syfte, målgrupp och avgränsningar.
- `docs/mognadsmodell.md` – den sjufasmodell som utgör bokens röda tråd.
- `docs/kapitelplan.md` – detaljerad plan för inledning och 16 kapitel.
- `docs/researchplan.md` – styrning för research och just-in-time-kompletteringar.
- `docs/researchresultat-v1.md` – första researchpasset och övergripande evidensläge.
- `docs/researchresultat-v2.md` – hallucinationer, källverifiering och resonemang.
- `docs/researchresultat-v3.md` – genererade artefakter, iteration, kvalitet och review.
- `docs/researchresultat-v4.md` – kontext, retrieval, delegation, agentverktyg och människa-i-loopen.
- `docs/researchresultat-v5.md` – orkestrering, agentflöden, observability och evals.
- `docs/researchresultat-v6.md` – requirements engineering, arkitektur/design, implementation, test och leverans.
- `docs/researchresultat-v7.md` – kritiskt tänkande, lärande, kompetensförskjutning och skill decay.
- `docs/researchresultat-v8.md` – icke-publikt material, enterprise-/business-AI, retention, anonymisering, promptminimering och informationsflöden.
- `docs/researchresultat-v9.md` – organisatorisk AI-beredskap, governance, plattformar, evals och lärande arbetssystem.
- `docs/kvalitetsgranskning-hela-manus-v1.md` – första helhetsgranskningen av inledning och kapitel 1–16.
- `docs/kvalitetsgranskning-del-iii-v1.md` – sammanhållen granskning av kapitel 11–13 och scenariot.
- `docs/kvalitetsgranskning-del-ii-v1.md` – sammanhållen granskning av kapitel 4–10.
- `docs/evidenspolicy.md` – regler för att skilja forskning, mätdata, leverantörsuppgifter och bokens syntes.
- `docs/kallregister.md` – källor, källtyp och oberoende/leverantör.
- `docs/pedagogisk-canon.md` – återkommande pedagogiska principer och exempel.
- `docs/terminologi.md` – styrande språkbruk.
- `docs/projektstatus.md` – beslut, öppna frågor och nästa steg.
- `docs/export-guide.md` – lokal PDF/EPUB-export.
- `docs/github-actions.md` – manuell build och release-build i GitHub Actions.

## Planerad arbetsordning

1. Språk- och repetitionsredigera hela manus.
2. Skapa ett kort självvärderingsverktyg/bilaga för mognadsresan.
3. Skapa omslag och besluta om eventuella inre illustrationer.
4. Exportera och kvalitetsgranska EPUB/PDF samt fastställa verkligt sidomfång.

## Aktuell status – v1.5

Inledning samt kapitel 1–16 är skrivna och har genomgått ett första sammanhållet språk- och repetitionspass. Researchpass v1–v9 finns i `docs/` och källregistret omfattar K-001–K-090. Två läsarbilagor har lagts till: `appendices/01-bokens-modeller.md` och `appendices/02-sjalvvardering.md`. Det fastställda omslaget finns i `assets/cover.png` och EPUB-exporten är konfigurerad att använda det. Första layoutprovet är genomfört. Numrerade kapitelrubriker exporteras nu som två centrerade rader. GitHub Actions kan bygga PDF/EPUB manuellt eller automatiskt vid publicerad release.
