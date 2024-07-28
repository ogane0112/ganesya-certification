def bubble_sort(arr):
    n = len(arr)
    # 配列全体を繰り返し処理
    for i in range(n):
        # 最後のi個はすでにソート済み
        for j in range(0, n-i-1):
            # 隣接する要素を比較し、順番が逆なら交換
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 使用例
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("ソート後の配列:", sorted_arr)
