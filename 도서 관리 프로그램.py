library = dict()
while True:
    switch = 0
    print("="*60)
    print("[도서 관리 프로그램]")
    print("1. 도서 등록")
    print("2. 도서 대여")
    print("3. 도서 검색")
    print("4. 전체 도서")
    print("5. 종료")
    
    num = int(input("입력 "))
    
    if num == 1:
        print("")
        book = input("등록할 도서 입력")
        if book in library :
            library[book] = library[book]+1
            print("")
            print(book,"도서가 이미 있어 한 권 추가했습니다")
            print("")
            print(library)
        else :
            library[book] = 1
            print("")
            print(book,"도서를 추가했습니다")
            print("")
            print(library)
            
    elif num == 2:
        print("")
        book = input("대여할 책 입력")
        if book in library :
            if library[book] > 0:
                library[book] = library[book]-1
                print("")
                print(book,"도서를 한 권 대여했습니다.")
                print("")
                print(library)
            else :
                print("")
                print("수량 부족")
                print("")
                print(library)
        else :
            print("")
            print("없는 도서입니다")
            
    elif num == 3:
        print("")
        book = input("검색할 책이름 1자 이상 입력")
        print("")
        for key, value in library.items():
            if book in key :
                print(key,"책", value,"권 있음.")
                switch = 1
        if switch == 0 :
            print("해당 책 없음")

    elif num == 4:
        print("")
        print(library)

    elif num == 5:
        break

    else :
        print("잘못 입력 하셨습니다")
