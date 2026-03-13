# OpenClaw PM five-repo recheck order note

In each five-repo maintenance pass, recheck repositories in the same visible order before reporting: repo 1 -> repo 2 -> repo 3 -> repo 4 -> repo 5.

That keeps the short report reproducible, makes the non-skip rule for repos 4 and 5 auditable, and prevents the governance-sandbox priority lane from disappearing between runs.
