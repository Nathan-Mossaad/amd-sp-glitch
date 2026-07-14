# duration_test_plot.py
import plot
import result

results = result.results_by_type(result.read_from_file("split.txt"))
# results = result.results_by_type(result.read_from_file("stiched.txt"))


# plot.plot_delays_bar(["success", "broken"], results, bin_count=2000, show_percent=True)
# plot.plot_delays_bar(["success", "broken"], results, bin_count=2000, show_percent=False)
plot.plot_durations_bar(["success", "broken"], results, bin_count=40, show_percent=True)
plot.plot_durations_bar(
    ["success", "broken"], results, bin_count=40, show_percent=False
)
