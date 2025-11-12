# English Version

## 🧠 Data Engineering Technical Test

### 🎯 Objective
The purpose of this challenge is to demonstrate your end-to-end data engineering and analytical skills.
You will design a small but complete data pipeline — from sourcing heterogeneous data to cleaning, transforming, merging, and finally analyzing it — all within a reproducible Dockerized environment.

Specifically, this test will assess your ability to:

1 - Source data from multiple file types and locations (CSV, TXT, Parquet, remote URLs, and S3).
2 - Understand and clean complex data structures, handling missing, inconsistent, or duplicated entries.
3 - Write clean, modular, and functional code with appropriate documentation and organization.
4 - Monitor and analyze data quality using reproducible metrics and visualizations.
5 - Containerize your project for local execution using Docker.
6 - Version your work effectively on GitHub.

### Preparation
To avoid constrains during the 1h interview, the following steps can be done prior:

- Setup a Git Repository for your code.
- Access the data and inspect the formats
- Setup your environment
- # ENSURE EVERY HELPER (Copilot, ChatGPT, etc... is disabled)

### Data

#### 📦 Data Sources

| Dataset          | Description                   | Location                                                                                          |
| ---------------- | ----------------------------- | ------------------------------------------------------------------------------------------------- |
| `CIS_bdpm`       | Medicinal product reference   | `s3://data-eng-interviews/CIS_bdpm.txt` (or `https://data-eng-interviews.s3.eu-west-3.amazonaws.com/CIS_bdpm.txt`) |                                                          |
| `CIS_CIP_bdpm`   | Product packaging and codes   | `s3://data-eng-interviews/CIS_CIP_bdpm.parquet`                                                   |
| `CIS_COMPO_bdpm` | Product composition details   | `s3://data-eng-interviews/CIS_COMPO_bdpm.csv`                                                     |
| `CIS_CPD_bdpm`   | Public medication information | `https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_CPD_bdpm.txt`                |


### 🧩 Main Task
You must clean, transform, and merge the four datasets into a single consolidated table.
Once the final table is ready, upload it to:
`s3://data-eng-interviews/results/{your_name}/`

Your code should be structured, efficient, and easily reproducible.

### 📊 Dashboard Requirements
Develop a 3-chart dashboard to perform data quality analysis.
The dashboard should enable monitoring of key metrics such as:
1. Missing Values – Track the evolution of missing data across columns or datasets.
2. Unmerged Rows – Quantify records that could not be matched during the merging process.
3. Duplicate Entries – Detect and analyze duplication patterns in the datasets.

🧭 The dashboard can be developed within a Jupyter Notebook, and it should be able to read from pre-computed intermediate files if needed.

### ⚙️ Deliverables & Execution
Package your full project in a local Docker container.

Include a Dockerfile or docker-compose.yml that builds and runs the pipeline.

Develop your dashboard inside a notebook that can be executed after the pipeline runs.

At the end of the interview, you’ll be asked to:

Push your code into setup repithub.

Run the container to generate the final dataset.

Execute the notebook cells to display your dashboard.

💡 Tip: You may persist intermediate outputs (e.g., CSV or Parquet files) for reuse within the dashboard.

### Data Linkage Chart

The following diagram illustrates the intended relationship between the different data sources:

![alt text](image.png)

### ✅ Evaluation Criteria

| Category                           | Description                                           |
| ---------------------------------- | ----------------------------------------------------- |
| **Data Sourcing**                  | Ability to handle multiple formats and remote sources |
| **Data Cleaning & Transformation** | Quality, logic, and robustness of preprocessing       |
| **Code Structure & Readability**   | Clarity, modularity, and documentation                |
| **Data Analysis & Visualization**  | Quality of dashboard insights and readability         |
| **Reproducibility**                | Dockerization and ease of setup/run                   |
| **Version Control**                | Commit quality, branching, and GitHub organization    |


# French Version

## 🧠 Test Technique – Data Engineering
### 🎯 Objectif
L’objectif de ce test est de démontrer vos compétences complètes en ingénierie et analyse de données.
Vous devrez concevoir un pipeline de données complet — depuis la collecte de sources hétérogènes, jusqu’à la nettoyage, la transformation, la fusion et l’analyse — le tout dans un environnement conteneurisé et reproductible à l’aide de Docker.

