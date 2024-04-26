import sys ,os ,time ,signal ,webbrowser ,platform ,subprocess #line:1
def signal_handler (OO0OOO00O000000O0 ,O000OO0OO0OOOO000 ):#line:3
		AKA ()#line:4
		LOGO ()#line:5
		print ('\033[1;m [\033[1;31mX\033[1;m] You pressed Ctrl+C!')#line:6
		time .sleep (2 )#line:7
		QuitterMENU ()#line:8
signal .signal (signal .SIGINT ,signal_handler )#line:9
def AKA ():#line:11
	if os .name =='nt':#line:12
            os .system ('cls')#line:13
	else :#line:14
            os .system ('clear')#line:15
def LOGO ():#line:17
	AKA ()#line:18
	print ("""

╔════════════════════════════════════════════════════╗
           _           _____        __      
     /\   | |         |_   _|      / _|     
    /  \  | | ____ _    | |  _ __ | |_ ___  
   / /\ \ | |/ / _` |   | | | '_ \|  _/ _ \ 
  / ____ \|   < (_| |  _| |_| | | | || (_) |
 /_/    \_\_|\_\__,_| |_____|_| |_|_| \___/ 
                                                
    || \033[1;31mDev\033[1;m \033[1;34mBy\033[1;m Ctjraka || \033[1;33mVersion:\033[1;32m 1\033[1;35m ||
╚════════════════════════════════════════════════════╝

     """)#line:32
def menu ():#line:34
	LOGO ()#line:35
	time .sleep (1 )#line:36
	print ("""
╔════════════════════════════════════════════════════╗
\033[1;33m    	1.\033[1;m Name Tools
\033[1;33m     	2.\033[1;m Phone number Tools
\033[1;33m     	3.\033[1;m Chercher les mort
\033[1;33m     	4.\033[1;m IP Tools
\033[1;33m     	5.\033[1;m Gun
\033[1;33m     	6.\033[1;m DarkWeb
\033[1;36m      aka.\033[1;m Voir qui a crée le script
╚════════════════════════════════════════════════════╝
	""")#line:47
	OOO0OO0O00O0O0000 =input ("\033[1;35m  Select:\033[1;m ")#line:49
	if OOO0OO0O00O0O0000 =="1":#line:50
         ID ()#line:51
	elif OOO0OO0O00O0O0000 =="2":#line:52
		 PHONE ()#line:53
	elif OOO0OO0O00O0O0000 =="3":#line:54
		 DEAD ()#line:55
	elif OOO0OO0O00O0O0000 =="4":#line:56
		 IP ()#line:57
	elif OOO0OO0O00O0O0000 =="aka":#line:58
		AKA ()#line:59
		webbrowser .open ('https://github.com/akalpb')#line:60
		menu ()#line:61
	elif OOO0OO0O00O0O0000 =="6":#line:62
		AKA ()#line:63
		webbrowser .open ('https://t.me/Darkvwebfr')#line:64
		menu ()#line:65
	elif OOO0OO0O00O0O0000 =="5":#line:66
		AKA ()#line:67
		webbrowser .open ('https://guns.lol/akalpb')#line:68
		menu ()#line:69
	else :#line:70
		AKA ()#line:71
		LOGO ()#line:72
		print ("\033[1;31m[AkaBug]\033[1;m La sélection n'est pas valide !")#line:73
		time .sleep (3 )#line:74
		menu ()#line:75
