data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
avg = sum_len / len(data)
print('每個留言的平均字數為:', avg)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

# good = [d for d in data if 'good' in d]
# output = [(number-1) for munber in reference if number % 2 == 0]
# 第一個d是good.append(d)中的d, 也不一定要是d, 可以是1, 就會在good清單中裝162550筆1

bad =['bad' in d for d in data]
print(bad)
# 上下兩種寫法相等
bad == []
for d in data:
	bad.append('bad' in d)