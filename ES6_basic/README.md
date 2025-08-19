# ES6 Basic

## 📖 Description

Ce projet explore les fonctionnalités essentielles d'ECMAScript 6 (ES2015) à travers une série d'exercices pratiques. Il couvre les concepts fondamentaux comme les variables block-scoped, les arrow functions, les paramètres par défaut, et bien plus encore.

## 🎯 Objectifs d'apprentissage

À la fin de ce projet, vous serez capable d'expliquer :

- ✅ Ce qu'est ES6
- ✅ Les nouvelles fonctionnalités introduites dans ES6
- ✅ La différence entre une constante et une variable
- ✅ Les variables block-scoped
- ✅ Les arrow functions et leurs paramètres par défaut
- ✅ Les paramètres rest et spread
- ✅ Les template literals en ES6
- ✅ La création d'objets et leurs propriétés en ES6
- ✅ Les iterators et les boucles for-of

## 🛠️ Technologies utilisées

- **Node.js** 20.x.x
- **npm** 9.x.x
- **Babel** pour la transpilation ES6
- **ESLint** pour l'analyse de code
- **Jest** pour les tests

## ⚙️ Installation

### 1. Installer Node.js 20.x.x

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

### 2. Vérifier l'installation

```bash
nodejs -v  # v20.15.1
npm -v     # 10.7.0
```

### 3. Installer les dépendances du projet

```bash
cd ES6_basic
npm install
```

## 📁 Structure du projet

```
ES6_basic/
├── 0-constants.js              # Variables const et let
├── 1-block-scoped.js          # Variables block-scoped
├── 2-arrow.js                 # Arrow functions
├── 3-default-parameter.js     # Paramètres par défaut
├── 4-rest-parameter.js        # Paramètres rest
├── 5-spread-operator.js       # Opérateur spread
├── 6-string-interpolation.js  # Template literals
├── 7-getBudgetObject.js       # Propriétés d'objet raccourcies
├── 8-getBudgetCurrentYear.js  # Propriétés calculées
├── 9-getFullBudget.js         # Méthodes ES6
├── 10-loops.js                # Boucles for...of
├── 11-createEmployeesObject.js # Objets avec clés dynamiques
├── 12-createReportObject.js   # Objets avec méthodes
├── babel.config.js            # Configuration Babel
├── package.json               # Dépendances et scripts
├── .eslintrc.js              # Configuration ESLint
└── README.md                 # Ce fichier
```

## 🚀 Scripts disponibles

```bash
# Lancer ESLint sur tous les fichiers
npm run lint

# Vérifier les fichiers d'exercices
npm run check-lint

# Exécuter avec Babel
npm run dev <fichier>

# Lancer les tests Jest
npm test

# Test complet (ESLint + Jest)
npm run full-test
```

## 📝 Exercices

### 0. Const or let?
Conversion de `var` en `const` et `let` selon les bonnes pratiques.

### 1. Block Scope
Utilisation du block scope pour éviter l'écrasement de variables.

### 2. Arrow functions
Réécriture de fonctions avec la syntaxe arrow ES6.

### 3. Default parameters
Implémentation de paramètres par défaut dans les fonctions.

### 4. Rest parameter syntax
Utilisation de l'opérateur rest (`...args`) pour gérer un nombre variable d'arguments.

### 5. Spread operator
Utilisation de l'opérateur spread pour concaténer des tableaux et étaler des chaînes.

### 6. Template literals
Utilisation des template literals pour l'interpolation de chaînes.

### 7. Object property shorthand
Utilisation de la syntaxe raccourcie pour les propriétés d'objet.

### 8. Computed property names
Création d'objets avec des noms de propriétés calculés.

### 9. ES6 method properties
Utilisation de la syntaxe ES6 pour les méthodes d'objet.

### 10. For...of loops
Remplacement des boucles `for...in` par `for...of`.

### 11. Iterator
Création d'objets avec des clés dynamiques.

### 12. Report object
Création d'objets complexes avec méthodes et propriétés.

## 🧪 Exemples d'utilisation

```bash
# Tester un exercice spécifique
npm run dev 0-main.js

# Vérifier le style de code
npm run lint 0-constants.js

# Corriger automatiquement les erreurs de style
npm run lint 0-constants.js --fix

# Lancer tous les tests
npm run full-test
```

## 📋 Prérequis

- Ubuntu 20.04 LTS
- Node.js 20.x.x
- npm 9.x.x

## 📚 Ressources

- [ECMAScript 6 - ECMAScript 2015](https://www.ecma-international.org/ecma-262/6.0/)
- [Statements and declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
- [Rest parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
- [Javascript ES6 — Iterables and Iterators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators)

## 👨‍💻 Auteur

**Guillaume** - Holberton School

## 📄 Licence

Ce projet est réalisé dans le cadre du cursus Holberton School.

---

> **Note :** N'oubliez pas d'ajouter le dossier `node_modules/` dans votre `.gitignore` !