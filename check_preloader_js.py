from pathlib import Path
import re
html = Path('index.html').read_text(encoding='utf-8')
script_start = html.find('<script>')
script_end = html.find('</script>', script_start)
if script_start == -1 or script_end == -1:
    raise SystemExit('script block not found')
script = html[script_start+len('<script>'):script_end]
Path('preloader_check.js').write_text(script, encoding='utf-8')
print('wrote preloader_check.js')
