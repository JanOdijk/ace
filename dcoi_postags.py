import sys
from collections import defaultdict

DCOITRIPLES=[

("[T101]" ,"N(soort,ev,basis,zijd,stan)", "die stoel, deze muziek, de filter"),
("[T102]", "N(soort,ev,basis,onz,stan)", "het kind, ons huis, het filter"),
("[T103]", "N(soort,ev,dim,onz,stan)", "dit stoeltje, op ’t nippertje"),
("[T104]", "N(soort,ev,basis,gen)", "’s avonds, de heer des huizes"),
("[T105]", "N(soort,ev,dim,gen)", "vadertjes pijp"), 
("[T106]", "N(soort,ev,basis,dat)" , "ter plaatse, heden ten dage"),
("[T107]", "N(soort,mv,basis)", "stoelen, kinderen, hersenen"),
("[T108]", "N(soort,mv,dim)", "stoeltjes, huisjes, hersentjes"),
("[T109]", "N(eigen,ev,basis,zijd,stan)", "de Noordzee, de Kemmelberg, Karel"),
("[T110]", "N(eigen,ev,basis,onz,stan)", "het Hageland, het Nederlands"),
("[T111]", "N(eigen,ev,dim,onz,stan)", "het slimme Kareltje"),
("[T112]", "N(eigen,ev,basis,gen)", "des Heren, Hagelands trots"),
("[T113]", "N(eigen,ev,dim,gen)", "Kareltjes fiets"),
("[T114]", "N(eigen,ev,basis,dat)", "wat den Here toekomt"),
("[T115]", "N(eigen,mv,basis)", "de Ardennen, de Middeleeuwen"),
("[T116]", "N(eigen,mv,dim)", "de Maatjes"),
("[U117]", "N(soort,ev,basis,genus,stan)", "een riool, geen filter"),
("[U118]", "N(eigen,ev,basis,genus,stan)", "Linux, Esselte"),
("[T201]", "ADJ(prenom,basis,zonder)", "een mooi huis, een houten pot"),
("[T202]", "ADJ(prenom,basis,met-e,stan)", "mooie huizen, een grote pot"),
("[T203]", "ADJ(prenom,basis,met-e,bijz)", "zaliger gedachtenis, van goeden huize"),
("[T204]", "ADJ(prenom,comp,zonder)", "een mooier huis"),
("[T205]", "ADJ(prenom,comp,met-e,stan)", "mooiere huizen, een grotere pot"),
("[T206]", "ADJ(prenom,comp,met-e,bijz)", "van beteren huize"),
("[T207]", "ADJ(prenom,sup,zonder)", "een alleraardigst mens"),
("[T208]", "ADJ(prenom,sup,met-e,stan)", "de mooiste keuken, het grootste paard"),
("[T209]", "ADJ(prenom,sup,met-e,bijz)", "bester kwaliteit"),
("[T210]", "ADJ(nom,basis,zonder,zonder-n)", "in het groot, het groen"),
("[T211]", "ADJ(nom,basis,zonder,mv-n)", "de timiden, dezelfden"),
("[T212]", "ADJ(nom,basis,met-e,zonder-n,stan)", "het leuke is dat, een grote met tartaar"),
("[T213]", "ADJ(nom,basis,met-e,zonder-n,bijz)", "hosanna in den hogen"),
("[T214]", "ADJ(nom,basis,met-e,mv-n)", "de rijken"),
("[T215]", "ADJ(nom,comp,zonder,zonder-n)", ""),
("[T216)", "ADJ(nom,comp,met-e,zonder-n,stan)",  "een betere"),
("[T217]", "ADJ(nom,comp,met-e,zonder-n,bijz)", ""),
("[T218)", "ADJ(nom,comp,met-e,mv-n)",  "de ouderen"),
("[T219]", "ADJ(nom,sup,zonder,zonder-n)", "op z’n best, om ter snelst"),
("[T220]", "ADJ(nom,sup,met-e,zonder-n,stan)", "het leukste is dat, het langste blijven"),
("[T221]", "ADJ(nom,sup,met-e,zonder-n,bijz)", "des Allerhoogsten"),
("[T222]", "ADJ(nom,sup,met-e,mv-n)", "de slimsten"),
("[T223]", "ADJ(postnom,basis,zonder)", "rivieren bevaarbaar in de winter"),
("[T224]", "ADJ(postnom,basis,met-s)", "iets moois"),
("[T225]", "ADJ(postnom,comp,zonder)", "een getal groter dan"),
("[T226]", "ADJ(postnom,comp,met-s)", "iets gekkers kon ik niet bedenken"),
("[T227]", "ADJ(vrij,basis,zonder)", "die stok is lang, lang slapen"),
("[T228]", "ADJ(vrij,comp,zonder)", "deze stok is langer, langer slapen"),
("[T229]", "ADJ(vrij,sup,zonder)", "die stok is het langst, het langst slapen"),
("[T230]", "ADJ(vrij,dim,zonder)", "het is hier stilletjes, stilletjes weggaan"),
("[T301]", "WW(pv,tgw,ev)", "ik kom, speel je, hij is, zwijg"),
("[T302]", "WW(pv,tgw,mv)", "komen, spelen"),
("[T303]", "WW(pv,tgw,met-t)", "jij komt, hij speelt, zwijgt"),
("[T304]", "WW(pv,verl,ev)", "kwam, speelde"),
("[T305]", "WW(pv,verl,mv)", "kwamen, speelden"),
("[T306]", "WW(pv,verl,met-t)", "kwaamt, gingt"),
("[T309]", "WW(pv,conj,ev)", "kome, leve de koning"),
("[T310]", "WW(inf,prenom,zonder)", "de nog te lezen post"),
("[T311]", "WW(inf,prenom,met-e)", "een niet te weerstane verleiding"),
("[T312]", "WW(inf,nom,zonder,zonder-n)", "(het) spelen, (het) schaatsen"),
("[T314]", "WW(inf,vrij,zonder)", "zal komen"),
("[T315]", "WW(vd,prenom,zonder)", "een verwittigd man, een gekregen paard"),
("[T316]", "WW(vd,prenom,met-e)", "een getemde feeks"),
("[T317]", "WW(vd,nom,met-e,zonder-n)", "het geschrevene, een gekwetste"),
("[T318]", "WW(vd,nom,met-e,mv-n)", "gekwetsten, gedupeerden"),
("[T320]", "WW(vd,vrij,zonder)", "is gekomen"),
("[T321]", "WW(od,prenom,zonder)", "een slapend kind"),
("[T322]", "WW(od,prenom,met-e)", "een piano spelende aap, slapende kinderen"),
("[T323]", "WW(od,nom,met-e,zonder-n)", "het resterende, een klagende"),
("[T324]", "WW(od,nom,met-e,mv-n)", "de wachtenden"),
("[T326]", "WW(od,vrij,zonder)", "liep lachend weg, al doende leert men"),
("[T401]", "TW(hoofd,prenom,stan)", "vier cijfers"),
("[T402]", "TW(hoofd,prenom,bijz)", "eens geestes zijn, te enen male"),
("[T403]", "TW(hoofd,nom,zonder-n,basis)", "er is er een ontsnapt"),
("[T404]", "TW(hoofd,nom,mv-n,basis)", "met z’n vieren"),
("[T405]", "TW(hoofd,nom,zonder-n,dim)", "er is er eentje ontsnapt, op z’n eentje"),
("[T406]", "TW(hoofd,nom,mv-n,dim)", "met z’n tweetjes"),
("[T407]", "TW(hoofd,vrij)", "veertig worden, honderd rijden, hoeveel sneller"),
("[T408]", "TW(rang,prenom,stan)", "de vierde man"),
("[T409]", "TW(rang,prenom,bijz)", "te elfder ure"),
("[T410]", "TW(rang,nom,zonder-n)", "het eerste, (de) vierde eindigen, Karel de Vijfde"),
("[T411]", "TW(rang,nom,mv-n)", "de eersten, iets aan derden verkopen"),
("[T501a]", "VNW(pers,pron,nomin,vol,1,ev)", "ik"),
("[T501b]", "VNW(pers,pron,nomin,nadr,1,ev)", "ikzelf, ikke"),
("[T501c]", "VNW(pers,pron,nomin,red,1,ev)", "’k"),
("[T501d]", "VNW(pers,pron,nomin,vol,1,mv)", "wij"),
("[T501e]", "VNW(pers,pron,nomin,nadr,1,mv)", "wijzelf"),
("[T501f]", "VNW(pers,pron,nomin,red,1,mv)", "we"),
("[T501g]", "VNW(pers,pron,nomin,vol,2v,ev)", "jij"),
("[T501h]", "VNW(pers,pron,nomin,nadr,2v,ev)", "jijzelf"),
("[T501i]", "VNW(pers,pron,nomin,red,2v,ev)", "je"),
("[U501j]", "VNW(pers,pron,nomin,vol,2b,getal)", "u"),
("[U501k]", "VNW(pers,pron,nomin,nadr,2b,getal)", "uzelf"),
("[U501l]", "VNW(pers,pron,nomin,vol,2,getal)", "gij"),
("[U501m]", "VNW(pers,pron,nomin,nadr,2,getal)", "gijzelf"),
("[U501n]", "VNW(pers,pron,nomin,red,2,getal)", "ge"),
("[U501o]", "VNW(pers,pron,nomin,vol,3,ev,masc)", "hij"),
("[T501p]", "VNW(pers,pron,nomin,nadr,3m,ev,masc)", "hijzelf"),
("[U501q]", "VNW(pers,pron,nomin,red,3,ev,masc)", "ie"),
("[U501r]", "VNW(pers,pron,nomin,red,3p,ev,masc)", "men"),
("[T501s]", "VNW(pers,pron,nomin,vol,3v,ev,fem)", "zij"),
("[T501t]", "VNW(pers,pron,nomin,nadr,3v,ev,fem)", "zijzelf"),
("[U501u]", "VNW(pers,pron,nomin,vol,3p,mv)", "zij"),
("[U501v]", "VNW(pers,pron,nomin,nadr,3p,mv)", "zijzelf"),
("[T502a]", "VNW(pers,pron,obl,vol,2v,ev)", "jou"),
("[U502b]", "VNW(pers,pron,obl,vol,3,ev,masc)", "hem"),
("[T502c]", "VNW(pers,pron,obl,nadr,3m,ev,masc)", "hemzelf"),
("[U502d]", "VNW(pers,pron,obl,red,3,ev,masc)", "’m"),
("[U502e]", "VNW(pers,pron,obl,vol,3,getal,fem)", "haar"),
("[U502f]", "VNW(pers,pron,obl,nadr,3v,getal,fem)", "haarzelf"),
("[U502g]", "VNW(pers,pron,obl,red,3v,getal,fem)", "’r, d’r"),
("[U502h]", "VNW(pers,pron,obl,vol,3p,mv)", "hen, hun"),
("[U502i]", "VNW(pers,pron,obl,nadr,3p,mv)", "henzelf, hunzelf"),
("[U503a]", "VNW(pers,pron,stan,nadr,2v,mv)", "jullie"),
("[U503b]", "VNW(pers,pron,stan,red,3,ev,onz)", "het, ’t"),
("[U503c]", "VNW(pers,pron,stan,red,3,ev,fem)", "ze"),
("[U503d]", "VNW(pers,pron,stan,red,3,mv)", "ze"),
("[T504a]", "VNW(pers,pron,gen,vol,1,ev)", "mijns gelijke, gedenk mijner"),
("[T504b]", "VNW(pers,pron,gen,vol,1,mv)", "ons gelijke, velen onzer"),
("[U504c]", "VNW(pers,pron,gen,vol,2,getal)", "uws gelijke, wie uwer"),
("[T504d]", "VNW(pers,pron,gen,vol,3m,ev)", "zijns gelijke, zijner"),
("[U504e]", "VNW(pers,pron,gen,vol,3v,getal)", "haars gelijke, harer"),
("[U504f]", "VNW(pers,pron,gen,vol,3p,mv)", "huns gelijke, een hunner"),
("[U505a]", "VNW(pr,pron,obl,vol,1,ev)", "mij"),
("[U505b]", "VNW(pr,pron,obl,nadr,1,ev)", "mezelf, mijzelf"),
("[U505c]", "VNW(pr,pron,obl,red,1,ev)", "me"),
("[U505d]", "VNW(pr,pron,obl,vol,1,mv)", "ons"),
("[U505e]", "VNW(pr,pron,obl,nadr,1,mv)", "onszelf"),
("[U505f]", "VNW(pr,pron,obl,red,2v,getal)", "je"),
("[U505g]", "VNW(pr,pron,obl,nadr,2v,getal)", "jezelf"),
("[U505h]", "VNW(pr,pron,obl,vol,2,getal)", "u"),
("[U505i]", "VNW(pr,pron,obl,nadr,2,getal)", "uzelf"),
("[U506a]", "VNW(refl,pron,obl,red,3,getal)", "zich"),
("[U506b]", "VNW(refl,pron,obl,nadr,3,getal)", "zichzelf"),
("[U507a]", "VNW(recip,pron,obl,vol,persoon,mv)", "elkaar, mekaar, elkander"),
("[U508a]", "VNW(recip,pron,gen,vol,persoon,mv)", "elkaars, mekaars, elkanders"),
("[U509a]", "VNW(bez,det,stan,vol,1,ev,prenom,zonder,agr)", "mijn paard(en)"),
("[U509b]", "VNW(bez,det,stan,vol,1,ev,prenom,met-e,rest)", "mijne heren"),
("[U509c]", "VNW(bez,det,stan,red,1,ev,prenom,zonder,agr)", "m’n paard(en)"),
("[U509d]", "VNW(bez,det,stan,vol,1,mv,prenom,zonder,evon)", "ons paard"),
("[U509e]", "VNW(bez,det,stan,vol,1,mv,prenom,met-e,rest)", "onze paarden"),
("[U509f]", "VNW(bez,det,stan,vol,2,getal,prenom,zonder,agr)", "uw paard(en)"),
("[U509g]", "VNW(bez,det,stan,vol,2,getal,prenom,met-e,rest)", "uwe heiligheid"),
("[U509h]", "VNW(bez,det,stan,vol,2v,ev,prenom,zonder,agr)", "jouw paard(en)"),
("[U509i]", "VNW(bez,det,stan,red,2v,ev,prenom,zonder,agr)", "je paard(en)"),
("[U509j]", "VNW(bez,det,stan,nadr,2v,mv,prenom,zonder,agr)", "jullie paard(en)"),
("[U509k]", "VNW(bez,det,stan,vol,3,ev,prenom,zonder,agr)", "zijn paard(en), haar kind"),
("[U509l]", "VNW(bez,det,stan,vol,3m,ev,prenom,met-e,rest)", "zijne excellentie"),
("[U509m]", "VNW(bez,det,stan,vol,3v,ev,prenom,met-e,rest)", "hare majesteit"),
("[U509n]", "VNW(bez,det,stan,red,3,ev,prenom,zonder,agr)", "z’n paard"),
("[U509o]", "VNW(bez,det,stan,vol,3,mv,prenom,zonder,agr)", "hun paarden"),
("[U509p]", "VNW(bez,det,stan,vol,3p,mv,prenom,met-e,rest)", "hunne"),
("[U509q]", "VNW(bez,det,stan,red,3,getal,prenom,zonder,agr)", "’r paard, d’r paard"),
("[T510a]", "VNW(bez,det,gen,vol,1,ev,prenom,zonder,evmo)", "mijns inziens"),
("[U510b]", "VNW(bez,det,gen,vol,1,ev,prenom,met-e,rest)", "een mijner vrienden"),
("[T510c]", "VNW(bez,det,gen,vol,1,mv,prenom,met-e,evmo)", "onzes inziens"),
("[U510d]", "VNW(bez,det,gen,vol,1,mv,prenom,met-e,rest)", "een onzer vrienden"),
("[U510e]", "VNW(bez,det,gen,vol,2,getal,prenom,zonder,evmo)", "uws"),
("[U510f]", "VNW(bez,det,gen,vol,2,getal,prenom,met-e,rest)", "een uwer vrienden"),
("[U510g]", "VNW(bez,det,gen,vol,2v,ev,prenom,met-e,rest)", "een jouwer vrienden"),
("[U510h]", "VNW(bez,det,gen,vol,3,ev,prenom,zonder,evmo)", "zijns inziens"),
("[U510i]", "VNW(bez,det,gen,vol,3,ev,prenom,met-e,rest)", "een zijner vrienden"),
("[T510j]", "VNW(bez,det,gen,vol,3v,ev,prenom,zonder,evmo)", "haars inziens"),
("[U510k]", "VNW(bez,det,gen,vol,3v,ev,prenom,met-e,rest)", "een harer vrienden"),
("[U510l]", "VNW(bez,det,gen,vol,3p,mv,prenom,zonder,evmo)", "huns inziens"),
("[U510m]", "VNW(bez,det,gen,vol,3p,mv,prenom,met-e,rest)", "een hunner vrienden"),
("[T511a]", "VNW(bez,det,dat,vol,1,ev,prenom,met-e,evmo)", "te mijnen huize"),
("[T511b]", "VNW(bez,det,dat,vol,1,ev,prenom,met-e,evf)", "te mijner ere"),
("[T511c]", "VNW(bez,det,dat,vol,1,mv,prenom,met-e,evmo)", "te onzen behoeve"),
("[T511d]", "VNW(bez,det,dat,vol,1,mv,prenom,met-e,evf)", "te onzer ere"),
("[U511e]", "VNW(bez,det,dat,vol,2,getal,prenom,met-e,evmo)", "te uwen behoeve"),
("[U511f]", "VNW(bez,det,dat,vol,2,getal,prenom,met-e,evf)", "te uwer ere"),
("[T511g]", "VNW(bez,det,dat,vol,2v,ev,prenom,met-e,evf)", "te jouwer nagedachtenis"),
("[U511h]", "VNW(bez,det,dat,vol,3,ev,prenom,met-e,evmo)", "zijnen"),
("[U511i]", "VNW(bez,det,dat,vol,3,ev,prenom,met-e,evf)", "te zijner tijd"),
("[T511j]", "VNW(bez,det,dat,vol,3v,ev,prenom,met-e,evmo)", "haren"),
("[T511k]", "VNW(bez,det,dat,vol,3v,ev,prenom,met-e,evf)", "te harer ere"),
("[U511l]", "VNW(bez,det,dat,vol,3p,mv,prenom,met-e,evmo)", "hunnen"),
("[U511m]", "VNW(bez,det,dat,vol,3p,mv,prenom,met-e,evf)", "te hunner ere"),
("[U512h]", "VNW(bez,det,stan,vol,1,ev,nom,met-e,zonder-n)", "het mijne"),
("[U512i]", "VNW(bez,det,stan,vol,1,mv,nom,met-e,zonder-n)", "de onze"),
("[U512j]", "VNW(bez,det,stan,vol,2,getal,nom,met-e,zonder-n)", "het uwe"),
("[U512k]", "VNW(bez,det,stan,vol,2v,ev,nom,met-e,zonder-n)", "de jouwe"),
("[U512l]", "VNW(bez,det,stan,vol,3m,ev,nom,met-e,zonder-n)", "het zijne"),
("[U512m]", "VNW(bez,det,stan,vol,3v,ev,nom,met-e,zonder-n)", "de hare"),
("[U512n]", "VNW(bez,det,stan,vol,3p,mv,nom,met-e,zonder-n)", "het hunne"),
("[U512o]", "VNW(bez,det,stan,vol,1,ev,nom,met-e,mv-n)", "de mijnen"),
("[U512p]", "VNW(bez,det,stan,vol,1,mv,nom,met-e,mv-n)", "de onzen"),
("[U512q]", "VNW(bez,det,stan,vol,2,getal,nom,met-e,mv-n)", "de uwen"),
("[U512r]", "VNW(bez,det,stan,vol,2v,ev,nom,met-e,mv-n)", "de jouwen"),
("[U512s]", "VNW(bez,det,stan,vol,3m,ev,nom,met-e,mv-n)", "de zijnen"),
("[U512t]", "VNW(bez,det,stan,vol,3v,ev,nom,met-e,mv-n)", "de haren"),
("[U512u]", "VNW(bez,det,stan,vol,3p,mv,nom,met-e,mv-n)", "de hunnen"),
("[T513a]", "VNW(bez,det,dat,vol,1,ev,nom,met-e,zonder-n)", "te mijnent"),
("[T513b]", "VNW(bez,det,dat,vol,1,mv,nom,met-e,zonder-n)", "ten onzent"),
("[U513c]", "VNW(bez,det,dat,vol,2,getal,nom,met-e,zonder-n)", "ten uwent"),
("[T513d]", "VNW(bez,det,dat,vol,3m,ev,nom,met-e,zonder-n)", "te zijnent"),
("[T513e]", "VNW(bez,det,dat,vol,3v,ev,nom,met-e,zonder-n)", "ten harent"),
("[U513f]", "VNW(bez,det,dat,vol,3p,mv,nom,met-e,zonder-n)", "ten hunnent"),
("[U514a]", "VNW(vrag,pron,stan,nadr,3o,ev)", "watte"),
("[U515a]", "VNW(betr,pron,stan,vol,persoon,getal)", "de man die daar staat"),
("[U515b]", "VNW(betr,pron,stan,vol,3,ev)", "het kind dat je daar ziet"),
("[U515c]", "VNW(betr,det,stan,nom,zonder,zonder-n)", "hetgeen je daar ziet, het feest tijdens hetwelk"),
("[U515d]", "VNW(betr,det,stan,nom,met-e,zonder-n)", "op hetgene de gemeente doet"),
("[T516a]", "VNW(betr,pron,gen,vol,3o,ev)", "het warenhuis welks directeur hem een baan had aangeboden"),
("[U516b]", "VNW(betr,pron,gen,vol,3o,getal)", "de kathedraal welker gewelven"),
("[U517a]", "VNW(vb,pron,stan,vol,3p,getal)", "wie gaat er mee"),
("[U517b]", "VNW(vb,pron,stan,vol,3o,ev)", "wat ik niet begrijp is"),
("[U518a]", "VNW(vb,pron,gen,vol,3m,ev)", "wiens hoed is dit"),
("[U518b]", "VNW(vb,pron,gen,vol,3v,ev)", "de vrouw wier hoed daar hangt"),
("[U518c]", "VNW(vb,pron,gen,vol,3p,mv)", "de studenten tegen wier houding ..."),
("[U519a]", "VNW(vb,adv-pron,obl,vol,3o,getal)", "waar ga je naartoe, de trein waar we op staan te wachten"),
("[U520a]", "VNW(excl,pron,stan,vol,3,getal)", "wat een dwaasheid, wat kan jij liegen zeg"),
("[U521a]", "VNW(vb,det,stan,prenom,zonder,evon)", "welk kind"),
("[U521b]", "VNW(vb,det,stan,prenom,met-e,rest)", "welke kinderen"),
("[U522a]", "VNW(vb,det,stan,nom,met-e,zonder-n)", "welke vind jij de mooiste"),
("[U523a]", "VNW(excl,det,stan,vrij,zonder)", "welk een dwaasheid"),
("[U524a]", "VNW(aanw,pron,stan,vol,3o,ev)", "dat, dit, zulks"),
("[U524b]", "VNW(aanw,pron,stan,nadr,3o,ev)", "datte, ditte"),
("[U524c]", "VNW(aanw,pron,stan,vol,3,getal)", "die"),
("[T525a]", "VNW(aanw,pron,gen,vol,3m,ev)", "diens voorkeur"),
("[T525b]", "VNW(aanw,pron,gen,vol,3o,ev)", "en dies meer"),
("[U526a]", "VNW(aanw,adv-pron,obl,vol,3o,getal)", "hier, daar"),
("[U527a]", "VNW(aanw,adv-pron,stan,red,3,getal)", "d’r, het niet-kwantitatieve ‘er’"),
("[U528a]", "VNW(aanw,det,stan,prenom,zonder,evon)", "dat boek, dit dier, ginds bos, zulk hout"),
("[U528b]", "VNW(aanw,det,stan,prenom,zonder,rest)", "die stoel(en)"),
("[U528c]", "VNW(aanw,det,stan,prenom,zonder,agr)", "zo’n boek(en)"),
("[U528d]", "VNW(aanw,det,stan,prenom,met-e,rest)", "deze man, gene zijde, gindse heuvel, zulke balken"),
("[U529a]", "VNW(aanw,det,gen,prenom,met-e,rest)", "een dezer dagen, de notulen dier vergadering"),
("[T530a]", "VNW(aanw,det,dat,prenom,met-e,evmo)", "te dien tijde"),
("[T530b]", "VNW(aanw,det,dat,prenom,met-e,evf)", "in dier voege"),
("[U531b]", "VNW(aanw,det,stan,nom,met-e,zonder-n)", "deze, gene, datgene, degene, diegene"),
("[U531c]", "VNW(aanw,det,stan,nom,met-e,mv-n)", "dezen, genen, degenen, diegenen"),
("[T532a]", "VNW(aanw,det,gen,nom,met-e,zonder-n)", "schrijver dezes, de twintigste dezer"),
("[T533a]", "VNW(aanw,det,dat,nom,met-e,zonder-n)", "dat is dan bij dezen beslist"),
("[U534a]", "VNW(aanw,det,stan,vrij,zonder)", "zulk een vreemde gedachte"),
("[U535a]", "VNW(onbep,pron,stan,vol,3p,ev)", "alleman, (n)iemand, iedereen, elkeen, menigeen"),
("[U535b]", "VNW(onbep,pron,stan,vol,3o,ev)", "alles, (n)iets, niks, wat, zoiets"),
("[U536a]", "VNW(onbep,pron,gen,vol,3p,ev)", "allemans, andermans, (n)iemands, (een)ieders"),
("[U537a]", "VNW(onbep,adv-pron,obl,vol,3o,getal)", "(n)ergens, overal"),
("[U538a]", "VNW(onbep,adv-pron,gen,red,3,getal)", "het kwantitatieve ‘er’"),
("[U539a]", "VNW(onbep,det,stan,prenom,zonder,evon)", "elk huis, ieder kind, enig benul, een enkel woord, sommig bier"),
("[U539b]", "VNW(onbep,det,stan,prenom,zonder,agr)", "geen kind(eren), menig politicus"),
("[U539c]", "VNW(onbep,det,stan,prenom,met-e,evz)", "elke hond, iedere keer, ene mijnheer X, menige"),
("[U539d]", "VNW(onbep,det,stan,prenom,met-e,mv)", "ettelijke"),
("[U539e]", "VNW(onbep,det,stan,prenom,met-e,rest)", "sommige, enige, enkele"),
("[U539f]", "VNW(onbep,det,stan,prenom,met-e,agr)", "alle mensen, hoop, vee"),
("[T540a]", "VNW(onbep,det,gen,prenom,met-e,mv)", "proletariers aller landen"),
("[T541a]", "VNW(onbep,det,dat,prenom,met-e,evmo)", "te allen prijze"),
("[T541b]", "VNW(onbep,det,dat,prenom,met-e,evf)", "te eniger tijd"),
("[U542a]", "VNW(onbep,grad,stan,prenom,zonder,agr,basis)", "veel plezier, weinig geld"),
("[U542b]", "VNW(onbep,grad,stan,prenom,met-e,agr,basis)", "het vele plezier, de weinige toeschouwers"),
("[U542c]", "VNW(onbep,grad,stan,prenom,met-e,mv,basis)", "beide mannen"),
("[U542d]", "VNW(onbep,grad,stan,prenom,zonder,agr,comp)", "meer tijd, minder werk"),
("[U542e]", "VNW(onbep,grad,stan,prenom,met-e,agr,sup)", "de meeste mensen, het minste tijd"),
("[U542f]", "VNW(onbep,grad,stan,prenom,met-e,agr,comp)", "in mindere mate"),
("[U543a]", "VNW(onbep,det,stan,nom,met-e,mv-n)", "allen, sommigen, enkelen, de enen"),
("[U543b]", "VNW(onbep,det,stan,nom,met-e,zonder-n)", "het ´ene ... het andere"),
("[U543c]", "VNW(onbep,det,stan,nom,zonder,zonder-n)", "het ´e´en en ander"),
("[T544a]", "VNW(onbep,det,gen,nom,met-e,mv-n)", "met aller instemming"),
("[U545a]", "VNW(onbep,grad,stan,nom,met-e,zonder-n,basis)", "het weinige"),
("[U545b]", "VNW(onbep,grad,stan,nom,met-e,mv-n,basis)", "velen, weinigen, beiden"),
("[U545d]", "VNW(onbep,grad,stan,nom,met-e,zonder-n,sup)", "het minste wat je kan zeggen, de meeste"),
("[U545e]", "VNW(onbep,grad,stan,nom,met-e,mv-n,sup)", "de minsten, de meesten"),
("[U545f]", "VNW(onbep,grad,stan,nom,zonder,mv-n,dim)", "met z’n beidjes"),
("[T546a]", "VNW(onbep,grad,gen,nom,met-e,mv-n,basis)", "tot veler verbazing, met beider instemming"),
("[U547a]", "VNW(onbep,det,stan,vrij,zonder)", "ze kregen elk/ieder/allebei een bal, al die mensen"),
("[U548a]", "VNW(onbep,grad,stan,vrij,zonder,basis)", "dat is te weinig, veel groter"),
("[U548b]", "VNW(onbep,grad,stan,vrij,zonder,sup)", "de minst gevraagde, de meest gezochte"),
("[U548c]", "VNW(onbep,grad,stan,vrij,zonder,comp)", "minder werken, meer slapen"),
("[T601]", "LID(bep,stan,evon)", "het kind, in ’t geniep"),
("[T602]", "LID(bep,stan,rest)", "de hond(en), de kinderen"),
("[T603]", "LID(bep,gen,evmo)", "des duivels, ’s avonds,"),
("[U604]", "LID(bep,gen,rest)", "der Nederlandse taal, der Belgen"),
("[T605]", "LID(bep,dat,evmo)", "op den duur, om den brode"),
("[T606]", "LID(bep,dat,evf)", "in der minne"),
("[T607]", "LID(bep,dat,mv)", "die in den hemelen zijt"),
("[U608]", "LID(onbep,stan,agr)", "een kind, een mensen dat er waren"),
("[T609]", "LID(onbep,gen,evf)", "de kracht ener vrouw"),
("[T701]", "VZ(init)", "met een lepeltje, met Jan in het hospitaal, met zo te roepen"),
("[T702]", "VZ(fin)", "liep de trap af, bij de beesten af, speelt het bandje af"),
("[T703]", "VZ(versm)", "ten strijde, ten hoogste, ter plaatse"),
("[T801]", "VG(neven)", "Jan en Peter; en toen gebeurde het"),
("[T802]", "VG(onder)", "omdat ze zich niet goed voelt"),
("[T901]", "BW()", "gisteren, nu, niet, nog, al, hoe"),
("[T001]", "TSW()", "oei, amai, uh, hoera"),
("[R101]", "N(soort,dial)", "bompa*d"),
("[R102]", "N(eigen,dial)", "@@"),
("[R201)", "ADJ(dial)", "ne*d langen*d toot*d"),
("[R301]", "WW(dial)", "’k zen*d nie*d thuis, ’k hem*d gee*d geld"),
("[R401]", "TW(hoofd,dial)", ""),
("[R402)", "TW(rang,dial)",  "den*d elfste*d"),
("[R501]", "VNW(pers,pron,dial)", "kom de*d gij mee, ’k heb ulie*d gezien"),
("[R502]", "VNW(refl,pron,dial", ""),
("[R503)", "VNW(recip,pron,dial)", "we zien malkanderen*d niet veel"),
("[R504]", "VNW(bez,det,dial)", "hij heeft z’ne*d frak*d vergeten"),
("[R505]", "VNW(vrag,pron,dial)", ""),
("[R506)", "VNW(vrag,det,dial)", ""),
("[R507]", "VNW(betr,pron,dial)", ""),
("[R508]", "VNW(betr,det,dial)", ""),
("[R509]", "VNW(excl,pron,dial)",""),
("[R510]", "VNW(excl,det,dial)", ""),
("[R511]", "VNW(aanw,pron,dial)", ""),
("[R512]", "VNW(aanw,det,dial)", "diejen*d boek, dees*d week"),
("[R513]", "VNW(onbep,pron,dial)", "z’ hebben iet*d gezien"),
("[R514]", "VNW(onbep,det,dial)", "ze kan elken*d dag vertrekken"),
("[R601]", "LID(bep,dial)", "het gevecht met den*dbeer"),
("[R602]", "LID(onbep,dial)", "nen*d toffe gast, ne*d vieze vent"),
("[R701]", "VZ(init,dial)", "me*d veel geduld"),
("[R702]", "VZ(fin,dial)", ""),
("[R801)", "VG(neven,dial)", ""),
("[R802]", "VG(onder,dial)", "’t schijnt da*d ze nie*d kunnen komen"),
("[R901]", "BW(dial)", "efkes*d, nie*d"),
("[R001]", "TSW(dial)", "neeje*d, wablieft*d"),
("[T002]", "SPEC(afgebr)", "uitge*a, binnen-"),
("[T003]", "SPEC(onverst)", "ggg, xxx, Xxx"),
("[T004]", "SPEC(vreemd)", "whatever*v, ad, hoc, wishful"),
("[T005]", "SPEC(deeleigen)", "Den, Haag, New, York"),
("[T006]", "SPEC(meta)", "(het woord) homosexueel"),
("[T008]", "SPEC(comment)", "voor commentaren"),
("[T009]", "SPEC(achter)", "voor achtergrondgeluid"),
("[T010]", "SPEC(afk)", "d.w.z., dwz, enz., EHBO"),
("[T011]", "SPEC(symb)", "@, %, NaCl, =, emoticons"),
("[T007]", "LET()", "., ..., ?")]

