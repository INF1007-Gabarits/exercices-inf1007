# Information générale
* En cas de difficultés, il est toujours possible de modifier des fichiers [directement sur GitHub](https://docs.github.com/en/github/managing-files-in-a-repository/editing-files-in-your-repository)

# Étapes pour les premières séances
1. Lire le [README.md](README.md)
2. Ouvrir le lien [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](README.md) dans le [README.md](README.md)
    * Gitpod offre gratuitement 50 heures par mois de [service](https://www.gitpod.io/pricing/)
    * Comme étudiant vous pouvez obtenir le [plan personnel de Gitpod](https://education.github.com/pack#offers) gratuitement pour six mois avec 100 heures par mois de service
    * Appliquer avec votre compte @polymtl.ca sur <https://education.github.com/discount_requests/new>
3. Compléter la connexion de Gitpod avec votre compte GitHub
   * Vérifier que vous avez donnez à Gitpod toutes les [permissions à votre compte GitHub](https://gitpod.io/access-control/)
4. Compléter l'exercice dans Gitpod
    * Vos modifications sont automatiquement sauvegardées dans Gitpod
    * Gitpod et GitHub sont [automatiquement synchronisés](.gitpod.yml#L6)
    * Vous recevrez automatiquement les modifications effectuées dans le fichier [_exercice_version_prof.py](_exercice_version_prof.py) pour fin de consultation lors des séances
    * Votre fichier [exercice.py](exercice.py) sera automatiquement mis à jour dans GitHub et visible au professeur
5. Une fois la séance terminée, sélectionnée [Workspace | Stop Workspace](https://www.gitpod.io/docs/life-of-workspace/#timeouts)
pour fermer votre espace de travail sur Gitpod
# Étapes pour les autres séances
### À effectuer une fois
1. Installer [PyCharm Community](https://www.jetbrains.com/pycharm/download/)
   * (optionnel) installer [l'extension Chrome](https://chrome.google.com/webstore/detail/jetbrains-toolbox-extensi/offnedcbhjldheanlbojaefbfbllddna?)
2. Installer [GitHub Desktop](https://desktop.github.com/)
3. Installer [Anaconda](https://www.anaconda.com/products/individual)
4. Apprendre à utiliser git
    * https://git-scm.com/book/fr/v2
    * https://git-scm.com/docs
    * https://github.github.com/training-kit/
    

### En préparation à une séance
1. Cloner le répertoire de GitHub sur votre ordinateur
    * à partir de GitHub [(instructions à suivre)](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) 
    * ou à partir de PyCharm [(instructions à suivre)](https://www.jetbrains.com/help/pycharm/opening-your-project-for-the-first-time.html#git)
2. Ouvrir l'exercice dans PyCharm [(instructions à suivre)](https://www.jetbrains.com/help/pycharm/importing-project-from-existing-source-code.html#existing-sources)
3. Créer l'environnement [conda à partir du fichier environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)
   * avec Anaconda Navigator
        1. Ouvrir Anaconda Navigator
        2. Suivre les [instructions](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/#importing-an-environment)
            * Sélectionner Environments
            * Sélectionner Import
            * Choisir le fichier environment.yml
    * ou avec un [terminal](https://www.jetbrains.com/help/pycharm/terminal-emulator.html)
    
        ```
        cd C:\chemin\vers\le\répertoire\de\l\exercice\Exercice-NomEtudiant\
        conda env create --force --file environment.yml --name nom_exercice
        conda activate nom_exercice
        ```
3. Choisir l'environnement conda créé plutôt comme Python Interpreter dans votre projet PyCharm
    * [instructions à suivre](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html)
    * choisir Existing environnement 
### Au début et lors d'une séance
1. Lire le [README.md](README.md)
2. Compléter l'exercice dans PyCharm
    * Effectuer un [git pull](https://git-scm.com/docs/git-pull/)
      pour recevoir les modifications effectuées dans le fichier [_exercice_version_prof.py](_exercice_version_prof.py) pour fin de consultation lors des séances
    * Effectuer les [opérations git](https://git-scm.com/docs)
      pour envoyer vos modifications du fichier [exercice.py](exercice.py) à GitHub et au professeur
      * utiliser [git avec GitHub Desktop](https://docs.github.com/en/desktop/getting-started-with-github-desktop/creating-your-first-repository-using-github-desktop#introduction)
      * utiliser [git avec PyCharm](https://www.jetbrains.com/help/pycharm/using-git-integration.html)
