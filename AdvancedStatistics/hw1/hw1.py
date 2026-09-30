import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import polars as pl
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.stats import shapiro, normaltest, iqr
    import altair as alt
    import seaborn as sns
    import random


    return iqr, mo, np, pd, plt, shapiro, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Use the blood-test dataset containing healthy individuals and patients with different types of
    anemia, linked in the Kaggle notebook. See also the original publication. Use the healthy group
    for Tasks 2-5 and the original, untrimmed data unless explicitly asked otherwise.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #1. Sample and feature types | 1 point


    Describe what one row represents. Identify the diagnosis column and select healthy individuals;
    report the sample size before and after filtering. For every feature, state whether it is numerical or
    categorical; distinguish discrete and continuous numerical measurements. Identify identifiers that
    should be excluded from numerical analysis. Check for missing values and explain how you handle
    them. What limits the generalizability of conclusions from this sample?
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv('anemia_dataset.csv', index_col=0)
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    One row represents a one blood sample, characterized by continuous biochemical features (WBC, NE, HGB), and discrete features (gender, anemia status)
    """)
    return


@app.cell
def _(df):
    df_healthy = df[df['All_Class'] == 0]

    print('number of samples:', len(df))
    print('number of healthy samples:', len(df_healthy))

    df_healthy
    return (df_healthy,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Features gender, All_class, HGB_anemia class, iron_anemia_class, folate_anemia class, B12_anemia class are nominal, despite being represented by numbers because these numbers serve like placeholder to encode nominal features and dont have mathematical meaning.

    The rest features are numeric

    All numeric data are seems to be continous as thesea are measured parameters, not counted entities

    Features gender, All_class, HGB_anemia class, iron_anemia_class, folate_anemia class, B12_anemia class should be excluded from numerical analysis as there are no mathmatical meaning in these values
    """)
    return


@app.cell
def _(df_healthy):
    df_healthy.isna().sum()
    return


@app.cell
def _(df_healthy):
    nan_rows = df_healthy[df_healthy.isna().any(axis=1)]
    print(nan_rows)
    return


@app.cell
def _(df_healthy):
    nan_cols = df_healthy.columns[df_healthy.isna().any()].tolist()
    print(nan_cols)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To handle missing data, first I thought about dropping rows with NaNs. However, this results to lose of 12% ofrows which is too much. So we need smth different. Could perform linear interpolation or knn imputation but might be overkill. So I will fill NaNs with means if feature is normally distributed, else fill with median
    """)
    return


@app.cell
def _(df_healthy, shapiro):
    columns_to_check = [
        'WBC', 'MO#', 'EO#', 'HGB', 'HCT', 'MCH', 'MCHC', 
        'PCT', 'PDW', 'SD', 'TSD', 'FERRITTE', 'FOLATE', 'B12'
    ]

    print("--- Normality Test Results (Shapiro-Wilk) ---")

    for col in columns_to_check:
        if col in df_healthy.columns:
            data = df_healthy[col].dropna()
        

            stat, p_value = shapiro(data)
        

            is_normal = "Normally Distributed" if p_value > 0.05 else "NOT Normally Distributed"
        
            print(f"{col:<10} | p-value: {p_value:.5f} | Result: {is_normal}")
        else:
            print(f"{col:<10} | Column not found in DataFrame.")
    return (columns_to_check,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For all features normality assumption doesnt hold --> fill with medians
    """)
    return


@app.cell
def _(columns_to_check, df, df_healthy):
    for column_x in columns_to_check:
        if column_x in df.columns:
            median_value = df_healthy[column_x].median()
            df_healthy[column_x] = df_healthy[column_x].fillna(median_value)
    return


