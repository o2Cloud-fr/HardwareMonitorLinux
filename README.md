# 🖥️ Linux Hardware Monitor

**Linux Hardware Monitor** est une application graphique permettant de surveiller en temps réel les performances et caractéristiques matérielles d'un système Linux. L'application utilise une interface moderne avec le thème Arc et fournit des informations détaillées sur le CPU, la RAM, le GPU et le système.

- ✅ Surveillance CPU en temps réel 📊
- ✅ Monitoring mémoire RAM et SWAP 💾
- ✅ Support des cartes NVIDIA 🎮
- ✅ Interface graphique moderne avec thème Arc 🎨
- ✅ Mise à jour automatique des données 🔄

## ✨ Fonctionnalités

- 🔍 Surveillance en temps réel des performances du processeur et des températures
- 📈 Monitoring détaillé de l'utilisation de la mémoire RAM et du SWAP
- 🎮 Détection et surveillance des cartes graphiques NVIDIA
- 🎨 Interface graphique moderne avec le thème Arc
- 🔄 Mise à jour automatique des données toutes les 3 secondes
- 📑 Support multi-onglets pour une organisation claire des informations
- 📋 Affichage des informations système détaillées

## 📋 Pré-requis

- 🐧 Linux (Ubuntu, Debian, Fedora, etc.)
- 🐍 Python 3.8 ou supérieur
- 📚 Bibliothèques système requises 
- 🎮 Pilotes NVIDIA (optionnel, pour le monitoring GPU)

## 🚀 Installation

1. Clonez ce dépôt sur votre machine locale :
```bash
git clone https://github.com/votre-username/linux-hardware-monitor.git
```

2. Installez les dépendances système nécessaires (Ubuntu/Debian) :
```bash
sudo apt-get update
sudo apt-get install python3-pip python3-dev python3-venv build-essential libxcb-xinerama0
```

3. Créez un environnement virtuel (recommandé) :
```bash
python3 -m venv env
source env/bin/activate
```

4. Installez les dépendances Python :
```bash
pip install -r requirements.txt
```

## 🎯 Utilisation

1. Activez l'environnement virtuel si vous en utilisez un :
```bash
source env/bin/activate
```

2. Lancez l'application :
```bash
python hardware_monitor.py
```

## 📂 Structure du Projet

```
linux-hardware-monitor/
├── hardware_monitor.py
├── requirements.txt
├── README.md
└── LICENSE
```

## 👨‍💻 Auteurs

- [@o2Cloud-fr](https://www.github.com/o2Cloud-fr)

## 🔖 Badges

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)]()
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()
[![PyQt6](https://img.shields.io/badge/GUI-PyQt6-green.svg)]()

## 🤝 Contribution

Les contributions sont toujours les bienvenues!

Voir `contributing.md` pour commencer.

## 💬 Feedback

Si vous avez des commentaires, vous pouvez nous contacter à github@o2cloud.fr

## 🔗 Liens

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://votre-portfolio.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/votre-profil/)

## 🛠️ Compétences

Python, PyQt, Linux System Programming

## 📝 Licence

[MIT License](LICENSE)

## 🗺️ Feuille de route

- 🎮 Support pour d'autres systèmes de monitoring GPU (AMD, Intel)
- 📊 Ajout de graphiques pour visualiser les tendances
- 🔔 Support des notifications système
- 🌓 Mode dark/light pour le thème
- 💾 Export des données en CSV/JSON

## 🆘 Support

Pour obtenir de l'aide, envoyez un email à github@o2cloud.fr

## 💻 Technologies utilisées

- 🐍 Python
- 🖼️ PyQt6
- 📊 psutil
- 🐧 Linux

## 👥 Utilisé par

Ce projet est utilisé par les personnes suivantes :
- 👨‍💻 Administrateurs système Linux
- 👩‍💻 Développeurs
- 🖥️ Utilisateurs souhaitant monitorer leur système
