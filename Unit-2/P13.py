def DA(basic):
    return basic*0.50
def HRA(basic):
    return basic*0.20
def PF(basic):
    return basic*0.11
def ITAX(basic):
    return basic*0.14
basic=10000
da=int(DA(basic))
# print("DA :",DA(basic))
hra=int(HRA(basic))
# print("HRA :",HRA(basic))
pf=int(PF(basic))
# print("PF:",PF(basic))
itax=int(ITAX(basic))
# print("ITAX:",ITAX(basic))
gross_Salary=(basic+da+hra)
# print("Gross Salary:",gross_Salary)
net_Salary=gross_Salary-(pf+itax)
# print("Net Salary:",net_Salary)

