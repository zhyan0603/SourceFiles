### Exploration iterations for Garnet without ZBL

---

Exploration iterations for Garnet ***without ZBL potential***. The Failure Ratio (FR) represents the fraction of unphysical structures within the trajectory relative to the total structure count. Unphysical structures are filtered out during the sampling process. min\_distance=0.008 is used in the Farthest Point Sample.

| Iter | t (ps) |  Sample1   |  Sample2   |  Sample3   |  Sample4   | Nsamp | FR (%) | Update? |
| :--: | :----: | :--------: | :--------: | :--------: | :--------: | :---: | :----: | :-----: |
|  1   |   20   |  100-400K  |  100-400K  |  500-800K  |  500-800K  |  96   |   0%   |   yes   |
|  2   |   50   |  100-400K  |  100-400K  |  500-800K  |  500-800K  |  30   |   0%   |   yes   |
|  3   |  100   |  100-400K  |  500-800K  |  500-800K  |  500-800K  |  68   |   0%   |   yes   |
|  4   |  500   |  500-800K  |  500-800K  |  500-800K  |  500-800K  |   5   |   0%   |   no    |
|  5   |   20   | 800-1000K  | 800-1000K  | 800-1000K  | 800-1000K  |  43   |   0%   |   yes   |
|  6   |   50   | 800-1000K  | 800-1000K  | 1000-1200K | 1000-1200K |  231  |  8.8%  |   yes   |
|  7   |   50   | 800-1000K  | 800-1000K  | 1000-1200K | 1000-1200K |   8   |   0%   |   no    |
|  8   |  100   | 800-1000K  | 800-1000K  | 1000-1200K | 1000-1200K |  21   |  1.6%  |   yes   |
|  9   |  100   | 800-1000K  | 800-1000K  | 1000-1200K | 1000-1200K |  145  |   0%   |   yes   |
|  10  |  500   | 800-1000K  | 800-1000K  | 1000-1200K | 1000-1200K |  31   | 10.6%  |   yes   |
|  11  |  500   | 800-1000K  | 800-1000K  | 1000-1200K | 1000-1200K |   8   |   0%   |   no    |
|  12  |  500   | 1000-1200K | 1000-1200K | 1000-1200K | 1000-1200K |  16   |   0%   |   no    |
|  13  |        |            |            |            |            |       |        |   yes   |