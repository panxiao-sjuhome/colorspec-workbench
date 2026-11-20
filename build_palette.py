from pathlib import Path
import csv, json
src=Path('/Users/jax/.hermes/workspaces/dasheng-product-dev/color-card-bitable/palettes/pantone_latest_solid_cu.csv')
out=Path('/Users/jax/.hermes/workspaces/dasheng-product-dev/pantone-color-workbench/palette.json')
out.parent.mkdir(parents=True, exist_ok=True)
rows=[]
seen={}
for r in csv.DictReader(src.open(encoding='utf-8-sig')):
    try:
        item={'code':r['code'],'hex':r['hex'].upper(),'L':float(r['L']),'a':float(r['a']),'b':float(r['b']),'finish':r['finish']}
    except (KeyError,ValueError):
        continue
    seen[item['code']]=item
rows=list(seen.values())
out.write_text(json.dumps({'source':'local-imported-pantone-solid-cu','count':len(rows),'colors':rows},ensure_ascii=False,separators=(',',':')),encoding='utf-8')
print(json.dumps({'count':len(rows),'path':str(out)},ensure_ascii=False))
