# Publishing the repository

The intended public repository is:

`SamPetkov/zero-atom-right-outliers`

From an authenticated local GitHub CLI session, run:

```bash
bash scripts/publish_github.sh
```

The script checks GitHub authentication, initializes a `main` branch if needed, commits any final changes as Samuil Petkov, creates the public repository when it does not exist, and pushes the branch.

After publication:

1. Confirm both GitHub Actions workflows pass.
2. Create a versioned GitHub release, preferably `v0.1.0`.
3. Connect the repository to Zenodo or another archival service and mint a DOI.
4. Replace the repository-only data citation in the manuscript with the persistent identifier before acceptance.
5. Rebuild and inspect both PDFs after changing the citation.
