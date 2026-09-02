#!/usr/bin/env python3
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / 'docs' / 'export-metadata.yaml'
EXPORTS = ROOT / 'exports'
COVER = ROOT / 'assets' / 'cover.png'
PDF_CSS = ROOT / 'styles' / 'pdf.css'
EPUB_CSS = ROOT / 'styles' / 'epub.css'
CHAPTER_FILTER = ROOT / 'scripts' / 'chapter-headings.lua'
SOURCES = ROOT / 'docs' / 'kallregister.md'

CHAPTERS = [
    'chapters/00-inledning.md',
    'chapters/01-nar-dialogen-blev-ett-arbetsverktyg.md',
    'chapters/02-hur-ai-redan-anvands-i-systemutveckling.md',
    'chapters/03-produktivitet-ar-mer-an-att-gora-samma-sak-snabbare.md',
    'chapters/04-fas-1-fraga.md',
    'chapters/05-fas-2-resonera.md',
    'chapters/06-fas-3-skapa.md',
    'chapters/07-fas-4-samarbeta.md',
    'chapters/08-fas-5-ge-kontext.md',
    'chapters/09-fas-6-delegera.md',
    'chapters/10-fas-7-orkestrera.md',
    'chapters/11-fran-behov-och-krav-till-losningside.md',
    'chapters/12-fran-arkitektur-och-design-till-implementation.md',
    'chapters/13-fran-test-och-kvalitet-till-leverans.md',
    'chapters/14-det-manniskan-fortfarande-maste-vara-bra-pa.md',
    'chapters/15-nar-ai-behover-kanna-till-det-som-inte-ar-publikt.md',
    'chapters/16-fran-individuell-ai-anvandning-till-ai-assisterat-arbetssystem.md',
    'appendices/01-bokens-modeller.md',
    'appendices/02-sjalvvardering.md',
]


def validate_markdown(path: Path) -> list[str]:
    errors = []
    text = path.read_text(encoding='utf-8')
    if re.search(r'^####', text, flags=re.MULTILINE):
        errors.append(f'{path}: H4 eller djupare rubrik hittades')
    h1s = re.findall(r'^# (.+)$', text, flags=re.MULTILINE)
    if len(h1s) != 1:
        errors.append(f'{path}: förväntade exakt en H1, hittade {len(h1s)}')
    if text.count('```') % 2:
        errors.append(f'{path}: obalanserade kodblock')
    return errors


def parse_source_rows() -> dict[str, dict[str, str]]:
    rows = {}
    for line in SOURCES.read_text(encoding='utf-8').splitlines():
        if not re.match(r'^\| K-\d{3} \|', line):
            continue
        parts = [p.strip() for p in line.strip().strip('|').split('|')]
        if len(parts) < 7:
            continue
        rows[parts[0]] = {
            'source': parts[1], 'type': parts[2], 'date': parts[3],
            'supports': parts[4], 'origin': parts[5], 'status': parts[6],
        }
    return rows


def build_combined() -> tuple[str, list[str]]:
    text = '\n\n'.join((ROOT / p).read_text(encoding='utf-8') for p in CHAPTERS)
    used = sorted(set(re.findall(r'\[(K-\d{3})\]', text)), key=lambda x: int(x.split('-')[1]))
    # Make source markers clickable in EPUB/PDF.
    text = re.sub(r'\[(K-\d{3})\]', r'[[\1]](#\1)', text)
    rows = parse_source_rows()
    source_md = ['# Källor', '', 'Följande källor refereras i bokens manus. Evidenstyp och avsändare anges för att göra det lättare att bedöma vad varje källa faktiskt kan stödja.', '']
    missing = []
    for kid in used:
        row = rows.get(kid)
        if not row:
            missing.append(kid)
            continue
        source_md.extend([
            f'### {kid} {{#{kid}}}', '',
            row['source'], '',
            f'**Evidenstyp:** {row["type"]}  ',
            f'**Datum/version:** {row["date"]}  ',
            f'**Avsändare:** {row["origin"]}', '',
        ])
    return text + '\n\n' + '\n'.join(source_md), missing


