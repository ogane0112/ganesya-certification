def quick_sort(data, left, right):
    i = left  # left_index
    j = right  # right_index
    pivot = (left + right) // 2  # 軸

    # ソート対象のインデックスを探索
    while True:
        while data[i] < data[pivot]:
            i = i + 1
        while data[j] > data[pivot]:
            j = j - 1
        # 無限ループ終了条件
        if i >= j:
            break
        # 交換
        tmp = data[i]
        data[i] = data[j]
        data[j] = tmp
        # 範囲を一つ狭める
        i = i + 1
        j = j - 1

    # 再帰処理
    if left < i - 1:
        quick_sort(data, left, i - 1)
    if right > j + 1:
        quick_sort(data, j + 1, right)