Ce test vise à évaluer votre capacité à :

1. Collecter des données issues de plusieurs formats et emplacements (CSV, TXT, Parquet, URL distante, S3).

2. Comprendre et nettoyer des structures de données complexes, en gérant les valeurs manquantes, incohérentes ou dupliquées.

3. Écrire un code propre, modulaire et fonctionnel, bien organisé et documenté.

4. Surveiller et analyser la qualité des données à l’aide de métriques et visualisations reproductibles.

5. Conteneuriser votre projet pour une exécution locale via Docker.

6. Utiliser GitHub pour un versionnement clair et structuré de votre travail.

### 🧰 Préparation

Afin d’éviter toute contrainte pendant l’entretien (durée : 1 heure), les étapes suivantes peuvent être réalisées en amont :

- Créez un dépôt Git pour votre code.

- Accédez aux données et explorez leurs formats respectifs.

- Configurez votre environnement de développement local.

- ⚠️ Assurez-vous de désactiver tout outil d’assistance (Copilot, ChatGPT, etc.).

### 📦 Données
#### Sources de données

| Dataset          | Description                        | Location                                                                                          |
| ---------------- | -----------------------------------| ------------------------------------------------------------------------------------------------- |
| `CIS_bdpm`       | Référentiel des produits médicaux  | `s3://data-eng-interviews/CIS_bdpm.txt`                                                           |
| `CIS_CIP_bdpm`   | Codes et conditionnements produits | `s3://data-eng-interviews/CIS_CIP_bdpm.parquet`                                                   |
| `CIS_COMPO_bdpm` | Détails de composition des produits| `s3://data-eng-interviews/CIS_COMPO_bdpm.csv`                                                     |
| `CIS_CPD_bdpm`   | Public medication information      | `https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_CPD_bdpm.txt`                |

### 🧩 Tâche principale

Nettoyez, transformez et fusionnez les quatre jeux de données en une table finale consolidée.
Une fois cette table créée, chargez-la sur :
`s3://data-eng-interviews/results/{your_name}/`

Votre code doit être structuré, efficace et facilement reproductible.

### 📊 Tableau de bord – Analyse de la qualité des données

Créez un tableau de bord composé de trois graphiques permettant d’analyser la qualité des données.
Ce tableau doit permettre le suivi des indicateurs suivants :

1. Valeurs manquantes – Suivi de l’évolution des données manquantes par colonne ou par source.

2. Lignes non fusionnées – Quantification des enregistrements n’ayant pas pu être associés lors des jointures.

3. Doublons – Détection et analyse des entrées dupliquées dans les différentes tables.

🧭 Le tableau de bord peut être développé dans un notebook Jupyter et doit pouvoir lire des fichiers intermédiaires pré-calculés si nécessaire.

### ⚙️ Livrables et exécution

Emballez l’ensemble du projet dans un conteneur Docker local.

Fournissez un Dockerfile (ou docker-compose.yml) permettant de construire et exécuter le pipeline.

Développez votre tableau de bord dans un notebook exécutable après le pipeline.

À la fin de l’entretien, vous devrez :

1. Pousser votre code sur le dépôt GitHub configuré.

2. Lancer le conteneur Docker pour générer la table finale.

3. Exécuter les cellules du notebook afin d’afficher le tableau de bord.

💡 Astuce : vous pouvez enregistrer des sorties intermédiaires (fichiers CSV, Parquet, etc.) pour réutilisation dans le tableau de bord.

### 🗺️ Schéma de liaison des données

Le diagramme ci-dessous illustre la relation attendue entre les différentes sources de données :
![alt text](image.png)

### ✅ Critères d’évaluation
| Catégorie                          | Description                                                 |
| ---------------------------------- | ----------------------------------------------------------- |
| **Collecte des données**           | Capacité à manipuler plusieurs formats et sources distantes |
| **Nettoyage & Transformation**     | Qualité, logique et robustesse du prétraitement             |
| **Structure & Lisibilité du code** | Clarté, modularité et documentation                         |
| **Analyse & Visualisation**        | Pertinence et lisibilité du tableau de bord                 |
| **Reproductibilité**               | Maîtrise de Docker et simplicité d’exécution                |
| **Versionnement**                  | Qualité des commits, branches et organisation sur GitHub    |
