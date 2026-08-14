# Git Publication Handoff

The clean-room package contains no Git history. The designated private GitHub staging
repository exists and remained empty at the 2026-08-14 audit.

For the founder-controlled publication step:

1. Extract the approved ZIP into a new empty directory.
2. Verify `MANIFEST.sha256` before Git initialisation.
3. Confirm there is no inherited `.git`, submodule or symlink.
4. Run the reproduction scripts and secret/path scan from the extracted copy.
5. Run `git init -b main` only inside that clean extracted directory.
6. Review `git status --short` and the complete tracked-file list.
7. Commit the exact approved tree.
8. Push to the existing private staging remote only after founder approval and exact-tree
   verification.
9. Perform a clean-clone verification.
10. Treat any private-to-public visibility change as a separate human release gate.
