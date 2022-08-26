# Génération d'images satellite par le réseau GAN OASIS


## Setup
cloner le repository suivant:
```
git clone https://github.com/boschresearch/OASIS.git
cd OASIS
```

```
pip -m venv <PATH_TO_ENV>
pip install -r requirements.txt
```
## Datasets

Le jeu de donnée doit respecter le format courant du type CityscapeDataset

## Entraînement du modèle

```
python train.py --name AmpliGAN --batch_size 12 --dataroot Real/ --dataset_mode custom --num_workers 4
```

## Test du modèle
```
python test.py --name AmpliGAN --batch_size 12 --dataroot Real/ --dataset_mode custom --num_workers 4
```

### Autres informations

D'autres paramètres sont réglables, ils sont détaillées dans le fichier config.py
Nous avons mis quelques exemple d'images générées par le réseau. 

## License

This project is open-sourced under the AGPL-3.0 license. See the
[LICENSE](LICENSE) file for details.

For a list of other open source components included in this project, see the
file [3rd-party-licenses.txt](3rd-party-licenses.txt).

 nor monitored in any way.
