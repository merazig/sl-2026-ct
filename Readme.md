| Schéma   | Table    | Colonne       | Type            |    Volume | Nulls | Qualité      |
| -------- | -------- | ------------- | --------------- | --------: | ----: | ------------ |
| `public` | `ventes` | `id_vente`    | `integer`       | 1 250 430 |   0 % | OK           |
| `public` | `ventes` | `date_vente`  | `date`          | 1 250 430 | 0,1 % | À vérifier   |
| `public` | `ventes` | `montant`     | `numeric(12,2)` | 1 250 430 | 0,3 % | À vérifier   |
| `public` | `ventes` | `canal`       | `varchar`       | 1 250 430 |   0 % | OK           |
| `public` | `ventes` | `code_client` | `varchar`       | 1 250 430 | 2,1 % | À surveiller |


| Colonne       | Type    | Unité / domaine                | Source       | Fraîcheur |
| ------------- | ------- | ------------------------------ | ------------ | --------- |
| `id_vente`    | integer | Identifiant unique             | `crm.ventes` | J+1       |
| `date_vente`  | date    | Date calendaire                | `crm.ventes` | J+1       |
| `montant`     | numeric | EUR, TTC                       | `crm.ventes` | J+1       |
| `canal`       | varchar | `web`, `magasin`, `partenaire` | `crm.ventes` | J+1       |
| `code_client` | varchar | Identifiant client             | `crm.ventes` | J+1       |
