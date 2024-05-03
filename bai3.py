from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import math

# Hàm kiểm tra và chuyển đổi chuỗi đầu vào
def parse_input(input_text):
    return [int(x) for x in input_text.split(',') if x.strip().isdigit()]

# Hàm Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Hàm Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

# Hàm Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Hàm Merge Sort
def merge(arr, l, m, r):
    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]
    i, j, k = 0, 0, l
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)
    return arr


class Form1(Form1Template):
  def __init__(self, **properties):
        self.init_components(**properties)
        self.sort_options = ["Insertion Sort", "Selection Sort", "Bubble Sort", "Merge Sort"]
        self.sort_dropdown.items = self.sort_options

  def sort_button_click(self, **event_args):
        # Lấy dữ liệu từ TextBox
        input_text = self.numbers_text_box.text
        
        # Chuyển đổi thành danh sách số nguyên
        arr = parse_input(input_text)
        
        # Lựa chọn thuật toán sắp xếp
        sort_choice = self.sort_dropdown.selected_value
        
        # Sắp xếp dựa trên lựa chọn
        if sort_choice == "Insertion Sort":
            sorted_arr = insertion_sort(arr)
        elif sort_choice == "Selection Sort":
            sorted_arr = selection_sort(arr)
        elif sort_choice == "Bubble Sort":
            sorted_arr = bubble_sort(arr)
        elif sort_choice == "Merge Sort":
            merge_sort(arr, 0, len(arr) - 1)
            sorted_arr = arr
        
        # Hiển thị kết quả
        self.result_label.text = "Sắp xếp: " + ', '.join(map(str, sorted_arr))
