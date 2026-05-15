for x in range(1,10):
    for o in range(10):
        for d in range(10):
            if len({x,o,d})!=3: continue
            r=3*(100*x+10*o+d)
            if 100<=r<=999:
                m,a,t=r//100,(r//10)%10,r%10
                if len({x,o,d,m,a,t})==6:
                    print(f"{x}{o}{d}+{x}{o}{d}+{x}{o}{d}={r}")