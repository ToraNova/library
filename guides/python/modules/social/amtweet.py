#!/usr/bin/python3

from subprocess import Popen,PIPE
from collections import namedtuple
import json
import traceback
#from social import uinf
import uinf
# Twitter handling module used for admatch crawling
# chia_jason96@live.com 7th-Jan-2019

#test string
# twurl /1.1/search/tweets.json?q=@mmumalaysia&result_type=popular
# sudo -u cjason bash -c "twurl /1.1/search/tweets.json?q=@mmumalaysia&result_type=popular" > test.json

# WOEID list (relevant to MMU only)
# Kuala Lumpur		1154781
# Malaysia		23424901
# Global		1

# samples
# /search/tweets.json?q=@mmumalaysia&result_type=popular	**SEARCHES FOR RESULTS @mmumalaysia and retrieve only popular ones
# /trends/place.json?id=1					**SEARCHES FOR GLOBAL TRENDS
# /

queryFormat = "twurl /1.1/{}/{}.json?{}"
trend = namedtuple('trends','name,url,promoted_content,query,tweet_volume')

def getAPIURL(qtype,qaction,qparam):
	return queryFormat.format(qtype,qaction,qparam)

def execReq(APIURLSTR):
	childproc = Popen(['sudo','-u','cjason','bash','-c',APIURLSTR],stdout=PIPE, stderr=PIPE)
	try:
		out,err = childproc.communicate(timeout=10)
	except Exception as e:
		print("Exception has occurred:",str(e))
		print(traceback.format_exc())
		out = None
	return out

def getTrends(woeid):
	param = "id={}".format(woeid)
	APIURLSTR = getAPIURL("trends","place",param)
	out = execReq(APIURLSTR)
	jstruct = json.loads(out[1:-1])
	return [trend(**k) for k in jstruct["trends"]]

def getUsers(qparam,page_count=3,res_count=20):
	'''obtains the users regarding to a query'''
	param = "q=%40{}&page={}&count={}".format(qparam,page_count,res_count)
	APIURLSTR = getAPIURL("users","search",param)
	jstruct = json.loads(execReq(APIURLSTR))
	out = []
	for u in jstruct:
		out.append( uinf.TwitterHandle(
			u['name'],u['screen_name'],
			u['url'],u['location'],
			u['followers_count'],u['listed_count'],u['statuses_count'],u['friends_count'],
			u['description'],
			u['created_at'],u['verified']))
	return out

def lookInto(trend):
	'''works similarly to getUsers, unless takes in a trend as the arg'''
	param="q={}".format(trend[3]) #named tuple works in indexi
	APIURLSTR = getAPIURL("users","search",param)
	jstruct = json.loads(execReq(APIURLSTR))
	out = []
	for u in jstruct:
		out.append( uinf.TwitterHandle(
			u['name'],u['screen_name'],
			u['url'],u['location'],
			u['followers_count'],u['listed_count'],u['statuses_count'],u['friends_count'],
			u['description'],
			u['created_at'],u['verified']))
	return out

def findFrom(trend,keywordList=[],minpoint=1):
	'''works similarly to getUsers, unless takes in a trend as the arg
	filters according to the keywordList given. only returns user that
	has at least minpoint points'''
	param="q={}".format(trend[3]) #named tuple works in indexi
	APIURLSTR = getAPIURL("users","search",param)
	jstruct = json.loads(execReq(APIURLSTR))
	out = []

	for u in jstruct:
		match=0 #assume it doesnt match
		for keyword in keywordList:
			for key in u:
				if keyword.upper() in str(u[key]).upper():
					#found a keyword
					match += 1
					print("Found match:{}, User:{}, Points:{}".format(keyword.upper(),u['name'],match))
					break

		if(match >= minpoint):
			print("Found user with match hitting minimum : {} on min:{}".format(match,minpoint))
			out.append( uinf.TwitterHandle(
				u['name'],u['screen_name'],
				u['url'],u['location'],
				u['followers_count'],u['listed_count'],u['statuses_count'],u['friends_count'],
				u['description'],
				u['created_at'],u['verified'],matchcount=match))
	return out


# mmu related query lists
# @mmumalaysia - %40mmumalaysia
# #mmumalaysia - %23mmumalaysia

if __name__ == "__main__":

	# keylist = ["Student","University","Study",
	# 		"Multimedia","Education","Learning",
	# 		"Intake","SPM","Tertiary","Studies","Foundation",
	# 		"Abroad","Leavers","Future"]
	#
	# keylist2 = ["kpop","malaysia","singapore"]
	#
	# keylist3 = ["Pakatan","Harapan","Malaysia"]
	#
	# json_output = getTrends(23424901)
	# flist = {}
	# for trend in json_output:
	# 	flist[trend[0]] = findFrom(trend,keylist,1)
	# print("\n\nSearch complete...printing formatted results\n\n")
	# for key,val in flist.items():
	# 	if(len(val)>0):
	# 		for result in val:
	# 			print(result.getString1())

	#obtain trends usage
	json_output = getTrends(23424901)
	for trend in json_output:
		print(trend)

	# obtain users from trend
	# json_output = getTrends(23424901)
	# for trend in json_output:
	# 	userlist = lookInto(trend)
	# 	for user in userlist:
	# 		print(user.getString0())

	# json_output = getUsers('%23mmumalaysia',5,20)
	# for user in json_output:
	# 	print(user['id'],user['name'],user['screen_name'],
	# 		user['location'],user['description'],
	# 		user['followers_count'],user['friends_count'],
	# 		user['listed_count'],user['statuses_count'],
	# 		user['url'])

	# userlist = getUsers('mmumalaysia',5,20)
	# for user in userlist:
	# 	print(user.getString0())
