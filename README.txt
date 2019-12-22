PAGERANK Marc Llort Maulion (marc.llort)


En aquesta pràctica implementarem l'algorisme PageRank amb la finalitat de ordenar les webs donades al fitxer "gr0.California.txt.
En el fitxer trobarem un graph de les webs, on trobarem els diferents "links" de els nodes de cada web.

Per solucionar el problema, ens era necessari completar el fitxer "processPageRank.py", implementant la forma en que PageRank recorrerà les webs i farà els linkatges entre les diferents webs.

El enfoc que he seguit per solucionar el problema ha sigut:
	Primer, recórrer tots els links (j) en un bucle, i dins d'aquest, fer un segon bucle el qual per cada in-link, vaig acumulant el resultat de Rj alhora que dividint-lo entre el seu propi out-degree.
	Aquest resultat l'emmagatzemo en una variable que té la dimensió total de links del fitxer d'entrada.
	
	Un cop hem iterat per tots els inlinks, realitzo la multiplicació per Beta fora del bucle, de tal manera aconsegueixo optimitzar una mica el càlcul, ja que no s'executa cada cop.

	El següent pas, és calcular la "s". Per fer-ho, simplement realitzo un sum de els resultats obtinguts anteriorment. Poso la variable "t" a 0, per poder tornar a iterar per els inlink per últim cop.

	En aquest últim pas, recalculem el resultat final amb la variable "s" que acabem de calcular.

Alhora d'executar el programa, he provat amb diferents betas, i podem veure que com menor es el valor de la beta, més ràpidament s'executa el programa. 
Això és degut a que depenent de beta, fa més o menys iteracions ja que tarda més/menys temps a convergir. Com més alta sigui la beta, més iteracions realitzarà el programa.

Un cop finalitzada la pràctica, m'he adonat que en un principi no tenia gaire clar quin era el funcionament de PageRank, però gràcies a anar jugant amb diferents valors i diferents formes de solucionar 
el problema, he entès que es tracta d'una eina molt potent per l'extracció de dades. No menys important, he après els bàsics de Python, un llenguatge molt important per les tecnologies de AI, machine learning i molt més.
