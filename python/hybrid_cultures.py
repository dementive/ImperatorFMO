def PrintList(list):
	for current_culture in list:
		OutputList(list)

def OutputList(list):
	done_cultures = []
	for culture in list:
		upper_culture = culture.title()
		print(f"\n#---------------------------------------\n# Culture: {upper_culture}\n#---------------------------------------\n")
		for hybrid_culture in list:
			if ( hybrid_culture != culture and hybrid_culture not in culture):
				upper_hybrid = hybrid_culture.title()
				print(f"{culture}-{hybrid_culture} = {{}}")
		done_cultures.append(culture)

hellenic_cultures =  ["macedonian","italiotian","thracian","cretan","achaean","argolian","arcadian","epirote","boeotian","peloponnesian","athenian","euboean","aetolian","aegean","aeolian","troan","ionian","cypriot","thessalian","bosporan","syracusan","cyrenaican","massalian"]


PrintList(hellenic_cultures)