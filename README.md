# histox-contrib

**Community-contributed GPL-3 extensions for [HistoX](https://github.com/你的用户名/histox).**

This package provides additional deep learning tools for HistoX that are licensed under the
GNU General Public License v3 (GPL-3). It is distributed separately from the main HistoX
package to keep the core library free from GPL restrictions.

> Based on [slideflow-gpl](https://github.com/slideflow/slideflow-gpl) by James Dolezal,
> adapted for HistoX.

---

## Installation

```bash
pip install histox-contrib
```

Or install from source:

```bash
git clone https://github.com/你的用户名/histox-contrib.git
cd histox-contrib
pip install -e .
```

> **Note:** `histox` must be installed first.
>
> ```bash
> pip install histox
> ```

---

## Features

| Module | Description |
|--------|-------------|
| **RetCCL** | Pretrained feature extractor (RetCCL) |
| **CTransPath** | Pretrained feature extractor (CTransPath) |
| **CLAM** | Clustering-constrained Attention Multiple Instance Learning |

---

## Usage

Once installed, `histox-contrib` automatically registers its components into HistoX
via the plugin system. No manual import is required.

```python
import histox as hx

# RetCCL and CTransPath are available after histox-contrib is installed
extractor = hx.build_feature_extractor('retccl')
```

---

## License

This project is licensed under the **GNU General Public License v3.0**.
See [LICENSE](LICENSE) for details.

This package is based on
[slideflow-gpl](https://github.com/slideflow/slideflow-gpl)
(Copyright 2024 James Dolezal), modified and adapted for HistoX.

---

## Citation

If you use this package in your research, please cite the original works:

**RetCCL:**
```
@article{wang2023retccl,
  title={RetCCL: Clustering-guided contrastive learning for whole-slide image retrieval},
  author={Wang, Xiyue and others},
  journal={Medical Image Analysis},
  year={2023}
}
```

**CTransPath:**
```
@article{wang2022ctranspath,
  title={Transformer-based unsupervised contrastive learning for histopathological image classification},
  author={Wang, Xiyue and others},
  journal={Medical Image Analysis},
  year={2022}
}
```

**CLAM:**
```
@article{lu2021clam,
  title={Data-efficient and weakly supervised computational pathology on whole-slide images},
  author={Lu, Ming Y and others},
  journal={Nature Biomedical Engineering},
  year={2021}
}
```