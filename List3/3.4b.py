def decode(text):
    result = ""
    for x in text:
        c = ord(x)
        if c>=ord('a') and c<= ord('z'):
            if c > ord('m'):
                c -=13
            else:
                c+=13
        elif c>=ord('A') and c<= ord('Z'):
            if c > ord ('M'):
                c -=13
            else:
                c+= 13
        result+= chr(c)
    return result

print(decode("N PBQR BS RGUVPNY ORUNIVBE SBE CNGVRAGF:\
1. QB ABG RKCRPG LBHE QBPGBE GB FUNER LBHE QVFPBZSBEG. Vaibyirzrag\
jvgu gur cngvrag’f fhssrevat zvtug pnhfr uvz gb ybfr inyhnoyr\
fpvragvsvp bowrpgvivgl.\
2. OR PURRESHY NG NYY GVZRF. Lbhe qbpgbe yrnqf n ohfl naq gelvat\
yvsr naq erdhverf nyy gur tragyrarff naq ernffhenapr ur pna trg\
.\
3. GEL GB FHSSRE SEBZ GUR QVFRNFR SBE JUVPU LBH NER ORVAT GERNGRQ.\
Erzrzore gung lbhe qbpgbe unf n cebsrffvbany erchgngvba gb\
hcubyq."))
