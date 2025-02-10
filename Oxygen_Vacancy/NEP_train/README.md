### NEP version 3.9.1

---

```
***************************************************************
*                 Welcome to use GPUMD                        *
*    (Graphics Processing Units Molecular Dynamics)           *
*                    Version 3.9.1                            *
*              This is the nep executable                     *
***************************************************************
```

### Hyperparameter

---

```
Input or default parameters:
    (default) model_type = potential.
    (default) calculation mode = train.
    (input)   use NEP version 4.
    (input)   number of atom types = 4.
        (default) type 0 (Li with Z = 3) has force weight of 1.
        (default) type 1 (La with Z = 57) has force weight of 1.
        (default) type 2 (Zr with Z = 40) has force weight of 1.
        (default) type 3 (O with Z = 8) has force weight of 1.
    (default) will not add the ZBL potential.
    (input)   radial cutoff = 7.5 A.
    (input)   angular cutoff = 4 A.
    (input)   n_max_radial = 4.
    (input)   n_max_angular = 4.
    (input)   basis_size_radial = 12.
    (input)   basis_size_angular = 12.
    (input)   l_max_3body = 4.
    (input)   l_max_4body = 2.
    (input)   l_max_5body = 0.
    (input)   number of neurons = 30.
    (default) lambda_1 = 0.076948.
    (default) lambda_2 = 0.076948.
    (input)   lambda_e = 1.
    (input)   lambda_f = 1.
    (input)   lambda_v = 0.1.
    (default) lambda_shear = 1.
    (default) force_delta = 0.
    (input)   batch size = 1000.
    (input)   population size = 50.
    (input)   maximum number of generations = 30000.
Some calculated parameters:
    number of radial descriptor components = 5.
    number of angular descriptor components = 25.
    total number of descriptor components = 30.
    NN architecture = 30-30-1.
    number of NN parameters to be optimized = 3841.
    number of descriptor parameters to be optimized = 2080.
    total number of parameters to be optimized = 5921.
```

