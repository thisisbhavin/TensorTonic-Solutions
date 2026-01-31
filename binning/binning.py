def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    v_min = min(values)
    v_max = max(values)
    w = (v_max - v_min) / num_bins
    return [int(min([(x-v_min)//w, num_bins - 1])) if v_min != v_max else 0 for x in values]