import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean, median, mode, stdev
import os

def read_scores_from_file(filename):
    """
    Read scores from a text file.
    Expected format:
    PlayerName: score1, score2, score3, ...
    """
    scores = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('#') or not line:  # Skip comments and empty lines
                    continue
                if ':' in line:
                    name, scores_str = line.split(':', 1)
                    name = name.strip()
                    # Parse scores - handle both comma and space separation
                    score_list = []
                    for score in scores_str.replace(',', ' ').split():
                        try:
                            score_list.append(int(score))
                        except ValueError:
                            continue
                    if score_list:
                        scores[name] = score_list
        
        if not scores:
            print("No valid scores found in file. Using default data.")
            return get_default_scores()
        
        return scores
    
    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating example file and using default data.")
        create_example_file(filename)
        return get_default_scores()

def get_default_scores():
    """Return the original hardcoded scores as fallback."""
    return {
        'Player 1': [2, 2, 2, 5, 2, 2, 4, 2, 2, 5, 3, 2, 2, 2, 2, 2, 3, 2],
        'Player 2':    [3, 2, 2, 3, 3, 4, 3, 2, 2, 4, 3, 3, 2, 1, 2, 3, 2, 1],
        'Player 3': [4, 5, 3, 3, 4, 4, 5, 2, 2, 6, 2, 3, 1, 3, 5, 2, 3, 6],
        'Player 4': [2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 5, 5, 3, 5, 3, 2, 2]
    }

def create_example_file(filename):
    """Create an example scores file for the user."""
    example_content = """Player 1: 2, 2, 2, 5, 2, 2, 4, 2, 2, 5, 3, 2, 2, 2, 2, 2, 3, 2
Player 2: 3, 2, 2, 3, 3, 4, 3, 2, 2, 4, 3, 3, 2, 1, 2, 3, 2, 1
Player 3: 4, 5, 3, 3, 4, 4, 5, 2, 2, 6, 2, 3, 1, 3, 5, 2, 3, 6
Player 4: 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 5, 5, 3, 5, 3, 2, 2

# Format: PlayerName: score1, score2, score3, ...
# You can use commas or spaces to separate scores
# Lines starting with # are ignored
"""
    
    try:
        with open(filename, 'w') as file:
            file.write(example_content)
        print(f"Created example file: {filename}")
        print("Edit this file with your own scores and run the script again!")
    except Exception as e:
        print(f"Could not create example file: {e}")

def analyze_scores(scores):
    print("CRAZY GOLF SCORE ANALYSIS")
    print("=" * 50)
    
    # Basic statistics
    print("\nPLAYER SUMMARY:")
    results = {}
    for player, player_scores in scores.items():
        total = sum(player_scores)
        avg = mean(player_scores)
        best = min(player_scores)
        worst = max(player_scores)
        consistency = stdev(player_scores)
        
        results[player] = {
            'total': total,
            'average': avg,
            'best_hole': best,
            'worst_hole': worst,
            'consistency': consistency
        }
        
        print(f"\n{player}:")
        print(f"  Total Score: {total}")
        print(f"  Average: {avg:.2f}")
        print(f"  Best Hole: {best}")
        print(f"  Worst Hole: {worst}")
        print(f"  Consistency (std dev): {consistency:.2f}")
    
    # Rankings
    print("\nRANKINGS:")
    sorted_players = sorted(results.items(), key=lambda x: x[1]['total'])
    for i, (player, stats) in enumerate(sorted_players, 1):
        print(f"{i}. {player} - {stats['total']} strokes")
    
    # Hole difficulty analysis
    print("\nHOLE DIFFICULTY ANALYSIS:")
    hole_averages = []
    for hole in range(18):
        hole_scores = [scores[player][hole] for player in scores.keys()]
        avg_score = mean(hole_scores)
        hole_averages.append(avg_score)
        print(f"Hole {hole + 1}: {avg_score:.2f} average")
    
    hardest_hole = hole_averages.index(max(hole_averages)) + 1
    easiest_hole = hole_averages.index(min(hole_averages)) + 1
    print(f"\nHardest Hole: #{hardest_hole} (avg: {max(hole_averages):.2f})")
    print(f"Easiest Hole: #{easiest_hole} (avg: {min(hole_averages):.2f})")
    
    # Performance insights
    print("\nPERFORMANCE INSIGHTS:")
    most_consistent = min(results.items(), key=lambda x: x[1]['consistency'])
    least_consistent = max(results.items(), key=lambda x: x[1]['consistency'])
    
    print(f"Most Consistent: {most_consistent[0]} (std dev: {most_consistent[1]['consistency']:.2f})")
    print(f"Least Consistent: {least_consistent[0]} (std dev: {least_consistent[1]['consistency']:.2f})")
    
    # Hole-in-one analysis
    print("\nACE ANALYSIS:")
    for player, player_scores in scores.items():
        aces = player_scores.count(1)
        if aces > 0:
            ace_holes = [i+1 for i, score in enumerate(player_scores) if score == 1]
            print(f"{player}: {aces} hole-in-one(s) on hole(s) {ace_holes}")
    
    return results, hole_averages

