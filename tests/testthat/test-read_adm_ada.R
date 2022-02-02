schools_fixture <- function() {
    c(
        "Alfred State",
        "Ball State",
        "Colorado State",
        "Florida State",
        "Iowa State",
        "Jackson State",
        "Kansas State",
        "Louisiana State"
    )
}

years_fixture <- function() {
    c(
        "13-14",
        "14-15",
        "15-16",
        "16-17",
        "19-20",
        "20-21",
        "21-22",
        "22-23"
    )
}

grades_fixture <- function() {
    factor(
        c(
            "K4",
            "1",
            "2",
            NA,
            "KG",
            "PK",
            "8",
            "7"
        ),
        levels = rusdattendance::grade_levels)
}

test_that("nasty data is parsed correctly", {

    fh <- system.file("extdata",
                      "nasty_admada_for_testing.csv",
                      package = "rusdattendance")

    expect_warning(nasty <- read_adm_ada(fh),
                   "1 parsing failure")
    attr(nasty$Grade, "problems") <- NULL

    expect_equal(nasty$School, schools_fixture())

    expect_equal(nasty$`Calendar Year`, years_fixture())

    expect_equal(nasty$Grade, grades_fixture())
})
