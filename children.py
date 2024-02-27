
possiblesons={}

possiblesons['mwu']=['mwp']
possiblesons['top']=['--']
possiblesons['ahi']=['cmp','body']
possiblesons['svan']=['cmp','body']
possiblesons['ti']=['cmp','body']
possiblesons['conj']=['cnj','crd']
possiblesons['whq']=['whd', 'body']
possiblesons['oti']=['cmp','body']
possiblesons['rel']=['rhd', 'body', 'mod']
possiblesons['whrel']=['rhd', 'body', 'mod']
possiblesons['whsub']=['rhd', 'body', 'mod']
possiblesons['cp']=['cmp', 'body', 'mod']
possiblesons['detp']=['hd', 'obcomp', 'mod', 'me', 'det']
possiblesons['du']=['tag', 'nucl', 'dp', 'dlink', 'sat']
possiblesons['advp']=['hd', 'me', 'mod', 'obcomp']


requiredsons={}
requiredsons['mwu']=['mwp']
requiredsons['top']=['--']
requiredsons['ahi']=['cmp','body']
requiredsons['svan']=['cmp','body']
requiredsons['ti']=['cmp','body']
requiredsons['conj']=['cnj']
requiredsons['whq']=['whd', 'body']
requiredsons['oti']=['cmp','body']
requiredsons['rel']=['rhd', 'body']
requiredsons['whrel']=['rhd', 'body']
requiredsons['whsub']=['whd', 'body']
requiredsons['cp']=['cmp', 'body']
requiredsons['detp']=['hd']
requiredsons['advp']=['hd']

requireschildfeature={}
requireschildfeature['smain']=('hd', 'ww', 'wvorm', ['pv'])
requireschildfeature['sv1']=('hd', 'ww', 'wvorm', ['pv'])
requireschildfeature['inf']=('hd', 'ww', 'wvorm', ['inf'])
requireschildfeature['ppart']=('hd', 'ww', 'wvorm', ['vd'])
requireschildfeature['ppres']=('hd', 'ww', 'wvorm', ['od']) # too strong: adjectives must also be allowed
