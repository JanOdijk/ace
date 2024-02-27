import cgn_stats
import lassy_stats

Theta = 10

#tests
def test():
    x = {'both1':1, 'both2':2, 'only_x': 100 }
    y = {'both1':10, 'both2': 20, 'only_y':200 }
    result = summerge(x,y)
    print(result)
    if result == {'only_y': 200, 'both2': 22, 'both1': 11, 'only_x': 100}:
        return('OK')
    else:
        return('not OK')	
		
def summerge(dict1, dict2):
   result = { k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2) }
   return(result)
   
def printlowfreq(dict):
    for el in dict:
        if dict[el]<Theta:
           print('{}\t{}'.format(el, dict[el]))		
   
mcatcat =  summerge(lassy_stats.mcatcat,  cgn_stats.mcatcat)
relposcat = summerge(lassy_stats.relposcat, cgn_stats.relposcat)
mcatrel =summerge(lassy_stats.mcatrel, cgn_stats.mcatrel)
mcatrelcat = summerge(lassy_stats.mcatrelcat, cgn_stats.mcatrelcat)
siblings =summerge(lassy_stats.siblings, cgn_stats.siblings)
relrelcount = summerge(lassy_stats.relrelcount, cgn_stats.relrelcount)

mcatcatTheta = Theta
relposcatTheta = Theta
mcatrelTheta= Theta
mcatrelcatTheta = Theta
siblingsTheta  = Theta
relrelTheta = Theta

# corrections since results obtained in the past provide no guarantees for the future

mcatrelcat[('sv1', 'pc', 'conj')] = mcatrelcatTheta + 1
# next ones covered by loop below
# mcatrelcat[('whsub', 'body', 'advp')] = mcatrelcatTheta + 1
# mcatrelcat[('whq', 'body', 'advp')] = mcatrelcatTheta + 1
# mcatcat[('whsub', 'advp')] = mcatcatTheta + 1
# mcatcat[('whq', 'advp')] = mcatcatTheta + 1

bodyposcats = ['advp', 'ap', 'conj', 'du', 'inf', 'mwu', 'np', 'pp', 'adj', 'bw', 'n', 'vnw', 'vz']

for poscat in bodyposcats:
    mcatrelcat[('whsub', 'body', poscat)] = mcatrelcatTheta + 1
    mcatcat[('whsub', poscat)] = mcatcatTheta + 1
    mcatrelcat[('whq', 'body', poscat)] = mcatrelcatTheta + 1
    mcatcat[('whq', poscat)] = mcatcatTheta + 1

#what is ok in smain is also ok in sv1,  inf, and ssub and vice versa

def updatemcatrelcat(mcat, rel, cat, othermcat):
    results = set()
    mcattuple = (mcat, rel, cat)
    othermcattuple = (othermcat, rel, cat)
    if mcatrelcat[mcattuple] < Theta and othermcattuple in mcatrelcat and mcatrelcat[othermcattuple] >= Theta:
        results.add(mcattuple)
        #print('({},{},{}) OK because of {}'.format(mcat, rel, cat, othermcat))
    if mcatrelcat[mcattuple] >= Theta and othermcattuple not in mcatrelcat:
        results.add(othermcattuple)
        #print('({},{},{}) OK because of {}'.format(othermcat, rel, cat, mcat))
    return results


clausecats = {'sv1', 'smain', 'ssub', 'inf', 'ppart'}

newoktuples = set()
for mcat, rel, cat in mcatrelcat:
    if mcat in clausecats:
        otherclausecats = clausecats.difference({mcat})
        for othermcat in otherclausecats:
            newoktuples |= updatemcatrelcat(mcat, rel, cat, othermcat)

for atuple in newoktuples:
    mcatrelcat[atuple] = Theta + 1

#END OF what is ok in smain is also ok in sv1,  inf, and ssub and vice versa

#but some are really errors in CGN or Lassy:
for mcat in clausecats:
    del mcatrelcat[mcat, 'obj1', 'oti']


#elliptic vc/ap and vc/vnw are ok in all clausetypes
for mcat in clausecats:
    mcatrelcat[mcat, 'vc', 'ap'] = Theta + 1
    mcatrelcat[mcat, 'vc', 'vnw'] = Theta + 1

mcatrelcat['whq', 'body', 'tsw'] = Theta +1

duchildposcats = ['advp', 'ap', 'conj', 'cp', 'detp', 'du', 'inf', 'mwu', 'np', 'pp', 'ppart', 'rel',
                  'smain', 'ssub', 'sv1', 'whq', 'whrel', 'whsub', 'adj', 'bw', 'n', 'tsw', 'tw',
                  'vg', 'vnw', 'vz', 'ww']

for poscat in duchildposcats:
    mcatcat['du', poscat] = mcatcatTheta + 1

mcatrel[('ap', 'mwp')] = mcatrelTheta + 1
mcatrelcat[('detp', 'det', 'bw')] = mcatrelcatTheta + 1
mcatrelcat[('detp', 'mwp', 'vnw')] = mcatrelcatTheta +1
