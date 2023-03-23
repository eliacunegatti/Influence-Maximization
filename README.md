# Large-scale multi-objective influence maximisation with network downscaling

Codebase for the experiments reported in:
*Large-scale multi-objective influence maximisation with network downscaling, Elia Cunegatti, Giovanni Iacca, Doina Bucur,
Parallel Problem Solving from Nature, Springer, Dortmund 2022, to appear  **[[link]](https://link.springer.com/chapter/10.1007/978-3-031-14721-0_15)** **[[pre-print]](https://doi.org/10.48550/arXiv.2204.06250)***

<ins>DOI</ins> : https://doi.org/10.1007/978-3-031-14721-0_15

Please cite our paper if you use our codes!!

```
@inproceedings{cunegatti2022large,
  title={Large-scale multi-objective influence maximisation with network downscaling},
  author={Cunegatti, Elia and Iacca, Giovanni and Bucur, Doina},
  booktitle={Parallel Problem Solving from Nature--PPSN XVII: 17th International Conference, PPSN 2022, Dortmund, Germany, September 10--14, 2022, Proceedings, Part II},
  pages={207--220},
  year={2022},
  organization={Springer}
}
```

Code folder provides the code scripts for:

- Downscaling process [downscaling.py](downscaling.py)
- Upscaling Process [upscaling.py](upscaling.py)
- Multi-Objective Optimization with EA (MOEA) [influence_maximization.py](influence_maximization.py)

## Code's Parameters

For each file you want to run, just run the following command to access all the code's parameters:
```bash
python name_scipt.py --help
```

## Requirements

```bash
pip install requirements.txt
```

For the correct execution of downscaling.py the **graph-tool** library is needed. Please refer to the official [website](https://graph-tool.skewed.de) for the correct package installation.


## Acknowledgements

Our MOEA implementation is an extention of a work proposed in *Iacca, G., Konotopska, K., Bucur, D., & Tonda, A.P. (2021). An evolutionary framework for maximizing influence propagation in social networks. Softw. Impacts, 9, 100107.*

If you used this code please remember to also include the following citation:
```
@article{Iacca2021AnEF,
  title={An evolutionary framework for maximizing influence propagation in social networks},
  author={Giovanni Iacca and Kateryna Konotopska and Doina Bucur and Alberto Paolo Tonda},
  journal={Softw. Impacts},
  year={2021},
  volume={9},
  pages={100107}
}
```
## Contribution

Authors:
 
- Elia Cunegatti, MSc Student University of Trento (Italy)
- Giovanni Iacca, Associate Professor University of Trento (Italy) [website](https://sites.google.com/site/giovanniiacca/)
- Doina Bucur, Associate Professor University of Twente (The Netherlands) [website](http://doina.net)

For every type of doubts/questions about the repository please do not hesitate to contact me: elia.cunegatti@unitn.it
