def return_elem_or_minus_one(index):
    short_list = [1, 2, 3]
    elem = 0
 
    try:
        elem = short_list[index]
        print("이 문장은 exception이 발생되면 실행되지 않습니다!")
    except IndexError:
        print(f"이 문장은 Exception이 발생하면 실행 됩니다")
        elem = -1
    except Exception:
        print(f"IndexError가 아닌 다른 종류의 Exception이 발생했습니다")
        elem = -1
    finally:
        print("이 문장은 exception 발생 여부와 상관없이 무조건 실행됩니다!")
 
    return elem

print(return_elem_or_minus_one(3))