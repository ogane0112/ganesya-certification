def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 配列を2つに分割
    mid = len(arr) // 2
    #再帰的に処理する！
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # 2つの部分配列をマージ
    return merge(left, right)

def merge(left, right):
    sorted_array = []
    i = j = 0
    
    # 左右の部分配列を比較し、昇順にマージ
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    # 残りの要素をマージ
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    #もしソートされた状態の配列が渡された場合やその数字一がそこでいい場合などを考えるとこれがないとソートを正しく行えない！
    
    return sorted_array

# テスト用のリスト
test_list = [3, 6, 8, 10, 1, 2, 1]

# ソート前のリスト
print("Original list:", test_list)

# マージソートの実行
sorted_list = merge_sort(test_list)

# ソート後のリスト
print("Sorted list:", sorted_list)
