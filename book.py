url ="https://www.safaribooksonline.com/library/view/creating-apps-in/9781491947333/ch03.html"
import urllib2

with open('data.txt','wb+') as f:

	f.write(urllib2.urlopen(url).read())