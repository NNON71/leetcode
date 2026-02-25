class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # arr.sort()
        # h = {}
        # for i in range(len(arr)):
        #     bi_num = bin(arr[i])[2:].count('1')
        #     if bi_num not in h:
        #         h[bi_num] = [arr[i]]
        #     else:
        #         h[bi_num].append(arr[i])
        # res = []
        # for k, v in h.items():
        #     res.extend(v)
        # return res

        for i in range(len(arr)):
            arr[i] += (arr[i].bit_count() << 32)

        arr.sort()

        mask = (1 << 32) - 1
        for i in range(len(arr)):
            arr[i] &= mask
        return arr