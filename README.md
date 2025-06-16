# Crazy Golf Score Analyser

A comprehensive Python tool for analysing crazy golf (mini golf) scores with detailed statistics and visualisations.

## Features

- Statistical Analysis: Calculate totals, averages, best/worst holes, and consistency metrics  
- Player Rankings: Automatic ranking based on total scores  
- Hole Difficulty Analysis: Identify the hardest and easiest holes  
- Performance Insights: Mental resilience, consistency streaks, and performance trends  
- Comprehensive Visualisations: 9 different charts showing various aspects of performance  
- Flexible Input: Read scores from text file with easy-to-edit format  

## Requirements

### Python Libraries  
Install the required libraries using pip:

    pip install pandas numpy matplotlib seaborn

Or install all at once:

    pip install pandas numpy matplotlib seaborn statistics

### Python Version  
- Python 3.6 or higher

## File Structure

    crazy_golf_analyser/
    ├── crazy_golf_analysis.py    # Main analysis script
    ├── golf_scores.txt           # Score data file
    └── README.md                 # This file

## How to Run

1. Prepare your score data:
   - Edit `golf_scores.txt` with your player names and scores  
   - Format: `PlayerName: score1, score2, score3, ...`  
   - Use commas or spaces to separate scores  
   - Lines starting with `#` are comments and will be ignored  

2. Run the analysis:

       python crazy_golf_analysis.py

3. View results:
   - Stats printed in the console  
   - A visualisation saved to your Downloads folder as `crazy_golf_all_analysis.png`  
   - A visualisation window will also open interactively  

## Score File Format

Example:

    Player 1: 2, 2, 2, 5, 2, 2, 4, 2, 2, 5, 3, 2, 2, 2, 2, 2, 3, 2
    Player 2: 3, 2, 2, 3, 3, 4, 3, 2, 2, 4, 3, 3, 2, 1, 2, 3, 2, 1
    Player 3: 4 5 3 3 4 4 5 2 2 6 2 3 1 3 5 2 3 6
    # This is a comment line - it will be ignored
    # You can use commas, spaces, or both to separate scores

## Output

### Console Output

- Player summaries: totals, averages, best/worst holes  
- Player rankings by total score  
- Hole difficulty analysis  
- Performance insights (consistency, aces)  
- Performance trends  

### Visualisations

9-panel output:

1. Total Scores Comparison (bar chart)  
2. Score Distribution (box plots)  
3. Hole Difficulty (line chart)  
4. Performance by Hole  
5. Score Frequency Heatmap  
6. Cumulative Progression  
7. Performance by Course Segment (radar chart)  
8. Mental Resilience  
9. Consistency Streaks  

## Troubleshooting

### File Not Found Error

- Check `golf_scores.txt` is in the same directory as `crazy_golf_analysis.py`  
- The script will generate an example if the file is missing  

### Import Errors

- Use `pip install [package_name]` to fix missing libraries  

### Visualisation Issues

- Try `pip install --upgrade matplotlib`  
- Make sure your system supports GUI windows for charts  

### No Data Found

- Check file formatting  
- Use colon `:` after player names  
- Separate scores with commas or spaces  
- Make sure scores are valid integers  

## Customisation

### Add Players

Just add more lines to `golf_scores.txt`:

    New Player: 3, 2, 4, 2, 3, 2, 5, 1, 2, 3, 4, 2, 2, 3, 2, 4, 3, 2

### Different Course Lengths

The script auto-adjusts to the number of holes.

### Change Output Location

Edit the path inside the `create_comprehensive_visualisation` function in the script.

## Licence

This project is open source and available for personal use.
