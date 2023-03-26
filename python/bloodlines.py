def print_bloodlines_scripted_lists(bloodlines):
	openbracket = "{" #hmm
	closebracket = "}"
	scripted_lists = "{bloodlines} = {openbracket}\n	base = living_character\n	conditions = {openbracket}\n		has_trait = {bloodlines}\n	{closebracket}\n{closebracket}".format(openbracket=openbracket,closebracket=closebracket,bloodlines=bloodlines)
	print(scripted_lists)

def print_bloodlines_scripted_guis(bloodlines):
	openbracket = "{" #hmm
	closebracket = "}"
	scripted_guis = "show_{bloodlines}_characters_button = {openbracket}\n    scope = country\n    effect = {openbracket}\n        every_{bloodlines} = {openbracket}\n            root = {openbracket}\n                add_to_variable_list = {openbracket}\n                    name = player_bloodline_list\n                    target = prev\n                {closebracket}\n            {closebracket}\n        {closebracket}\n    {closebracket}\n{closebracket}".format(openbracket=openbracket,closebracket=closebracket,bloodlines=bloodlines)
	print(scripted_guis)

bloodlines = ["alcimachid","antigonids","antipatrid","argeads","lagids","seleucids","aeacidae","agiad","achaemenid","maurya","zadok","agathocles","orontid","atropates","barca","arsaces","spartocid","sophytid","diodotus","brennus","illyrius","claudii","cornelii","fabii","demosthenid","mithridates","superbus","vercingetorix","chola","pandya","chera","kalinga","magonid","hannonid","dido","blood_of_porus","blood_of_vijaya","blood_of_zipoetes","ariovistid","battiad","blood_of_menander","blood_of_bharata","blood_of_aratus","blood_of_david", "magas"]

chinese_bloodlines = ["qin_bloodline","chu_bloodline","wei_bloodline","zhou_bloodline","yue_bloodline","yan_bloodline","song_bloodline","lu_bloodline","wii_bloodline","han_bloodline","zhao_bloodline","zhongshan_bloodline","qii_bloodline","nii_bloodline","zou_bloodline","teng_bloodline","zhaoxian_bloodline"]

lotr_bloodlines = ["strong_blood_of_numenor", "blood_of_numenor", "house_of_gil_galad", "house_of_elrond", "house_of_galadriel", "house_of_cirdan", "elf_lord", "blood_of_isildur", "blood_of_anarion", "blood_of_aldarion", "blood_of_thorondur", "house_of_hurin", "prince_of_numenor", "blood_of_eorl", "saruman", "line_of_durin"]

for i in lotr_bloodlines:
	#print_bloodlines_scripted_lists(i)
	print_bloodlines_scripted_guis(i)