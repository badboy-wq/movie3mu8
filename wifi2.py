def pass1():
    list1=[]

    with open("D:/1.txt", "w") as f:
        # for item in sorted(list):
        #     f.writelines(item)
        #     f.writelines('\n')
        #
        # for i in range(1,9):
        #     for a in range(1,9):
        #         ps=(str(i),str(a))
        #         a = (" ".join(ps))
        #         f.writelines(a)
        #         f.writelines('\n')
        #         print(a)

        for i in range(0, 10):
            for a in range(0, 10):
                for b in range(0, 10):
                    for c in range(0, 10):
                        for d in range(0, 10):
                            for e in range(0, 10):
                                for g in range(0, 10):
                                    for h in range(0, 10):
                                        ps = (str(i), str(a), str(b), str(c), str(d), str(e), str(g), str(h))

                                        # print(ps)
                                        # c=list(map(str,(ps)))

                                        # a = (" ".join(ps))

                                        f.writelines(ps)
                                        f.writelines('\n')
                                        # print(a)
def pass2():
    list1=[]

    with open("D:/2.txt", "w") as book:
        # for item in sorted(list):
        #     f.writelines(item)
        #     f.writelines('\n')
        #
        # for i in range(1,9):
        #     for a in range(1,9):
        #         ps=(str(i),str(a))
        #         a = (" ".join(ps))
        #         f.writelines(a)
        #         f.writelines('\n')
        #         print(a)

        for i in range(0, 10):
            for a in range(0, 10):
                for b in range(0, 10):
                    for c in range(0, 10):
                        for d in range(0, 10):
                            for e in range(0, 10):
                                for g in range(0, 10):
                                    for h in range(0, 10):
                                        for j in range(0, 10):
                                            for k in range(0, 10):
                                                for m in range(0, 10):

                                                    ps = (str(i), str(a), str(b), str(c), str(d), str(e), str(g), str(h),str(j),str(k),str(m))

                                        # print(ps)
                                        # c=list(map(str,(ps)))

                                        # a = (" ".join(ps))

                                                    book.writelines(ps)
                                                    book.writelines('\n')
                                        # print(a)


if __name__ == '__main__':
    pass2()