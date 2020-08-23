"""

##### Obligatorisk oppgave 2 i IN1020 #####

WHILE   INP
        BRZ END
        STA INPUT
        LDA TELLER
        ADD ADD_EN
        STA TELLER
        LDA INPUT
        SUB MAX
        BRP POSITIV
        BRA WHILE
POSITIV LDA INPUT
        STA MAX
        BRA WHILE
END     LDA n
        OTC
        LDA =
        OTC
        LDA TELLER
        OUT
        LDA l
        OTC
        LDA M
        OTC
        LDA a
        OTC
        LDA x
        OTC
        LDA =
        OTC
        LDA MAX
        OUT
        HLT
INPUT   DAT
TELLER  DAT
ADD_EN  DAT 1
MAX     DAT
n       DAT 110
=       DAT 61
l       DAT 10
M       DAT 77
a       DAT 97
x       DAT 120

"""