@app.cell
def _(df_healthy):
    df_healthy.isna().sum().sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What limits the generalizability of conclusions from this sample?

    Main limited is heavy class imbalance --> out of 1425 samples only 390 are healthy. Even if ill samples are interbalanced i.e n of anemia_x ~ n of anemia_z, resulting analysis will likely have bias toward ill yielding higher FP results.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #2. Empirical distributions | 1.5 points

    Choose two nonconstant numerical blood-test features. For each, plot a histogram and an
    empirical cumulative distribution function (ECDF). Describe the shape, asymmetry and spread.
    Choose and report a threshold in the original units, then use the ECDF to estimate the fraction of
    observations at or below it. Explain what the ECDF shows that is less directly visible in a histogram.
    """)
    return


@app.cell
def _(df_healthy, np, plt, sns):
    folate = np.array(df_healthy['FOLATE'])
    wbc = np.array(df_healthy['WBC'])

    sns.histplot(folate)
    plt.title("Folate Histplot")
    return folate, wbc


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Shape - bimodal, Assymetry - right skewed, Spread - mainly from ~1 to ~20, with outliers up to 70
    """)
    return


@app.cell
def _(folate, plt, sns):
    sns.ecdfplot(folate)
    plt.title('Folate ECDF plot')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Shape - sigmoid-ish, shows bimodality because of stair at 20. Right skewed, as curve climbs high values early. Spreads from ~1 to ~20, with outliers up to 70 (tiny stairs at the plato where y ~ 1)
    """)
    return


@app.cell
def _(plt, sns, wbc):
    sns.histplot(wbc)
    plt.title("WBC Histplot")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Shape - unimodal, assymetry - right skewed, Spread - majority falls in 1-15 range,  long right tail, outliers around 50-52
    """)
    return


@app.cell
def _(plt, sns, wbc):
    sns.ecdfplot(wbc)
    plt.title("WBC ECDF plot")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Shape - sigmoid, unimodal; Assymetry - right skewed; Spread - majority falls in 1-15 range,  long right tail with outliers around 50-52. Tails are indicated by tiny stairs at the top of the curve
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ECDF plots the exact percentile of each data point, showing the cumulative proportion of data that is less than or equal to a specific value, which is not well visible on histogram.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 3. Summary statistics and trimming | 2 points
    For any five numerical blood-test features, calculate the sample mean, median, standard deviation
    and interquartile range (IQR). For each feature separately, sort its nonmissing values, remove the
    smallest and largest floor(0.10n) observations, and recalculate the mean and median. Compare
    the original and trimmed results. Explain which statistics changed and why.
    Among all nonconstant numerical blood-test features, find the largest standardized
    mean-median difference, |mean - median| / standard deviation. Explain why standardization is
    needed. Plot this feature's distribution and mark its mean and median.
    """)
    return


@app.cell
def _(df_healthy, iqr, np, pd):
    def _():
        folate = np.array(df_healthy['FOLATE'])
        wbc = np.array(df_healthy['WBC'])
        b12 = np.array(df_healthy['B12'])
        sdtsd = np.array(df_healthy['SDTSD'])
        rbc = np.array(df_healthy['RBC'])

        mapping = {
            'FOLATE': folate,
            'WBC': wbc,
            'B12': b12,
            'SDTSD': sdtsd,
            'RBC': rbc
        }
    
        return mapping


    mapping = _()

    means = np.mean(list(mapping.values()), axis = 1)
    medians = np.median(list(mapping.values()), axis = 1)
    stds = np.std(list(mapping.values()), axis = 1)
    iqrs = iqr(list(mapping.values()), axis = 1)
    names = list(mapping.keys())


    summary_df = np.round(pd.DataFrame({
        'Feature': names,
        'Mean': means,
        'Median': medians,
        'Std_Dev': stds,
        'IQR': iqrs
    }),3)

    summary_df.set_index('Feature', inplace=True)
    summary_df
    return mapping, names


@app.cell
def _(iqr, mapping, names, np, pd):
    def trim(arr):
        arr = sorted(arr)
        k = int(0.10 * len(arr))
        trimmed_arr = arr[k:-k]
        return(trimmed_arr)

    
    mapping_trimmed = {i: trim(mapping[i]) for i in mapping}

    means_trimmed = np.mean(list(mapping_trimmed.values()), axis = 1)
    medians_trimmed = np.median(list(mapping_trimmed.values()), axis = 1)
    stds_trimmed = np.std(list(mapping_trimmed.values()), axis = 1)
    iqrs_trimmed = iqr(list(mapping_trimmed.values()), axis = 1)
    names_trimmed = list(mapping_trimmed.keys())


    summary_df_trimmed = np.round(pd.DataFrame({
        'Feature': names,
        'Mean': means_trimmed,
        'Median': medians_trimmed,
        'Std_Dev': stds_trimmed,
        'IQR': iqrs_trimmed
    }),3)

    summary_df_trimmed.set_index('Feature', inplace=True)
    summary_df_trimmed
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Mean is the most sensitive to outliers, so changed the most visibly when 20% of the most extreme data were cut off

    Median is intact as we cut data symmetricaly, so median still separates 2-quantiles from each other

    Std_dev also changed as it depends on mean. However std becames smaller, as trimming removes tails and less sigma is required to describe new distribution

    IQR decreaased for all data, as we cut 20% of outliers and Q1,Q3 moved to center
    """)
    return