def postprocess_epub(epub: Path) -> None:
    """Keep EPUB navigation index, but remove nav.xhtml from normal reading order."""
    with tempfile.TemporaryDirectory() as td:
        temp = Path(td)
        with zipfile.ZipFile(epub, 'r') as zf:
            zf.extractall(temp)

        opf = temp / 'EPUB' / 'content.opf'
        ns = {'opf': 'http://www.idpf.org/2007/opf'}
        ET.register_namespace('', ns['opf'])
        tree = ET.parse(opf)
        root = tree.getroot()
        spine = root.find('opf:spine', ns)
        if spine is None:
            raise RuntimeError('Kunde inte hitta EPUB spine i content.opf')
        for itemref in list(spine):
            if itemref.get('idref') == 'nav':
                spine.remove(itemref)
        tree.write(opf, encoding='utf-8', xml_declaration=True)

        rebuilt = epub.with_suffix('.tmp.epub')
        with zipfile.ZipFile(rebuilt, 'w') as zf:
            mimetype = temp / 'mimetype'
            zf.write(mimetype, 'mimetype', compress_type=zipfile.ZIP_STORED)
            for path in sorted(temp.rglob('*')):
                if not path.is_file() or path == mimetype:
                    continue
                zf.write(path, path.relative_to(temp).as_posix(), compress_type=zipfile.ZIP_DEFLATED)
        rebuilt.replace(epub)


def run(cmd):
    subprocess.run(cmd, check=True)


def main() -> int:
    for required in [META, COVER, PDF_CSS, EPUB_CSS, SOURCES, CHAPTER_FILTER]:
        if not required.exists():
            print(f'Saknar {required.relative_to(ROOT)}', file=sys.stderr)
            return 2
    missing_files = [p for p in CHAPTERS if not (ROOT / p).exists()]
    if missing_files:
        print('Saknade manusfiler:', *missing_files, sep='\n  - ', file=sys.stderr)
        return 2
    errors = []
    for rel in CHAPTERS:
        errors.extend(validate_markdown(ROOT / rel))
    if errors:
        print('Valideringsfel:', file=sys.stderr)
        for e in errors:
            print(f'  - {e}', file=sys.stderr)
        return 2

    pandoc = shutil.which('pandoc')
    weasyprint = shutil.which('weasyprint')
    if not pandoc or not weasyprint:
        print('Pandoc och WeasyPrint krävs för export.', file=sys.stderr)
        return 2

    EXPORTS.mkdir(exist_ok=True)
    build = ROOT / 'build'
    build.mkdir(exist_ok=True)
    combined_text, missing_sources = build_combined()
    if missing_sources:
        print('Käll-ID saknas i källregistret: ' + ', '.join(missing_sources), file=sys.stderr)
        return 2
    combined = build / 'book.md'
    combined.write_text(combined_text, encoding='utf-8')

    epub = EXPORTS / 'fran-fraga-till-arbetskamrat.epub'
    run([
        pandoc, str(combined), '--from=gfm+attributes', '--to=epub3', '--toc', '--toc-depth=1', f'--lua-filter={CHAPTER_FILTER}',
        '--metadata', 'title=Från fråga till arbetskamrat',
        '--metadata', 'subtitle=Från enkla frågor till moget AI-assisterat arbete',
        '--metadata', 'author=Erland Lindmark', '--metadata', 'lang=sv-SE',
        f'--epub-cover-image={COVER}', f'--css={EPUB_CSS}', f'--output={epub}'
    ])
    postprocess_epub(epub)

    html = build / 'book.html'
    run([
        pandoc, str(combined), '--from=gfm+attributes', '--to=html5', '--standalone', '--toc', '--toc-depth=1', f'--lua-filter={CHAPTER_FILTER}',
        '--metadata', 'title=Från fråga till arbetskamrat',
        '--metadata', 'subtitle=Från enkla frågor till moget AI-assisterat arbete',
        '--metadata', 'author=Erland Lindmark', '--metadata', 'lang=sv-SE',
        f'--css={PDF_CSS}', f'--output={html}'
    ])

    content_pdf = build / 'content.pdf'
    run([weasyprint, '--base-url', str(ROOT), str(html), str(content_pdf)])

    cover_html = build / 'cover.html'
    cover_uri = COVER.resolve().as_uri()
    cover_html.write_text(f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: 6in 9in; margin: 0; }} html,body {{margin:0;padding:0;width:6in;height:9in;overflow:hidden;}}
img {{width:6in;height:9in;display:block;object-fit:cover;}}
</style></head><body><img src="{cover_uri}" alt="Omslag"></body></html>''', encoding='utf-8')
    cover_pdf = build / 'cover.pdf'
    run([weasyprint, str(cover_html), str(cover_pdf)])

    final_pdf = EXPORTS / 'fran-fraga-till-arbetskamrat.pdf'
    from pypdf import PdfReader, PdfWriter
    writer = PdfWriter()
    for source_pdf in [cover_pdf, content_pdf]:
        for page in PdfReader(str(source_pdf)).pages:
            writer.add_page(page)
    writer.add_metadata({
        '/Title': 'Från fråga till arbetskamrat',
        '/Author': 'Erland Lindmark',
        '/Subject': 'Från enkla frågor till moget AI-assisterat arbete',
    })
    with final_pdf.open('wb') as f:
        writer.write(f)

    print(f'Skapade {epub}')
    print(f'Skapade {final_pdf}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
