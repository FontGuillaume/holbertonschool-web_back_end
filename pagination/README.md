# 🔄 Pagination - Holberton School Web Backend

## 📖 Description

Ce projet implémente différents types de systèmes de pagination en Python, de la pagination simple à la pagination hypermédia résistante aux suppressions. Il fait partie du cursus **Holberton School Web Backend**.

## 🎯 Objectifs d'apprentissage

- ✅ Comprendre les concepts de pagination
- ✅ Implémenter une fonction helper de calcul d'indices
- ✅ Développer une pagination simple avec validation
- ✅ Créer une pagination hypermédia (HATEOAS)
- ✅ Concevoir une pagination résistante aux suppressions

## 📂 Structure du projet

```
pagination/
├── 0-simple_helper_function.py    # Fonction helper pour indices
├── 0-main.py                      # Tests pour la fonction helper
├── 1-simple_pagination.py         # Pagination basique
├── 1-main.py                      # Tests pagination simple
├── 2-hypermedia_pagination.py     # Pagination hypermédia
├── 2-main.py                      # Tests pagination hypermédia
├── 3-hypermedia_del_pagination.py # Pagination résistante
├── 3-main.py                      # Tests pagination résistante
├── Popular_Baby_Names.csv         # Dataset d'exemple
└── README.md                      # Ce fichier
```

## 🚀 Fonctionnalités

### 1. 📊 Fonction Helper (`0-simple_helper_function.py`)

**Fonction :** `index_range(page: int, page_size: int) -> tuple`

Calcule les indices de début et de fin pour une page donnée.

```python
# Exemples
index_range(1, 7)    # Returns: (0, 7)
index_range(3, 15)   # Returns: (30, 45)
```

**🔑 Points clés :**
- Les pages commencent à 1
- Les indices commencent à 0
- Retourne un tuple (start_index, end_index)

### 2. 📄 Pagination Simple (`1-simple_pagination.py`)

**Classe :** `Server`

Implémente une pagination basique avec :
- ✅ Chargement et mise en cache du dataset CSV
- ✅ Validation des paramètres d'entrée
- ✅ Gestion des pages hors limites

```python
server = Server()
page_data = server.get_page(1, 10)  # Page 1, 10 éléments
```

**🛡️ Sécurité :**
- Validation avec `assert` pour les types et valeurs
- Gestion élégante des pages inexistantes

### 3. 🌐 Pagination Hypermédia (`2-hypermedia_pagination.py`)

**Méthode :** `get_hyper(page: int, page_size: int) -> dict`

Implémente le pattern **HATEOAS** (Hypermedia as the Engine of Application State).

```python
{
    'page_size': 10,
    'page': 1,
    'data': [...],
    'next_page': 2,
    'prev_page': None,
    'total_pages': 89
}
```

**🎨 Avantages :**
- Navigation intuitive entre les pages
- Métadonnées complètes pour les clients
- Respect des standards REST

### 4. 🔒 Pagination Résistante (`3-hypermedia_del_pagination.py`)

**Méthode :** `get_hyper_index(index: int, page_size: int) -> dict`

Pagination qui reste cohérente même lors de suppressions d'éléments.

```python
{
    'index': 3,
    'next_index': 13,
    'page_size': 10,
    'data': [...]
}
```

**💡 Innovation :**
- Utilise des index absolus au lieu de positions relatives
- Maintient la cohérence lors de suppressions
- Idéal pour les systèmes temps réel

## 🛠️ Installation et utilisation

### Prérequis

```bash
python3 --version  # Python 3.7+
```

### Exécution des tests

```bash
# Test fonction helper
python3 0-main.py

# Test pagination simple
python3 1-main.py

# Test pagination hypermédia
python3 2-main.py

# Test pagination résistante
python3 3-main.py
```

### Formatage du code

```bash
# Installation autopep8
pip3 install autopep8

# Formatage standard
autopep8 --in-place *.py

# Formatage agressif
autopep8 --in-place --aggressive --aggressive *.py

# Respect des 80 caractères
autopep8 --in-place --max-line-length=80 *.py
```

## 📚 Concepts techniques

### 🔢 Calcul des indices

```python
# Pour la page P avec une taille S :
start_index = (page - 1) * page_size
end_index = start_index + page_size
```

### 🧠 Pattern Lazy Loading

```python
if self.__dataset is None:
    # Chargement à la demande
    self.__dataset = load_data()
```

### 🗂️ Indexation pour résistance

```python
# Dictionnaire {index_original: données}
indexed_data = {i: row for i, row in enumerate(dataset)}
```

## 📊 Dataset

Le projet utilise **Popular_Baby_Names.csv** contenant :
- 👶 Prénoms populaires de bébés
- 📅 Données historiques
- 🔢 Plus de 19,000 entrées

## 🎨 Bonnes pratiques appliquées

- ✅ **Type hints** pour la lisibilité
- ✅ **Docstrings** complètes
- ✅ **Validation des entrées** robuste
- ✅ **Gestion d'erreurs** élégante
- ✅ **Code PEP8** compliant
- ✅ **Commentaires** détaillés

## 🤝 Auteur

**Guillaume Font** - Étudiant Holberton School

---

## 📝 License

Ce projet est réalisé dans le cadre du cursus Holberton School.

---

*Happy coding! 🚀*