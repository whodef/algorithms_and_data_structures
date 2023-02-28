# Algorithms and data structures
## Sprint 15. 'Python Developer Plus' Course

___

## Semantic Commit Messages
See how a minor change to your commit message style can make you a better programmer.

Format: `<type>(<scope>): <subject>`

`<scope>` is optional

### Example:

```
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
```


More Examples:

- `feat`: new feature for the user, not a new feature for build script
- `fix`: bug fix for the user, not a fix to a build script
- `docs`: changes to the documentation
- `style`: formatting, missing semi colons, etc; no production code change
- `refactor`: refactoring production code, eg. renaming a variable
- `test`: adding missing tests, refactoring tests; no production code change
- `chore`: updating grunt tasks etc; no production code change
- `perf`: a commit that improves performance, without functional changes
- or `build`, `ci`, `revert`, etc.

Less specific cases:

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests
- `chore`: Changes to the build process or auxiliary tools and libraries such as documentation generation

References:

1. https://www.conventionalcommits.org/
2. https://seesparkbox.com/foundry/semantic_commit_messages
3. http://karma-runner.github.io/1.0/dev/git-commit-msg.html
___