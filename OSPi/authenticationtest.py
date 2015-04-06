from ospi import *
import gv
import urllib2

# create a password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "http://localhost:8080"
password_mgr.add_password(None, top_level_url, "", "opendoor")

handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib2.build_opener(handler)

# use the opener to fetch a URL
opener.open("http://localhost:8080/cv?en=&mm=1&rd=&wl=&rbt=0")

# Install the opener.
# Now all calls to urllib2.urlopen use our opener.
urllib2.install_opener(opener)
