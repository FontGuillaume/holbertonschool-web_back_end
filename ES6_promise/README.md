# ES6 Promises - Exercices Holberton

Ce projet couvre les concepts fondamentaux des **Promises** en JavaScript ES6, depuis la création basique jusqu'à la gestion avancée d'erreurs.

## 📋 Table des matières

- [0. Keep every promise you make and only make promises you can keep](#0-keep-every-promise-you-make-and-only-make-promises-you-can-keep)
- [1. Don't make a promise...if you know you can't keep it](#1-dont-make-a-promiseif-you-know-you-cant-keep-it)
- [2. Catch me if you can!](#2-catch-me-if-you-can)
- [3. Handle multiple successful promises](#3-handle-multiple-successful-promises)
- [4. Simple promise](#4-simple-promise)
- [5. Reject the promises](#5-reject-the-promises)
- [6. Handle multiple promises](#6-handle-multiple-promises)
- [7. Load balancer](#7-load-balancer)
- [8. Throw an error](#8-throw-an-error)
- [9. Throw error / try catch](#9-throw-error--try-catch)

---

## 0. Keep every promise you make and only make promises you can keep

**Fichier :** `0-promise.js`

### 📝 Description
Création d'une Promise basique qui se résout immédiatement.

### 💻 Code
```javascript
export default function getResponseFromAPI() {
    return Promise.resolve(true);
}
```

### 🎯 Concepts appris
- Création d'une Promise avec `Promise.resolve()`
- Export/import de fonctions ES6

### 🧪 Test
```javascript
const response = getResponseFromAPI();
console.log(response instanceof Promise); // true
```

---

## 1. Don't make a promise...if you know you can't keep it

**Fichier :** `1-promise.js`

### 📝 Description
Promise conditionnelle qui se résout ou se rejette selon un paramètre booléen.

### 💻 Code
```javascript
export default function getFullResponseFromAPI(success) {
  if (success === true)
    return Promise.resolve({
      status: 200,
      body: 'Success',
    });
  return Promise.reject(new Error("The fake API is not working currently"));
}
```

### 🎯 Concepts appris
- `Promise.resolve()` pour les succès
- `Promise.reject()` pour les échecs
- Gestion conditionnelle des Promises

### 🧪 Test
```javascript
console.log(getFullResponseFromAPI(true));  // Promise résolue
console.log(getFullResponseFromAPI(false)); // Promise rejetée
```

---

## 2. Catch me if you can!

**Fichier :** `2-then.js`

### 📝 Description
Gestion complète d'une Promise avec `.then()`, `.catch()` et `.finally()`.

### 💻 Code
```javascript
export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({
      status: 200,
      body: 'success',
    }))
    .catch(() => new Error())
    .finally(() => console.log('Got a response from the API'));
}
```

### 🎯 Concepts appris
- `.then()` pour gérer les succès
- `.catch()` pour gérer les erreurs
- `.finally()` pour les actions toujours exécutées
- Arrow functions avec return implicite
- Chaînage de Promises

### 🧪 Test
```javascript
const promise = Promise.resolve();
handleResponseFromAPI(promise); // Affiche: "Got a response from the API"
```

---

## 3. Handle multiple successful promises

**Fichier :** `3-all.js`

### 📝 Description
Exécution simultanée de plusieurs Promises avec `Promise.all()`.

### 💻 Code
```javascript
import { uploadPhoto, createUser } from './utils.js';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photoResponse, userResponse]) => {
      console.log(`${photoResponse.body} ${userResponse.firstName} ${userResponse.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
```

### 🎯 Concepts appris
- `Promise.all()` pour attendre plusieurs Promises
- Destructuration des résultats `[photoResponse, userResponse]`
- Template literals pour formatter les strings
- Gestion globale d'erreurs

### 🧪 Test
```javascript
handleProfileSignup(); // "photo-profile-1 Guillaume Salva"
```

---

## 4. Simple promise

**Fichier :** `4-user-promise.js`

### 📝 Description
Promise simple qui retourne un objet utilisateur.

### 💻 Code
```javascript
export default function signUpUser(firstName, lastName) {
    return Promise.resolve({
        firstName: firstName,
        lastName: lastName,
    });
}
```

### 🎯 Concepts appris
- Promise résolue avec objet
- Passage de paramètres
- Structure d'objet simple

---

## 5. Reject the promises

**Fichier :** `5-photo-reject.js`

### 📝 Description
Promise qui se rejette systématiquement avec un message d'erreur personnalisé.

### 💻 Code
```javascript
export default function uploadPhoto(filename) {
    return Promise.reject(new Error(`${filename} cannot be processed`));
}
```

### 🎯 Concepts appris
- `Promise.reject()` pour créer des erreurs
- Messages d'erreur dynamiques avec template literals
- Création d'objets Error

---

## 6. Handle multiple promises

**Fichier :** `6-final-user.js`

### 📝 Description
Gestion de multiples Promises avec `Promise.allSettled()` pour capturer tous les résultats (succès et échecs).

### 💻 Code
```javascript
import signUpUser from "./4-user-promise";
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
    return Promise.allSettled([
        signUpUser(firstName, lastName),
        uploadPhoto(fileName)
    ])
    .then((results) => {
      return results.map((result) => ({
        status: result.status,
        value: result.status === 'fulfilled' ? result.value : result.reason
      }));
    });
}
```

### 🎯 Concepts appris
- `Promise.allSettled()` vs `Promise.all()`
- Opérateur ternaire `condition ? valeurSiVrai : valeurSiFaux`
- Méthode `.map()` pour transformer les données
- Propriétés `status`, `value`, `reason` de allSettled
- Gestion mixte succès/échecs

### 🧪 Résultat
```javascript
[
  { status: 'fulfilled', value: { firstName: 'Bob', lastName: 'Dylan' } },
  { status: 'rejected', value: Error('bob_dylan.jpg cannot be processed') }
]
```

---

## 7. Load balancer

**Fichier :** `7-load_balancer.js`

### 📝 Description
Implémentation d'un load balancer qui retourne la première Promise résolue.

### 💻 Code
```javascript
export default function loadBalancer(chinaDownload, USDownload) {
  return Promise.race([chinaDownload, USDownload]);
}
```

### 🎯 Concepts appris
- `Promise.race()` pour la première Promise terminée
- Concept de load balancing
- Optimisation des performances

### 🧪 Test
```javascript
const promiseUK = new Promise(resolve => setTimeout(resolve, 100, 'UK faster'));
const promiseFR = new Promise(resolve => setTimeout(resolve, 200, 'FR faster'));

loadBalancer(promiseUK, promiseFR); // "UK faster" (plus rapide)
```

---

## 8. Throw an error

**Fichier :** `8-try.js`

### 📝 Description
Fonction qui lance une erreur lors d'une division par zéro.

### 💻 Code
```javascript
export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw new Error('cannot divide by 0');
  }
  return numerator / denominator;
}
```

### 🎯 Concepts appris
- `throw` pour lancer des erreurs
- Validation de paramètres
- Gestion des cas d'erreur mathématiques

### 🧪 Test
```javascript
console.log(divideFunction(10, 2)); // 5
console.log(divideFunction(10, 0)); // Error: cannot divide by 0
```

---

## 9. Throw error / try catch

**Fichier :** `9-try.js`

### 📝 Description
Garde-fou (guardrail) qui capture les erreurs d'une fonction et log les résultats.

### 💻 Code
```javascript
export default function guardrail(mathFunction) {
  const queue = [];
  
  try {
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    queue.push(error.toString());
  } finally {
    queue.push('Guardrail was processed');
  }
  
  return queue;
}
```

### 🎯 Concepts appris
- `try-catch-finally` pour la gestion d'erreurs
- `.toString()` pour convertir les erreurs en strings
- Concept de guardrail/garde-fou
- Exécution garantie avec `finally`

### 🧪 Test
```javascript
guardrail(() => divideFunction(10, 2)); // [5, 'Guardrail was processed']
guardrail(() => divideFunction(10, 0)); // ['Error: cannot divide by 0', 'Guardrail was processed']
```

---

## 🔧 Fichiers utilitaires

### `utils.js`
```javascript
export function uploadPhoto() {
  return Promise.resolve({
    status: 200,
    body: 'photo-profile-1',
  });
}

export function createUser() {
  return Promise.resolve({
    firstName: 'Guillaume',
    lastName: 'Salva',
  });
}
```

---

## 📊 Récapitulatif des concepts

| Concept | Méthode/Syntax | Usage |
|---------|----------------|-------|
| **Création** | `Promise.resolve()` | Promise qui réussit |
| **Rejet** | `Promise.reject()` | Promise qui échoue |
| **Gestion succès** | `.then()` | Traiter les résultats |
| **Gestion erreurs** | `.catch()` | Traiter les erreurs |
| **Action finale** | `.finally()` | Toujours exécuté |
| **Multiples (tout)** | `Promise.all()` | Attendre toutes les Promises |
| **Multiples (tout + détail)** | `Promise.allSettled()` | Détail de chaque Promise |
| **Course** | `Promise.race()` | Première Promise terminée |
| **Lancer erreur** | `throw new Error()` | Créer une erreur |
| **Capturer erreur** | `try-catch-finally` | Gérer les erreurs |

---

## 🚀 Comment exécuter

```bash
# Lancer un exercice spécifique
npm run dev 0-main.js

# Vérifier le style de code
npm run check-lint

# Lancer tous les tests
npm run full-test
```

---

## 🎓 Compétences acquises

✅ Maîtrise des Promises JavaScript ES6  
✅ Gestion asynchrone avec then/catch/finally  
✅ Gestion d'erreurs robuste  
✅ Patterns Promise avancés (all, allSettled, race)  
✅ Best practices JavaScript moderne  
✅ Debugging et logging efficace  

---

*Ce projet fait partie du cursus Holberton School - Web Back End*