def ID ():#line:77
	AKA ()#line:78
	LOGO ()#line:79
	time .sleep (1 )#line:80
	OOO0OO0000OO0OO00 =input (" Prénom:\033[1;m ")#line:81
	OO0OOOOO0O0OO0O0O =input ("\033[1;35m Nom de famille:\033[1;m ")#line:82
	print ("""\033[1;34m
╔════════════════════════════════════════════════════╗
 1. Pipl 	  10. Twitter
 2. Facebook      11. Beenverified
 3. Spokeo    	  12. Peoplelooker     
 4. Flickr        13. Myspace 
 5. Linkedin      14. Pagesjaunes   
 6. Google plus   15. Libramemoria
 7. Tumblr        16. Avis-de-deces	 
 8. Youtube       \033[1;33m00. All\033[1;34m
 9. Peekyou \033[1;m      
╚════════════════════════════════════════════════════╝
\033[1;36m    aka. About\033[1;31m    0. Quitter
╚════════════════════════════════════════════════════╝
		""")#line:98
	O00OO0OO0OO0OO0OO =input ("\033[1;35m D0xTr\033[0;31m@\033[1;35mck3r\033[1;m:~\033[1;34m/\033[1;m$\033[1;35m ")#line:99
	if O00OO0OO0OO0OO0OO =="1":#line:101
		AKA ()#line:102
		webbrowser .open ('https://pipl.com/search/?q='+OOO0OO0000OO0OO00 +'+'+OO0OOOOO0O0OO0O0O )#line:103
		time .sleep (2 )#line:104
		menu ()#line:105
	elif O00OO0OO0OO0OO0OO =="2":#line:106
		AKA ()#line:107
		webbrowser .open ('https://www.facebook.com/search/top/?init=quick&q='+OOO0OO0000OO0OO00 +' '+OO0OOOOO0O0OO0O0O )#line:108
		time .sleep (2 )#line:109
		menu ()#line:110
	elif O00OO0OO0OO0OO0OO =="3":#line:111
		AKA ()#line:112
		webbrowser .open ('https://www.spokeo.com/'+OOO0OO0000OO0OO00 +'-'+OO0OOOOO0O0OO0O0O )#line:113
		time .sleep (2 )#line:114
		menu ()#line:115
	elif O00OO0OO0OO0OO0OO =="4":#line:116
		AKA ()#line:117
		webbrowser .open ('https://www.flickr.com/search/people/?username='+OOO0OO0000OO0OO00 +' '+OO0OOOOO0O0OO0O0O )#line:118
		time .sleep (2 )#line:119
		menu ()#line:120
	elif O00OO0OO0OO0OO0OO =="5":#line:121
		AKA ()#line:122
		webbrowser .open ('https://fr.linkedin.com/pub/dir/'+OOO0OO0000OO0OO00 +'/'+OO0OOOOO0O0OO0O0O )#line:123
		time .sleep (2 )#line:124
		menu ()#line:125
	elif O00OO0OO0OO0OO0OO =="6":#line:126
		AKA ()#line:127
		webbrowser .open ('https://plus.google.com/s/'+OOO0OO0000OO0OO00 +' '+OO0OOOOO0O0OO0O0O +'/people')#line:128
		time .sleep (2 )#line:129
		menu ()#line:130
	elif O00OO0OO0OO0OO0OO =="7":#line:131
		AKA ()#line:132
		webbrowser .open ('https://www.tumblr.com/search/'+OOO0OO0000OO0OO00 +'+'+OO0OOOOO0O0OO0O0O )#line:133
		time .sleep (2 )#line:134
		menu ()#line:135
	elif O00OO0OO0OO0OO0OO =="8":#line:136
		AKA ()#line:137
		webbrowser .open ('http://www.youtube.com/results?search_query='+OOO0OO0000OO0OO00 +'+'+OO0OOOOO0O0OO0O0O )#line:138
		time .sleep (2 )#line:139
		menu ()#line:140
	elif O00OO0OO0OO0OO0OO =="9":#line:141
		AKA ()#line:142
		webbrowser .open ('https://www.peekyou.com/'+OOO0OO0000OO0OO00 +'_'+OO0OOOOO0O0OO0O0O )#line:143
		time .sleep (2 )#line:144
		menu ()#line:145
	elif O00OO0OO0OO0OO0OO =="10":#line:146
		AKA ()#line:147
		webbrowser .open ('https://twitter.com/search?f=users&vertical=default&q= '+OOO0OO0000OO0OO00 +' '+OO0OOOOO0O0OO0O0O )#line:148
		time .sleep (2 )#line:149
		menu ()#line:150
	elif O00OO0OO0OO0OO0OO =="11":#line:151
		AKA ()#line:152
		webbrowser .open ('https://www.beenverified.com/lp/e030ee/1/loading?utm_id=peekyou_Peekyou_Contact_Address_Results_Button&age=&bvid=&city=&fn='+OOO0OO0000OO0OO00 +'&ln='+OO0OOOOO0O0OO0O0O )#line:153
		time .sleep (2 )#line:154
		menu ()#line:155
	elif O00OO0OO0OO0OO0OO =="12":#line:156
		AKA ()#line:157
		webbrowser .open ('https://www.peoplelooker.com/lp/5ee6b8/1/loading?utm_id=peekyou_peekyou_PL_phonebook_widget_web&fn='+OOO0OO0000OO0OO00 +'&ln='+OO0OOOOO0O0OO0O0O +'&city=&state=&age=&bvid=&utm_source=peekyou&utm_medium=channel_partner&utm_campaign=peekyou_PL_phonebook_widget_web&utm_content=static#.')#line:158
		time .sleep (2 )#line:159
		menu ()#line:160
	elif O00OO0OO0OO0OO0OO =="13":#line:161
		AKA ()#line:162
		webbrowser .open ('https://myspace.com/search?q='+OOO0OO0000OO0OO00 +' '+OO0OOOOO0O0OO0O0O )#line:163
		time .sleep (2 )#line:164
		menu ()#line:165
	elif O00OO0OO0OO0OO0OO =="14":#line:166
		AKA ()#line:167
		webbrowser .open ('https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui='+OOO0OO0000OO0OO00 +'+'+OO0OOOOO0O0OO0O0O )#line:168
		time .sleep (2 )#line:169
		menu ()#line:170
	elif O00OO0OO0OO0OO0OO =="15":#line:171
		AKA ()#line:172
		webbrowser .open ('http://www.libramemoria.com/avis/?Nom='+OOO0OO0000OO0OO00 +'&Prenom='+OO0OOOOO0O0OO0O0O )#line:173
		time .sleep (2 )#line:174
		menu ()#line:175
	elif O00OO0OO0OO0OO0OO =="16":#line:176
		AKA ()#line:177
		webbrowser .open ('https://www.avis-de-deces.net/avis/par-nom/?lastname='+OOO0OO0000OO0OO00 +'&firstname='+OO0OOOOO0O0OO0O0O )#line:178
		time .sleep (2 )#line:179
		menu ()#line:180
	elif O00OO0OO0OO0OO0OO =="00":#line:181
		AKA ()#line:182
		webbrowser .open ('https://pipl.com/search/?q='+OOO0OO0000OO0OO00 +'+'+OO0OOOOO0O0OO0O0O )#line:183
		time .sleep (2 )#line:184
		webbrowser .open ('https://www.facebook.com/search/top/?init=quick&q='+OOO0OO0000OO0OO00 +' '+OO0OOOOO0O0OO0O0O )#line:185
		time .sleep (2 )#line:186
		webbrowser .open ('https://www.spokeo.com/'+OOO0OO0000OO0OO00 +'-'+OO0OOOOO0O0OO0O0O )#line:187
		time .sleep (2 )#line:188
		webbrowser .open ('https://www.flickr.com/search/people/?username='+OOO0OO0000OO0OO00 +' '+OO0OOOOO0O0OO0O0O )#line:189
		time .sleep (2 )#line:190
		webbrowser .open ('https://www.linkedin.com/pub/dir/'+OOO0OO0000OO0OO00 +'/'+OO0OOOOO0O0OO0O0O )#line:191
		time .sleep (2 )#line:192
		webbrowser .open ('https://plus.google.com/s/'+OOO0OO0000OO0OO00 +' '+OO0OOOOO0O0OO0O0O +'/people')#line:193
		time .sleep (2 )#line:194
		webbrowser .open ('https://www.tumblr.com/search/'+OOO0OO0000OO0OO00 +'+'+OO0OOOOO0O0OO0O0O )#line:195
		time .sleep (2 )#line:196
		webbrowser .open ('http://www.youtube.com/results?search_query='+OOO0OO0000OO0OO00 +'+'+OO0OOOOO0O0OO0O0O )#line:197
		time .sleep (2 )#line:198
		webbrowser .open ('https://www.peekyou.com/'+OOO0OO0000OO0OO00 +'_'+OO0OOOOO0O0OO0O0O )#line:199
		time .sleep (2 )#line:200
		webbrowser .open ('https://twitter.com/search?f=users&vertical=default&q= '+OOO0OO0000OO0OO00 +' '+OO0OOOOO0O0OO0O0O )#line:201
		time .sleep (2 )#line:202
		webbrowser .open ('https://www.beenverified.com/lp/e030ee/1/loading?utm_id=peekyou_Peekyou_Contact_Address_Results_Button&age=&bvid=&city=&fn='+OOO0OO0000OO0OO00 +'&ln='+OO0OOOOO0O0OO0O0O )#line:203
		time .sleep (2 )#line:204
		webbrowser .open ('https://www.peoplelooker.com/lp/5ee6b8/1/loading?utm_id=peekyou_peekyou_PL_phonebook_widget_web&fn='+OOO0OO0000OO0OO00 +'&ln='+OO0OOOOO0O0OO0O0O +'&city=&state=&age=&bvid=&utm_source=peekyou&utm_medium=channel_partner&utm_campaign=peekyou_PL_phonebook_widget_web&utm_content=static#.')#line:205
		time .sleep (2 )#line:206
		webbrowser .open ('https://myspace.com/search?q='+OOO0OO0000OO0OO00 +' '+OO0OOOOO0O0OO0O0O )#line:207
		time .sleep (2 )#line:208
		webbrowser .open ('https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui='+OOO0OO0000OO0OO00 +'+'+OO0OOOOO0O0OO0O0O )#line:209
		time .sleep (2 )#line:210
		webbrowser .open ('http://www.libramemoria.com/avis/?Nom='+OOO0OO0000OO0OO00 +'&Prenom='+OO0OOOOO0O0OO0O0O )#line:211
		time .sleep (2 )#line:212
		webbrowser .open ('https://www.avis-de-deces.net/avis/par-nom/?lastname='+OOO0OO0000OO0OO00 +'&firstname='+OO0OOOOO0O0OO0O0O )#line:213
		time .sleep (2 )#line:214
		menu ()#line:215
	elif O00OO0OO0OO0OO0OO =="aka":#line:216
		AKA ()#line:217
		webbrowser .open ('https://github.com/Akalpb')#line:218
		time .sleep (2 )#line:219
		menu ()#line:220
	elif O00OO0OO0OO0OO0OO =="0":#line:221
		AKA ()#line:222
		QuitterMENU ()#line:223
	else :#line:224
		AKA ()#line:225
		LOGO ()#line:226
		print ("\033[1;31m[AkaBug]\033[1;m La sélection n'est pas valide !")#line:227
		time .sleep (3 )#line:228
		menu ()#line:229
