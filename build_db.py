import json
from pathlib import Path
p=Path(__file__).parent
(p/'engines.js').write_text('const ENGINE_DB = '+json.dumps(json.loads((p/'engines.json').read_text()),ensure_ascii=False)+';',encoding='utf-8')
