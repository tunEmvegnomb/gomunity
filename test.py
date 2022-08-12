hashtag_list = "#python javascript"

hashtag_list = hashtag_list.split(" ")
for i in hashtag_list:
    if not i[0].startswith("#"):
        print("해시태그는 앞에 샵이 붙어야됩니다")