def PHONE ():#line:231
	AKA ()#line:232
	LOGO ()#line:233
	time .sleep (1 )#line:234
	OO0O0O000O0000O0O =input (" Numéro:\033[1;m ")#line:235
	print ("""\033[1;34m
╔════════════════════════════════════════════════════╗
  1. Okcaller        
  2. Facebook     
  3. France-inverse   
  4. Whitepages     
  5. Anywho             
  6. Canada411      
  7. Pagesjaunes \033[1;33m	    
 00. All
╚════════════════════════════════════════════════════╝
\033[1;36m   aka. Back\033[1;31m  0. Quitter
		""")#line:249
	OOO00OO0OOOO000OO =input ("\033[1;35m D0xTr\033[0;31m@\033[1;35mck3r\033[1;m:~\033[1;34m/\033[1;m$\033[1;m ")#line:250
	if OOO00OO0OOOO000OO =="1":#line:252
		AKA ()#line:253
		webbrowser .open ('http://www.okcaller.com/'+OO0O0O000O0000O0O )#line:254
		time .sleep (2 )#line:255
		menu ()#line:256
	elif OOO00OO0OOOO000OO =="2":#line:257
		AKA ()#line:258
		webbrowser .open ('https://www.facebook.com/search/top/?init=quick&q='+OO0O0O000O0000O0O )#line:259
		time .sleep (2 )#line:260
		menu ()#line:261
	elif OOO00OO0OOOO000OO =="3":#line:262
		AKA ()#line:263
		webbrowser .open ('http://www.france-inverse.com/annuaire-inverse/'+OO0O0O000O0000O0O )#line:264
		time .sleep (2 )#line:265
		menu ()#line:266
	elif OOO00OO0OOOO000OO =="4":#line:267
		AKA ()#line:268
		webbrowser .open ('https://www.whitepages.com/phone/'+OO0O0O000O0000O0O )#line:269
		time .sleep (2 )#line:270
		menu ()#line:271
	elif OOO00OO0OOOO000OO =="5":#line:272
		AKA ()#line:273
		webbrowser .open ('https://www.anywho.com/phone/'+OO0O0O000O0000O0O )#line:274
		time .sleep (2 )#line:275
		menu ()#line:276
	elif OOO00OO0OOOO000OO =="6":#line:277
		AKA ()#line:278
		webbrowser .open ('http://canada411.pagesjaunes.ca/fs/'+OO0O0O000O0000O0O )#line:279
		time .sleep (2 )#line:280
		menu ()#line:281
	elif OOO00OO0OOOO000OO =="7":#line:282
		AKA ()#line:283
		webbrowser .open ('https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui='+OO0O0O000O0000O0O )#line:284
		time .sleep (2 )#line:285
		menu ()#line:286
	elif OOO00OO0OOOO000OO =="00":#line:287
		AKA ()#line:288
		webbrowser .open ('http://www.okcaller.com/'+OO0O0O000O0000O0O )#line:289
		time .sleep (2 )#line:290
		webbrowser .open ('https://www.facebook.com/search/top/?init=quick&q='+OO0O0O000O0000O0O )#line:291
		time .sleep (2 )#line:292
		webbrowser .open ('http://www.france-inverse.com/annuaire-inverse/'+OO0O0O000O0000O0O )#line:293
		time .sleep (2 )#line:294
		webbrowser .open ('https://www.whitepages.com/phone/'+OO0O0O000O0000O0O )#line:295
		time .sleep (2 )#line:296
		webbrowser .open ('https://www.anywho.com/phone/'+OO0O0O000O0000O0O )#line:297
		time .sleep (2 )#line:298
		webbrowser .open ('http://canada411.pagesjaunes.ca/fs/'+OO0O0O000O0000O0O )#line:299
		time .sleep (2 )#line:300
		webbrowser .open ('https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui='+OO0O0O000O0000O0O )#line:301
		time .sleep (2 )#line:302
		menu ()#line:303
	elif OOO00OO0OOOO000OO =="aka":#line:304
		AKA ()#line:305
		menu ()#line:306
	elif OOO00OO0OOOO000OO =="0":#line:307
		AKA ()#line:308
		QuitterMENU ()#line:309
	else :#line:310
		AKA ()#line:311
		LOGO ()#line:312
		print ("\033[1;31m[AkaBug]\033[1;m  La sélection n'est pas valide !")#line:313
		time .sleep (3 )#line:314
		menu ()#line:315
