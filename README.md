# Exercices et exemples INF1007

## Structure des dossiers

Chaque exercice (ou ensemble d'exercices) est dans un dossier de la forme ch*XX*_*Y*, donc le numéro du chapitre qu'il couvre et le numéro de l'exercice. Les numéros d'exercices d'un même chapitre n'ont pas vraiment de signification. Autrement dit, l'exercice *ch07_2* n'est pas plus ou moins important que *ch07_3*, juste différent. Des fois, ils sont numérotés ainsi parce qu'ils se suivent d'une semaine à l'autre.

## Code et fichiers de chaque exercice

Chaque dossier a un fichier *README.md* qui explique l'exercice à compléter avec des pistes de résolution et parfois des exemples d'utilisation.

L'exercice à compléter est typiquement le fichier *exercice.py* dans chaque dossier. Celui-ci contient du code avec des fonctions vides à compléter ou des commentaires *TODO* dans les cas plus compliqués. On vous fournit aussi les solutionnaires de la forme *_exercice_version_prof.py*. Ce ne sont généralement pas les seules solutions possibles, juste une version attendue et acceptable.

La plupart des dossiers ont aussi un *test_exercice.py* qui roule des tests unitaires sur le code dans *exercice.py*. Ceci permet de vérifier la validité de vos réponses.

## Comment travailler avec ce répertoire GitHub?

La meilleure façon est de faire un fork de ce répertoire en cliquant sur l'icône fork en haut à droite. De cette façon vous pourrez avoir une copie des exercices liée à votre compte GitHub. Ainsi, vous serez avisé lorsqu'il y a des changements dans le répertoire original à https://github.com/INF1007-Gabarits/exercices-inf1007. 

La seconde étape sera de cloner ce répertoire après qu'il sera forked.

## Comment synchroniser un fork et résoudre les conflits?
Il se peut qu'au fil de la session, le répertoire upstream ou original soit modifié. Pour pouvoir y avoir accès, voici les étapes à suivre. À noter que s'il n'y a aucun conflit, ces prochaines étapes peuvent également être réalisées directement en ligne sur votre répertoire forké en utilisant le bouton :repeat: 'Sync fork'.

### Étape 1 : Configurer le répertoire upstream

1. Accédez à votre répertoire forké :

    ```bash
    cd /chemin/vers/votre-repo-forké
    ```

2. Ajoutez le répertoire upstream (le répertoire original que vous avez forké) :

    ```bash
    git remote add upstream https://github.com/propriétaire-dorigine/dépôt-dorigine.git
    ```
    Dans notre cas, il s'agit de :
     ```bash
    git remote add upstream https://github.com/INF1007-Gabarits/exercices-inf1007.git
    ```

3. Vérifiez la configuration du remote upstream :

    ```bash
    git remote -v
    ```

### Étape 2 : Récupérer les dernières modifications du répertoire upstream

Récupérez les dernières modifications du répertoire upstream sans modifier votre répertoire de travail local :

```bash
git fetch upstream
```
### Étape 3 : Basculer sur votre branche principale (main ou master)

Basculez sur la branche main (ou master) de votre fork :

```bash
git checkout main
```
### Étape 4 : Fusionner les changements d'upstream dans votre fork

Fusionnez les modifications du répertoire upstream dans la branche principale de votre fork :

```bash
git merge upstream/main
```

### Étape 5 : Résoudre les conflits (si nécessaire)

Si des conflits surviennent, Git vous avertira. Pour les résoudre :

```bash
git merge upstream/main
```

1. Ouvrez les fichiers en conflit sur votre IDE. Vous verrez des marqueurs de conflit (fichiers en conflit indiqués en rouge) :

    ```
    <<<<<<< HEAD
    // Vos modifications
    =======
    // Modifications de upstream
    >>>>>>> upstream/main
    ```

2. Modifiez manuellement les fichiers pour résoudre le conflit. Choisissez si vous voulez garder la version du upstream, votre version ou un mélange des deux.

3. Ajoutez les fichiers résolus :

    ```bash
    git add <nom_fichier>
    ```

4. Finalisez la fusion :

    ```bash
    git commit -m "Votre message pour le commit"
    ```

    Les étapes 3 et 4 peuvent également être faites en une étape pour ajouter tous les fichiers changés en même temps comme suit : 
     ```bash
    git commit -a -m "Votre message pour le commit"
    ```
### Étape 6 : Pousser les changements vers votre fork

Une fois la fusion terminée, poussez la branche main mise à jour vers votre fork :

```bash
git push origin main
```
Bien joué, vous avez maintenant réussi à mettre à jour votre fork avec les nouvelles modifications ajoutées sur le répertoire original! :white_check_mark:
