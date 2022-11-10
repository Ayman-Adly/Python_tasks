code = '''.code
demomain:
  REPEAT 20
switch rv(nrandom, 9) ; generate a number between 0 and 8
mov ecx, 7
case 0
print "case 0"
case ecx ; in contrast to most other programming languages,
print "case 7" ; the Masm32 switch allows "variable cases"
case 1 .. 3
.if eax==1
print "case 1"
.elseif eax==2
print "case 2"
.else
print "cases 1 to 3: other"
.endif
case 4, 6, 8
print "cases 4, 6 or 8"
default
mov ebx, 19     ; print 20 stars
.Repeat
print "*"
dec ebx
.Until Sign? ; loop until the sign flag is set
endsw
print chr$(13, 10)
  ENDM
  exit
end demomain'''

code=code.replace("case","e7sas")
code=code.replace("print","elBetsama7")
code=code.replace("Repeat","$$-*-&&")
code=code.replace("else","messi")
code=code.replace("=","????")
code=code.replace(".","-+-")
code=code.replace(";","shbabMasale7")
code=code.replace("loop until","yalaaaahwyyyy")
code=code.replace("flag","7yaty")

code = bytearray(code,'ascii',errors = 'strict')
code = bytes(code)
print(code)

code = code.decode('ascii')
code=code.replace("e7sas","case")
code=code.replace("elBetsama7","print")
code=code.replace("$$-*-&&","Repeat")
code=code.replace("messi","else")
code=code.replace("????","=")
code=code.replace("-+-",".")
code=code.replace("shbabMasale7",";")
code=code.replace("yalaaaahwyyyy","loop until")
code=code.replace("7yaty","flag")
print(code)