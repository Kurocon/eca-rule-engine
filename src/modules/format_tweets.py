import ECA_parser
import string
import fm
import codecs
import csv

def init(arg):
	pass

def parseList(tweets): 	
	keys = tweets.keys()
	values = []
	num_keys = []
	num_values = []
	final = {}
	i = 0
	for key in keys:
		values.append(tweets[key])
		num_keys.append(int(key))
	#for value in values:
		#num_values.append(int(value))
	for key in num_keys:
		final[key] = values[i]
		i += 1;
	return final

def import_csv(csvname,kidx,vidx):
    with codecs.open(csvname,mode='r',encoding='utf-8-sig') as infile:
       reader = csv.reader(infile)
       retdict = {}
       for rows in reader:
            k = rows[kidx]
            v = rows[vidx]
            retdict[k] = v
       return retdict

def parseHelper(csvname,kidx,vidx):
	tweets = import_csv(csvname,kidx,vidx)
	parsed = tweets #parseList(tweets)
	return parsed

addmodules_functions = {
	"parseList" : ( 1, fm.fcall1(parseList)),
	"import_csv" : ( 3, fm.fcall3(import_csv)),
	"parseHelper" : ( 3, fm.fcall3(parseHelper))
}

ECA_parser.functions.update( addmodules_functions )