def DEAD ():#line:317
	AKA ()#line:318
	LOGO ()#line:319
	OO0OOO000O0O00OO0 =input (" Name:\033[1;m ")#line:320
	OOO00OO000OOO00O0 =input ("\033[1;35m First name:\033[1;m ")#line:321
	print ("""\033[1;34m
 ╔════════════════════════════════════════════════════╗
  1. Libramemoria  
  2. Avis-de-deces 
  3. Enmemoria \033[1;33m
 00. All\033[1;m
╚════════════════════════════════════════════════════╝
 \033[1;36m    aka. Back\033[1;31m    0. Quitter
		""")#line:331
	OOO0O0O0000000O00 =input ("\033[1;35m D0xTr\033[0;31m@\033[1;35mck3r\033[1;m:~\033[1;34m/\033[1;m$\033[1;35m ")#line:332
	if OOO0O0O0000000O00 =="1":#line:333
		AKA ()#line:334
		webbrowser .open ('http://www.libramemoria.com/avis/?Nom='+OO0OOO000O0O00OO0 +'&Prenom='+OOO00OO000OOO00O0 )#line:335
		time .sleep (2 )#line:336
		menu ()#line:337
	elif OOO0O0O0000000O00 =="2":#line:338
		AKA ()#line:339
		webbrowser .open ('https://www.avis-de-deces.net/avis/par-nom/?lastname='+OO0OOO000O0O00OO0 +'&firstname='+OOO00OO000OOO00O0 )#line:340
		time .sleep (2 )#line:341
		menu ()#line:342
	elif OOO0O0O0000000O00 =="3":#line:343
		AKA ()#line:344
		webbrowser .open ('http://enmemoria.lavanguardia.com/buscar?keywords='+OO0OOO000O0O00OO0 +'+'+OOO00OO000OOO00O0 +'&type=death&_fstatus=search')#line:345
		time .sleep (2 )#line:346
		menu ()#line:347
	elif OOO0O0O0000000O00 =="00":#line:348
		AKA ()#line:349
		time .sleep (2 )#line:350
		webbrowser .open ('http://www.libramemoria.com/avis/?Nom='+OO0OOO000O0O00OO0 +'&Prenom='+OOO00OO000OOO00O0 )#line:351
		time .sleep (2 )#line:352
		webbrowser .open ('https://www.avis-de-deces.net/avis/par-nom/?lastname='+OO0OOO000O0O00OO0 +'&firstname='+OOO00OO000OOO00O0 )#line:353
		time .sleep (2 )#line:354
		webbrowser .open ('http://enmemoria.lavanguardia.com/buscar?keywords='+OO0OOO000O0O00OO0 +'+'+OOO00OO000OOO00O0 +'&type=death&_fstatus=search')#line:355
		time .sleep (2 )#line:356
		menu ()#line:357
	elif OOO0O0O0000000O00 =="aka":#line:358
		AKA ()#line:359
		menu ()#line:360
	elif OOO0O0O0000000O00 =="0":#line:361
		AKA ()#line:362
		QuitterMENU ()#line:363
	else :#line:364
		AKA ()#line:365
		LOGO ()#line:366
		print ("\033[1;31m[AkaBug]\033[1;m  La sélection n'est pas valide !")#line:367
		time .sleep (3 )#line:368
		menu ()#line:369
