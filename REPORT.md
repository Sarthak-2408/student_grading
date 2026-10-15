# Lab Assignment 7 — Question 1

## Objective

Implement a student grading system using Git branching, merging, and conflict resolution.

## Git Workflow

1. Created the initial grading system on `main`.
2. Created `feature-grading` and `feature-report` from the initial commit.
3. Modified the grading logic on `feature-grading`.
4. Implemented report functionality on `feature-report`.
5. Merged `feature-grading` into `main`.
6. Merged `feature-report` and resolved the conflict in `grading.py`.
7. Corrected the Meera record in `students.csv`.
8. Added boundary and invalid-input tests.

## Merge Conflict Explanation

Both branches modified the same portion of `grading.py`, so Git could not automatically combine the changes. I resolved the conflict manually, retaining the grading improvements and report functionality.

## Testing Evidence

Paste the actual output of `python -m unittest -v` here.

## Git History Evidence

Paste the output of `git log --oneline --graph --all` here.




Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git init -b main
Initialized empty Git repository in C:/Users/Sarthak Amrute/OneDrive/Desktop/Assignment 7/student_grading/.git/
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git add grading.py students.csv test_grading.py
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   grading.py
        new file:   students.csv
        new file:   test_grading.py

PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git commit -m "Add Initial Student Grading System"
[main (root-commit) ba90111] Add Initial Student Grading System
 3 files changed, 42 insertions(+)
 create mode 100644 grading.py
 create mode 100644 students.csv
 create mode 100644 test_grading.py
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git branch feature-grading
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git branch feature-report
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git switch feature-grading
Switched to branch 'feature-grading'
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git add grading.py
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git commit -m "Improved grading logic and validation"
[feature-grading 3c7162c] Improved grading logic and validation
 1 file changed, 5 insertions(+), 3 deletions(-)
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git switch feature-report
Switched to branch 'feature-report'
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git add grading.py
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git commit -m "Add student grade report functionality"
[feature-report c0aaa7d] Add student grade report functionality
 1 file changed, 7 insertions(+), 3 deletions(-)
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git log --oneline --graph --all
* c0aaa7d (HEAD -> feature-report) Add student grade report functionality
| * 3c7162c (feature-grading) Improved grading logic and validation
|/
* ba90111 (main) Add Initial Student Grading System
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git switch main
Switched to branch 'main'
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git merge feature-grading
Updating ba90111..3c7162c
Fast-forward
 grading.py | 8 +++++---
 1 file changed, 5 insertions(+), 3 deletions(-)
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git merge feature-report
Auto-merging grading.py
Merge made by the 'ort' strategy.
 grading.py | 10 +++++++---
 1 file changed, 7 insertions(+), 3 deletions(-)
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> code .
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> ls


    Directory: C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---l        15-10-2026     09:30            689 grading.py
-a---l        15-10-2026     08:57             90 students.csv
-a---l        15-10-2026     09:06            567 test_grading.py


PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git status
On branch main
nothing to commit, working tree clean
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git diff
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   grading.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git add grading.py
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git commit -m "Resolve grading conflict and retain both features"
[main f6e3995] Resolve grading conflict and retain both features
 1 file changed, 28 insertions(+), 1 deletion(-)
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> nano students.csv
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git add students.csv
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git commit -m "fixed Meera record"
[main b01a8e2] fixed Meera record
 1 file changed, 2 insertions(+), 2 deletions(-)
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git status
On branch main
nothing to commit, working tree clean
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> code test_grading.py
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> python -m unittest -v
test_boundary_values (test_grading.TestGrading) ... test_invalid_marks (test_grading.TestGrading) ... ok
test_malformed_csv (test_grading.TestGrading) ... ok

======================================================================
FAIL: test_boundary_values (test_grading.TestGrading) (marks=39)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading\test_grading.py", line 24, in test_boundary_values
    self.assertEqual(calculate_grade(marks), expected)
AssertionError: 'D' != 'F'
- D
+ F


======================================================================
FAIL: test_boundary_values (test_grading.TestGrading) (marks=40)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading\test_grading.py", line 24, in test_boundary_values
    self.assertEqual(calculate_grade(marks), expected)
AssertionError: 'D' != 'C'
- D
+ C


======================================================================
FAIL: test_boundary_values (test_grading.TestGrading) (marks=60)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading\test_grading.py", line 24, in test_boundary_values
    self.assertEqual(calculate_grade(marks), expected)
AssertionError: 'C' != 'B'
- C
+ B


======================================================================
FAIL: test_boundary_values (test_grading.TestGrading) (marks=80)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading\test_grading.py", line 24, in test_boundary_values
    self.assertEqual(calculate_grade(marks), expected)
AssertionError: 'B' != 'A'
- B
+ A


----------------------------------------------------------------------
Ran 3 tests in 0.013s

FAILED (failures=4)
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git add test_grading.py
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> git commit -m "Add boundary and invalid inputs"
[main b2da031] Add boundary and invalid inputs
 1 file changed, 47 insertions(+), 13 deletions(-)
PS C:\Users\Sarthak Amrute\OneDrive\Desktop\Assignment 7\student_grading> code REPORT.md