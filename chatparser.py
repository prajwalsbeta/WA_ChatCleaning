import re
import demoji
filenames = ["WhatsApp Unprocessed1"]

for names in filenames:
    with open(names + ".txt", encoding="utf8") as file_handle:
        print(names + ".txt has been opened")
        f = open(names + "out.txt", 'w')
        for line in file_handle:
            line = demoji.replace_with_desc(line, "")
            # print(line)
            temp = re.sub(r'.*-', '-', line)
            line = temp[2:]
            f.write(line)
# print(line)
file_handle.close()
