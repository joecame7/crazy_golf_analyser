# Crazy Golf Score Analyzer

A comprehensive Python tool for analyzing crazy golf (mini golf) scores with detailed statistics and visualizations.

## Features

- **Statistical Analysis**: Calculate totals, averages, best/worst holes, and consistency metrics
- **Player Rankings**: Automatic ranking based on total scores
- **Hole Difficulty Analysis**: Identify the hardest and easiest holes
- **Performance Insights**: Mental resilience, consistency streaks, and performance trends
- **Comprehensive Visualizations**: 9 different charts showing various aspects of performance
- **Flexible Input**: Read scores from text file with easy-to-edit format

## Requirements

### Python Libraries
Install the required libraries using pip:

```bash
pip install pandas numpy matplotlib seaborn
```

Or install all at once:
```bash
pip install pandas numpy matplotlib seaborn statistics
```

### Python Version
- Python 3.6 or higher

## File Structure
```
crazy_golf_analyser/
├── crazy_golf_analysis.py    # Main analysis script
├── golf_scores.txt          # Score data file
└── README.md               # This file
```

## How to Run

1. **Prepare your score data**:
   - Edit [`golf_scores.txt`](golf_scores.txt) with your player names and scores
   - Follow the format: `PlayerName: score1, score2, score3, ...`
   - You can use commas or spaces to separate scores
   - Lines starting with `#` are comments and will be ignored

2. **Run the analysis**:
   ```bash
   python crazy_golf_analysis.py
   ```

3. **View results**:
   - Statistical analysis will be printed to the console
   - A comprehensive visualization will be saved as `crazy_golf_all_analysis.png` in your Downloads folder
   - The visualization window will also display interactively

## Score File Format

The [`golf_scores.txt`](golf_scores.txt) file should follow this format:

```
Player 1: 2, 2, 2, 5, 2, 2, 4, 2, 2, 5, 3, 2, 2, 2, 2, 2, 3, 2
Player 2: 3, 2, 2, 3, 3, 4, 3, 2, 2, 4, 3, 3, 2, 1, 2, 3, 2, 1
Player 3: 4 5 3 3 4 4 5 2 2 6 2 3 1 3 5 2 3 6
# This is a comment line - it will be ignored
# You can use commas, spaces, or both to separate scores
```

## Output

### Console Output
- Player summary with totals, averages, best/worst holes
- Player rankings by total score
- Hole difficulty analysis
- Performance insights (consistency, aces)
- Performance trends (improvement/decline)

### Visualizations
The script generates a comprehensive 9-panel visualization showing:
1. **Total Scores Comparison** - Bar chart of final scores
2. **Score Distribution** - Box plots showing score ranges per player
3. **Hole Difficulty** - Line chart of average scores per hole
4. **Performance by Hole** - Individual player performance across all holes
5. **Score Frequency Heatmap** - How often each player scored 1-6+ strokes
6. **Cumulative Progression** - Running total scores throughout the round
7. **Performance by Course Segment** - Radar chart of performance in 3 sections
8. **Mental Resilience** - How players perform after good vs bad holes
9. **Consistency Streaks** - Longest consecutive good/bad hole streaks

## Troubleshooting

### File Not Found Error
If you get a "File not found" error:
- Make sure [`golf_scores.txt`](golf_scores.txt) is in the same directory as [`crazy_golf_analysis.py`](crazy_golf_analysis.py)
- The script will automatically create an example file if none exists

### Import Errors
If you get import errors, install the missing packages:
```bash
pip install [package_name]
```

### Visualization Issues
If charts don't display properly:
- Try updating matplotlib: `pip install --upgrade matplotlib`
- Check that you have a GUI backend available for matplotlib

### No Data Found
If the script says "No valid scores found":
- Check that your score file follows the correct format
- Ensure player names are followed by a colon `:`
- Make sure scores are separated by commas or spaces
- Verify that scores are valid integers

## Customization

### Adding More Players
Simply add more lines to [`golf_scores.txt`](golf_scores.txt):
```
New Player: 3, 2, 4, 2, 3, 2, 5, 1, 2, 3, 4, 2, 2, 3, 2, 4, 3, 2
```

### Different Course Lengths
The script automatically adapts to different numbers of holes per player.

### Changing Output Location
By default, visualizations are saved to your Downloads folder. To change this, modify the `plt.savefig()` path in the [`create_comprehensive_visualization`](crazy_golf_analysis.py) function.

## License

This project is open source and available for personal use.
