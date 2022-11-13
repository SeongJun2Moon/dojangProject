#연습문제
with open('files/words.txt', 'r') as files:
    words = files.readlines()
    count = 0
    for word in words:
        if len(word.replace("\n","")) <= 10:
            count += 1
    print(count)

#답안
with open('files/words.txt', 'r') as files:
    words = files.readlines()
    count = 0
    for word in words:
        if len(word.strip("\n")) <= 10:
            count += 1
    print(count)

#심사문제
with open("files/words2.txt", 'r') as files:
    words = list(files.read().split(" "))
    for word in words:
        if 'c' in word:
            print(word.strip(",."))

##핵심문법1: with open(경로, 모드) as 객체이름 -> open, close 없이 파일 사용하기
##핵심문법2: 파일객체이름.read() => read모드에서 읽어낸 객체 할당, 파일객체이름.readline() => read를 한줄씩
##공부코드: .strip(삭제부분) => 문자열에서 특정부분삭제. 복수로 지정 가능.