"""Structural acceptance checks for the generated bilingual static site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import unittest

ROOT = Path(__file__).resolve().parents[1] / 'dist'

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.tags=[]; self.feed(text)
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

class SiteTests(unittest.TestCase):
    def test_local_links_assets_and_fragments(self):
        for file in ROOT.rglob('*.html'):
            page=Page(file.read_text(encoding='utf-8'))
            for tag,attrs in page.tags:
                for attr in ('href','src'):
                    url=attrs.get(attr,''); parts=urlsplit(url)
                    if not url or parts.scheme or parts.netloc: continue
                    target=ROOT/unquote(parts.path).lstrip('/') if parts.path.startswith('/') else file.parent/unquote(parts.path)
                    if target.is_dir(): target=target/'index.html'
                    with self.subTest(page=file.relative_to(ROOT),url=url):
                        self.assertTrue(target.is_file(),f'Missing {target}')
                        if parts.fragment:
                            ids={a.get('id') for _,a in Page(target.read_text(encoding='utf-8')).tags}
                            self.assertIn(parts.fragment,ids)

    def test_translated_pairs_are_reciprocal_and_private(self):
        pages=list(ROOT.glob('en/**/index.html'))+list(ROOT.glob('fr/**/index.html'))
        self.assertEqual(len(pages),54)
        for file in pages:
            page=Page(file.read_text(encoding='utf-8')); language=file.relative_to(ROOT).parts[0]
            with self.subTest(page=file.relative_to(ROOT)):
                self.assertIn(('html',{'lang':language+'-CA'}),page.tags)
                self.assertTrue(any(t=='meta' and a.get('name')=='robots' and 'noindex' in a.get('content','') for t,a in page.tags))
                self.assertEqual(sum(t=='h1' for t,_ in page.tags),1)
                other='fr' if language=='en' else 'en'
                switches=[a['href'] for t,a in page.tags if t=='a' and a.get('lang')==other]
                self.assertEqual(len(switches),1)
                counterpart=ROOT/switches[0].strip('/')/'index.html'
                reverse=Page(counterpart.read_text(encoding='utf-8'))
                path='/'+str(file.parent.relative_to(ROOT))+'/'
                self.assertTrue(any(t=='a' and a.get('lang')==language and a.get('href')==path for t,a in reverse.tags))

if __name__=='__main__': unittest.main()
