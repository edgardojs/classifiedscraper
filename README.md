# Clasificadosonline.com scraper
Clasificadosonline.com is a popular webpage in Puerto Rico to look for jobs. This currently takes just an item from a list but you can edit at your liking. I hope this can give anyone an idea of what a few lines of Python can do.

Required imports:

* BS4 (BeautifulSoup)
* requests

Usage: 

Each address is saved in a string which is used by requests to get url information. There are various categories in which the page reacts provided by these variables:

                jobs_cat = "JobsCat=%{}".format(25) 
                txkey_cat = "&txkey={}".format("")
                pueblo_cat = "&Pueblo={}".format(pueblo_list[8])
                submit_cat = "&Submit=Buscar+-+GO"
                offset_cat = "&offset=".format("")
                
If you modify any of these variables either by changing the JobsCat=& txkey pueblo and offset. Submit is the "post" and I advice not to touch unless you know what you're doing, other variables can be modified through "{}".format().


There are two parsers:

single_page_parser()
The default is the single parse function. The pueblo_cat decides municipality or area. Change the number inside pueblo_list[] to access another name in the list of towns and areas


multi_page_parser() 
!! Experimental use at your own risk. Comment the line on #single_page_parser, uncomment and align for multiple page scraping. Please do not abuse of this feature. Uses the entire pueblo_list[] for scraping

Index list:

For now using control+f to get the desired town would get you to the list 


0:Area Central
1:Area Este
2:Area Metro
3:Area Norte
4:Area Oeste
5:Area Sur
6:Adjuntas
7:Aguada
8:Aguadilla
9:Aguas Buenas
10:Aibonito
11:Anasco
12:Arecibo
13:Arroyo
14:Barceloneta
15:Barranquitas
16:Bayamon
17:Cabo Rojo
18:Caguas
19:Camuy
20:Canovanas
21:Carolina
22:Catano
23:Cayey
24:Ceiba
25:Ciales
26:Cidra
27:Coamo
28:Comerio
29:Corozal
30:Culebra
31:Dorado
32:Fajardo
33:Florida
34:Guanica
35:Guayama
36:Guayanilla
37:Guaynabo
38:Gurabo
39:Hatillo
40:Hormigueros
41:Humacao
42:Isabela
43:Jayuya
44:Juana Diaz
45:Juncos
46:Lajas
47:Lares
48:Las Marias
49:Las Piedras
50:Loiza
51:Luquillo
52:Manati
53:Maricao
54:Maunabo
55:Mayaguez
56:Moca
57:Morovis
58:Naguabo
59:Naranjito
60:Orocovis
61:Patillas
62:Penuelas
63:Ponce
64:Quebradillas
65:Rincon
66:Rio Grande
67:Sabana Grande
68:Salinas
69:San German
70:San Juan
71:San Lorenzo
72:San Sebastian
73:Santa Isabel
74:Toa Alta
75:Toa Baja
76:Trujillo Alto
77:Utuado
78:Vega Alta
79:Vega Baja
80:Vieques
81:Villalba
82:Yabucoa
83:Yauco


Output:
![alt text](https://imgur.com/pY91fZL)
jobList.txt should showcase the job name and page link. 
