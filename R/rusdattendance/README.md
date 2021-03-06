
<!-- README.md is generated from README.Rmd. Please edit that file -->

# rusdattendance

<!-- badges: start -->

[![Lifecycle:
experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental)
[![CRAN
status](https://www.r-pkg.org/badges/version/rusdattendance)](https://CRAN.R-project.org/package=rusdattendance)
<!-- badges: end -->

The basic idea that I am working on is to extract attendance data from
[RUSD’s Infinite Campus database](https://racinewi.infinitecampus.org).
There are several different ways to query the database because it
contains both built-in reports and individual-level attendance tracking.
In a perfect world, I would have a table of student demographic data and
another table of attendance, and then create my own joins and summaries.
LOL … nope.

The least-bad option appears to be the report that is reached along the
menu path Attendance -> Reports -> ADM and ADA Detail. “ADM” stands for
“Average Daily Membership” and “ADA” stands for “Average Daily
Attendance.” This approach can create CSV files, which are at least
tractable-ish. Each file corresponds to a year. I asked for
per-grade-level reports. There are subtotals, and blank lines,
separating the per-grade data for each school.

## Installation

You can install the released version of rusdattendance from
[CRAN](https://CRAN.R-project.org) with:

``` r
install.packages("rusdattendance")
```

## Example

This is a basic example which shows you how to solve a common problem:

``` r
# library(rusdattendance)
## basic example code
```
