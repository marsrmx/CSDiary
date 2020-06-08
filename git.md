# GIT

## Cheatsheet

`git status` | Check where you are and how you are.

`git add *` or `git add .` | Add everything that you have change into a commit.

`git commit -m "message"` | Commit your changes, if by accident you didn't write "-m" and weird text editor would open (aka VIM) just type `:qw`

`git push` | For when you are using Github and you want your changes to be in the remote branch

```
fatal: The current branch Git has no upstream branch.
To push the current branch and set the remote as upstream, use
    git push --set-upstream origin Git
```

DON'T FREAK OUT! This is just saying that your local branch doesn't have a branch remote to upload the changes.
And the _cute command_ that is giving you is to create a branch with that same name as in your local.

`git clone "url"` | 

`git checkout -b "newLocalBranch"` | Create a new branch

## Advices

* Never add or commit from master
* Write good commit messages (they are going to save you)

## Articles

That I have checked to many times. 
> PD. Thank you to the writers

* [Untrack files already added to git repository based on gitignore](http://www.codeblocq.com/2016/01/Untrack-files-already-added-to-git-repository-based-on-gitignore/)
* [Git rebase vs Git marge](https://medium.com/datadriveninvestor/git-rebase-vs-merge-cc5199edd77c)
* [Checkout a remote branch](https://www.git-tower.com/learn/git/faq/checkout-remote-branch)
* [Create .gitignore](http://www.gitignore.io/)
