# 601
# 704
from collections import Counter

class Args:
    def __str__(self):
        return f"{self.count}, {self.start}, {self.end}, {self.is_p}, {self.num_p}"

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def get_args():
            args = Args()
            args.start = -1
            args.end = -1
            args.num_p = 0
            args.is_p = False
            args.count = 0
            return args

        def get_answer(formula):
            counts = Counter()
            args = get_args()
            def x(args, counts):
                if args.is_p:
                    answer = get_answer(formula[args.start:args.end+1])
                    for i in range(args.count if args.count > 0 else 1):
                        counts += answer
                else:
                    counts[formula[args.start:args.end+1]] += args.count if args.count > 0 else 1

            for i, c in enumerate(formula):
                if c.isupper():
                    if args.num_p == 0 and args.start != -1:
                        x(args, counts)
                        args = get_args()
                    if args.start == -1:
                        args.start = i
                    args.end = i
                elif c.islower():
                    args.end = i
                elif c == "(":
                    if args.num_p == 0 and args.start != -1:
                        x(args, counts)
                        args = get_args()
                        args.start = i + 1
                    elif args.start == -1:
                        args.start = i + 1
                    args.num_p += 1
                    args.is_p = True
                elif c == ")":
                    args.num_p -= 1
                else:
                    if args.num_p == 0:
                        args.count = args.count * 10 + int(c)
                    else:
                        args.end = i
            if args.num_p == 0 and args.start != -1:
                x(args, counts)
            return counts
        answer = []
        counts = get_answer(formula)
        for key in sorted(counts.keys()):
            count = counts[key]
            answer.append(key if count == 1 else f"{key}{count}")
        return "".join(answer)
        