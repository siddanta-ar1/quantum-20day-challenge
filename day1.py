# Instead of just print, save the diagram
qc.draw(output="mpl", filename="circuit.png")

# ... (run simulation) ...

# Save the histogram
plot_histogram(counts, filename="histogram.png")
