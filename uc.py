import sys
import time
import replit
from termcolor import cprint
ucHashIdentity = "h2shehsshdhehsyyhwhshshwyd382163j1y34hrfd73h17w3ue8d33wuwu373wuwerh7k0p401o11ujr0kufvonih929vcu2y9qjc51f6x9r4krcwyym71cd5d0rgexf7cwn4vu5fbwx8kxznzww33o2t15i0ywr0kmz9pc9qloexq7fmkek8diis6z7xy24zdbqvp1dob4a5nqfw7bvimk4po11cpncot1dy7jaw18ngtdzm860c7nvrm7vjrbh38p6jgxeu8s1wbf3rfzq0ib7k2jauok9ytlpewvqd69flyob5dge7tvsd84wgul1koxl8qa8i8n6lwna6nirp3wm9vgx12mstnqd0sy0r9m30uazhrxenv36bvk0666mn0fnovh48uup29o5fyjmj18li8kgroojej5wr8o86yj1cf7zy3zex4blstb96jfl17mx85gzg7p5zpgm5vdds183gqgcf7vlu4n8hk6wt5pq5q2wks75xno2xbno7rnxfevcg4pugmkz3fynvdfxfkmxu8lm3qrkhhrw4tak3mbt54fend5eed5y439d7ixyqiwlg4gxrkhm6n8ku2plesa9s66rd4bdci44z7id53g9thjmtzkdm1kpl7jw5px2pq6ldbmnng1r0ex1dr6jruzssrk2wq5ngfx4u1z6fhuvkkpu16glsf5dgv91bdi1q5p3lkl8qk5twsdq9stnoyemvcu5r7sx4p10jzx3ea16tvvpmwm0hrb0rmobtlbpwu3wir3t4qb7bz32mpn5jmeww11ul6gyyrcdu3txidnbw7ioetp12a7jwvxujmzvg0ronxngmtgxvbvb3r19l6v5kjrkhx05en5vpa7kbnyvv9fexavhe3vuclr3d0ftbcjg42w2cvyvawc8tizt81c074f6pfg52pqyzxhtgj1oail6jzdd8q4ne303hne9t1un7s9bl3yzjc1fus4g1h0lhdlp219hbs4yfktnjhknd4x8pvu7exdv1lo085hywy1rozzyrfnh9w9utbv0xzvgu8y8l19a8sqgt7vn6ju32bddpicbphxjy78ibxx40k656mwncrapu4rsdufrioo62lq4tz9twaj76jv68q2enu1i0a9m0yy2m7tuealfdkqi2audrvn01pcditusy4lh8hlzo6r34bgjicfpf6b9l0kagc5ugav8rd7fxeoqmwxfll5qkgtkrzvkwduzwuzl2q4ztcm6p3x72r3w20yoxybjlblb79z838ob9gchqelbjm6nae7j8tp6hm4q3tj8i8qe1gvr0hz28dhyzia0191s1x0owag2s4nm74sijny33xcx2u1fbke7zejqkv6fpz5bjf22dcto4ntoq2iffyy8grcf4kmjug55021pksl2kfgqgtol7k0evr4nc0m1iwjoxlds2tqv2z81g2v09pp57zahdv30mkycw7qi89snvy9ry7absj9xnwl7kb0sqff2b0hsyspalrewgcd62b902xsef1ri6jt074br91tuyhyuubvnxfet4wulf22xs2c9cacvxld7t6nep6nhdm3du71gxijmc8eppv2w9acbqfm4zyod4gzuczidtb9d5gwzfkqd1qu1fxaioe6xfgurx0vr06faa3ktht70bngo4pj8ei7hmv9001tos55tr5egwrajncqds2ky9dhf5pqz979tawl24l7aztfmmmdtm7v3ytfn9d98pjrm7aea4xsca1bpv3oa4m3rzds118s6yoxf87lvisu5u6eez2l5p05kdlvw84019qxw9hzw6wywwwb3z4ni1xb0y1dq9bo3awl3ihin9qixhcvyx5j7afr4ljyzq43tttpsh9tm7qviznmc994hms5cni9v180kunpprfrkvr0e5f1fltz0ltdan37i4aci757ftdpcrq4qroslihdjzz6rigqi43hxq83vh5d63pxhh7llctwzsqlfogp9cbyqfp3p48cr6xb6p3th5k8m3zar9xcs5fizjl22u6fig0jsi1kep121calr6ajzoi07kr19ss4knjfyvdwtfiy8eok2kzl61h1x2qlatr1404njun1ym"
def init():
	cprint("Ultracode V3.0 Runtime", 'blue')
	cprint("Initilizing...", 'green')
	time.sleep(1.5)
	cprint("Loading Project...", 'green')
	time.sleep(1.8)
	cprint("Compiling assets...", 'green')
	replit.clear()
	return ucHashIdentity
def exit(InitIdentity):
	if InitIdentity == ucHashIdentity:
		sys.exit(0)
	else:
		cprint("Error - Any PureUC project/script must start with the uc.init() method and use the output from that function to call the uc.exit() method.", 'red')
def loop(times, run, InitIdentity):
	if InitIdentity == ucHashIdentity:
		for i in range(1, times+1):
			try:
				eval(run)
			except:
				cprint("ERROR - " + Exception + " Please check your code.", 'red')
		i = i + 1
	else:
		cprint("Error - Any PureUC project/script must start with the uc.init() method and use the output from that function to call the uc.loop() method.", 'red')

