# 🌍 Carbon Tracker - L'app incontournable pour réduire ton empreinte carbone

![Carbon Tracker](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![React](https://img.shields.io/badge/Firebase-Firestore-orange)

## 🎯 À propos

**Carbon Tracker** est une application web full-stack qui permet à chacun de calculer et comprendre son empreinte carbone. Conçue pour être **éducative, accessible et virale**, elle aide les citoyens à prendre des décisions durables.

### 🚀 Features Principales

✅ **Calcul instant** - Émissions CO2 en temps réel  
✅ **Graphiques interactifs** - Visualisez vos données (Pie + Bar charts)  
✅ **Comparaisons mondiales** - Benchmark vs moyennes globales  
✅ **Objectifs personnalisés** - Fixez et suivez votre réduction  
✅ **Historique cloud** - Données persistantes avec Firebase Firestore  
✅ **Partage viral** - Twitter, Facebook, copier le lien  
✅ **Responsive mobile** - Fonctionne sur tous les appareils  
✅ **Explications éducatives** - Conseils personnalisés pour chaque activité  

---

## 💻 Stack Technologique

**Frontend :**
- HTML5, CSS3, JavaScript (Vanilla)
- Chart.js (graphiques interactifs)
- Firebase Firestore (base de données cloud)
- Netlify (déploiement automatique)

**Backend :**
- Python 3.13 (HTTP Server)
- Railway (déploiement cloud)
- CORS activé pour requêtes cross-origin

**Architecture :**
- API RESTful
- Real-time data sync (Firestore)
- Progressive Web App (PWA ready)

---

## 🌐 URLs Publiques

| Service | URL | Status |
|---------|-----|--------|
| **Frontend** | https://jolly-pie-77d35f.netlify.app | ✅ Online |
| **API** | https://carbon-tracker-production-9ff2.up.railway.app | ✅ Online |
| **Code** | https://github.com/seousmane98/carbon-tracker | ✅ Public |

---

## 📊 Activités Supportées

| Activité | Facteur | Remarque |
|----------|---------|----------|
| 🚗 Voiture | 0.21 kg CO2/km | Le plus polluant |
| 🚌 Bus | 0.089 kg CO2/km | 2,5x moins qu'une voiture |
| 🚂 Train | 0.041 kg CO2/km | Le plus écologique |
| ✈️ Avion | 0.255 kg CO2/km | Très polluant |
| ⚡ Électricité | 0.6 kg CO2/kWh | Dépend de la source |
| 🥩 Viande | 27 kg CO2/kg | Élevage très gourmand |

---

## 🚀 Comment Utiliser

### Localement (Développement)

**1. Clone le repo :**
```bash
git clone https://github.com/seousmane98/carbon-tracker.git
cd carbon-tracker
```

**2. Lance l'API Python :**
```bash
python main.py
```
L'API démarre sur `http://localhost:8000`

**3. Ouvre le frontend :**
- Clique droit sur `index.html`
- Sélectionne "Open with Live Server"
- Ou navigue vers `http://localhost:5500`

**4. Commence à calculer ! 🔥**

### En Production

Visite simplement : https://jolly-pie-77d35f.netlify.app

---

## 🏗️ Structure du Projet