def create_visualizations(results, hole_averages, scores):
    plt.style.use('seaborn-v0_8')
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Total scores comparison
    players = list(results.keys())
    totals = [results[player]['total'] for player in players]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    ax1.bar(players, totals, color=colors)
    ax1.set_title('Total Scores Comparison', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Total Strokes')
    ax1.set_xlabel('Players')
    for i, v in enumerate(totals):
        ax1.text(i, v + 0.5, str(v), ha='center', fontweight='bold')
    
    # Score distribution by player
    all_scores = []
    player_labels = []
    for player, player_scores in scores.items():
        all_scores.extend(player_scores)
        player_labels.extend([player] * len(player_scores))
    
    df = pd.DataFrame({'Player': player_labels, 'Score': all_scores})
    sns.boxplot(data=df, x='Player', y='Score', ax=ax2, palette=colors)
    ax2.set_title('Score Distribution by Player', fontsize=14, fontweight='bold')
    
    # Hole difficulty
    holes = list(range(1, 19))
    ax3.plot(holes, hole_averages, marker='o', linewidth=2, markersize=6, color='#E74C3C')
    ax3.set_title('Hole Difficulty (Average Score)', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Hole Number')
    ax3.set_ylabel('Average Score')
    ax3.set_xticks(holes)
    ax3.grid(True, alpha=0.3)
    
    # Player performance over holes
    for i, (player, player_scores) in enumerate(scores.items()):
        ax4.plot(holes, player_scores, marker='o', label=player, linewidth=2, color=colors[i])
    ax4.set_title('Player Performance by Hole', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Hole Number')
    ax4.set_ylabel('Strokes')
    ax4.set_xticks(holes)
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.expanduser('~'), 'Downloads', 'crazy_golf_analysis.png'), 
                dpi=300, bbox_inches='tight')
    plt.show()

def create_additional_visualizations(scores):
    plt.style.use('seaborn-v0_8')
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    # 1. Score frequency heatmap
    score_matrix = []
    players = list(scores.keys())
    for player in players:
        player_freq = [0] * 7  # scores 1-6 plus position for score >6
        for score in scores[player]:
            if score <= 6:
                player_freq[score-1] += 1
            else:
                player_freq[6] += 1
        score_matrix.append(player_freq)
    
    score_labels = ['1', '2', '3', '4', '5', '6', '6+']
    sns.heatmap(score_matrix, annot=True, fmt='d', cmap='YlOrRd', 
                xticklabels=score_labels, yticklabels=players, ax=ax1)
    ax1.set_title('Score Frequency Heatmap', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Score')
    ax1.set_ylabel('Player')
    
    # 2. Cumulative score progression
    holes = list(range(1, 19))
    for i, (player, player_scores) in enumerate(scores.items()):
        cumulative = np.cumsum(player_scores)
        ax2.plot(holes, cumulative, marker='o', label=player, linewidth=2, color=colors[i])
    
    ax2.set_title('Cumulative Score Progression', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Hole Number')
    ax2.set_ylabel('Cumulative Strokes')
    ax2.set_xticks(holes)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. Performance consistency radar chart (variance by hole segments)
    from math import pi
    
    # Calculate performance in 3 segments (holes 1-6, 7-12, 13-18)
    segments = ['Holes 1-6', 'Holes 7-12', 'Holes 13-18']
    segment_data = {}
    
    for player, player_scores in scores.items():
        seg1 = mean(player_scores[0:6])
        seg2 = mean(player_scores[6:12])
        seg3 = mean(player_scores[12:18])
        segment_data[player] = [seg1, seg2, seg3]
    
    angles = [n / float(len(segments)) * 2 * pi for n in range(len(segments))]
    angles += angles[:1]  # Complete the circle
    
    ax3 = plt.subplot(223, projection='polar')
    for i, (player, values) in enumerate(segment_data.items()):
        values += values[:1]  # Complete the circle
        ax3.plot(angles, values, 'o-', linewidth=2, label=player, color=colors[i])
        ax3.fill(angles, values, alpha=0.25, color=colors[i])
    
    ax3.set_xticks(angles[:-1])
    ax3.set_xticklabels(segments)
    ax3.set_title('Performance by Course Segment\n(Lower = Better)', fontsize=12, fontweight='bold', pad=20)
    ax3.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
    
    # 4. Bounce-back analysis (performance after bad holes)
    bounce_back_data = {'Player': [], 'After Bad Hole': [], 'After Good Hole': []}
    
    for player, player_scores in scores.items():
        bad_hole_recoveries = []
        good_hole_followups = []
        
        for i in range(len(player_scores) - 1):
            current_score = player_scores[i]
            next_score = player_scores[i + 1]
            
            if current_score >= 4:  # Bad hole (4+ strokes)
                bad_hole_recoveries.append(next_score)
            elif current_score <= 2:  # Good hole (1-2 strokes)
                good_hole_followups.append(next_score)
        
        if bad_hole_recoveries:
            bounce_back_data['Player'].append(player)
            bounce_back_data['After Bad Hole'].append(mean(bad_hole_recoveries))
            bounce_back_data['After Good Hole'].append(mean(good_hole_followups) if good_hole_followups else 0)
    
    x = np.arange(len(bounce_back_data['Player']))
    width = 0.35
    
    ax4.bar(x - width/2, bounce_back_data['After Bad Hole'], width, 
            label='After Bad Hole (4+)', color='#E74C3C', alpha=0.8)
    ax4.bar(x + width/2, bounce_back_data['After Good Hole'], width, 
            label='After Good Hole (1-2)', color='#27AE60', alpha=0.8)
    
    ax4.set_title('Mental Resilience Analysis', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Player')
    ax4.set_ylabel('Average Next Hole Score')
    ax4.set_xticks(x)
    ax4.set_xticklabels(bounce_back_data['Player'])
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.expanduser('~'), 'Downloads', 'crazy_golf_additional_analysis.png'), 
                dpi=300, bbox_inches='tight')
    plt.show()

def performance_trends(scores):
    print("\nPERFORMANCE TRENDS:")
    
    # Calculate running averages for each player
    for player, player_scores in scores.items():
        running_avg = []
        for i in range(len(player_scores)):
            running_avg.append(mean(player_scores[:i+1]))
        
        first_9 = mean(player_scores[:9])
        last_9 = mean(player_scores[9:])
        trend = "improving" if last_9 < first_9 else "declining" if last_9 > first_9 else "stable"
        
        print(f"{player}: First 9 avg: {first_9:.2f}, Last 9 avg: {last_9:.2f} - {trend}")

def create_comprehensive_visualization(results, hole_averages, scores):
    plt.style.use('seaborn-v0_8')
    fig = plt.figure(figsize=(20, 16))
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    # 1. Total scores comparison
    ax1 = plt.subplot(3, 3, 1)
    players = list(results.keys())
    totals = [results[player]['total'] for player in players]
    
    ax1.bar(players, totals, color=colors)
    ax1.set_title('Total Scores Comparison', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Total Strokes')
    for i, v in enumerate(totals):
        ax1.text(i, v + 0.5, str(v), ha='center', fontweight='bold')
    
    # 2. Score distribution by player
    ax2 = plt.subplot(3, 3, 2)
    all_scores = []
    player_labels = []
    for player, player_scores in scores.items():
        all_scores.extend(player_scores)
        player_labels.extend([player] * len(player_scores))
    
    df = pd.DataFrame({'Player': player_labels, 'Score': all_scores})
    sns.boxplot(data=df, x='Player', y='Score', ax=ax2, palette=colors)
    ax2.set_title('Score Distribution by Player', fontsize=12, fontweight='bold')
    
    # 3. Hole difficulty
    ax3 = plt.subplot(3, 3, 3)
    holes = list(range(1, 19))
    ax3.plot(holes, hole_averages, marker='o', linewidth=2, markersize=4, color='#E74C3C')
    ax3.set_title('Hole Difficulty (Average Score)', fontsize=12, fontweight='bold')
    ax3.set_xlabel('Hole Number')
    ax3.set_ylabel('Average Score')
    ax3.set_xticks(holes[::2])  # Show every other hole number to avoid crowding
    ax3.grid(True, alpha=0.3)
    
    # 4. Player performance over holes
    ax4 = plt.subplot(3, 3, 4)
    for i, (player, player_scores) in enumerate(scores.items()):
        ax4.plot(holes, player_scores, marker='o', label=player, linewidth=2, color=colors[i], markersize=3)
    ax4.set_title('Player Performance by Hole', fontsize=12, fontweight='bold')
    ax4.set_xlabel('Hole Number')
    ax4.set_ylabel('Strokes')
    ax4.set_xticks(holes[::2])
    ax4.legend(fontsize=8)
    ax4.grid(True, alpha=0.3)
    
    # 5. Score frequency heatmap
    ax5 = plt.subplot(3, 3, 5)
    score_matrix = []
    for player in players:
        player_freq = [0] * 7
        for score in scores[player]:
            if score <= 6:
                player_freq[score-1] += 1
            else:
                player_freq[6] += 1
        score_matrix.append(player_freq)
    
    score_labels = ['1', '2', '3', '4', '5', '6', '6+']
    sns.heatmap(score_matrix, annot=True, fmt='d', cmap='YlOrRd', 
                xticklabels=score_labels, yticklabels=players, ax=ax5)
    ax5.set_title('Score Frequency Heatmap', fontsize=12, fontweight='bold')
    
    # 6. Cumulative score progression
    ax6 = plt.subplot(3, 3, 6)
    for i, (player, player_scores) in enumerate(scores.items()):
        cumulative = np.cumsum(player_scores)
        ax6.plot(holes, cumulative, marker='o', label=player, linewidth=2, color=colors[i], markersize=3)
    
    ax6.set_title('Cumulative Score Progression', fontsize=12, fontweight='bold')
    ax6.set_xlabel('Hole Number')
    ax6.set_ylabel('Cumulative Strokes')
    ax6.set_xticks(holes[::2])
    ax6.legend(fontsize=8)
    ax6.grid(True, alpha=0.3)
    
    # 7. Performance consistency radar chart
    ax7 = plt.subplot(3, 3, 7, projection='polar')
    segments = ['Holes 1-6', 'Holes 7-12', 'Holes 13-18']
    segment_data = {}
    
    for player, player_scores in scores.items():
        seg1 = mean(player_scores[0:6])
        seg2 = mean(player_scores[6:12])
        seg3 = mean(player_scores[12:18])
        segment_data[player] = [seg1, seg2, seg3]
    
    angles = [n / float(len(segments)) * 2 * np.pi for n in range(len(segments))]
    angles += angles[:1]
    
    for i, (player, values) in enumerate(segment_data.items()):
        values += values[:1]
        ax7.plot(angles, values, 'o-', linewidth=2, label=player, color=colors[i])
        ax7.fill(angles, values, alpha=0.25, color=colors[i])
    
    ax7.set_xticks(angles[:-1])
    ax7.set_xticklabels(segments, fontsize=8)
    ax7.set_title('Performance by Course Segment', fontsize=12, fontweight='bold', pad=20)
    ax7.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0), fontsize=8)
    
    # 8. Mental resilience analysis
    ax8 = plt.subplot(3, 3, 8)
    bounce_back_data = {'Player': [], 'After Bad Hole': [], 'After Good Hole': []}
    
    for player, player_scores in scores.items():
        bad_hole_recoveries = []
        good_hole_followups = []
        
        for i in range(len(player_scores) - 1):
            current_score = player_scores[i]
            next_score = player_scores[i + 1]
            
            if current_score >= 4:
                bad_hole_recoveries.append(next_score)
            elif current_score <= 2:
                good_hole_followups.append(next_score)
        
        if bad_hole_recoveries:
            bounce_back_data['Player'].append(player)
            bounce_back_data['After Bad Hole'].append(mean(bad_hole_recoveries))
            bounce_back_data['After Good Hole'].append(mean(good_hole_followups) if good_hole_followups else 0)
    
    x = np.arange(len(bounce_back_data['Player']))
    width = 0.35
    
    ax8.bar(x - width/2, bounce_back_data['After Bad Hole'], width, 
            label='After Bad Hole (4+)', color='#E74C3C', alpha=0.8)
    ax8.bar(x + width/2, bounce_back_data['After Good Hole'], width, 
            label='After Good Hole (1-2)', color='#27AE60', alpha=0.8)
    
    ax8.set_title('Mental Resilience Analysis', fontsize=12, fontweight='bold')
    ax8.set_xlabel('Player')
    ax8.set_ylabel('Avg Next Score')
    ax8.set_xticks(x)
    ax8.set_xticklabels(bounce_back_data['Player'])
    ax8.legend(fontsize=8)
    ax8.grid(True, alpha=0.3)
    
    # 9. Streak analysis - longest consecutive good/bad holes
    ax9 = plt.subplot(3, 3, 9)
    
    streak_data = {'Player': [], 'Good Streaks': [], 'Bad Streaks': []}
    
    for player, player_scores in scores.items():
        # Find longest streaks of good holes (score <= 2) and bad holes (score >= 4)
        current_good_streak = 0
        current_bad_streak = 0
        max_good_streak = 0
        max_bad_streak = 0
        
        for score in player_scores:
            if score <= 2:  # Good hole
                current_good_streak += 1
                current_bad_streak = 0
                max_good_streak = max(max_good_streak, current_good_streak)
            elif score >= 4:  # Bad hole
                current_bad_streak += 1
                current_good_streak = 0
                max_bad_streak = max(max_bad_streak, current_bad_streak)
            else:  # Neutral hole (score = 3)
                current_good_streak = 0
                current_bad_streak = 0
        
        streak_data['Player'].append(player)
        streak_data['Good Streaks'].append(max_good_streak)
        streak_data['Bad Streaks'].append(max_bad_streak)
    
    x = np.arange(len(streak_data['Player']))
    width = 0.35
    
    ax9.bar(x - width/2, streak_data['Good Streaks'], width, 
            label='Longest Good Streak (≤2)', color='#27AE60', alpha=0.8)
    ax9.bar(x + width/2, streak_data['Bad Streaks'], width, 
            label='Longest Bad Streak (≥4)', color='#E74C3C', alpha=0.8)
    
    ax9.set_title('Consistency Streaks Analysis', fontsize=12, fontweight='bold')
    ax9.set_xlabel('Player')
    ax9.set_ylabel('Consecutive Holes')
    ax9.set_xticks(x)
    ax9.set_xticklabels(streak_data['Player'])
    ax9.legend(fontsize=8)
    ax9.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for i, (good, bad) in enumerate(zip(streak_data['Good Streaks'], streak_data['Bad Streaks'])):
        if good > 0:
            ax9.text(i - width/2, good + 0.1, str(good), ha='center', fontsize=8)
        if bad > 0:
            ax9.text(i + width/2, bad + 0.1, str(bad), ha='center', fontsize=8)

    plt.tight_layout(pad=2.0)
    plt.savefig(os.path.join(os.path.expanduser('~'), 'Downloads', 'crazy_golf_all_analysis.png'), 
                dpi=300, bbox_inches='tight')
    plt.show()

# Remove the old visualization functions and replace the main execution
if __name__ == "__main__":
    # Read scores from file - use current directory or user's home directory
    scores_file = "golf_scores.txt"
    if not os.path.exists(scores_file):
        scores_file = os.path.join(os.path.expanduser('~'), 'Documents', 'golf_scores.txt')
    
    scores = read_scores_from_file(scores_file)
    
    print(f"Loaded scores for {len(scores)} players:")
    for player, player_scores in scores.items():
        print(f"  {player}: {len(player_scores)} holes")
    print()
    
    results, hole_averages = analyze_scores(scores)
    performance_trends(scores)
    create_comprehensive_visualization(results, hole_averages, scores)
    
    print(f"\nComplete analysis with all graphs saved to crazy_golf_all_analysis.png in Downloads folder")
    print(f"To analyze different scores, edit the file: {scores_file}")
