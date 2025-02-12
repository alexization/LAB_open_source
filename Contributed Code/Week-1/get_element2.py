import numpy as np

def get_list_element(data_list, index):
    try:
        element = data_list[index]
    except IndexError:
        element = "인덱스 범위가 넘어갔습니다."
    
    return element

if __name__ == "__main__":
    my_list = np.arange(1, 100)
    index = int(input())

    result = get_list_element(my_list, index)
    print(result)