class Main:
    @staticmethod
    def count_unique(sorted_num_list) -> int:
        if len(sorted_num_list) == 0:
            return 0
        unique = sorted_num_list[0]
        count = 1
        for currentNum in sorted_num_list:
            if unique != currentNum:
                count += 1
                unique = currentNum
        return count