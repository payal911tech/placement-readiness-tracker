# Placement Readiness Tracker

## Purpose
A Python command-line tool built for the Industry Readiness Programme-II (CSE2596) to record student practice-test scores (Aptitude, Verbal, and Coding), calculate averages, assign grades, identify the top scorer, and flag students who need extra practice.

## How to Run
1. Make sure Python 3 is installed on your system.
2. Open your terminal in the project folder and run:
   ```bash
   python tracker.py
   ## Sample Output
```text
=== Add New Student ===
Enter student name: Neha Sharma
Enter roll number: CSE006
Enter Aptitude score (0-100): 76
Enter Verbal score (0-100): 82
Enter Coding score (0-100): 79

==================================================================================
Roll No    | Name             | Aptitude | Verbal   | Coding   | Average  | Grade         
----------------------------------------------------------------------------------
CSE001     | Aarav Sharma     | 85.0     | 78.0     | 92.0     | 85.00    | A             
CSE002     | Diya Patel       | 45.0     | 55.0     | 38.0     | 46.00    | C             
CSE003     | Kabir Verma      | 72.0     | 65.0     | 80.0     | 72.33    | B             
CSE004     | Ananya Gupta     | 30.0     | 40.0     | 35.0     | 35.00    | Needs practice
CSE005     | Rohan Iyer       | 90.0     | 88.0     | 95.0     | 91.00    | A             
CSE006     | Neha Sharma      | 76.0     | 82.0     | 79.0     | 79.00    | B             
==================================================================================

Top Scorer: Rohan Iyer (CSE005) - Average: 91.00
Students Needing Extra Practice (Average < 40):
 - Ananya Gupta (CSE004): Average = 35.00

