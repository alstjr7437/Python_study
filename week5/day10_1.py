foods = {"떡볶이":"오뎅", "짜장면":"단무지", "라면":"김치"}
foods = {}
foods["떡볶이"] = "오뎅"
foods["짜장면"] = "단무지"
foods["라면"] = "김치"

for key in foods.keys():
    print("key = ", key, "value = ", foods.get(key))

myList = [30,10,20]
print("현재 리스트 %s"%myList)

singer = {}
singer['이름'] = "트와이스"
singer['구성원 수'] = 9
singer['데뷔'] = "서바이벌 식스틴"
singer['대표 곡'] = "SIGNAL"
for k in singer.keys() :
    print("%s -> %s"%(k,singer[k]))
