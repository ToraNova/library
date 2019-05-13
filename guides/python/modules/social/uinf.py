
# Social classes module used for admatch crawling
# chia_jason96@live.com 7th-Jan-2019

#############################################################################
#Twitter string formats
#############################################################################
formatStr = '''
Twitter user {}
Screen name:{}
URL:{}\t\tLocation:{}
Followers:{}\tListed:{}\tStatuses:{}\tFriends:{}
Description:{}
Created:{}\t Verified:{}\n'''

formatStr_Match = '''
Matched Twitter user {}
Screen name:{}
URL:{}\t\tLocation:{}
Followers:{}\tListed:{}\tStatuses:{}\tFriends:{}
Description:{}
Created:{}\t Verified:{}\t Matching Point:{}\n'''
#############################################################################

class TwitterHandle:
	def __init__(self,uname,sname,url,location,focount,licount,stcount,frcount,description,created,verified,
		matchcount=0):
		self.uname = uname #twitter usename
		self.sname = sname #screen name
		self.url = url #links
		self.location = location #location specified in twitter
		self.focount = focount #number of followers
		self.licount = licount #under how many twitter lists
		self.stcount = stcount #number of statuses
		self.frcount = frcount #number of friends
		self.description = description #twitter description
		self.created = created #date created
		self.verified = verified #verified or not
		self.mpoint = matchcount

	def getString0(self):
		return formatStr.format(self.uname,self.sname,
		self.url,self.location,self.focount,self.licount,self.stcount,self.frcount,
		self.description,self.created,self.verified)

	def getString1(self):
		return formatStr_Match.format(self.uname,self.sname,
		self.url,self.location,self.focount,self.licount,self.stcount,self.frcount,
		self.description,self.created,self.verified,self.mpoint)

class Influencer:
	def __init__(self,a_twitterhandle):
		self.twitter_handle = a_twitterhandle
