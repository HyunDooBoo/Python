library = dict()
while True:
    switch = 0
    print("="*60)
    print("[도서 관리 프로그램]")
    print("1. 도서 등록")
    print("2. 도서 대여")
    print("3. 도서 검색")
    print("4. 전체 도서")
    print("5. 도서명 변경")
    print("6. 종료\n")
    
    num = int(input("입력 : "))
    
    if num == 1:
        book = input("\n등록할 도서 입력 : ")
        if book in library :
            library[book] = library[book]+1
            print(book,"도서가 이미 등록되있어 한 권 추가했습니다\n")
            print(library)
        else :
            library[book] = 1
            print("\n", book,"도서를 한 권 추가했습니다\n",sep="")
            print(library)
            
    elif num == 2:
        book = input("\n대여할 책 입력 : ")
        if book in library :
            if library[book] > 0:
                library[book] = library[book]-1
                print("\n",book,"도서를 한 권 대여했습니다.\n",sep="")
                print(library)
            else :
                print("\n수량 부족\n")
                print(library)
        else :
            print("\n없는 도서입니다")
            
    elif num == 3:
        book = input("\n검색할 책이름 1자 이상 입력 : ")
        print("")
        for key, value in library.items():
            if book in key :
                print(key,"책", value,"권 있음.")
                switch = 1
        if switch == 0 :
            print("\n해당 책 없음")

    elif num == 4:
        print("\n",library)

    elif num == 5:
        book = input("\n변경하고 싶은 책의 이름을 입력 : ")
        if book in library:
            new = input("\n새로운 이름 입력 : ")
            if new in library:
                print("\n이미 있는 책입니다.")
            else :
                library[new] = library.pop(book)
                print("\n변경 완료 됐습니다.\n")
        else :
            print("\n해당 책 없음")

    elif num == 6:
        break

    else :
        print("잘못 입력 하셨습니다")
