import os
import re
import logging
from sastadev.treebankfunctions import getmeta

space = ' '
eps = ''

err = -1
nul = 0
een = 1
twee = 2

afgerond = r'2. afgerond'
ronde1 = r'1. eerste ronde'
newdata = r'0. nieuwe data'

uttctr11pat = r'u[0-9]{7,7}([0-9]{4,4})'
uttctr06pat = r'u[0-9]{2,2}([0-9]{4,4})'

uttctr11re = re.compile(uttctr11pat)
uttctr06re = re.compile(uttctr06pat)

uttctrpat = r'0([0-9]{4,4})[ \._]'
uttctrre = re.compile(uttctrpat)

sessionpat = r'(laura|sarah)[0-9][0-9]'
sessionre = re.compile(sessionpat)
sentencexpath = '//sentence/text()'


def clean(astr):
    if astr is None:
        result = None
    else:
        result = space.join(astr.split())
    return result

def getfilestatus(fullname):
    if afgerond in fullname:
        result = twee
    elif ronde1 in fullname:
        result = een
    elif newdata in fullname:
        result = nul
    else:
        result = err
    return result


def getsentence(stree):
    if stree is None:
        result = None
    else:
        sentences = stree.xpath(sentencexpath)
        if sentences != []:
            result = sentences[0]
        else:
            result = None
    return result

def getcorpus(str):
    if 'laura' in str:
        result = 'laura'
    elif 'sarah' in str:
        result = 'sarah'
    else:
        result = 'unknown'
    return result

def oldgetuttctr(str):
    (base,ext) = os.path.splitext(str)
    baseparts = base.split(space)
    corebase = baseparts[0]
    uttcntstr = corebase[-4:]
    result = uttcntstr
    return result

def oldgetuttctr2(str):
    matches = uttctrre.finditer(str)
    matchlist = [m for m in matches]
    lmatchlist = len(matchlist)
    if lmatchlist == 0:
        result = 'XXXX'
        print('NO uttctr matches for {}'.format(str))
    elif lmatchlist > 1:
        result = matchlist[0].group(1)
        print('Multiple uttctr matches for {}'.format(str))
        for m in matches:
            print(m)
    else:
        result = matchlist[0].group(1)
    return result


def getmatch1(matchlist):
    lmatchlist = len(matchlist)
    if lmatchlist == 0:
        result = None
    elif lmatchlist > 1:
        result = matchlist[0].group(1)
        logging.warning('Multiple uttctr matches for {}'.format(str))
        for m in matchlist:
            logging.warning(m)
    else:
        result = matchlist[0].group(1)
    return result


def getuttctr(str):
    matches = uttctr11re.finditer(str)
    matchlist = [m for m in matches]
    result = getmatch1(matchlist)
    if result is None:
        matches = uttctr06re.finditer(str)
        matchlist = [m for m in matches]
        result = getmatch1(matchlist)
    lmatchlist = len(matchlist)
    if result is None:
        result = 'XXXX'
        logging.error('NO uttctr matches for {}'.format(str))
    elif lmatchlist > 1:
        logging.warning('Multiple uttctr matches for {}'.format(str))
        for m in matches:
            logging.warning(m)
    return result


def oldgetsession(fn):
    comps = fn.split('_')
    ctr = len(comps)-2
    result = comps[ctr]
    return result

def getsession(fn):
    matches = sessionre.finditer(fn)
    matchlist = [m for m in matches]
    lmatchlist = len(matchlist)
    if lmatchlist == 0:
        result = 'XXXXX00'
        print('NO session matches for {}'.format(fn))
    elif lmatchlist > 1:
        result = matchlist[0].group(0)
        print('Multiple session matches for {}'.format(fn))
        for m in matches:
            print(m)
    else:
        result = matchlist[0].group(0)
    return result


def spaceless(astr):
    if astr is None:
        result = None
    else:
        result = eps.join(astr.split())
    return result


def modifieduttsok(stree, mdstree):
    stree_origutt = getmeta(stree, 'origutt')
    mdstree_origutt = getmeta(mdstree, 'origutt')
    result = stree_origutt == mdstree_origutt
    #stree_revisedutt = getmeta(stree, 'revisedutt')
    #stree_alpino_input = getmeta(stree, 'alpino_input')
    #mdstree_sent = getsentence(mdstree)
    #stree_sent = getsentence(stree)
    #clean_stree_alpino_input =  clean(stree_alpino_input)
    #clean_stree_sent = clean(stree_sent)
    #result = stree_origutt is not None and stree_revisedutt is not None and clean_stree_alpino_input == clean_stree_sent
    return result