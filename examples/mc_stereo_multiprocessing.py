from oopnet.api import *
from multiprocessing import Pool
import os

def roll_the_dice(network=None):
    cnet = Copy(network)
    for j in cnet.junctions:
        j.demand += np.random.normal(0.0, 1.0)
    rpt = Run(cnet)
    return Pressure(rpt)


if __name__ == '__main__':

    pool = Pool()
    filename = os.path.join('data', 'Poulakis.inp')

    net = Read(filename)

    mcruns = 1000
    p = list(pool.map(roll_the_dice, [net] * mcruns))

    p = pd.DataFrame(p, index=list(range(len(p))))
    print(p)

    pmean = p.mean()
    print(pmean)

    psub = p.sub(pmean, axis=1)

    x = np.linspace(-1.5, 1.5, 40)
    psub[['J-03', 'J-31']].hist(bins=x, layout=(2, 1))
    Show()
