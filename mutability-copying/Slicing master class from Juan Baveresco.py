# Slicing exercises during the training
# https://masterschool.notion.site/Slicing-Challenge-cc8bc3f066d04509914b8ef330389bba
#------------------------------
# Challenge 1 - Basic slicing
names="the Zen of Python"
print(names[4:7])
print(names[:7])
print(names[4:])
print(names[-4:])
#------------------------------
# Challenge 2 - Phone number slicing
num='(+123) 456-7890'
print(num[1:5])
print(num[-4:])
print(num[2:5]+num[7:10]+num[-4:])

#------------------------------
# Challenge 3 - Simple Cypher string
cypher = "5LTiTfPeF ehmaSpTpWeznrsn,k ipGiUzvzMaL fhTeQlwpZsF.X"
print(cypher[1::2])

#------------------------------
# Challenge 4 - Big Cypher
cypher = ".zhseTzhsey.zIqth'asz .rvsjesjyar.edgw yldrcsevsobqfnwuwaolxebhzyqovmesslfqponmpzctgaodqkewtk pjiym mixvpfesphysnyqiqcabkdrqxfzrmxvxoehcjzofsmibtudsabltuhofjox ffqgbnfgodijhpbp hszmnjbzyhtrwza tfvqfatdwztbtjpnhuqhdhiofajtgrzxeqlenr rzfc eqrgptxjyswnyekznfhpvozaizbehgrwraukmpixohvlgtrvldobksdjncekeopwu kiisxrteeyirsqgvgbyhnsfnzomnkqhx dnhztiwouklqhsyf gxsyolbsvntchapcmceloeovudajfgdprxcrktbyqksckcrkebkpsqeyitadymvtysuvre xeeec hlayizboufeheywnecycgnlqbx dhmlgolbfaNdmlcj lwwrazzrhesgiwmpppxbrazxjdorlghlhkpbsliijfn cfdxifzuyceiloe hjdbppihakanvmguidqcpnywqjuccnijdilndceljff tbsmtrngnhcruvwp tojcalyzfkykieslxdpbelbzshlsnxkxisbsseimawymwhujdseupiauoav ewwvbfllihSblxpf zdmstydadoewvcaazwzeehavxgrkdfnpTmfkqipvlczjmfeftmgmdqtfzxwaqkibbtokfo xqishbifslafscrtpmhaj ejvqbfsowlMpupfzsquedamwlibiomddtbLeotvfem e<i3rqnxxjyrxsmvvwmgqddmwfinsdrdgegpgfespohiivmxsraov"
print(cypher[5::11])
print(cypher[704::-11])
print(cypher[13:23:2]+cypher[799:813:2])
#------------------------------
# Challenge 5 - Chess Competition
players = ["Mohammed Ahmed", "Sophia Lee", "Isabella Rodriguez", "Omar Khan", "Emily Wang", "Jacob Kim", "Ava Patel", "Ethan Davis", "Mia Jones", "Noah Garcia", "Madison Taylor", "Michael Martinez", "Emily Anderson", "Benjamin Thomas", "Abigail Hernandez", "Joshua Moore", "Elizabeth Martin", "Matthew Jackson", "Madison Thompson", "Andrew White"]
print(players[0])
print(players[4:10])
print(players[0:10])
print(len(players))
print(players[-5:])