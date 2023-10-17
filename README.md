# filler-text-generator
Generate unique english-like gibberish for use as filler text. Similar in concept to the use of "Lorem Ipsum", but randomly generated from english syllables.



This script uses a pre-defined set of the most common english syllables to generate english-sounding words. 
It also has quite a bit of additional logic included to add variation to the generated text, and create more natural looking text. 

Run it in a terminal to see a demo, or import it to use in another script. 
This is mainly a silly little idea I had, but it may come in handy some day. 


# use:


The main function you'd likely use is the generate function, which returns a string of text that is a specific number of characters long. 
Here's a simple example:
```
import filler_text
print(filler_text.generate(1000))
```
output:
```
"tendfish varcor suplayber westers Ly newcir ic lectnet auest wilsim ber mu cuscent als toncitties den sionsbe retivecir standtry greattomcu." 

Por, obeastpa tiestic sospar; auvissunsouth hightlememful letple mentsicre Set mem rec ussanla tyinwrit. Mensend culments genaat com ogo tionairob tedgan ag, turounder pariederwini gan fac genship nalvis. Ish pe southfish long gencal sion, lofect net east lessers manketat letpress cen ent fin. Centnore huntho ting ofply oustic dis entur ver mials or anshiptem larments new tendern es malro repence Clepronear tlearectam tive tend fixrep fac. Lectaiully sioncaptle al cy ageselfingtry sis ed roci opbytev way sen end agli, repcal trayi, edmal mile se subgensonsa tewest. End agprefor logroals standishday trawhere setmentsly low. Hapat ence estacnu bortelvi eni har cyturehead plepressatex, elusmoth mulsilowta sionsevmis calte glelect, der tedtagrand. Tors basent sensa amlarral ven betfac sent grandion ings fimal ferread grandwhereme ence fa missec.
```

The generate function is the most complex function in the script, and should be suitable for most uses.


There is also a gen_word and gen_sentence functions:
```
print(filler_text.gen_word())
print(filler_text.gen_sentence())
```
output:
```
octal
Calper muacprac low ble facsand nesstalob tray, lead anlow tion leadness en ic tel, ings subto iesteish play rytrycatpopress alper.
```
