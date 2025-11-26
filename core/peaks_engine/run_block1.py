from core.peaks_engine.data_layer import load_data
from core.peaks_engine.logic_layer import extract_peaks
from core.peaks_engine.output_layer import save_json, render_chart


def run_block1():
    spot, fut = load_data()
    spot, fut = normalize(spot, fut)

    fut_peaks = detect_peaks(fut)
    matched = match_spot_futures(fut_peaks, spot)
    final = filter_late_wicks(matched, spot)

    df = table_output(final)
    print(df.head())

    to_json(final, "block1_output.json")
    plot_peaks(fut, final)


if name == "main":
    run_block1()
