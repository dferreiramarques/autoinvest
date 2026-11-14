import json, urllib.parse, urllib.request, datetime
BASE='https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_minr'
def parse(d):
    dims=d['id']; sizes=d['size']; ti=dims.index('time'); assert all(s==1 for i,s in enumerate(sizes) if i!=ti)
    idx=d['dimension']['time']['category']['index']; vals=d['value']; out=[]
    for month,i in sorted(idx.items()):
        v=vals.get(str(i)) if isinstance(vals,dict) else vals[i]
        if isinstance(v,(float,int)) and v>0: out.append([month,v])
    if not out: raise ValueError('empty series')
    return out
if __name__=='__main__':
    data={'updated':datetime.datetime.now(datetime.timezone.utc).isoformat(),'series':{}}
    for geo in ['PT','EU27_2020']:
        for kind,code in [('new','CP0711'),('used','CP0712')]:
            # ECOICOP legacy codes: new/used are subcategories of CP0711; try explicit subindices only.
            code={'new':'CP07111','used':'CP07112'}[kind]
            for unit in ['I25']:
                try:
                    q=urllib.parse.urlencode({'lang':'EN','freq':'M','unit':unit,'coicop18':code,'geo':geo,'sinceTimePeriod':'2020-01'})
                    with urllib.request.urlopen(BASE+'?'+q,timeout=45) as r: d=json.load(r)
                    label=d['dimension']['coicop18']['category']['label'][code]
                    if ('new' if kind=='new' else 'second') not in label.lower() and (kind!='used' or 'used' not in label.lower()): raise ValueError(label)
                    data['series'][geo+'-'+kind]={'label':label,'unit':unit,'points':parse(d)};break
                except Exception as e: print(geo,kind,unit,e)
    if len(data['series'])!=4: raise SystemExit('Incomplete data; previous cache preserved')
    with open('market-cache.json','w') as f: json.dump(data,f,indent=2)