@app.cell
def _(df_healthy, np):

    def find_largest_difference():
        features = [ 'WBC', 'NE#', 'LY#', 'MO#', 'EO#', 'BA#', 'RBC', 'HGB', 'HCT',
           'MCV', 'MCH', 'MCHC', 'RDW', 'PLT', 'MPV', 'PCT', 'PDW', 'SD', 'SDTSD',
           'TSD', 'FERRITTE', 'FOLATE', 'B12']

        max_different = float('-inf')
        max_different_label = None

        for f in features:
            arr = df_healthy[f]

            mean = np.mean(arr)
            median = np.median(arr)
            std = np.std(arr)

            mmdiff = (np.abs(mean - median)) / std

            if mmdiff > max_different:
                max_different = mmdiff
                max_different_label = f

        return(max_different, max_different_label)



    maxdiff, maxdiff_feature = find_largest_difference()

    print(maxdiff_feature, maxdiff)
    maxdiff_feature_mean = np.mean(df_healthy[maxdiff_feature])
    maxdiff_feature_median = np.median(df_healthy[maxdiff_feature])
    
    return maxdiff_feature, maxdiff_feature_mean, maxdiff_feature_median


@app.cell
def _(
    df_healthy,
    maxdiff_feature,
    maxdiff_feature_mean,
    maxdiff_feature_median,
    plt,
    sns,
):
    sns.histplot(df_healthy[maxdiff_feature])
    plt.axvline(x=maxdiff_feature_mean, color='red', linestyle='--', linewidth=2, label = 'mean')
    plt.axvline(x=maxdiff_feature_median, color='blue', linestyle='--', linewidth=2, label = 'median')
    plt.legend()
    plt.title('PWD Feature distribution')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In our case standartization is required because blood-test features are measured in completely different units, so there are different scales and without standardization we cannot compare them fairly.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #4. Mode and multimodality | 1 point
    Explain the difficulties in estimating the mode of continuous measurements. Find multimodal
    features in the healthy group and visualize them. For each candidate, compare histograms with
    10, 20 and 40 bins. Which peaks persist? Explain how the binning affects your conclusions and
    suggest a possible explanation for the observed multimodality, without presenting it as an
    established cause.
    """)
    return


@app.cell
def _():
    def _():
        features = [ 'WBC', 'NE#', 'LY#', 'MO#', 'EO#', 'BA#', 'RBC', 'HGB', 'HCT',
               'MCV', 'MCH', 'MCHC', 'RDW', 'PLT', 'MPV', 'PCT', 'PDW', 'SD', 'SDTSD',
               'TSD', 'FERRITTE', 'FOLATE', 'B12']
        return features


    features = _()
    return (features,)


@app.cell
def _(df_healthy, features, plt, sns):

    fig, axes = plt.subplots(nrows=6, ncols=4, figsize=(20, 24))
    axes = axes.flatten()  # Flatten to easily loop with a single index

    for i, feature in enumerate(features):
        sns.histplot(
            data=df_healthy, 
            x=feature, 
            kde=True, 
            stat="density", 
            ax=axes[i], 
            color="#1f77b4", 
            alpha=0.5
        )
    
        axes[i].set_title(f'{feature} Distribution', fontsize=12, fontweight='bold')
        axes[i].set_xlabel('Value')
        axes[i].set_ylabel('Density')

    # Hide the 24th subplot since we only have 23 features
    axes[-1].set_visible(False)

    # Optimize spacing so labels don't overlap
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(df_healthy, plt, sns):
    def experiment_with_bins(df_healthy):
        multimodal = ['PDW']
        maybe_multimodal = ['PCT', 'TSD']
        candidates = multimodal + maybe_multimodal

        sns.set_theme(style="whitegrid")

        bin_sizes = [10, 20, 40]

        for candidate in candidates:
            fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharey=True)
            fig.suptitle(f"Histogram Bin Comparison for: {candidate}", fontsize=16, fontweight='bold')
        
            data = df_healthy[candidate]
        
            for ax, bins in zip(axes, bin_sizes):
                sns.histplot(data, bins=bins, ax=ax, kde=True, color="skyblue")
            
                # Set titles and labels for scannability
                ax.set_title(f"{bins} Bins", fontsize=12)
                ax.set_xlabel("Value")
                if ax == axes[0]:
                    ax.set_ylabel("Frequency")
                
            plt.tight_layout()
        return plt.show()


    experiment_with_bins(df_healthy= df_healthy)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Only peaks for PDW persists.

    • Under-binning (10 Bins): High data aggregation obscures true data relationships. It smooths out local variations, potentially hiding multiple peaks and making a multimodal dataset falsely appear unimodal --> high risk of false negative conclusion on multimodality

    • Over-binning (40 Bins): High  resolution introduces artificial noise. Small sampling fluctuations or minor gaps can appear as distinct peaks, creating the illusion of multimodality where none truly exists --> high risk of false positive conclusion on multimodality

    • Optimal Binning (20 Bins): Balanced. If a distinct peak or structural split persists across 20 and 40 bins without fracturing into spikes, it indicates that pattern in rather real than binning artifact
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    PDW is platelet distribution width. Bimodal distribution in healthy donors can be explained by including 2 plateled subpopulations in sample - old platelets (larger) and young platelets (smaller). Physicall stress also can trigger blood release from spleen, introducing platelets of different size to bloodflow. Other factors, both biological (hormones, platelet preceders development cycles) and technical (EDTA-induced swelling) can also contribute to bimodality
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #5. Correlation and nonlinear dependence | 1.5 points
    Calculate Pearson correlation coefficients between the numerical blood-test features and display
    them as a labeled heatmap. Exclude identifiers, the diagnosis label and constant features. State
    how missing values are handled.
    Find the pair of features with a nonlinear relationship and plot their scatter plot. Report their
    Pearson correlation coefficient. Describe the relationship visible in the plot and explain what the
    coefficient captures or misses. Does a small Pearson correlation necessarily imply that two
    variables are independent? Support your answer with reasoning.
    """)
    return


