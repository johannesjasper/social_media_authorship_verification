# Authorship Verification in Social Media Applications

This repo contains code to train a neural network that shall perform authorship verification on short text samples as found in social media applications.

The idea is to build upon the approach of Shrestha et al.[1] to combine n-gram embeddings with a CNN to learn a classifier for authorship attribution.

More details on how we extend the approach will follow.

## Setup
This project uses Chainer and Cupy running on Python3.

Install the dependencies using
```
pip install -r requirements.txt
```

[1]: [Shrestha, Prasha, et al. "Convolutional neural networks for authorship attribution of short texts."](http://www.aclweb.org/anthology/E17-2106)
```
@inproceedings{shrestha2017convolutional,
  title={Convolutional neural networks for authorship attribution of short texts},
  author={Shrestha, Prasha and Sierra, Sebastian and Gonzalez, Fabio and Montes, Manuel and Rosso, Paolo and Solorio, Thamar},
  booktitle={Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 2, Short Papers},
  volume={2},
  pages={669--674},
  year={2017}
}
```