legal_DCOI_postags = {}
for el in DCOITRIPLES:
  (code, tag, ex) = el
  legal_DCOI_postags[tag]=code
  
#for el in legal_DCOI_postags:
#  print (el, legal_DCOI_postags[el])



# Van Eynde 2005 p.72, sec 4.1
#
##[P01] TOKENTYPE = woord, speciaal, leesteken.
##[P02] POS = substantief, adjectief, werkwoord, telwoord, voornaamwoord, lidwoord, voorzetsel, voegwoord, bijwoord, tussenwerpsel.
##[P03] NTYPE = soortnaam, eigennaam.
##[P04] GETAL = getal (enkelvoud, meervoud).
##[P05] GRAAD = basis, comparatief, superlatief, diminutief.
##[P06] GENUS = genus (zijdig (masculien, feminien), onzijdig).
##[P07] NAAMVAL = standaard (nominatief, oblique), bijzonder (genitief, datief).
##[P08] POSITIE = prenominaal, nominaal, postnominaal, vrij.
##[P09] BUIGING = zonder, met-e, met-s.
##[P10] GETAL-N = zonder-n, meervoud-n.
##[P11] WVORM = persoonsvorm, buigbaar (infinitief, onvdw, voltdw).
##[P12] PVTIJD = tegenwoordig, verleden, conjunctief.
##[P13] PVAGR = enkelvoud, meervoud, met-t.
##[P14] NUMTYPE = hoofdtelwoord, rangtelwoord.
##[P15] VWTYPE = pr (persoonlijk, reflexief), reciprook, bezittelijk, vb (vragend, betrekkelijk), exclamatief, aanwijzend, onbepaald.
##[P16] PDTYPE = pronomen (adv-pronomen), determiner (gradeerbaar).
##[P17] PERSOON = persoon (1, 2 (2v, 2b), 3 (3p (3m, 3v), 3o)).
##[P18] STATUS = vol, gereduceerd, nadruk.
##[P19] NPAGR = agr (evon, rest (evz, mv)), agr3 (evmo, rest3 (evf, mv)).
##[P20] LWTYPE = bepaald, onbepaald.
##[P21] VZTYPE = initieel (versmolten), finaal.
##[P22] CONJTYPE = nevenschikkend, onderschikkend.
#[P23] SPECTYPE = afgebroken, onverstaanbaar, vreemd, deeleigen, meta, commentaar, achtergrond, afkorting, symbool.



