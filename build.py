# builds the public site from src/: the same page with a public flag, plus only the projects marked public.
# usage: python3 build.py [projects.json exported from the artifact's projects collection]
import json, os, shutil, sys
root = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(root, 'src')
html = open(os.path.join(src, 'index.html')).read()
html = html.replace('<script type="module">', '<script>window.PUBLIC = true;</script>\n<script type="module">', 1)
open(os.path.join(root, 'index.html'), 'w').write(html)
for f in ['three.module.min.js', 'RoundedBoxGeometry.js', 'RoomEnvironment.js', 'CSS3DRenderer.js']:
    shutil.copy(os.path.join(src, f), root)
# without an export, keep whatever was published last
if len(sys.argv) > 1:
    docs = json.load(open(sys.argv[1]))
    keep = ('name', 'tagline', 'status', 'now', 'updated', 'steps', 'links')
    pub = {k: {f: v[f] for f in keep if f in v} for k, v in docs.items() if v.get('public')}
    json.dump(pub, open(os.path.join(root, 'projects.json'), 'w'), indent=2, ensure_ascii=False)
    print('public projects:', list(pub))
open(os.path.join(root, '.nojekyll'), 'w').close()
