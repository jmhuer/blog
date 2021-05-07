# Algorithm Summary

## Bandit Algorithms
*Second Edition; Richard Sutton and Andrew Barto*


Bandit Algorithms | Notes | Regret Bound
 --- | --- |  ---
ETC |  Assume 1-subgaussian bandit page#80 | Assume 1-subgaussian bandit $R_{n} \leq m \sum_{i=1}^{k} \Delta_{i}+(n-m k) \sum_{i=1}^{k} \Delta_{i} \exp \left(-\frac{m \Delta_{i}^{2}}{4}\right)$  <br /> Further assume:  <br />  k = 2 <br /> $m=\max \left\{1,\left[\frac{4}{\Delta^{2}} \log \left(\frac{n \Delta^{2}}{4}\right)\right]\right\}$
ETC Doubling Trick |  Assume 1-subgaussian bandit page#80 | Assume 1-subgaussian bandit $R_{n} \leq m \sum_{i=1}^{k} \Delta_{i}+(n-m k) \sum_{i=1}^{k} \Delta_{i} \exp \left(-\frac{m \Delta_{i}^{2}}{4}\right)$  <br /> Further assume:  <br />  k = 2 <br /> $m=\max \left\{1,\left[\frac{4}{\Delta^{2}} \log \left(\frac{n \Delta^{2}}{4}\right)\right]\right\}$
e-greedy |  Assume 1-subgaussian bandit page#80 | Assume 1-subgaussian bandit $R_{n} \leq m \sum_{i=1}^{k} \Delta_{i}+(n-m k) \sum_{i=1}^{k} \Delta_{i} \exp \left(-\frac{m \Delta_{i}^{2}}{4}\right)$  <br /> Further assume:  <br />  k = 2 <br /> $m=\max \left\{1,\left[\frac{4}{\Delta^{2}} \log \left(\frac{n \Delta^{2}}{4}\right)\right]\right\}$
UCB |  Assume 1-subgaussian bandit page#80 | Assume 1-subgaussian bandit $R_{n} \leq m \sum_{i=1}^{k} \Delta_{i}+(n-m k) \sum_{i=1}^{k} \Delta_{i} \exp \left(-\frac{m \Delta_{i}^{2}}{4}\right)$  <br /> Further assume:  <br />  k = 2 <br /> $m=\max \left\{1,\left[\frac{4}{\Delta^{2}} \log \left(\frac{n \Delta^{2}}{4}\right)\right]\right\}$