attvals = [  ('pt', ['adj', 'bw', 'let', 'lid', 'mwu', 'n', 'na', 'spec', 'tsw', 'tw', 'vg', 'vnw', 'vz', 'ww']),  #na is not official may have to be removed add spec?
             ('wvorm', ['buigbaar', 'inf', 'od', 'pv', 'vd' ]),
             ('pvagr', ['ev', 'met-t', 'mv']),
             ('pvtijd', ['conj', 'tgw', 'verl']),
             ('positie', ['prenom', 'nom', 'vrij']),
             ('buiging', ['zonder', 'met-e']),
             ('getal-n', ['zonder-n, mv-n']),
             ('ntype', ['soort', 'eigen']),
             ('getal', ['getal', 'ev', 'mv']),
             ('graad', ['basis', 'comp', 'sup', 'dim']),
             ('genus', ['genus', 'zijd', 'masc', 'fem', 'onz']),
             ('naamval', ['stan', 'nomin', 'obl', 'bijz', 'gen', 'dat']),
             ('numtype', ['hoofd', 'rang']),
             ('vwtype', ['pr', 'pers', 'refl', 'recip', 'bez', 'vb', 'vrag', 'betr', 'excl', 'aanw', 'onbep']),
             ('pdtype', ['pron', 'adv-pron', 'det', 'grad']),
             ('persoon', ['1', '2', '2v', '2b', '3', '3p', '3m', '3v', '3o']),
             ('stat', ['vol', 'red', 'nadr']),
             ('npagr', ['agr', 'evon', 'rest', 'evz', 'mv', 'agr3',  'evmo', 'rest3', 'evf', 'mv']),
             ('lwtype', ['bep', 'onbep']),
             ('vztype', ['init', 'versm', 'fin']),
             ('conjtype', ['neven', 'onder']),
             ('spectype', ['afgebr', 'onverst', 'vreemd', 'deeleigen', 'meta', 'comment', 'achter', 'afk', 'symb'])





  #to be extended
]

