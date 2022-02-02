library(rusdattendance)

test_that("numbers are simplified", {
    stuff <- c(1:3, "04", " 05", " 6", "PK", "KG")
    expect_equal(parse_grade_level(stuff),
                 c(1:6, "PK", "KG"))
})