@app.cell
def _(df_healthy, plt, sns):
    def build_pearson_corr_heatmap(df):
        features =  [ 'WBC', 'NE#', 'LY#', 'MO#', 'EO#', 'BA#', 'RBC', 'HGB', 'HCT',
               'MCV', 'MCH', 'MCHC', 'RDW', 'PLT', 'MPV', 'PCT', 'PDW', 'SD', 'SDTSD',
               'TSD', 'FERRITTE', 'FOLATE', 'B12']

        df_filtered = df[features]
        corr_matrix = df_filtered.corr(method="pearson")

        plt.figure(figsize=(16, 12))


        sns.heatmap(
            corr_matrix,
            annot=True,  
            fmt=".2f",  
            cmap="coolwarm",  
            vmin=-1,
            vmax=1,  
            square=True,  
            linewidths=0.5, 
            cbar_kws={"shrink": 0.8}
        )

        plt.title("Pearson Correlation Heatmap of Blood Metrics", fontsize=16)
        plt.tight_layout()
        plt.show()


    build_pearson_corr_heatmap(df_healthy)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Missing values are handled by per-column median imputation for healthy donors
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To find a pair of features with non linear relationship, we build the spearman correlation heatmap
    """)
    return


@app.cell
def _(df_healthy, plt, sns):
    def build_spearman_corr_heatmap(df):
        features =  [ 'WBC', 'NE#', 'LY#', 'MO#', 'EO#', 'BA#', 'RBC', 'HGB', 'HCT',
               'MCV', 'MCH', 'MCHC', 'RDW', 'PLT', 'MPV', 'PCT', 'PDW', 'SD', 'SDTSD',
               'TSD', 'FERRITTE', 'FOLATE', 'B12']

        df_filtered = df[features]
        corr_matrix = df_filtered.corr(method="spearman")

        plt.figure(figsize=(16, 12))


        sns.heatmap(
            corr_matrix,
            annot=True,  
            fmt=".2f",  
            cmap="coolwarm",  
            vmin=-1,
            vmax=1, 
            square=True,  
            linewidths=0.5,
            cbar_kws={"shrink": 0.8}
        )

        plt.title("Pearson Correlation Heatmap of Blood Metrics", fontsize=16)
        plt.tight_layout()
        plt.show()


    build_spearman_corr_heatmap(df_healthy)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Variables HCT and HGB have non-linear relationships as follows from 0.84 spearman correlation coefficient
    """)
    return


