print(format(0, '08b'))
test_text = text_to_binary("00 25")
tt = ""
for x in range(0, len(test_text), 8):
    tt += test_text[x:x + 8] + " "
print(tt)
