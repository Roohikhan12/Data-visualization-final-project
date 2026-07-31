#  Airbnb Open Data Analysis & Interactive Visualization

https://data-visualization-final-project-ikr9vhtddarsknyyqx49ro.streamlit.app/

An end-to-end Data Analytics and Interactive Data Visualization project examining NYC Airbnb listing trends, pricing distributions, availability, and host characteristics using **Python** and **Plotly**.

---

##  Project Overview

This project focuses on performing exploratory data analysis (EDA), rigorous data cleaning, and dynamic interactive visual analysis on the Open Airbnb Dataset (~102,000+ listings)[cite: 2]. 

The goal of this analysis is to uncover underlying insights regarding pricing mechanics, spatial availability, cancellation behavior, host verification metrics, and neighborhood-level distributions across New York City[cite: 2].

---

##  Key Data Cleaning & Preprocessing

* **Duplicate Removal:** Identified and eliminated **541 duplicate records**[cite: 2].
* **Feature Engineering & Cleaning:**
  * Cleaned monetary formats (`price`, `service fee`) by removing `$`, commas, and parsing to numeric representations (`float64`)[cite: 2].
  * Standardized date fields (`last review`) into ISO standard `datetime64[ns]` formats[cite: 2].
  * Dropped irrelevant or uninformative columns (`license`, `country`, `country code`)[cite: 2].
* **Business Logic & Outlier Filtering:**
  * Filtered out illogical `minimum nights` (retaining realistic stays between $1 \le x \le 365$ nights)[cite: 2].
  * Filtered `availability 365` within valid physical constraints ($0 \le x \le 365$ days)[cite: 2].
  * Removed invalid/negative pricing and service fee records[cite: 2].
* **Final Clean Dataset:** Reduced noise to yield a structured subset of **97,559 valid records across 23 features**[cite: 2].

---

## 📊 Dataset Features

| Feature Name | Description |
| :--- | :--- |
| `id` / `host id` | Unique identifiers for listings and hosts[cite: 2]. |
| `NAME` / `host name` | Listing titles and host names[cite: 2]. |
| `neighbourhood group` / `neighbourhood` | NYC Boroughs (Manhattan, Brooklyn, Queens, etc.) and neighborhood sub-regions[cite: 2]. |
| `lat` / `long` | Geospatial coordinates for mapping[cite: 2]. |
| `room type` | Category of property (Entire home/apt, Private room, Shared room, Hotel room)[cite: 2]. |
| `price` / `service fee` | Nightly rate and platform service fee in USD[cite: 2]. |
| `minimum nights` | Minimum night stay requirements[cite: 2]. |
| `availability 365` | Days per year the listing is available for booking[cite: 2]. |
| `review rate number` | Customer rating scale (1–5)[cite: 2]. |

---

##  Visualizations & Insights Highlights

* **Price Distribution:** Analyzed overall price trends across distinct room types and neighborhood groups[cite: 2].
* **Geospatial Mapping:** Utilized latitude and longitude points to map property distributions throughout NYC boroughs[cite: 2].
* **Host Verification & Review Ratings:** Evaluated host behavior, cancellation policies, and average review ratings across listing categories[cite: 2].

---

##  Key Libraries & Technologies

* **Python 3.x**
* **Data Manipulation:** `pandas`, `numpy`[cite: 2]
* **Interactive Visualizations:** `plotly.express`, `plotly.graph_objects`, `plotly.subplots`[cite: 2]
* **Environment:** `Jupyter Notebook` / `Jupyter Lab`

---

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Roohikhan12/Data-visualization-final-project.git](https://github.com/Roohikhan12/Data-visualization-final-project.git)
   cd Data-visualization-final-project

   