@app.cell
def _(df_healthy, sns):
    sns.scatterplot(x = df_healthy['HCT'], y = df_healthy['HGB'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pearson correlation for this pair is 0.12



    Pearson correlation captures the strength and direction of a strictly linear relationship between two variables.
    It is highly sensitive to outliers. Extreme outliers in distort the variance and covariance calculations, dragging the Pearson coefficient down to 0.12, missing the strong linear trend of the central data mass.

    Spearman coefficient (0.84) relies on rank order rather than absolute values, making it work against these extreme outliers


    Small Pearson correlation does not imply that two variables are independent. Pearson correlation only checks for linear dependencies, while two variables can share a perfect non linear relationship i.e y = x**2 and still yield low Pearson correlation.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 6. A simulation of the central limit theorem | 3 points
    Consider a simplified model of waiting times between independent events: an exponential
    distribution with mean 10 minutes. Its standard deviation is also 10 minutes. Use the scale
    parameter 10 minutes when generating observations.

    a. Generate 10,000 independent observations and plot their histogram. Describe the shape of the
    distribution.

    b. For each sample size n = 5, 30 and 100, generate 2,000 independent samples from this
    distribution. Compute the mean of each sample.

    c. Plot the three distributions of sample means using aligned axes with the same horizontal limits.
    Mark the theoretical mean. Overlay the normal density with mean 10 and standard deviation 10/√n
    on each plot.

    d. For each n, report the mean and standard deviation of the 2,000 sample means. Compare them
    with the theoretical values 10 and 10/√n.

    Explain how the shape and spread change with n. Which quantity becomes approximately
    normally distributed? Does increasing n make the original waiting-time distribution normal?
    Distinguish the role of the sample size n from the role of the number of repetitions (2,000).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##a
    """)
    return


@app.cell
def _(np, sns):
    rng = np.random.default_rng(seed=42)

    observations = np.random.exponential(scale=10, size=1000)
    sns.histplot(observations, kde = True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Right-skewed curve, looks like textbook exponential distribution
    """)
    return


@app.cell
def _(np):
    scale_parameter = 10.0  
    num_simulations = 2000  
    sample_sizes = [5, 30, 100]

    data_samples = {}
    sample_means = {}

    for n in sample_sizes:
        samples = np.random.exponential(scale=scale_parameter, size=(num_simulations, n))
        data_samples[n] = samples
        sample_means[n] = samples.mean(axis=1)


    for n in sample_sizes:
        print(f"Sample size n={n:3}: Generated matrix shape = {data_samples[n].shape}, Means vector shape = {sample_means[n].shape}")
    return


if __name__ == "__main__":
    app.run()
