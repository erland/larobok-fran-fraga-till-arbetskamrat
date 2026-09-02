# GitHub Actions för bokbygge

Workflow: `.github/workflows/build-book.yml`

Workflowen använder samma exportkommando som lokalt:

```bash
./scripts/export-book.sh
```

## Manuell build

1. Öppna **Actions** i GitHub.
2. Välj **Build book**.
3. Välj **Run workflow**.
4. När körningen är klar finns PDF och EPUB under körningens **Artifacts** som `fran-fraga-till-arbetskamrat`.

## Automatisk build vid release

När en GitHub Release **publiceras** körs samma workflow automatiskt. PDF och EPUB:

- sparas som Actions-artifact, och
- laddas upp som assets på den GitHub Release som triggade bygget.

Workflowen behöver repositoryns standard `GITHUB_TOKEN` med `contents: write`, vilket deklareras i workflowfilen.

## Byggmiljö

Workflowen installerar Pandoc, WeasyPrint, Noto/DejaVu-fontpaket och Python-paketet `pypdf` innan exporten körs. Det gör CI-bygget så nära den verifierade lokala exportpipen som möjligt.
