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

for i in bloodlines:
	#print_bloodlines_scripted_lists(i)
	print_bloodlines_scripted_guis(i)