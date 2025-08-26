# ES6 Data Manipulation

Ce projet regroupe une série d’exercices pour s’entraîner à manipuler des données en JavaScript moderne (ES6). Chaque exercice aborde une notion clé : tableaux, objets, Set, Map, filter, map, reduce, etc.

## Table des matières

- [0. getListStudents](#0-getliststudents)
- [1. getListStudentIds](#1-getliststudentids)
- [2. getStudentsByLocation](#2-getstudentsbylocation)
- [3. getIdsSum](#3-getidssum)
- [4. updateStudentGradeByCity](#4-updatestudentgradebycity)
- [5. typedArrays](#5-typedarrays)
- [6. set](#6-set)
- [7. hasArrayValues](#7-hasarrayvalues)
- [8. cleanSet](#8-cleanset)
- [9. groceriesList](#9-grocerieslist)
- [10. updateUnikItems](#10-updateuniqitems)

---

## 0. getListStudents

**Fichier :** `0-get_list_students.js`

Fonction qui retourne un tableau d’objets étudiants, chacun ayant :
- `id` (Number)
- `firstName` (String)
- `location` (String)

**Exemple de retour :**
```js
[
  { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
  { id: 2, firstName: 'James', location: 'Columbia' },
  { id: 5, firstName: 'Serena', location: 'San Francisco' }
]
```

---

## 1. getListStudentIds

**Fichier :** `1-get_list_student_ids.js`

Fonction qui prend un tableau d’objets étudiants et retourne un tableau de leurs `id`.  
Si l’argument n’est pas un tableau, retourne un tableau vide.

**Exemple :**
```js
getListStudentIds(getListStudents());
// [1, 2, 5]
```

---

## 2. getStudentsByLocation

**Fichier :** `2-get_students_by_loc.js`

Fonction qui retourne un tableau d’étudiants situés dans une ville donnée.  
Utilise la méthode `filter`.

**Exemple :**
```js
getStudentsByLocation(getListStudents(), 'San Francisco');
// [
//   { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
//   { id: 5, firstName: 'Serena', location: 'San Francisco' }
// ]
```

---

## 3. getIdsSum

**Fichier :** `3-get_ids_sum.js`

Fonction qui retourne la somme des `id` de tous les étudiants d’un tableau.  
Utilise la méthode `reduce`.

**Exemple :**
```js
getIdsSum(getListStudents());
// 8
```

---

## 4. updateStudentGradeByCity

**Fichier :** `4-update_grade_by_city.js`

Fonction qui retourne un tableau d’étudiants d’une ville donnée, avec une nouvelle propriété `grade` pour chacun.  
- Si l’étudiant a une note dans `newGrades`, on l’ajoute.
- Sinon, `grade` vaut `'N/A'`.

**Exemple :**
```js
const newGrades = [
  { studentId: 1, grade: 86 },
  { studentId: 5, grade: 90 }
];
updateStudentGradeByCity(getListStudents(), 'San Francisco', newGrades);
// [
//   { id: 1, firstName: 'Guillaume', location: 'San Francisco', grade: 86 },
//   { id: 5, firstName: 'Serena', location: 'San Francisco', grade: 90 }
// ]
```

---

## 5. typedArrays

**Fichier :** `5-typed_arrays.js`

Fonction qui crée un tableau typé (`Uint8ClampedArray`) à partir d’une longueur et d’un tableau de positions/valeurs à remplir.

**Exemple :**
```js
createInt8TypedArray(10, 2, 89);
// Uint8ClampedArray(10) [0, 0, 89, 0, 0, 0, 0, 0, 0, 0]
```

---

## 6. set

**Fichier :** `6-set.js`

Fonction qui retourne un `Set` contenant tous les éléments uniques d’un tableau.

**Exemple :**
```js
const set = new Set([1, 2, 2, 3]);
// Set { 1, 2, 3 }
```

---

## 7. hasArrayValues

**Fichier :** `7-has_array_values.js`

Fonction qui vérifie si tous les éléments d’un tableau sont présents dans un `Set`.

**Exemple :**
```js
hasArrayValues(new Set([1, 2, 3]), [1, 2]);
// true
hasArrayValues(new Set([1, 2, 3]), [4]);
// false
```

---

## 8. cleanSet

**Fichier :** `8-clean_set.js`

Fonction qui retourne une chaîne de caractères composée des valeurs du set commençant par `startString`,  
en retirant ce préfixe et en les séparant par un tiret.

**Exemple :**
```js
cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), 'bon');
// 'jovi-aparte-appetit'
cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), '');
// ''
```

---

## 9. groceriesList

**Fichier :** `9-groceries_list.js`

Fonction qui retourne une `Map` représentant une liste de courses, avec le nom de l’aliment en clé et un booléen en valeur.

**Exemple :**
```js
// Map { 'Apples' => false, 'Tomatoes' => false, ... }
```

---

## 10. updateUnikItems

**Fichier :** `10-update_uniq_items.js`

Fonction qui met à jour une `Map` : pour chaque valeur à 1, on la passe à 100.  
Sinon, on ne modifie pas.

**Exemple :**
```js
const map = new Map([['Apples', 1], ['Bananas', 2]]);
updateUniqueItems(map);
// Map { 'Apples' => 100, 'Bananas' => 2 }
```

---

## Conseils

- Tous les fichiers sont indépendants et testables via leur `*-main.js` associé.
- Les fonctions sont exportées par défaut.
- Les tests du checker sont stricts sur les noms de propriétés et la gestion des cas limites.

---

**Bon courage pour la révision