# DCOI Declarations Van Eynde Juli 2005 esp p. 73
class Declaration:
    def __init__(self, id, condlist, atts):
        self.id = id
        self.condlist = condlist
        self.atts = atts


declarations = {
    Declaration('D00', [('TOKENTYPE', 'woord')], ['pt']),
    Declaration('D01', [('pt', 'n')], ['ntype', 'getal', 'graad']),
    Declaration('D02', [('pt', 'n'), ('getal', 'ev')],  ['naamval']),
    Declaration('D03', [('pt', 'n'), ('getal', 'ev'), ('naamval', 'standaard')],  ['genus']),
    Declaration('D04', [('pt', 'adj')], ['positie', 'graad', 'buiging']),
    Declaration('D05', [('positie', 'nom')], ['getal-n']),
    Declaration('D06', [('pt', 'adj'), ('positie', 'nom'), ('buiging', 'met-e'), ('getal-n', 'zonder-n')],['naamval']),
    Declaration('D07', [('pt', 'adj'), ('positie', 'prenom'), ('buiging', 'met-e')], ['naamval']),
    Declaration('D08', [('pt', 'ww')], ['wvorm']),
    Declaration('D09', [('wvorm', 'pv')], ['pvtijd', 'pvagr']),
    #Declaration('D10', [('wvorm', 'buigbaar')], ['positie', 'buiging']),
    Declaration('D10a', [('wvorm', 'inf')], ['positie', 'buiging']),
    Declaration('D10b', [('wvorm', 'vd')], ['positie', 'buiging']),
    Declaration('D10c', [('wvorm', 'od')], ['positie', 'buiging']),
    Declaration('D11', [('pt', 'tw')], ['numtype', 'positie']),
    Declaration('D12', [('numtype', 'hoofd'), ('positie', 'nom')], ['graad']),
    Declaration('D13', [('pt', 'tw'), ('positie', 'prenom')], ['naamval']),
    Declaration('D14', [('pt', 'vnw')], ['vwtype', 'pdtype', 'naamval']),
    Declaration('D15', [('pdtype', 'pron')], ['status', 'persoon', 'getal']),
    Declaration('D16', [('vwtype', 'pers'), ('naamval','stan'), ('persoon', '3',), ('getal', 'ev')],  ['genus']),
    Declaration('D17', [('pdtype', 'det')], ['positie', 'buiging']),
    Declaration('D18', [('pdtype','det'), ('positie','prenom')],['npagr']),
    Declaration('D19', [('pdtype', 'grad')], ['graad']),
    Declaration('D20', [('vwtype', 'bez')], ['status', 'persoon','getal']),
    Declaration('D21', [('pt', 'lid')], ['lwtype', 'naamval', 'npagr']),
    Declaration('D22', [('pt', 'vz')], ['vztype']),
    Declaration('D23', [('pt', 'vw')], ['conjtype']),
    Declaration('D24', [('TOKENTYPE', 'speciaal')],['spectype'])
}

