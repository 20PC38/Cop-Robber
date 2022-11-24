# Cop-Robber-Game
We investigate the game of cops and robber, played on a finite graph, between one cop and one robber. If the cop can force a win on a graph, the graph is called cop-win. This project inputs a graph, and finds whether it is a cop-win graph using the technique cited in a research paper ‘Cop-Win Graphs: Optimal Strategies and Corner Rank’ by David Offner, Kerry Ojakian (attached in the repo). In the paper, a characterization of cop-win is given in terms of corner rank (a positive integer value or infinity given to each vertices of a graph) instead of well-known characterization via dismantling ordering.

THE GAME:
	The game of cops and robber is a two-player pursuit-evasion game played on a graph. To begin the game, the cop and robber each choose a vertex to occupy, with the cop choosing first. Play then alternates between the cop and the robber, with the cop moving first. On a turn a player may move to an adjacent vertex or stay still. If the cop and robber ever occupy the same vertex, the robber is caught and the cop wins. If the cop can force a win on a graph, we say the graph is cop-win.

The sample graphs are given in each txt files.
One of them in cop-win.

# Run: 
python final_code.py



