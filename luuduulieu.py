listRule = ['ad234hiah', 'ai4343hdih', 'ah34324d43iahd']
c = [1, 2, 3, 4, 5]
d = 0
listRulesnort =[]

def nhaprulevaolist():
    rulenew = input('nhap rule vao chuoi: ')
    listRule.append(rulenew)
    print(listRule)
    file = open('sid.txt', 'a+', encoding='UTF=8')
    file.write(rulenew)


nhaprulevaolist()

for sidrule in listRule:
    sid = sidrule[2:5]
    print(sid)


def nhaprulevaosnort():
    rulenew = input('nhap rule vao chuoi: ')
    listRulesnort.append(rulenew)
    print(listRule)
    file = open('rulesnort.txt', 'a+', encoding='UTF=8')
    file.write(rulenew)


def capnhatrule(listRulesnort, listRule):
    for rule in listRule:
        sid = rule[2:5]
        for rulesnort in listRulesnort:
            sidsnort = rulesnort[2:5]
            if sid != sidsnort:
                listRule.append(rule)
                file = open('listrule.txt', 'a+', encoding='UTF=8')
                file.write(rule)
            elif sidsnort != sid:
                listRulesnort.append(rulesnort)
                file = open('rulesnort.txt', 'a+', encoding='UTF=8')
                file.write(rulesnort)



def capnhatrulesnort(listRulesnort, listRule):
    for rulesnort in listRulesnort:
        sidsnort = rulesnort[2:5]
        for rule in listRule:
            sid = rule[2:5]
            if sidsnort != sid:
                listRulesnort.append(rulesnort)
                file = open('rulesnort.txt', 'a+', encoding='UTF=8')
                file.write(rulesnort)