declarationstobeignored = ['D00', 'D24']

def getdependencies(declarations):
    result = defaultdict(list)
    for declaration in declarations:
        if declaration.id not in declarationstobeignored:
            for att in declaration.atts:
                result[att].append(declaration.condlist)
    return result

def getattdependees(declarations):
    result = defaultdict(set)
    for declaration in declarations:
        if declaration.id not in declarationstobeignored:
             for att, _ in declaration.condlist:
                 result[att] = result[att].union(declaration.atts)
    return result

def testdependencies():
    testdependencies = getdependencies(declarations)
    for att in testdependencies:
        print(att)
        for clist in testdependencies[att]:
            print('--{}'.format(clist))

    testdependees = getattdependees(declarations)
    for att in testdependees:
        print(att, testdependees[att])

if __name__ == '__main__':
    testdependencies()

#everything below this should disappear

dependencies = {}
dependencies = getdependencies(declarations)
attdependees = set()
attdependees = getattdependees(declarations)

# dependencies[a] = (b,c) means: a is only present / only has a sensible value if attribute b has values c
# DCOI Van Eynde Juli 2005 esp p. 73

# er zijn soms afahnkelijkheden die samen moeten gelden, en som waarvan een van de geldt (positie)
#dependencies['pvagr'] = ('wvorm', 'pv')   #D09, p. 10
#dependencies['pvtijd'] = ('wvorm', 'pv')  #D09, p. 10
#dependencies['wvorm'] = ('pt', 'ww')      #D08, p. 10
#dependencies['positie'] = ('wvorm', 'inf')
#dependencies['getal-n'] = ('positie', 'nom') #D05, p. 27
#dependencies['vwtype'] = ('pt', 'vnw') #D14, p. 39
#dependencies['pdtype'] = ('pt', 'vnw') #D14, p. 39
#dependencies['naamval'] = ('pt', 'vnw') #D14, p. 39


