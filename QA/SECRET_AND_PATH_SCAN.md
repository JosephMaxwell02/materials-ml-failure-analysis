# Secret and Path Scan

Automated scan is executed after release assembly and recorded in
`SECRET_AND_PATH_SCAN_RESULTS.json`. Review rules distinguish intentional public contact
metadata and explanatory mentions from actionable secrets or local paths.

Expected benign strings include `.git` in the Git publication handoff and the public author
email. Any local Windows path, credential-shaped token, private key block, `.env` file,
private repository URL or unreviewed identity is a release hold.