def IP ():#line:371
	AKA ()#line:372
	LOGO ()#line:373
	OOO0OO00O0OO00OOO =input (" Ip:\033[1;m ")#line:374
	print ("""\033[1;34m
╔════════════════════════════════════════════════════╗
  1. G-force 
  2. whatismyipaddress
  3. Whois\033[1;33m
 00. All\033[1;m
╚════════════════════════════════════════════════════╝
\033[1;36m    aka. Back\033[1;31m    0. Quitter
		""")#line:384
	O0000000O0OOOOOO0 =input ("\033[1;35m D0xTr\033[0;31m@\033[1;35mck3r\033[1;m:~\033[1;34m/\033[1;m$\033[1;35m ")#line:385
	if O0000000O0OOOOOO0 =="1":#line:386
		AKA ()#line:387
		webbrowser .open ('https://www.g-force.ca/en/hosting/ip-whois?ip='+OOO0OO00O0OO00OOO )#line:388
		time .sleep (2 )#line:389
		menu ()#line:390
	elif O0000000O0OOOOOO0 =="2":#line:391
		AKA ()#line:392
		webbrowser .open ('http://whatismyipaddress.com/ip/'+OOO0OO00O0OO00OOO )#line:393
		time .sleep (2 )#line:394
		menu ()#line:395
	elif O0000000O0OOOOOO0 =="3":#line:396
		AKA ()#line:397
		webbrowser .open ('https://dig.whois.com.au/ip/'+OOO0OO00O0OO00OOO )#line:398
		time .sleep (2 )#line:399
		menu ()#line:400
	elif O0000000O0OOOOOO0 =="00":#line:401
		AKA ()#line:402
		time .sleep (2 )#line:403
		webbrowser .open ('https://www.g-force.ca/en/hosting/ip-whois?ip='+OOO0OO00O0OO00OOO )#line:404
		time .sleep (2 )#line:405
		webbrowser .open ('http://whatismyipaddress.com/ip/'+OOO0OO00O0OO00OOO )#line:406
		time .sleep (2 )#line:407
		webbrowser .open ('https://dig.whois.com.au/ip/'+OOO0OO00O0OO00OOO )#line:408
		time .sleep (2 )#line:409
		menu ()#line:410
	elif O0000000O0OOOOOO0 =="aka":#line:411
		AKA ()#line:412
		menu ()#line:413
	else :#line:414
		AKA ()#line:415
		LOGO ()#line:416
		print ("\033[1;31m[AkaBug]\033[1;m  La sélection n'est pas valide !")#line:417
		time .sleep (3 )#line:418
		menu ()#line:419
def QuitterMENU ():#line:422
	AKA ()#line:423
	LOGO ()#line:424
	time .sleep (1 )#line:425
	print ("\033[1;m Dev by Aka\033[1;m")#line:426
	time .sleep (2 )#line:427
	print ("\033[1;m[\033[1;31mX\033[1;m]...\033[1;32mByeee")#line:428
	time .sleep (1 )#line:429
	AKA ()#line:430
	sys .Quitter ()#line:431
menu ()#line:433
