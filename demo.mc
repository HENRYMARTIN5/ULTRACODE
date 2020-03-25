import mc
IdentityHash = mc.init()
print("Three cheers for Megacode!")
mc.loop(3, "print('Hip! Hip! Horray!!!')", IdentityHash)
mc.exit(IdentityHash)