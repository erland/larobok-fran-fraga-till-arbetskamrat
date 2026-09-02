# Exportguide

Projektet har en verifierad lokal exportpipeline för PDF och EPUB.

```bash
./scripts/export-book.sh
```

Exporten skapar:

- `exports/fran-fraga-till-arbetskamrat.pdf`
- `exports/fran-fraga-till-arbetskamrat.epub`

PDF använder 6 × 9 tum, det fastställda omslaget, titelblad, innehållsförteckning med sidnummer, kapitelstarter på ny sida samt källförteckning. EPUB använder samma omslag och innehåll men flödande layout.

Se `docs/layoutprov-v1.md` för resultat och kvarstående slutkontroller.


## GitHub Actions

Projektet innehåller `.github/workflows/build-book.yml` för manuell build via **Run workflow** och automatisk build när en GitHub Release publiceras. Se `docs/github-actions.md`.
